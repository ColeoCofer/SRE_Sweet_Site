# Team Sweet Team Name - SRE Project

### Site Endpoints
Vote: http://34.66.4.34/polls/ <br>
Admin: http://34.66.4.34/admin/ <br>

### How to migrate database & collect static content
I created an alias to do this, you can just type `migrate` instead of the following: <br>
This will collect static content into the directory specified in `mysite/settings.py` <br>
```
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic
```

### Useful alias's
Activate virtual environment: `virtual` <br>
Migrate database & collect static content: `migrate` <br>
Start the server locally: `runserver` <br>
Start gunicorn: `rungunicorn` <br>
Start gunicorn in background (you can close your terminal): `rungunicornbg` <br>
Restart NGINX: `restartnginx` <br>
Edit Database settings (with emacs of course): `editsettings` <br>
Edit the NGINX confic file: `editnginx` <br>
List processes using port 8000: `8000` <br>
Kill processes using port 8000: `kill8000` <br>

### Creating a polling question example
This can also be achieved via the `/admin` endpoint. <br>
```
./manage shell
from polls.models import Choice, Question
from django.utils import timezone
q = Question(question_text="Cats or Dogs?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text='Cats!', votes=0)
q.choice_set.create(choice_text='Dogs!', votes=0)
exit()
```

### Install Postgres Database & NGINX locally Mac
Make sure you are in the virtual environment and it's activated: `source sreprojectenv/bin/activate`  
1. `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. `brew install postgresql`
3. `brew install nginx`

### Pip requirements
If you save these into a file called `requirements.txt` you can install them via `pip install -r requirements.txt` <br>
```
Django==2.2.6
gunicorn==19.9.0
psycopg2-binary==2.8.4
pytz==2019.3
sqlparse==0.3.0
```
