"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from rxconfig import config

from .components.sidebar import sidebar_bottom_profile

from .pages.principal import center_container
from .pages.show_product import show_product_page
from .pages.add_product import add_product_page

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
            sidebar_bottom_profile(),
            center_container(),
        )

def show_product() -> rx.Component:
    # Show Products Page
    return rx.vstack(
        sidebar_bottom_profile(),
        show_product_page(),
    )

def add_product() -> rx.Component:
    # Add Products Page
    return rx.vstack(
        sidebar_bottom_profile(),
        add_product_page(),
    )   

app = rx.App()
app.add_page(index)
app.add_page(show_product, route='show_product')
app.add_page(add_product, route='add_product')
