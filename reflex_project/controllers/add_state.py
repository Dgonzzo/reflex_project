import reflex as rx
from ..models import Product

class AddState(rx.State):
    form_data: dict = {}
        
    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        
        with rx.session() as session:
            session.add(
                Product(
                    identificator= form_data['identificator'],
                    name=form_data['product_name'],
                    price=form_data['product_price'],
                )
            )
            session.commit()
        
        return rx.redirect('/show_product')
