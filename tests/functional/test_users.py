import json


def test_register_valid(test_client, init_database, load_users_test_data):
    users = load_users_test_data
    valid_user = users['valid_user']
    request = dict(username=valid_user['username'], password=valid_user['password'], email=valid_user['email'])
    response = test_client.post('/drugs/register', data=json.dumps(request), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200


def test_register_dupe_username(test_client, init_database, load_users_test_data):
    valid_user = load_users_test_data['valid_user']
    request = dict(username=valid_user['username'], password=valid_user['password'], email=valid_user['email'])
    response = test_client.post('/drugs/register', data=json.dumps(request), headers={'Content-Type': 'application/json'})

    assert response.status_code == 400


def test_register_with_conditions(test_client, init_database, load_users_test_data):
    user = load_users_test_data['valid_user_conditions']
    request = dict(username=user['username'], password=user['password'], email=user['email'], conditions=user['conditions'])
    response = test_client.post('/drugs/register', data=json.dumps(request), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200


def test_valid_user_login(test_client, init_database, load_users_test_data):
    user = load_users_test_data['valid_user_conditions']
    request = dict(username=user['username'], password=user['password'])
    response = test_client.post('/drugs/login', data=json.dumps(request), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200
