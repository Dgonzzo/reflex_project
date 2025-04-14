import reflex as rx
from ..models import Product

class ConsultState(rx.State):
    form_data: dict = {}
    updated_product: Product = None

    @rx.var
    def get_code(self) -> str:
        return self.router.page.params.get('code') 

    @rx.event
    def get_product(self):
        with rx.session() as session:
            self.updated_product = session.exec(
                Product.select().where(
                    Product.identificator == int(self.get_code())
                )
            ).one_or_none()

    @rx.event
    def handle_submit(self, form_data:dict) -> None:
        '''Handle the form submit'''
        self.form_data = form_data
        with rx.session() as session:
            self.actual_product = session.exec(
                Product.select().where(
                    Product.identificator == int(self.get_code())
                )
            ).one_or_none()
            self.actual_product.identificator = form_data['identificator']
            self.actual_product.name = form_data['product_name']
            self.actual_product.price = form_data['product_price']
            session.add(self.actual_product)
            session.commit()
        
        return rx.redirect('/list')
