from app import db 


class Drug(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), index=True, unique=True)
	interventions = db.relationship('Intervention', backref='drug', lazy='dynamic')
	effects = db.relationship('Effect', backref='drug', lazy='dynamic')
	

class Condition(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True, unique=True)
	interventions = db.relationship('Intervention', backref='condition', lazy='dynamic')


class Intervention(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	score = db.Column(db.Integer, index=True)
	no_studies = db.Column(db.Integer)
	no_tested = db.Column(db.Integer)
	drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))
	condition_id = db.Column(db.Integer, db.ForeignKey('condition.id'))


class Effect(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True)
	percent_effected = db.Column(db.Integer)
	no_effected = db.Column(db.Integer)
	drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))
