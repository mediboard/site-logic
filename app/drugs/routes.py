from app.drugs import bp
from app import db
from app.drugs.models import Drug, Effect
from app.errors import errors

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def success_response(message):
	payload = {'status': HTTP_STATUS_CODES.get(200, 'Unknown error')}
	if message:
		payload['message'] = message
	response = jsonify(payload)
	response.status_code = 200
	return response


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
	drug = Drug.query.filter_by(name=name).first()
	if not drug:
		return errors.bad_request('drug with name ' + name + ' does not exist')

	effects = Effect.query.filter_by(drug_id=drug.id).all()
	effects.sort(reverse=True, key=lambda x: x.no_effected)
	return success_response(
		{'effects': [effect.to_dict() for effect in effects]})


@bp.route('/top', methods=['GET'])
def get_top_drugs():
	drugs = Drug.query.all()
	return success_response({'drugs': [drug.to_dict() for drug in drugs]})

