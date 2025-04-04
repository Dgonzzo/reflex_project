import reflex as rx
from models import Product

class AddState(rx.State):

    def add():
        with rx.session() as session:
            session.add(
                Product(
                    identificator="test",
                    name="admin@reflex.dev",
                    price="admin",
                )
            )
            session.commit()
