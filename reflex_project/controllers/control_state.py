import reflex as rx
from ..models import Product

class ConsultState(rx.State):
    form_data: dict = {}
    updated_product: Product = None

    @rx.var
    def get_code(self) -> str:
        return self.router.page.params.get('code') 

    @rx.var
    def get_product(self):
        with rx.session() as session:
            self.updated_product = session.exec(
                Product.select().where(
                    Product.identificator == int(self.get_code())
                )
            ).one_or_none()

    @rx.event
    def handle_submit(self, form_data:dict) -> None:
        '''Handle the form submission'''
        self.form_data = form_data
        with rx.session() as session:
            session.add(
                Product(
                    identificator=form_data['identificator'],
                    name=form_data['name_product'],
                    price=form_data['price_product'],
                )
            )
            session.commit()
        return rx.redirect('/list')
