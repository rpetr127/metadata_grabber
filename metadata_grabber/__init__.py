from flask import Flask, request
from .database import table


app = Flask(__name__)

@app.route('/')
async def index():
    from .controller import home, radio_metadata

    if request.args.get('name'):
        name = request.args.get('name')
        metadata = await radio_metadata(name, table)
        return metadata
    else:
        return home()


def main(app):
    app.run('127.0.0.1', 5050)