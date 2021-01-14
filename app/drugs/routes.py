from app.drugs import bp 
from app import db
from app.drugs.models import Drug, Effect
from app.errors import errors

@bp.route('/')
def hello_world():
	return "Hello World!"


@bp.route('/<string:name>/info', methods=['GET'])
def get_drug_info(name):
	return "Hello " + name + "!"


@bp.route('/<string:name>/conditions', methods=['GET'])
def get_drug_conditions(name):
	return "Hello " + name + "!"


@bp.route('/<string:name>/effects', methods=['GET'])
def get_drug_effects(name):
	drugs = db.session.query(Drug).filter(Drug.name == name)
	if not drugs:
		return errors.bad_request('drug with name '+name+' does not exist')
	
	return "Hello " + name + "!"
