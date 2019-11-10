# Team Sweet Team Name - SRE Project

### Site Endpoints
Vote: http://35.225.249.122/polls/ <br>
Admin: http://35.225.249.122/admin/ <br>
Monitoring Dashboard: https://app.google.stackdriver.com/?project=sreproject

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
Restart NGINX: `restartnginx` <br>
Edit Database settings (emacs): `editsettings` <br>
Edit Database settings (vim): `veditsettings` <br>
Edit the NGINX config file (emacs): `editnginx` <br>
Edit the NGINX config file (vim): `veditnginx` <br>
List processes using port 8000: `8000` <br>
Kill processes using port 8000: `kill8000` <br>

### How to run gunicorn in the background
TODO: Use the supervisor package to automatically start gunicorn on startup <br>
1. `screen -xR` to open a new session
2. `. ~/.profile` to load in alias's
3. `virtual` activate virtual env
4. `rungunicorn` run gunicorn
5. `Ctrl + A Ctrl + D` to leave session
6. `8000` to verifiy that gunicorn is listening to port 8000
7. You should now be good to close your terminal and still hit the site

### Create duplicate / Snapshot of instance
1. Create snapshot using the `sweet-project-instance` selected as the `Source Disk` option: https://console.cloud.google.com/compute/snapshots?showFTMessage=false&project=sreproject&tab=snapshots&snapshotssize=50
2. Create a new instance and select the snapshot you just created as the `boot disk` option.
3. Ssh into the instance, login as root, and edit the mysite/mysite/settings.py file and add the instance's IP address into the `ALLOWED_HOSTS` array.
4. Run the commands `virtual` and `migrate`
5. Run gunicornm (you may need to run it on a different port like `8001`
6. You should now be able to hit the site via `http://<ip-address>:8001/polls`

## Stop Postgres
1. `sudo su - postgres`
2. `/usr/lib/postgresql/9.6/bin/pg_ctl -D /usr/lib/postgresql/ -l /root/mysite/logfile.txt stop`

### Start Postgres
1. Login as your normal user (not root or postgres)
2. `/usr/lib/postgresql/9.6/bin/pg_ctl -D /root/mysite/db.cluster/ -l /root/mysite/logfile.txt start`

#### Site not working?
Things to check: <br>
1. Try running your browser incognito (it might be appending `https` instead of `http)
2. Is gunicorn running? Run `8000` to see if gunicorn is listening to port 8000
3. Make sure you are hitting the `/polls` or `/admin` endpoint - we have no home page yet

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
