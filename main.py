from fastapi import FastAPI

app = FastAPI()


@app.get('/', description='GET Methods Example')
async def get():
    return {"message": "GET Methods"}


@app.post('/', description='POST Methods Example')
async def post():
    return {"message": "POST Methods"}


@app.put('/{id}/update', description='PUT Methods Example')
async def put():
    return {"message": "PUT Methods"}


@app.patch('/{id}/update', description='PATCH Methods Example')
async def patch():
    return {"message": "PATCH Methods"}


@app.delete('/{id}/delete', description='DELETE Methods Example')
async def delete():
    return {"message": "DELETE Methods"}


@app.get('/items', description='Item List')
async def get_item():
    return {"message": "Item List"}


@app.get('/items/{item_id}', description='Get Item by ID')
async def get_item_id(item_id: int):
    return {"message": item_id}
