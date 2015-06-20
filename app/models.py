from app import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    def __init__(self, uname, email, password):
        self.uname = uname
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Username - {}>'.format(self.uname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String(140))
    post_body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, title, body, timestamp, author):
        self.post_title=title
        self.post_body=body
        self.timestamp=timestamp
        self.author=author
    
    def __repr__(self):
        return '<Post %r>' % (self.post_body)
