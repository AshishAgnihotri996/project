from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate, MigrateCommand #to migrate the data with command db
from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES #uploads not working instead , reuploaded is working
from flask_login import LoginManager

app = Flask(__name__)

#instantiate
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Desktop/twitter-clone/engage.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/new_clone'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uhmmfxnusjcuzn:c2fe993a81dd023ab9017003349aff9e1c110f65239749cb8a2b3b16907eb058@ec2-44-205-112-253.compute-1.amazonaws.com:5432/dbpkmc0aiuhrba'
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
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()