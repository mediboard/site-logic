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
	tags = db.relationship('Tag', backref='drug', lazy='dynamic')

	def to_dict(self):
		return {
			"id": self.id,
			"name": self.name
		}


class Condition(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True, unique=True)
	interventions = db.relationship('Intervention', backref='condition', lazy='dynamic')
	afflictions = db.relationship('Affliction', backref='condition', lazy='dynamic')
	tags = db.relationship('Tag', backref='condition', lazy='dynamic')

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


class Affliction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	condition_id = db.Column(db.Integer, db.ForeignKey('condition.id'))
	condition_name = db.Column(db.String(100))  # TODO this is asking for trouble

	def to_dict(self):
		return {
			'id': self.id,
			'user_id': self.user_id,
			'condition_id': self.condition_id,
			'condition_name': self.condition_name
		}


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), index=True, unique=True)
	email = db.Column(db.String(100), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	afflictions = db.relationship('Affliction', backref='user', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def to_dict(self):
		return {
			'id': self.id,
			'username': self.username,
			'email': self.email
		}


@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(2000))
	likes = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	condition_id = db.Column(db.Integer, db.ForeignKey('condition.id'))
	drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), index=True)
	body = db.Column(db.String(6000))  # This might be a little too low
	likes = db.Column(db.Integer)
	category = db.Column(db.String(50), index=True)
	tags = db.relationship('Tag', backref='post', lazy='dynamic')
	comments = db.relationship('Comment', backref='post', lazy='dynamic')


