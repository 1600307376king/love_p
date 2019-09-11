from app import db


class Analysis(db.Model):
    __table_name__ = 'analysis'
    id = db.Column(db.INT, primary_key=True)

    def __init__(self):
        pass
