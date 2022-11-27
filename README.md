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

Откройте файл .gitignore и расскомментируйте строки:
```
.vscode/*
.VSCode*/*
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
pip install -r ./requirements/dev.txt
```

### 1.1. Запустить сервер разработки:

```
python manage.py migrate
python manage.py runserver
```

Убедившись, что все хорошо, создаем суперюзера:
```
python manage.py createsuperuser
```

На этом установка приложения и его проверка локально завершена.
Сейчас переходим к размещению данного проекта на своем github репозитории, для будущего деплоя на хостинг.


## 1. Загрузить проект на GitHub

### 1.1. Загрузка проекта на GitHub

Создайте пустой репозиторий на GitHub через сайт (галочки редми, лицензии и т.д. не ставим), далее после этого выполните команду (вместо main можете использовать любое наименование ветки), далее в каталоге с проектом введите:
```
git branch -M main
git remote add origin https://github.com/examples-code/reponame.git
git push -u origin main
```
Где "https://github.com/examples-code/reponame.git" - это ссылка на ваш репозиторий
При этом GitHub попросит логин и пароль, вместо пароля вводите токен (гуглите как его создать).



## 1. Деплой проекта на облачный хостинг NetAngels

### 1.1. Создаем аккаунт на сайте


### 1.1.

Выбираем в левом меню сайт, вкладка "Файлы" там выбираем "Терминал", в открывшемся терминале вводим: 

```
rm -r app
mkdir app
cd app
git clone https://<github-token>@github.com/examples-code/django-hosting-netangels.git . -b main
```

Где <github-token> - это ваш токен в гитхаб (чтоб не вводить логин пароль).
а "github.com/examples-code/django-hosting-netangels.git" - это ваш репозиторий

Далее устанавливаете зависимости:
```
pip install -r ./requirements/prod.txt
```

Применим миграции:
```
python manage.py migrate
```

Проверим что при запуске сервера нет ошибок:
```
python manage.py runserver
```

Убедившись, что все хорошо, создаем суперюзера:
```
python manage.py createsuperuser
```
