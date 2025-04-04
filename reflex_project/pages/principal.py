import reflex as rx
from ..controllers import PrincipalState

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
                default_value=PrincipalState.text,
                on_change=PrincipalState.update_text,
            ),

            rx.hstack(
                rx.button('Increase 1',size='4', border_radius='80px', on_click=lambda: PrincipalState.increment(1)),
                rx.button('Increase 30',size='4', border_radius='80px', on_click=lambda: PrincipalState.increment(30)),
                rx.button('Reset',size='4', border_radius='80px', on_click= PrincipalState.reset_button),
                rx.text(PrincipalState.count, color=PrincipalState.color, margin='10px', size='6'),
                align='center',
            ),

            rx.box(
                rx.foreach(
                    PrincipalState.students,
                    render_student,
                    #lambda student: rx.text(student, size='4', color='green'),
                )
            ),
            
            rx.hstack(
                rx.cond(
                    PrincipalState.color == 'red',
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

