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

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/#"),
        sidebar_item("Projects", "square-library", "/#"),
        sidebar_item("Analytics", "bar-chart-4", "/#"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )

def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        sidebar_item(
                            "Settings", "settings", "/#"
                        ),
                        sidebar_item(
                            "Log out", "log-out", "/#"
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "My account",
                                    size="3",
                                    weight="bold",
                                ),
                                rx.text(
                                    "user@reflex.dev",
                                    size="2",
                                    weight="medium",
                                ),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                height="100%",
                # height="650px",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_item(
                                        "Settings",
                                        "settings",
                                        "/#",
                                    ),
                                    sidebar_item(
                                        "Log out",
                                        "log-out",
                                        "/#",
                                    ),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                "My account",
                                                size="3",
                                                weight="bold",
                                            ),
                                            rx.text(
                                                "user@reflex.dev",
                                                size="2",
                                                weight="medium",
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
        min_height="100vh",
    )

def _center_container() -> rx.Component:
    return rx.container(
        rx.vstack(
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
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
            sidebar_bottom_profile(),
            _center_container(),
            spacing="8",
            justify="center",
            align="center",
            min_height="85vh",
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
