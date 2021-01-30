import json


def test_create_post_no_tags(test_client, init_database, load_posts_test_data):
    post_data = load_posts_test_data
    post = post_data['posts'][0]
    response = test_client.post('/board/posts', data=json.dumps(post), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200


def test_create_post_with_tags(test_client, init_database, load_posts_test_data):
    post_data = load_posts_test_data
    post = post_data['posts'][1]
    response = test_client.post('/board/posts', data=json.dumps(post), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200


def test_create_comment(test_client, init_database, load_users_test_data, load_posts_test_data, load_comments_test_data):
    post_data = load_posts_test_data
    post = post_data['posts'][1]
    comment_data = load_comments_test_data
    comment = comment_data['comments'][0]
    user_data = load_users_test_data
    user = user_data['valid_user_conditions']

    login_request = dict(username=user['username'], password=user['password'])
    login_response = test_client.post('/drugs/login', data=json.dumps(login_request), headers={'Content-Type': 'application/json'})
    assert login_response.status_code == 200

    comment_request = dict(**comment, post_id=post[''])

