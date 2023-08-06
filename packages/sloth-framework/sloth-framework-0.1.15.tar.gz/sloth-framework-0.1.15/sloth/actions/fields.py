from django import forms
from django.apps import apps
from . import inputs


class QrCodeField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(widget=inputs.QrCodeInput())
        super().__init__(*args, **kwargs)

class PhotoField(forms.CharField):
    def __init__(self, *args, max_width=200, max_height=200, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.attrs.update(
            {'data-max-width': max_width, 'data-max-height': max_height, 'accept': 'image/*', 'capture': ''}
        )


class ModelChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset, *args, **kwargs):
        if isinstance(queryset, str):
            queryset = apps.get_model(queryset).objects
        self.username_lookup = kwargs.pop('username_lookup', None)
        super().__init__(queryset, *args, **kwargs)


class TextField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(widget=forms.Textarea())
        super().__init__(*args, **kwargs)


class CurrentUserField(forms.ModelChoiceField):
    def __init__(self, **kwargs):
        from django.contrib.auth.models import User
        super().__init__(User.objects, **kwargs)
