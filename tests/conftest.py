from flask import Flask
import pytest

from flask_ping import get_ping_blueprint


@pytest.fixture(scope='module')
def client():
    app = Flask('flask_ping.flask_test_app')
    app.register_blueprint(get_ping_blueprint())
    return app.test_client()
