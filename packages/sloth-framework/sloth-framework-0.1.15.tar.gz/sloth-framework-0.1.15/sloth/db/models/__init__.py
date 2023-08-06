# -*- coding: utf-8 -*-
import datetime
import json
from sloth import threadlocals
from decimal import Decimal
from django.apps import apps
from django.db import models
from django.db.models import *
from django.db.models import base
from django.db.models.query_utils import DeferredAttribute
from django.forms.models import model_to_dict
from sloth.core.queryset import QuerySet
from sloth.core.base import ModelMixin
from sloth.utils import serialize


class GenericModelWrapper(object):
    def __init__(self, obj):
        self._wrapped_obj = obj

    def __getattr__(self, attr):
        if attr == 'prepare_database_save':
            raise AttributeError()
        return getattr(self._wrapped_obj, attr)

    def __setattr__(self, attr, value):
        if attr == '_wrapped_obj':
            super().__setattr__(attr, value)
        elif self._wrapped_obj is not None:
            self._wrapped_obj.__setattr__(attr, value._wrapped_obj)

    def __str__(self):
        return self._wrapped_obj.__str__()

    def __repr__(self):
        return self._wrapped_obj.__repr__()


class GenericValue(object):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        if isinstance(self.value, str) and '::' in self.value:
            value_type, value = self.value.split('::')
            if '.' in value_type:
                self.value = apps.get_model(value_type).objects.get(pk=value)
            elif value_type == 'str':
                self.value = value
            elif value_type == 'int':
                self.value = int(value)
            elif value_type == 'Decimal':
                self.value = Decimal(value)
            elif value_type in ('date', 'datetime'):
                self.value = datetime.datetime.strptime(value[0:10], '%Y-%m-%d')
            elif value_type == 'float':
                self.value = float(value)
            elif value_type == 'bool':
                self.value = value == 'True'
            elif value_type == 'list':
                self.value = json.loads(value)
        return self.value

    def dumps(self):
        value = self.value
        if value is not None:
            if isinstance(value, Model):
                value = GenericModelWrapper(value)
            if isinstance(value, GenericModelWrapper):
                return '{}.{}::{}'.format(
                    value.metaclass().app_label, value.metaclass().model_name, value.pk
                )
            if hasattr(value, 'model'):
                value = list(value.values_list('pk', flat=True))
            if isinstance(value, list):
                value = json.dumps(value)
            return '{}::{}'.format(type(value).__name__, value)
        return None


class GenericFieldDescriptor(DeferredAttribute):
    def __get__(self, instance, cls=None):
        obj = super().__get__(instance, cls=cls)
        if isinstance(obj.value, Model):
            return GenericModelWrapper(obj.value)
        return obj.get_value()

    def __set__(self, instance, value):
        instance.__dict__[self.field.attname] = GenericValue(value)


class GenericField(CharField):
    descriptor_class = GenericFieldDescriptor

    def __init__(self, *args, max_length=255, null=True, **kwargs):
        super().__init__(*args, max_length=max_length, null=null, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            if isinstance(value, GenericValue):
                value = value.dumps()
            else:
                value = GenericValue(value).dumps()
        return value


class ColorField(CharField):
    def __init__(self, *args, max_length=7, **kwargs):
        super().__init__(*args, max_length=max_length, **kwargs)

    def formfield(self, **kwargs):
        from sloth.actions.inputs import ColorInput
        field = super().formfield(**kwargs)
        field.widget = ColorInput()
        return field


class PhotoField(ImageField):
    def __init__(self, *args, max_width=200, max_height=200, **kwargs):
        self.max_width = max_width
        self.max_height = max_height
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        field.widget.attrs.update(
            {'data-max-width': self.max_width, 'data-max-height': self.max_height, 'accept': 'image/*', 'capture': ''}
        )
        return field


class CharField(CharField):
    def __init__(self, *args, max_length=255, **kwargs):
        self.mask = kwargs.pop('mask', None)
        self.rmask = kwargs.pop('rmask', None)
        super().__init__(*args, max_length=max_length, **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        field.widget.mask = self.mask
        field.widget.rmask = self.rmask
        return field


class BooleanChoiceField(BooleanField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from ...actions import BooleanChoiceField
        kwargs.update(form_class=BooleanChoiceField)
        return super().formfield(**kwargs)


class BrCepField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(mask='00.000-000')
        super().__init__(*args, **kwargs)


class BrCpfField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(mask='000.000.000-00')
        super().__init__(*args, **kwargs)


class BrCnpjField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(mask='00.000.000/0000-00')
        super().__init__(*args, **kwargs)


class BrCarPlateField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(mask='AAA-0A00')
        super().__init__(*args, **kwargs)


class BrPhoneField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(mask='0000-0000')
        super().__init__(*args, **kwargs)


class BrRegionalPhoneField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(mask='(00) 00000-0000')
        super().__init__(*args, **kwargs)


class TextField(TextField):
    def __init__(self, *args, formatted=False, **kwargs):
        self.formatted = formatted
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        field.widget.formatted = self.formatted
        return field


class ForeignKey(ForeignKey):
    def __init__(self, to, on_delete=CASCADE, **kwargs):
        self.picker = kwargs.pop('picker', None)
        self.addable = kwargs.pop('addable', False)
        self.username_lookup = kwargs.pop('username_lookup', None)
        self.lookups = kwargs.pop('lookups', None)
        super().__init__(to=to, on_delete=on_delete, **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        field.addable = self.addable
        if self.picker:
            field.picker = self.picker
        if self.username_lookup:
            field.username_lookup = self.username_lookup
        if self.lookups:
            field.lookups = self.lookups
        return field


class CurrentUserField(ForeignKey):
    def __init__(self, *args, **kwargs):
        kwargs.update(to='auth.User')
        super().__init__(*args, **kwargs)


class ManyToManyField(ManyToManyField):
    def __init__(self, to, **kwargs):
        if hasattr(to, 'model'):
            self.queryset = to
            to = to.model
        else:
            self.queryset = None
        self.picker = kwargs.pop('picker', None)
        self.addable = kwargs.pop('addable', False)
        super().__init__(to, **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        field.addable = self.addable
        if self.picker:
            field.picker = self.picker
        if self.queryset:
            field.queryset = self.queryset
        return field


class OneToOneField(OneToOneField):
    def __init__(self, to, on_delete=SET_NULL, **kwargs):
        if kwargs.get('blank'):
            kwargs.update(null=True)
        super().__init__(to=to, on_delete=on_delete, **kwargs)


class OneToManyField(ManyToManyField):
    one_to_many = True

    def __init__(self, *args, min=0, max=3, **kwargs):
        self.min = min
        self.max = max
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        field.min = self.min
        field.max = self.max
        return field


class DecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        decimal_places = kwargs.pop('decimal_places', 2)
        max_digits = kwargs.pop('max_digits', 9)
        super().__init__(*args, decimal_places=decimal_places, max_digits=max_digits, **kwargs)

    def formfield(self, **kwargs):
        from ...actions import DecimalField
        kwargs.update(form_class=DecimalField)
        return super().formfield(**kwargs)


class Decimal3Field(models.DecimalField):
    def __init__(self, *args, **kwargs):
        decimal_places = kwargs.pop('decimal_places', 3)
        max_digits = kwargs.pop('max_digits', 9)
        super().__init__(*args, decimal_places=decimal_places, max_digits=max_digits, **kwargs)


class Manager(QuerySet):
    def queryset(self):
        return self


class ModelBase(base.ModelBase):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if cls.metaclass() and getattr(cls.metaclass(), 'autouser', False):
            cls.add_to_class('autouser', models.ForeignKey('auth.user', verbose_name='Usuário', null=True, on_delete=models.CASCADE))
        return cls


class Model(models.Model, ModelMixin, metaclass=ModelBase):

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__['__diff__'] = {}
        if not hasattr(type(self), '__fieldnames__'):
            type(self).__fieldnames__ = [f.name for f in type(self)._meta.get_fields()]

    def __setattr__(self, key, value):
        if getattr(self.metaclass(), 'logging', False) and self.__dict__.get('__diff__') is not None and key != 'id':
            if value != self.__dict__.get(key) and key in type(self).__fieldnames__:
                field_names = getattr(self.metaclass(), 'logging')
                if field_names is True or key in field_names:
                    if self.__dict__.get('{}_id'.format(key), 0) is None:
                        previous = None
                    else:
                        previous = serialize(getattr(self, key), identifier=True)
                    self.__dict__['__diff__'][key] = previous, serialize(value, identifier=True)
        super().__setattr__(key, value)

    def pre_save(self, *args, **kwargs):
        setattr(self, '_pre_saved', True)
        if hasattr(self, '__roles__'):
            setattr(self, '_role_tuples', self.get_role_tuples(True))

    def save(self, *args, **kwargs):
        pre_saved = getattr(self, '_pre_saved', False)
        if pre_saved is False:
            self.pre_save()

        super().save(*args, **kwargs)

        if pre_saved is False:
            self.post_save()

    def post_save(self, *args, **kwargs):
        self.__log__()
        if hasattr(self, '__roles__') and hasattr(self, '_role_tuples'):
            self.sync_roles(getattr(self, '_role_tuples'))

    def delete(self, *args, **kwargs):
        if getattr(self.metaclass(), 'logging', False):
            field_names = getattr(self.metaclass(), 'logging')
            for key in type(self).__fieldnames__:
                if field_names is True or key in field_names:
                    self.__dict__['__diff__'][key]= serialize(self.__dict__.get(key), identifier=True), None
            self.__log__(delete=True)
        if hasattr(self, '__roles__'):
            setattr(self, '_role_tuples', self.get_role_tuples(True))
        super().delete(*args, **kwargs)
        if hasattr(self, '__roles__') and hasattr(self, '_role_tuples'):
            self.sync_roles(getattr(self, '_role_tuples'))

    def __log__(self, delete=False):
        if getattr(self.metaclass(), 'logging', False) and hasattr(threadlocals, 'transaction'):
            if self.__dict__['__diff__']:
                if delete:
                    operation = 'delete'
                elif 'id' in self.__dict__['__diff__']:
                    operation = 'add'
                else:
                    operation = 'edit'
                threadlocals.transaction['operation'] = operation
                threadlocals.transaction['diff'].append(
                    dict(pk=self.pk, model='{}.{}'.format(
                        self.metaclass().app_label, self.metaclass().model_name
                    ), fields=self.__dict__['__diff__'])
                )

    def __str__(self):
        for field in self.metaclass().fields:
            if isinstance(field, models.CharField):
                return getattr(self, field.name)
        return '{} #{}'.format(self.metaclass().verbose_name, self.pk)


    def send_mail(self, to, subject, content, from_email=None):
        from sloth.api.models import Email
        Email.objects.send(to, subject, content, from_email)