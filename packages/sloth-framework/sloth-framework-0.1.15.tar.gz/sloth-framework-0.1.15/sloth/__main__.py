import sys
import os
from sloth.conf import settings
from django.core.management import ManagementUtility


URLS_FILE_CONTENT = '''from django.urls import path, include

urlpatterns = [
    path('', include('sloth.api.urls')),
]
'''

MODELS_FILE_CONTENT = '''from sloth.db import models, role, meta
'''

ACTIONS_FILE_CONTENT = '''from sloth import actions
'''

TASKS_FILE_CONTENT = '''from sloth.api.tasks import Task
'''

TEST_FILE_CONTENT = '''from sloth.test import SeleniumTestCase

"""
Tu run the tests, execute:
    python manage.py test
To run the tests in the browser, execute:
    python manage.py test --browser
To resume the execution from the fourth step for example, execute:
   python manage.py test --browser --from 2
To create development database from the fourth step for example, execute:
   python manage.py test --restore 4
To run the test as a tutorial, execute:
   python manage.py test --tutorial
"""

class TesteIntegracao(SeleniumTestCase):

    def test(self):
        self.create_superuser('admin', '123')

        if self.step():
            self.login('admin', '123')
            self.logout()

        if self.step():
            self.click_link('Cadastrar-se')
            with self.look_at_popup_window():
                self.enter('Usuário', 'user')
                self.enter('Senha', '123')
                self.enter('Confirmação', '123')
                self.click_button('Cadastrar-se')
            self.login('user', '123')
            self.logout()
'''

LOCAL_SETTINGS_FILE_CONTENT = '''_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '?',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}'''

DASHBOARD_FILE_CONTENT = '''from sloth.api.dashboard import Dashboard
from .models import *


class AppDashboard(Dashboard):

    def __init__(self, request):
        super().__init__(request)
        self.styles('/static/css/sloth.css')
        self.scripts('/static/js/sloth.js')
        self.libraries(fontawesome=False, materialicons=False)
        self.web_push_notification(False)
        self.login(logo='/static/images/logo.png', title=None, mask=None, two_factor=False, actions=['signup', 'reset_password'])
        self.navbar(title='Sloth', icon='/static/images/icon.png', favicon='/static/images/icon.png')
        self.header(title='Sloth', shadow=True)
        self.settings_menu('change_password')
        self.tools_menu('show_icons')
        self.footer(title='© 2022 Sloth', text='Todos os direitos reservados', version='1.0.0')

    def view(self):
        return self.value_set()

'''

DEPLOY_WORKFLOW_CONTENT = '''name: DEPLOY

on:
  push:
    branches: [ "main", "master" ]
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        env:
          TOKEN: ${{ secrets.TOKEN }}
        run: |
          curl -X POST https://deploy.cloud.aplicativo.click/ -d '{"action": "deploy", "repository": "${{ github.repositoryUrl }}", "token": "${{ secrets.TOKEN }}"}'

'''

DOCKER_FILE_CONTENT = '''FROM sloth
WORKDIR /opt/app
EXPOSE 8000
ADD . .
ENTRYPOINT ["python", "manage.py", "startserver", "{}"]
'''

DOCKER_COMPOSE_FILE_CONTENT = '''version: '3.9'

services:
  web:
    ports:
      - "8000"
    build:
      context: .
      dockerfile: Dockerfile
    restart: always
    volumes:
      - .docker/media:/opt/app/media
      - ./static:/opt/app/static
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      REDIS_HOST: redis
      POSTGRES_HOST: postgres
      WEASYPRINT_HOST: weasyprint
  redis:
    image: redis
    hostname: redis
    restart: always
    ports:
      - "6379"
    command: redis-server --loglevel warning
    volumes:
      - .docker/redis:/data
  postgres:
    image: postgres
    hostname: postgres
    environment:
      POSTGRES_DB: ${DATABASE_NAME:-database}
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD:-password}
    ports:
      - "5432"
    volumes:
      - .docker/postgres:/var/lib/postgresql/data
    healthcheck:
      test: psql -U postgres -d $$POSTGRES_DB -c "SELECT version();"
  weasyprint:
    image: weasyprint
    hostname: weasyprint
    ports:
      - "8888"
'''

DOCKER_IGNORE_FILE_CONTENT = '''.docker
.github
.git
.gitignore
.dockerignore
docker-compose.yml
Dockerfile
static
media
*.pyc
*.sqlite3
*.md
local_settings.py
'''

REQUIREMENTS = '''
sloth-framework
'''

def startproject():
    name = os.path.basename(os.path.abspath('.'))
    ManagementUtility(['django-admin.py', 'startproject', name, '.']).execute()
    settings_path = os.path.join(name, 'settings.py')
    settings_content = open(settings_path).read().replace(
        "'django.contrib.admin'",
        "'{}', 'oauth2_provider', 'sloth.api'".format(name)
    ).replace('from pathlib', 'import os\nfrom pathlib')
    settings_content = settings_content.replace("'db.sqlite3'", "'db.sqlite3', 'TEST': {'NAME': 'test.sqlite3'}")
    settings_append = open(settings.__file__).read().replace('import os', '').replace('# ', '')
    with open(settings_path, 'w') as file:
        file.write('{}{}'.format(settings_content, settings_append))
    local_settings_path = os.path.join(name, 'local_settings.py')
    with open(local_settings_path, 'w') as file:
        file.write(LOCAL_SETTINGS_FILE_CONTENT.replace('?', name))
    urls_path = os.path.join(name, 'urls.py')
    with open(urls_path, 'w') as file:
        file.write(URLS_FILE_CONTENT)
    models_path = os.path.join(name, 'models.py')
    with open(models_path, 'w') as file:
        file.write(MODELS_FILE_CONTENT)
    actions_path = os.path.join(name, 'actions.py')
    with open(actions_path, 'w') as file:
        file.write(ACTIONS_FILE_CONTENT)
    tasks_path = os.path.join(name, 'tasks.py')
    with open(tasks_path, 'w') as file:
        file.write(TASKS_FILE_CONTENT)
    dashboard_path = os.path.join(name, 'dashboard.py')
    with open(dashboard_path, 'w') as file:
        file.write(DASHBOARD_FILE_CONTENT)
    test_path = os.path.join(name, 'tests.py')
    with open(test_path, 'w') as file:
        file.write(TEST_FILE_CONTENT)
    workflows_path = os.path.join('.github', 'workflows')
    os.makedirs(workflows_path, exist_ok=True)
    deploy_workflow_path = os.path.join(workflows_path, 'deploy.yml')
    with open(deploy_workflow_path, 'w') as file:
        file.write(DEPLOY_WORKFLOW_CONTENT)
    ignore = ['bin/server.log', '.idea/', 'db.sqlite3', '*.pyc', '.DS_Store', 'geckodriver.log', '.docker', 'media', 'local_settings.py']
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'a') as file:
            file.write('\n'.join(ignore))
    else:
        with open('.gitignore', 'w') as file:
            file.write('\n'.join(ignore))
    with open('Dockerfile', 'w') as file:
        file.write(DOCKER_FILE_CONTENT.format(name))
    with open('docker-compose.yml', 'w') as file:
        file.write(DOCKER_COMPOSE_FILE_CONTENT)
    with open('.dockerignore', 'w') as file:
        file.write(DOCKER_IGNORE_FILE_CONTENT)
    with open('requirements.txt', 'w') as file:
        file.write(REQUIREMENTS)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        startproject()
        os.system('python3 manage.py sync')
    if len(sys.argv) == 2:
        if sys.argv[1] == 'build':
            os.system('docker build --target sloth-src -t sloth {}'.format(os.path.dirname(__file__)))
            os.system('docker build --target sloth-weasyprint -t weasyprint {}'.format(os.path.dirname(__file__)))
        if sys.argv[1] == 'cloud':
            os.system('python3 {}'.format(os.path.join(os.path.dirname(__file__), 'cloud', 'server.py')))
