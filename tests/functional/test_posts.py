import json


def test_create_new_post_no_tags(test_client, init_database, load_posts_test_data):
    post_data = load_posts_test_data
    post = post_data['posts'][0]
    response = test_client.post('/board/posts', data=json.dumps(post), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200
