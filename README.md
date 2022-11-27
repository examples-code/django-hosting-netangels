# Django проект для деплоя на хостинг NetAngels.ru
В данном репозитории размещен Django проект, который настроен для деплоя на хостинг NetAngels.ru
Ниже представлена инструкция по запусу проекта.

## 1. Развернуть проект локально (DEV) 

### 1.1. Клонируйте репозиторий:
Клонируйте репозиторий к себе на локальную машину, для этого в командной строке вводим:
```

```


### 1.1. Создать виртуальное окружение:
Создаем виртуальное окружение, активируем его и обновляем pip

```
python3.11 -m venv django_env && \
source django_env/bin/activate && \
pip install --upgrade pip
```

### 1.1. Установка зависимостей


```
pip install -r ./requirements.txt
```

### 1.1. Создание проекта, точка - в текущей директории
```
django-admin startproject project .
```


### 1.1. Запустить сервер разработки:

```
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```
