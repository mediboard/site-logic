from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Drug(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), index=True, unique=True)
	brand_name = db.Column(db.String(40))
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


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), index=True, unique=True)
	email = db.Column(db.String(100), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))

