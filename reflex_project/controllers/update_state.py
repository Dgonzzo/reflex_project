import reflex as rx
from ..models import Product

class UpdateState(rx.State):
    form_data: dict = {}
    actual_product: Product = None

    @rx.event
    def handle_update(self, form_data: dict):
        self.form_data = form_data
        with rx.session() as session:
            product = session.exec(
                product.select().where(
                    Product.identificator == form_data['identificator']
                    )
            )