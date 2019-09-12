from app import db


class FirstConstellation(db.Model):
    __table_name__ = 'first_constellation'
    id = db.Column(db.INT, primary_key=True)
    obj = db.Column(db.String(255))
    score = db.Column(db.String(255))
    love = db.Column(db.TEXT)
    family = db.Column(db.TEXT)
    friendly = db.Column(db.TEXT)
    note = db.Column(db.TEXT)

    def __init__(self, kwargs):
        self.obj = kwargs['obj']
        self.score = kwargs['score']
        self.love = kwargs['love']
        self.family = kwargs['family']
        self.friendly = kwargs['friendly']
        self.note = kwargs['note']
