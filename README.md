# erp_backend


# First Time installations
## create a virtual enviroment
```
# linux/mac user
python3 -m venv venv

# window user
python -m venv venv
```

## activate the virtual enviroment
```
# linx/mac user
source venv/bin/activate

# window user
. venv/Script/activate
```

## install requirement 
```
cd erp
pip install -r requirements.txt
```

## run the app
```
python manage.py runserver
```

# running app after subsequently
```
cd erp
python manage.py runserver
```