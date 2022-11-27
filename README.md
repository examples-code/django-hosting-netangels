# Django проект для деплоя на хостинг NetAngels.ru
В данном репозитории размещен Django проект, который настроен для деплоя на хостинг NetAngels.ru
Ниже представлена инструкция по запусу проекта.

## 1. Развернуть проект локально (DEV) 

### 1.1. Клонируйте репозиторий:
Создайте у себя локально каталог проекта, название каталога может быть любым, перейдите в него:
```
mkdir projectname
cd projectname
```

Клонируйте репозиторий к себе на локальную машину, в каталог проекта, для этого в командной строке вводим:
```
git clone https://github.com/examples-code/django-hosting-netangels.git . master
```

Удаляем каталог .git для того, чтоб отвязать каталог проекта от удаленного репозитория с шаблоном и инициировать свой git
```
rm -r .git
git init
git add .
git commit -m 'first commit'
```

### 1.1. Создать виртуальное окружение:
Создаем виртуальное окружение, активируем его и обновляем pip (версия Питона на ваше усмотрение):
```
python3.11 -m venv django_env && \
source django_env/bin/activate && \
pip install --upgrade pip
```

### 1.1. Установка зависимостей

```
pip install -r ./requirements.txt
```

### 1.1. Запустить сервер разработки:

```
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```
