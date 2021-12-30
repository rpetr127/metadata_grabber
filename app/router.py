import asyncio

from app import app, request
from app.controller import home, radio_metadata


@app.route('/')
async def index():
    if request.args.get('name'):
        name = request.args.get('name')
        metadata = await radio_metadata(name)
        return metadata
    else:
        return home()

@app.route('/streams')
def result():
    data = radio_metadata()
    return data