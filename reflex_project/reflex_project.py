"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from rxconfig import config

from .components.sidebar import sidebar_bottom_profile
from .pages.principal import center_container

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
            sidebar_bottom_profile(),
            center_container(),
        )

def test() -> rx.Component:
    return rx.container(
        rx.heading("Test Page", size="9"),
        rx.text("This is a test page.", size="5"),
        rx.link('Back to main', href='/'),

        spacing="8",
        justify="center",
        align="center",
        min_height="85vh",
    )

app = rx.App()
app.add_page(index)
app.add_page(test, route='/h')
