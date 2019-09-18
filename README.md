# Flask-ping
Blueprint for a `/ping` endpoint that can be added to python [Flask](https://flask.palletsprojects.com/en/1.1.x/) applications.

## Usage
To add the `/ping` endpoint to your application add the following:
```python
from flask_ping import get_ping_blueprint

app.register_blueprint(get_ping_blueprint())
```

Once registered, you will be able to access the following endpoint:

 GET `/ping`

Response:

DATA `pong`

STATUS 200

Headers:

`Content-type: text/plain`

`Cache-Control: no-store, must-revalidate`

See [ping.py](flask_ping.ping.py) for implementation details
