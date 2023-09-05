from enum import Enum
import uvicorn
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


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get('/foods/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "Vegetables"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "Fruits"}

    return {"food_name": food_name, "message": "Dairy"}


fake_items_db = [
    {"item_name": "Foo"}, {"item_name": "Foo2"}, {"item_name": "Foo3"}, {"item_name": "Foo4"}
]


@app.get('/items', description='Item List')
async def get_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}', description='Get Item by ID')
async def get_item_id(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({
            "q": q
        })
    if not short:
        item.update({
            "description": "Lorem Ipsum do not....."
        })
    return item


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)