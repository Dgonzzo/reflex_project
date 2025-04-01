import reflex as rx
from ..state import MyState, TableForEachState

def show_product_page() -> rx.Component:
    return rx.container(
        foreach_table_example(),
    )


def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )


def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Full name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Group"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                TableForEachState.people, show_person
            )
        ),
        width="100%",
    )