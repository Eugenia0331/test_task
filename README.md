# test_task

# Структура проекта
saucedemo-autotests/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── utils/
│   ├── __init__.py
│   └── driver_factory.py
│
├── requirements.txt
├── pytest.ini
├── Dockerfile
└── README.md

## Saucedemo Login Autotests

## Установка

pip install -r requirements.txt

## Запуск тестов

pytest

## Allure-отчет

allure serve allure-results

## Docker

docker build -t saucedemo-tests .
docker run saucedemo-tests

