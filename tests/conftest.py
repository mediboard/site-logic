import pytest
import json

from app import create_app
from app import db


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

    yield db

    db.drop_all()
