#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os
import sys
import webbrowser

def main():
    greeting()
    #stepsToRun = sys.argv[1] or steps
    #steps = [A_CreateVM, B_CreateDatabase, C_CreateVirtualPythonEnv, D_CreateDjangoProject, E_RunGunicornServer, F_IntegrateNGINXListener, G_DeployAndTestDjangoApp]
    #map(lambda stepFunc: stepFunc(), steps)

    A_CreateVM()
    B_CreateDatabase()
    C_CreateVirtualPythonEnv()
    D_CreateDjangoProject()
    E_RunGunicornServer()
    F_IntegrateNGINXListener()
    G_DeployAndTestDjangoApp()

def A_CreateVM():
    print("\n\n=== A: Creating a VM and Install Infrastructure Softwareprint===\n")
    run('sudo apt update')
    run('sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl')

def B_CreateDatabase():
    print("\n=== B: Creating a Postgres Database ===\n")
    print("Need to run something like this here: psql -U postgres postgres -f setupDB.sql\n")
    # run('psql -U postgres postgres -f setupDB.sql')

    ### This doesn't work - it doesn't type the commands into postgres interactive mode
    #run('sudo -u postgres psql')
    # os.system('CREATE DATABASE sreproject;')
    # os.system("CREATE USER sreprojectuser WITH PASSWORD 'trump';")
    # os.system("ALTER ROLE sreprojectuser SET client_encoding TO 'utf8';")
    # os.system("ALTER ROLE sreprojectuser SET client_encoding TO 'utf8';")
    # os.system("ALTER ROLE sreprojectuser SET timezone TO 'UTC';")
    # os.system('GRANT ALL PRIVILEGES ON DATABASE sreproject TO sreprojectuser;')
    # os.system('\\q')

def C_CreateVirtualPythonEnv():
    print("=== C: Creating an Isolated Python Environment ===\n")
    os.system('sudo -H pip3 install --upgrade pip')
    os.system('sudo -H pip3 install virtualenv')
    os.system('mkdir ~/sreprojectdir')
    os.system('cd ~/sreprojectdir')
    os.system('virtualenv sreprojectenv')
    os.system('. sreprojectenv/bin/activate')
    os.system('pip install django gunicorn psycopg2-binary')

def D_CreateDjangoProject():
    print("=== D: Creating and Configuring a New Django Project ===\n")
    os.system('django-admin.py startproject sreproject ~/sreprojectdir')
    os.system('cd ~/sreprojectdir/sreproject')
    os.system('cp ~/Automation/settings.py ./settings.py')
    os.system('~/sreprojectdir/manage.py makemigrations')
    os.system('~/sreprojectdir/manage.py migrate')
    os.system('~/sreprojectdir/manage.py createsuperuser')
    os.system('apple')
    os.system('aasquier@pdx.edu')
    os.system('orange')
    os.system('orange')
    os.system('~/sreprojectdir/manage.py collectstatic')
    os.system('yes')

    webbrowser.open('https://console.cloud.google.com/compute/instancesDetail/zones/us-central1-a/instances/instance-1?project=cs410-site-reliability-eng&organizationId=39525358122&supportedpurview=project')
    input("Press Enter to continue...")

    os.system('~/sreprojectdir/manage.py runserver 0.0.0.0:8000')

    webbrowser.open('http://34.67.211.3:8000')
    input("Press Enter to continue...")

def E_RunGunicornServer():
    print("=== E: Integrating Gunicorn Application Server ===\n")
    os.system('cd ~/sreprojectdir')
    os.system('gunicorn --bind 0.0.0.0:8000 sreproject.wsgi')

    webbrowser.open('http://34.67.211.3:8000')
    input("Press Enter to continue...")

def F_IntegrateNGINXListener():
    print("=== F: Integrating NGINX Web Listener ===\n")
    os.system('sudo su -')
    os.system('cd /etc/nginx/sites-available')
    os.system('cp /home/aasquier/Automation/sreproject ./')
    os.system('chown root ./sreproject')
    os.system('ln -s /etc/nginx/sites-available/sreproject ../sites-enabled/sreproject')
    os.system('rm ../sites-enabled/default')
    os.system('nginx -t')
    input("Press Enter to continue...")

    os.system('systemctl restart nginx')
    webbrowser.open('http://34.67.211.3')
    input("Press Enter to continue...")

def G_DeployAndTestDjangoApp():
    print("=== G: Deploying and Testing Application ===\n")
    print("Checking Django was installed...")
    os.system("python -m django --version")
    os.system("django-admin startproject djangoSite")

def greeting():
    print("\n=== Welcome to Assignment #2 Site Builder! ===\n")
    print("This script will:\n")
    print("  A: Create a VM and Install Infrastructure Softwareprint")
    print("  B: Create a Postgres Database")
    print("  C: Create an Isolated Python Environment")
    print("  D: Create and Configure a New Django Project")
    print("  E: Integrate Gunicorn Application Server")
    print("  F: Integrate NGINX Web Listener")
    print("  G: Deploy and Test Application")

def run(command):
    print("\n* Running: " + command)
    os.system(command)

main()
