import pytest

from saas.app import create_app


@pytest.fixture(scope="session")
def app():
    """
    Setup Flask test app

    :return: Flask app
    """
    params = {"DEBUG": False, "TESTING": True}

    # override app settings, create a new app context to use for testing
    _app = create_app(settings_override=params)
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="function")
def client(app):
    """
    Setup an app client for test functions

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
