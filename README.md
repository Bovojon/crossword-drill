# Crossword Drill

To start the project, `git clone` the repo and then run:
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/xword_data.json
python manage.py runserver
```

Then navigate to `http://localhost:8000/drill/`.

To run the tests:
```
python manage.py test
```