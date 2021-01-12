from app import db 


class Drug(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), index=True, unique=True)


class Condition(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True, unique=True)


class Intervention(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	score = db.Column(db.Integer, index=True)
	no_studies = db.Column(db.Integer)
	no_tested = db.Column(db.Integer)
	