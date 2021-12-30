from flask import Flask, request

from .app.controller import home, radio_metadata


server = Flask(__name__)


@server.route('/')
async def index():
    if request.args.get('name'):
        name = request.args.get('name')
        metadata = await radio_metadata(name)
        return metadata
    else:
        return home()
