#
import requests

#
MAILGUN_APY_KEY = 'edf7959bce6a84d12f16e4470b85e247-7fba8a4e-736c3794'
MAILGUN_URL = 'https://api.mailgun.net/v3/scimagine.com/messages'
FROM_EMAIL = 'Administration <no-reply@mcconstruct.com>'


#
def _send_email(data):
    r = requests.post(MAILGUN_URL, auth=("api", MAILGUN_APY_KEY), data=data)


#
def send_confirmation_email(user, html):
    data = {
        "from": FROM_EMAIL,
        "to": [user.email],
        "subject": "Email Verification",
        "html": html,
    }
    _send_email(data)


#
def send_card_creation_email(user, html):
    data = {
        "from": FROM_EMAIL,
        "to": [user.email],
        "subject": "New card created",
        "html": html
    }
    _send_email(data)


#
def send_service_add_email(user, html):
    data = {
        "from": FROM_EMAIL,
        "to": [user.email],
        "subject": "New service added",
        "html": html
    }
    _send_email(data)
