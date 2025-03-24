"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class MyState(rx.State): # Backend
    count: int = 0
    color: str = 'red'

    @rx.event
    def increment(self) -> None:
        self.count += 1
        if self.count % 2 == 0:
            self.color = 'green'
        else:
            self.color = 'red'
        
    @rx.event
    def reset_button(self) -> None:
        self.count = 0
        self.color = 'red'


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Gipsyland!", size="9"),
            rx.heading("A place to learn and have fun with Python!", size="5"),
            rx.heading('Programing subject'),
            
            rx.hstack(
                rx.button('Increase',size='4', border_radius='80px', on_click= MyState.increment),
                rx.button('Reset',size='4', border_radius='80px', on_click= MyState.reset_button),
                rx.text(MyState.count, color=MyState.color, margin='10px', size='6'),
                align='center',
            ),

            spacing="8",
            justify="center",
            min_height="85vh",
        ),
        
        
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
