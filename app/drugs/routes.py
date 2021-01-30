from app.drugs import bp
from app import db
from app.models import Drug, Effect, User, Condition, Affliction
from app.errors import errors

from flask import jsonify, request
from werkzeug.http import HTTP_STATUS_CODES
from flask_login import login_user
from sqlalchemy import or_


def success_response(message):
    payload = {'status': HTTP_STATUS_CODES.get(200, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = 200
    return response


def get_drug_if_exists(drug_name):
    return Drug.query.filter(or_(Drug.name == drug_name, Drug.brand_name == drug_name)).first()


def get_condition_if_exists(condition_name):
    return Condition.query.filter_by(name=condition_name).first()


@bp.route('/')
@bp.route('/index')
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


@bp.route('/login', methods=['GET', 'POST'])
def login():
    data = request.json or {}
    user = User.query.filter_by(username=data.get('username', '')).first()
    if user is None or not user.check_password(data.get('password', '')):
        return errors.bad_request("username or password incorrect")

    login_user(user, remember=True)

    return success_response({'user': user.to_dict(),
                             'conditions': [a.to_dict() for a in user.afflictions]})


# TODO add email validation
# TODO make sure this lines up with the front end
# TODO dont allow empty user names
@bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    user = User.query.filter_by(username=data.get('username', '')).first()
    if user is not None:
        return errors.bad_request("username already taken")

    user = User.query.filter_by(email=data.get('email', '')).first()
    if user is not None:
        return errors.bad_request("account with this email already exists")

    new_user = User()
    new_user.username = data['username']  # Should already be checked by this point
    new_user.email = data['email']  # ditto
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    conditions = Condition.query.filter(Condition.id.in_([x['name'] for x in data.get('conditions', [])])).all()
    for condition in conditions:
        db.session.add(Affliction(user_id=new_user.id, condition_id=condition.id))
    db.session.commit()

    login_user(new_user)
    return success_response('user signed up')

