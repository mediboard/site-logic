import pytest
import json

from app import create_app
from app import db
from app.models import Drug, User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope='module')
def load_users_test_data():
    with open('testdata/users.json') as f:
        users = json.load(f)
        f.close()
        return users


@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    db.session.add(Drug(name='Gabapentin', brand_name='Neurontin'))

    db_user = User()
    db_user.id = 10
    db_user.username = 'username'
    db_user.email = 'username@me.com'
    db_user.set_password('password')
    db.session.add(db_user)
    db.session.commit()

    yield db

    db.drop_all()


@pytest.fixture(scope='module')
def load_posts_test_data():
    with open('testdata/posts.json') as f:
        posts = json.load(f)
        f.close()
        return posts


@pytest.fixture(scope='model')
def load_comments_test_data():
    with open('testdata/comments.json') as f:
        comments = json.load(f)
        f.close()
        return comments