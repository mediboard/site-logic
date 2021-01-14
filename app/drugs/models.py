from app import db 


class Drug(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), index=True, unique=True)
	interventions = db.relationship('Intervention', backref='drug', lazy='dynamic')
	effects = db.relationship('Effect', backref='drug', lazy='dynamic')

	def to_dict(self):
		return {
			"id": self.id,
			"name": self.name
		}


class Condition(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True, unique=True)
	interventions = db.relationship('Intervention', backref='condition', lazy='dynamic')

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name
		}


class Intervention(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	score = db.Column(db.Integer, index=True)
	no_studies = db.Column(db.Integer)
	no_tested = db.Column(db.Integer)
	drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))
	condition_id = db.Column(db.Integer, db.ForeignKey('condition.id'))

	def to_dict(self):
		return {
			'id': self.id,
			'score': self.score,
			'no_studies': self.no_studies,
			'no_tested': self.no_tested,
			'drug_id': self.drug_id,
			'condition_id': self.condition_id
		}


class Effect(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True)
	percent_effected = db.Column(db.Integer)
	no_effected = db.Column(db.Integer)
	drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'percent_effected': self.percent_effected,
			'no_effected': self.no_effected,
			'drug_id': self.drug_id
		}
