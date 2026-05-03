from user import User 

def test_profile_format():
    user = User(name="mujab")
    assert user.get_profile() == "Name : mujab"

def test_empty_name():
    user = User(name=" ")
    assert "Name : " in user.get_profile()