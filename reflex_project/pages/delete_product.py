import reflex as rx
from ..controllers import UpdateState

def form_update_product():
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
            on_submit=UpdateState.handle_update,
            reset_on_submit=True,
        ),
        align="center",
        justify="center",
    )

# def add_product_page() -> rx.Component:
#     return rx.container(
#         rx.vstack(
#             rx.text("Add Products", size="9"),
#             form_add_product(),  
#         )
#     ),

def delete_update_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Delete/Update", size="9"),
            form_update_product(),
        ),
        align="center",
        justify="center",
    )
  