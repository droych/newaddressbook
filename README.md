# Adress book app 
> Adress book app Readme
## Usage
```
unicorn main:app --reload

```
Go to [http://localhost:8000/docs](http://localhost:8000/docs)
## Development
### Local Environment Setup
python -m venv {nameofvenv}
### Activate  virtual env , install dependencies 
```
pip install -r requirements.txt
```
### Create tables
```
alembic upgrade head
```

