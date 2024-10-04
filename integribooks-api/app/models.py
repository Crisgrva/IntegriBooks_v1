from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean, default=False)
    cover = db.Column(db.String(255))

    def __repr__(self):
        return f'<Book {self.id}: {self.title} by {self.author}>'
