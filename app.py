from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate, MigrateCommand #to migrate the data with command db
#from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES #uploads not working instead , reuploaded is working
from flask_login import LoginManager

app = Flask(__name__)

#instantiate
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Desktop/twitter-clone/engage.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/new_clone'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fzlhtaiwunmeak:e1a639d47e78bd9ea37de5d4f63f7560fe1427312e0214ae90aad701ecb0d1dd@ec2-3-223-242-224.compute-1.amazonaws.com:5432/d24g04jsjb4men'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ksdlfkdsofidsithnaljnfadksjhfdskjfbnjewrhewuirhfsenfdsjkfhdksjhfdslfjasldkj' #cross seite request handling

#instantitate
login_manager = LoginManager(app)
login_manager.login_view = 'login'

configure_uploads(app, photos)

#instantitate
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

#command attached with db
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()