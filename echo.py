#!/usr/bin/env python3
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    return {
        "method": request.method,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "data": request.get_json(force=True, silent=True),
    }

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', '--port', type=int, help='port', default=5000)
    parser.add_argument('--host', default='127.0.0.1', help='host to listen on')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=True)
