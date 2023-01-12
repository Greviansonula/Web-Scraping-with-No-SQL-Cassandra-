from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]

class ProductListSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]

class ProductScrapeEventSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]
    price_str: Optional[str]

class ProductScrapeDetailEventSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]