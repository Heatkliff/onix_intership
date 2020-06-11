from django.core.mail import send_mail
from onix.celery import app


@app.task
def country_created(mail):
    message = 'Congratulations! Your country was successfully added!'
    send_mail('Country created',
              message,
              'admin@world.com',
              [mail])


@app.task
def country_updated(mail, name, link):
    message = f"Your country {name} was changed.\n You can view changes at {link}"
    send_mail("Country update",
              message,
              'admin@world.com',
              [mail])


@app.task
def periodic_task():
    print('TASK-20')
