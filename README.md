# Crossword Drill

To run the program:
```
pip install -r requirements.txt
python manage.py loaddata fixtures/xword_data.json
python manage.py makemigrations
python manage.py migrate
```

To run the test:
```
python manage.py migrate
```