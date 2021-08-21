import pytest
import jwt
from src.auth import auth_register, auth_login

first_name = 'David'
last_name = 'Zhan'
valid_email = 'validemail@gmail.com'
valid_password = '123abc!@#'
new_valid_password = 'abc123@#$'


def test_register_login():
    result = auth_register(valid_email,valid_password,first_name,last_name)
    auth_login(valid_email,valid_password)
    assert result == auth_login(valid_email,valid_password)



