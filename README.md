# E-Wallet_Backend

## How to run on local machine
* mkdir backend
* cd backend
* git clone https://github.com/Vputri/E-Wallet_Backend
* virtualenv -p python3 env
* source virtmetalite/bin/activate
* cd api
* pip install -r requirements.txt

* add export virtualenviroment variabel to virtmetalite/bin/activate
```
export SECRET_KEY='abcd'
export DJANGO_DEBUG=True
export ALLOWED_HOSTS=127.0.0.1

```

* source ../env/bin/activate
* python manage.py migrate
* python manage.py runserver
