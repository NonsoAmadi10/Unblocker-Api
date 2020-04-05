def test_new_user(new_user):
    """
    GIVEN a User Model
    WHEN a new User is created
    THEN the credentials should be correct
    """
    assert new_user.email == 'amadi@gmail.com'
    assert new_user.password_hash != 'cat'