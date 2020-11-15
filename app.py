"""app.py"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
import flask
from flask_sqlalchemy import SQLAlchemy
import flask_socketio
import bot
import models


CHAT_RECEIVED_CHANNEL = 'messages received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.environ['DATABASE_URL']


app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()

def _emit_all_chats(channel):
    all_messages = [ \
        db_message.message for db_message in \
        db.session.query(models.Chat).all()
    ]
    socketio.emit(channel, {
        'allMessages': all_messages
    })
@socketio.on('connect')
def _on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
@socketio.on('login')
def _on_login(data):
    if data['isLoggedIn']:
        _emit_all_chats(CHAT_RECEIVED_CHANNEL)
@socketio.on('disconnect')
def _on_disconnect():
    print ('Someone disconnected!')
@socketio.on('new message input')
def _on_new_address(data):
    print("Got an event for new message input with data:", data)
    db.session.add(models.Chat(data["message"]))
    db.session.commit()
    string= []
    if "!! " in data["message"]:
        if "!! about" in data["message"]:
            db.session.add(models.Chat(bot.about(data["message"])))
            db.session.commit()
        if "!! help" in data["message"]:
            db.session.add(models.Chat(bot.helps(data["message"])))
            db.session.commit()
        if "!! date" in data["message"]:
            db.session.add(models.Chat(bot.dates(data["message"])))
            db.session.commit()
        if "!! funtranslate" in data["message"]:
            string = data["message"]
            word = string.split("!!funtranslate")
            db.session.add(models.Chat(bot.fun_translate(data["message"], word[1])))
            db.session.commit()
    _emit_all_chats(CHAT_RECEIVED_CHANNEL)
@app.route('/')
def _index():
    _emit_all_chats(CHAT_RECEIVED_CHANNEL)
  #  emit_all_oauth_users(USERS_UPDATED_CHANNEL)
    return flask.render_template("index.html")
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', '8080')),
        debug=True
    )
    