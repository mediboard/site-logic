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



