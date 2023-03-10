from fastapi import FastAPI
from typing import List

from cassandra.cqlengine.management import sync_table
from . import (
    config,
    db,
    models,
    schema
)

settings = config.get_settings()

Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

app = FastAPI()

session = None

@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(Product)
    sync_table(ProductScrapeEvent)

@app.get("/products", response_model=List[schema.ProductListSchema])
def products_list_view():
    return list(Product.objects.all())

@app.get("/products/{asin}",)
def products_detail_view(asin):
    data = dict(Product.objects.get(asin=asin))
    events = list(ProductScrapeEvent.objects().filter(asin=asin))
    events = [schema.ProductScrapeDetailEventSchema(**x) for x in events]
    data['events'] = events
    return data