# API_YAMDB
![example workflow](https://github.com/y0urchaper0ne/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

YaMDb — сервис по сбору отзывов о фильмах, книгах или музыке. Проект собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Пользователи имеют возможность не только оставлять отзывы, но и комментировать их.

## Технологии

Стэк технологий, использованных в проекте:

- REST API
- Django

## Установка

Создание и сборка контейнеров
```sh
docker-compose up -d --build
```
Выполнение миграций, создание суперпользователя, сбор статики
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

После выполнения команд проект будет доступен по адресу
```sh
http://localhost
```

## Шаблон заполнения .env

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## Авторы проекта
- Первый разработчик - [Николай Никулин](https://github.com/Troynik27)
- Второй разработчик - [Илья Никитин](https://github.com/y0urchaper0ne)
- Третий разработчик - [Дмитрий Гнибида](https://github.com/Dmitriy153)
