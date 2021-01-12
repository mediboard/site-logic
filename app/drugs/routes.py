from app.drugs import bp 


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
	return "Hello " + name + "!"
