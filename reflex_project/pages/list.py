import reflex as rx
from ..controllers import ListState
from ..models import Product

def show_products(product: Product):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(rx.link(product.identificator, href=f"consultar/{product.id}")),
        rx.table.cell(product.name),
        rx.table.cell(product.price),
    )

def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Identificator"),
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Price"),
            ),
        ),
        rx.table.body(
            rx.foreach(ListState.products, show_products)
        ),
        width="100%",
    )

def show_list() -> rx.Component:
    return  rx.container(
        foreach_table_example(),
    ),