import reflex as rx
from ..state import MyState

def render_student(student:str) -> rx.Component:
    return rx.text(student, size='4', color=MyState.color)

def center_container() -> rx.Component:
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
                    render_student,
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

