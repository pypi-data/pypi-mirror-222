import sys
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '..'))
from src.external_user import ExternalUser
import pytest
import dotenv
from datetime import datetime



dotenv.load_dotenv()

USER_EXTERNAL="TEST"+str(datetime.now())

@pytest.mark.test
def test_insert_get():
    ExternalUser.insert_or_update_external_user_access_token(
        USER_EXTERNAL, 2, 1, "access_token_test")
    token = ExternalUser.get_access_token(USER_EXTERNAL, 2, 1)
    assert token[0] == "access_token_test"


@pytest.mark.test
def test_update_access_token():
    ExternalUser.update_user_external_access_token(USER_EXTERNAL, 1, 2, "access_token_test2")
    token = ExternalUser.get_access_token(USER_EXTERNAL, 2, 1)
    assert token[0] == "access_token_test2"


@pytest.mark.test
def test_delete_access_token():
    ExternalUser.delete_access_token(USER_EXTERNAL, 1, 2)
    token = ExternalUser.get_access_token(USER_EXTERNAL, 2, 1)
    assert token is None

