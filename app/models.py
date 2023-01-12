from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


# List View -> Detail View
class Product(Model): # -> table
    __keyspace__ = "scrapped_data"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")

# Detail View for asin
class ProductScrapeEvent(Model): # -> table
    __keyspace__ = "scrapped_data"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")

# def this -> ProductScrapeEvent.objects().filter(asin="SFDFFS")

# not this -> Product.objects().filter(titile="Mark 3")

data = {
    "asin" : "TESTING1D23",
    "title" : "Mark 7898",
}