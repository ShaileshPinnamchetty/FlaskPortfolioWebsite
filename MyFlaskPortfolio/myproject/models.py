from myproject import db

class Message(db.Model):

    __tablename__ = 'message'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    message = db.Column(db.Text)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f"Message from {self.name}: {self.message} -- Email: {self.email} -- MsgID: {self.id}"