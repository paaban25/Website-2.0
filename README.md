# Aries

## setup

1 got to backend folder, run 
``` 
poetry install
pip install pre-commit
pre-commit
poetry run ./manage.py migrate
poetry run ./manage.py runserver

```
2 got to Frontend folder, run 
``` 
yarn
yarn dev
```

3 samples
```DJ_DATABASE_URL=postgres://username:password@localhost:5432/db_name```
