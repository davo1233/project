import pytest
from src.auth import *

first_name = 'David'
last_name = 'Zhan'
valid_email = 'validemail@gmail.com'
valid_password = '123abc!@#'
new_valid_password = 'Make America Gr8 Again!'


def test_login_with_registered_valid_account():
    clear_v1()
    result = auth_register(valid_email,valid)

