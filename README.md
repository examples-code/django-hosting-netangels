# Django проект для деплоя на хостинг NetAngels.ru
В данном репозитории размещен Django проект, который настроен для деплоя на хостинг NetAngels.ru
Ниже представлена инструкция по запусу проекта.

## Развернуть проект локально (DEV)

### Клонируйте репозиторий:
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

### Создать виртуальное окружение:
Создаем виртуальное окружение, активируем его и обновляем pip (версия Питона на ваше усмотрение):
```
python3.11 -m venv django_env && \
source django_env/bin/activate && \
pip install --upgrade pip
```

### Установка зависимостей

```
pip install -r ./requirements/dev.txt
```

### Запустить сервер разработки:

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


## Загрузить проект на GitHub

### Загрузка проекта на GitHub

Создайте пустой репозиторий на GitHub через сайт (галочки редми, лицензии и т.д. не ставим), далее после этого выполните команду (вместо main можете использовать любое наименование ветки), далее в каталоге с проектом введите:
```
git branch -M main
git remote add origin https://github.com/examples-code/reponame.git
git push -u origin main
```
Где "https://github.com/examples-code/reponame.git" - это ссылка на ваш репозиторий
При этом GitHub попросит логин и пароль, вместо пароля вводите токен (гуглите как его создать).


## Деплой проекта на облачный хостинг NetAngels

### Создаем аккаунт на сайте и настраиваем

* Инструкция по создания аккаунта см. тут: https://devnote.ural-site.ru/deploj-na-xosting *

### Загрузка проекта

Выбираем в левом меню сайт, вкладка "Файлы" там выбираем "Терминал", в открывшемся терминале вводим: 

Обновляем pip
```
pip install --upgrade pip
```

Создаем каталоги для статики и медиа
```
cd www && mkdir static && mkdir media && cd ..
```

Удалим app с содержимым и создадим снова (чтоб был пустой):
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

Проверим что при запуске сервера нет ошибок (кроме ошибки с IP):
```
python manage.py runserver
```

Убедившись, что все хорошо, создаем суперюзера:
```
python manage.py createsuperuser
```

Далее выполним сборку статики
```
python manage.py collectstatic
```

Создаем символическую ссылку на wsgi.py
```
ln -s ./config/wsgi.py ./
```

Перезагружаем Python в панели управления.

Если были выявлены ошибки, исправляем их в коде локально, делаем коммит, пуш в ветку на гитхаб, затем в терминале на сервере в каталоге app выполняем команду:

```
git pull https://<github-token>@github.com/examples-code/django-hosting-netangels.git main
```
Где <github-token> - это ваш токен в гитхаб (чтоб не вводить логин пароль).
а "github.com/examples-code/django-hosting-netangels.git" - это ваш репозиторий

*Готово.*