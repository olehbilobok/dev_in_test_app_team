import pytest
from tests.sidebar.sidebar_test_data import valid_data, invalid_data


@pytest.mark.parametrize('email, password, expected_result', valid_data)
def test_user_login_positive(sidebar_fixture, configure_logging,  email, password, expected_result):

    actual = sidebar_fixture.sidebar_main(email, password)
    expected = expected_result

    if actual == expected:
        configure_logging.info(f'INPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                               f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')
    else:
        configure_logging.error(f'Check if the data is correct\nINPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                                f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')

    assert actual == expected


@pytest.mark.parametrize('email, password, expected_result', invalid_data)
def test_user_login_negative(sidebar_fixture, configure_logging,  email, password, expected_result):

    actual = sidebar_fixture.sidebar_main(email, password)
    expected = expected_result

    if actual == expected:
        configure_logging.info(f'INPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                               f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')
    else:
        configure_logging.error(f'Check if the data is correct\nINPUT DATA:\nEMAIL={email}, PASSWORD={password}\n'
                                f'OUTPUT DATA:\nACTUAL={actual}\nEXPECTED={expected}')

    assert actual == expected
