from flask import Blueprint, Response, request


def get_ping_blueprint() -> Blueprint:
    blueprint = Blueprint('ping', __name__)

    @blueprint.route('/ping', methods=['GET'])
    def ping() -> Response:
        response = Response(response='pong', status=200, mimetype='text/plain')
        response.headers['Cache-Control'] = 'no-store, must-revalidate'
        if request.environ.get('SERVER_PROTOCOL') == 'HTTP/1.0':
            response.headers['Expires'] = 0
        return response

    return blueprint
