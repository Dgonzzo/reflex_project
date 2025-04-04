import reflex as rx


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

            # ! FormState has to be changed
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
    )

def add_product_page() -> rx.Component:
    return rx.container(
        rx.text("Add Products", size="9"),
        form_add_product(),

    ),