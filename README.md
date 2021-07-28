# Store

_Hardware [Store]_

## Starting 🚀

_These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._

Look **Deployment** to know how to deploy the project.


### Pre requirements 

_A series of step-by-step examples that tells you what to run to get a development environment running_

_Clone the repository_

```
git clone git@github.com:luckdeluxe/Petgram.git && cd Petgram
```

_Create a virtual Python environment:_

```
python3 -m venv .venv
```

_Activate the virtual environment_

```
sorce .venv/bin/activate
```

_Create database from models_

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Installation 🔧

_What things do you need to install the software and how to install them_

```
asgiref==3.4.1
astroid==2.6.2
Django==3.2.5
isort==5.9.2
lazy-object-proxy==1.6.0
mccabe==0.6.1
Pillow==8.3.1
psycopg2-binary==2.9.1
pylint==2.9.3
pylint-django==2.4.4
pylint-plugin-utils==0.6
pytz==2021.1
sqlparse==0.4.1
toml==0.10.2
wrapt==1.12.1
```

## Running the tests ⚙️

```
python3 manage.py runserver
```
