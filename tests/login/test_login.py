import pytest
from tests.login.login_test_data import invalid_credentials, valid_credentials


@pytest.mark.parametrize('email, password, expected_result', valid_credentials)
def test_user_login_positive(user_login_fixture, configure_logging,  email, password, expected_result):

    actual = user_login_fixture.main(email, password)
    expected = expected_result

    if actual == expected:
        configure_logging.info(f'INPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                               f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')
    else:
        configure_logging.error(f'Check if the data is correct\nINPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                                f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')

    assert actual == expected


@pytest.mark.parametrize('email, password, expected_result', invalid_credentials)
def test_user_login_negative(user_login_fixture, configure_logging, email, password, expected_result):

    actual = user_login_fixture.main(email, password)
    expected = expected_result

    if actual == expected:
        configure_logging.info(f'INPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                               f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')
    else:
        configure_logging.error(f'Check if the data is correct\nINPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                                f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')

    assert actual == expected
