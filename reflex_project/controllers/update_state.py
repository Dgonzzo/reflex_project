import reflex as rx
from ..models import Product

class UpdateState(rx.State):
    name: str
    price: float 

    @rx.event
    def modify_product(self) -> None:
        with rx.session() as session: 
            product = session.exec(
                Product.select().where(
                    (Product.identificator == self.identificator)
                )
            ).first()
            product.name = self.name
            product.price = self.price
            session.add(product)
            session.commit()