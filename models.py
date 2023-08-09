from app import db



#setting up db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
   
    def __repr__(self):
        return f'<Student {self.title} was created {self.date}>'