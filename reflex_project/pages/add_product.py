import reflex as rx
from ..controllers import AddState

def form_add_product():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Product ID",
                    name="identificator",
                ),
                rx.input(
                    placeholder="Name",
                    name="product_name",
                ),
                rx.input(
                    placeholder="Price",
                    name="product_price",
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=AddState.handle_submit,
            reset_on_submit=True,
        ),
        align="center",
        justify="center",
    )

def add_product_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Add Products", size="9"),
            form_add_product(),  
        )
    ),