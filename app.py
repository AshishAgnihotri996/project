from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager



app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Desktop/twitter-clone/engage.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cfklubtewoobrk:b01635c2fa9bba29e70c07b8389b4aefa1bfbf30587d49826e314b69190d555e@ec2-50-19-255-190.compute-1.amazonaws.com:5432/d493ujk0fq25q'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ksdlfkdsofidsithnaljnfadksjhfdskjfbnjewrhewuirhfsenfdsjkfhdksjhfdslfjasldkj'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.template_filter('time_since')
def time_since(delta):

    seconds = delta.total_seconds()

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        return '%dd' % (days)
    elif hours > 0:
        return '%dh' % (hours)
    elif minutes > 0:
        return '%dm' % (minutes)
    else:
        return 'Just now'

from views import *


if __name__ == '__main__':
    app.run()