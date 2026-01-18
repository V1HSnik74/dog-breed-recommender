Сервис подбора пород собак для будущих владельцев с целью рекомендации подходящей породы по образу жизни и условиям содержания

Система помогает пользователям определиться с выбором питомца, предоставляя несколько вариантов по введенным пользователем данным.

**Ссылка на рабочий проект**: https://vhsnik74.pythonanywhere.com/

**Технологии**
1) Python 3.11
2) Django 5.2.1
3) deep-translator 1.11.4 (для перевода названий пород собак с английского на русский)
4) Bootstrap 5

**Скриншоты**
1) Форма для заполнения пользователем https://drive.google.com/file/d/1QLMZNYAqwKYXVyfHjQ9r35_cViqouEGy/view?usp=drive_link
Здесь происходит заполнение пользователем нужных для составления рекомендаций данных

2) Рекомендации https://drive.google.com/file/d/1k7vaHnNI1m37DJ4UsD7nA8z8c9YC6-qh/view?usp=sharing
Здесь пользователю показывется топ-20 подходящих ему собак

**Как запустить проект локально**
1) **Клонируйте репозиторий:**
   в PyCharm нажать clone repository / project from version control
   Вставить ссылку на репозиторий gitHub https://github.com/V1HSnik74/dog-breed-recommender
2) **Создайте и активируйте виртуальное окружение:**
   В окне create virtual enviroment нажать cancel
   ```bash
   python -m venv venv
   source venv/bin/activate  # для Linux/Mac
   venv\Scripts\activate     # для Windows
   ```
3) **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
4) **Выполните миграции:**
   ```bash
   python manage.py makemigrations 
   Ввести в консоль 1, нажать enter. Повторить этот шаг
   python manage.py migrate
   ```
5) **Получите данные из API**
   Зарегистрируйтесь на сайте api-ninja, скопируйте ключ в личном кабинете
   ```bash
   python manage.py breedsloader --key [key] (где [key] - скопированный ключ)
   ```
6) **Настройте settings.py**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Полученный ключ вставьте в файл settings.py в поле SECRET_KEY
   Поле DEBUG перевести в True (Так и не поняла, как статику собирать на локальном сервере при выключенном DEBUG, даже если в STATIC_ROOT собираются файлы, сервер их блокирует, при этом на pythonanywhere такой проблемы не было при DEBUG=False)
7) **Добавьте SuperUser (Если нужен вход в админку)**
   ```bash
   python manage.py createsuperuser 
   ```
8) **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```
9) **Откройте проект в браузере:**
   Перейдите по ссылке: http://127.0.0.1:8000/