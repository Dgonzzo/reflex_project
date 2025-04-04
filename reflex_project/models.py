import reflex as rx

class Product(rx.Model, table=True):
    identificator: int
    name: str
    description: str
    