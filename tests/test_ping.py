

def test_http_1_0_ping_response(client):
    response = client.get('/ping', environ_overrides={'SERVER_PROTOCOL': 'HTTP/1.0'})

    assert response.status_code == 200
    assert response.content_type == 'text/plain; charset=utf-8'
    assert response.data == b'pong'
    assert response.headers['Cache-Control'] == 'no-store, must-revalidate'
    assert response.headers['Expires'] == '0'


def test_http_1_1_ping_response(client):
    response = client.get('/ping', environ_overrides={'SERVER_PROTOCOL': 'HTTP/1.1'})

    assert response.status_code == 200
    assert response.content_type == 'text/plain; charset=utf-8'
    assert response.data == b'pong'
    assert response.headers['Cache-Control'] == 'no-store, must-revalidate'
    assert response.headers.get('Expires') is None
