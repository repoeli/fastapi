from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import logging
import time

app = FastAPI()
items = {}
current_id = 0

# Logging setup
logging.basicConfig(
    filename='api.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    log_data = {
        "method": request.method,
        "url": str(request.url),
        "status_code": response.status_code,
        "process_time": process_time
    }
    logging.info(log_data)
    return response

class Item(BaseModel):
    name: str
    price: float

@app.post("/item")
async def create_item(item: Item):
    global current_id
    current_id += 1
    items[current_id] = item.dict()
    return {"id": current_id, **item.dict()}

# Advanced step : Validate GET Parameters
@app.get("/item")
async def read_item(request: Request):
    params = request.query_params
    if not params:
        raise HTTPException(status_code=400, detail="No parameters provided")
    total = 0
    errors = []
    for key, value in params.items():
        try:
            total += int(value)
        except ValueError:
            errors.append(f"Parameter '{key}' must be an integer")
    if errors:
        raise HTTPException(status_code=400, detail=errors)
    return {"sum": total}

@app.put("/item/{id}")
async def update_item(id: int, item: Item):
    if id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[id] = item.dict()
    return {"id": id, **item.dict()}

@app.delete("/item/{id}")
async def delete_item(id: int):
    if id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[id]
    return {"message": "Item deleted"}