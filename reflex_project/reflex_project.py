"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class MyState(rx.State): # Backend
    count: int = 0
    color: str = 'red'
    text: str = 'Hello'
    students: list = ['Alice', 'Bob', 'Charlie']

    @rx.event
    def increment(self, value:int) -> None:
        self.count += value
        if self.count % 2 == 0:
            self.color = 'green'
        else:
            self.color = 'red'
        
    @rx.event
    def reset_button(self) -> None:
        self.count = 0
        self.color = 'green'

    @rx.event
    def update_text(self, new_text:str) -> None:
        self.text = new_text

def _render_student(student:str) -> rx.Component:
    return rx.text(student, size='4', color=MyState.color)


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to " + MyState.text + '!', size="9"),
            rx.heading("A place to learn and have fun with Python!", size="5"),
            rx.heading('Programing subject'),
            rx.link('Test Page', href='/h'),
            rx.input(
                default_value=MyState.text,
                on_change=MyState.update_text,
            ),

            rx.hstack(
                rx.button('Increase 1',size='4', border_radius='80px', on_click=lambda: MyState.increment(1)),
                rx.button('Increase 30',size='4', border_radius='80px', on_click=lambda: MyState.increment(30)),
                rx.button('Reset',size='4', border_radius='80px', on_click= MyState.reset_button),
                rx.text(MyState.count, color=MyState.color, margin='10px', size='6'),
                align='center',
            ),

            rx.box(
                rx.foreach(
                    MyState.students,
                    _render_student,
                    #lambda student: rx.text(student, size='4', color='green'),
                )
            ),
            
            rx.hstack(
                rx.cond(
                    MyState.color == 'red',
                    rx.text('Red color'),
                    rx.text('Green color'),
                ),
                align='center',

            ),

            spacing="8",
            justify="center",
            align="center",
            min_height="85vh",
        ),
        
        
        rx.logo(),
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
