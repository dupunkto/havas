from flask_sqlalchemy import SQLAlchemy
import random
import string
import json


def random_base36_id(length=8):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choices(chars, k=length))


db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.String(8), primary_key=True, default=random_base36_id)

    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    content = db.Column(db.Text, nullable=False)
    html = db.Column(db.Text, nullable=False)

    authors_json = db.Column(db.Text, nullable=True)
    tags_json = db.Column(db.Text, nullable=True)

    datetime_made = db.Column(db.DateTime, nullable=False)
    datetime_edited = db.Column(db.DateTime, nullable=False)

    cover_image_id = db.Column(db.String(12), nullable=True)

    archived = db.Column(db.Boolean, default=False)

    @property
    def authors(self):
        return json.loads(self.authors_json or "[]")

    @authors.setter
    def authors(self, value):
        self.authors_json = json.dumps(value)

    @property
    def tags(self):
        return json.loads(self.tags_json or "[]")

    @tags.setter
    def tags(self, value):
        self.tags_json = json.dumps(value)
