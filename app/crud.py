import uuid
from . models import Product, ProductScrapeEvent
import copy

# session = get_session()
# sync_table(Product)
# sync_table(ProductScrapeEvent)

# product = ProductSchema(**data)

def create_entry(data:dict):
    return Product.create(**data)

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() # includes timestamp in it
    return ProductScrapeEvent.create(**data)

def add_scrape_entry(data:dict, fresh=False):
    if fresh:
        data = copy.deepcopy(data)
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product, scrape_obj
