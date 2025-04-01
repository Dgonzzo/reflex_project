import reflex as rx
from ..state import MyState

def delete_product_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Show Products", size="9"),
        rx.hstack(
            rx.text("Product Name", size="4"),
            rx.text("Product Price", size="4"),
            rx.text("Product Description", size="4"),
            spacing="2",
        ),
        spacing="8",
        justify="center",
        align="center",
        min_height="85vh",
    )
  