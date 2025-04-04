import reflex as rx

def add_product_page() -> rx.Component:
    return rx.container(
        rx.heading("Add Product", size="9"),
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