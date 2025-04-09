import reflex as rx
from ..controllers import ConsultState

def form_add_product():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    value = ConsultState.get_product.identificator,
                    placeholder="Product ID",
                    name="identificator",
                ),
                rx.input(
                    value = ConsultState.get_product.name,
                    placeholder="Name",
                    name="product_name",
                ),
                rx.input(
                    value = ConsultState.get_product.price,
                    placeholder="Price",
                    name="product_price",
                ),
                rx.button('Submit', type='submit'),
            ),
            on_submit=ConsultState.handle_submit,
            reset_on_submit=True,
        ),
    )

def consult_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text('Update Products', size='9'),
            form_add_product(),
        )
    )
