from app import db


class BuYiJu(db.Model):
    __table_name__ = 'buyiju'
    id = db.Column(db.INT, primary_key=True)
    obj = db.Column(db.String(255))
    score = db.Column(db.String(255))
    res = db.Column(db.TEXT)

    def __init__(self, kwargs):
        self.obj = kwargs['obj']
        self.score = kwargs['score']
        self.res = kwargs['res']
