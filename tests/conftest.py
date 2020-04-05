import pytest
from api.models import User

@pytest.fixture(scope='module')
def new_user():
    new_user = User(email='amadi@gmail.com')
    new_user.set_password('cat')
    return new_user