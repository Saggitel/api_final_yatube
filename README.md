## **Как запустить проект**
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/slapeach/api_final_yatube.git
```
```
cd api_final_yatube
```

Cоздать виртуальное окружение:
```
python3 -m venv env
```
На Windows:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source env/bin/activate
```
На Windows:
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
На Windows:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```
На Windows:
```
python manage.py migrate
```

Запустить проект:
```
python3 manage.py runserver
```
На Windows:
```
python manage.py runserver
```