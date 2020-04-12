import pytest
from api import create_app, db
from api.models import User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
     # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()
    
    
@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    user1 = User('nonsoamadi@aol.com')
    user1.set_password('biggie10')
    db.session.add(user1)
    db.session.commit()
    
    yield db
    
    db.drop_all()

@pytest.fixture(scope='module')
def new_user():
    new_user = User(email='amadi@gmail.com')
    new_user.set_password('cat')
    return new_user