

from flask import Flask
import flask_cache
import ses_mailer
import flask_mail
import flask_cloudy
import flask_recaptcha
from juice import Juice
from juice.ext import mail, cache, storage, recaptcha, csrf

conffile = "config.py"

_ = Juice(__name__, config=conffile)

# Recaptcha
def test_recaptcha():
    assert isinstance(recaptcha, flask_recaptcha.ReCaptcha)

# Storage
def test_storage():
    assert isinstance(storage, flask_cloudy.Storage)

# Cache
def test_cache():
    assert isinstance(cache, flask_cache.Cache)

# Mailer
def test_mailer_none():
    assert mailer.mail is None

def test_mailer_ses():
    app = Flask(__name__)
    app.config.update(**{
        "MAILER_PROVIDER": "SES",
        "MAILER_SES_ACCESS_KEY": "",
        "MAILER_SES_SECRET_KEY": ""
    })
    mailer.init_app(app)
    assert isinstance(mailer.mail, ses_mailer.Mail)

def test_mailer_smtp():
    app = Flask(__name__)
    app.config.update(**{
        "MAILER_PROVIDER": "SMTP",
        "MAILER_SMTP_URI": "smtp://user:pass@mail.google.com:25",
        "DEBUG": False,
        "TESTING": False
    })

    mailer.init_app(app)
    assert isinstance(mailer.mail, flask_mail.Mail)