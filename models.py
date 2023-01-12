from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid, secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Meme(db.Model):
    id = db.Column(db.String, primary_key=True)
    meme_url = db.Column(db.String)

    def __init__(self, id, meme_url):
        self.id = id
        self.meme_url = meme_url

    def __repr__(self):
        return 'Meme template added to database'

class UserMeme(db.Model):
    id = db.Column(db.String, primary_key=True)
    meme_template = db.Column(db.String, db.ForeignKey('meme.id'), nullable=False)
    meme_url = db.Column(db.String, nullable=True)
    user_token = db.Column(db.String, nullable=False)
    user_input1 = db.Column(db.String, nullable=False)
    user_input2 = db.Column(db.String, nullable=True)
    user_input3 = db.Column(db.String, nullable=True)
    user_input4 = db.Column(db.String, nullable=True)
    input1_positioning = db.Column(db.JSON, nullable=False)
    input2_positioning = db.Column(db.JSON, nullable=True)
    input3_positioning = db.Column(db.JSON, nullable=True)
    input4_positioning = db.Column(db.JSON, nullable=True)


    def __init__(self, meme_template, meme_url, user_token, user_input1, user_input2, user_input3, user_input4, input1_positioning, input2_positioning, input3_positioning, input4_positioning):
        self.id = self.set_id()
        self.meme_template = meme_template
        self.meme_url = meme_url
        self.user_token = user_token
        self.user_input1 = user_input1
        self.user_input2 = user_input2
        self.user_input3 = user_input3
        self.user_input4 = user_input4
        self.input1_positioning = input1_positioning
        self.input2_positioning = input2_positioning
        self.input3_positioning = input3_positioning
        self.input4_positioning = input4_positioning

    def set_id(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return 'A meme has been added to the database'

class MemeSchema(ma.Schema):
    class Meta:
        fields = ['id', 'meme_template', 'meme_url', 'user_input1', 'user_input2', 'user_input3', 'user_input4', 'input1_positioning', 'input2_positioning', 'input3_positioning', 'input4_positioning']

meme_schema = MemeSchema()
meme_schemas = MemeSchema(many=True)


