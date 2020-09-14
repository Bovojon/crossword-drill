# Crossword Drill

To run the program:
```
pip install -r requirements.txt
python manage.py loaddata fixtures/xword_data.json
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then navigate to `http://localhost:8000/drill/`.

To run the test:
```
python manage.py migrate
```