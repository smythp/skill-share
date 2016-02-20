from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(5000), index=True, unique=True)

# class Game(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
