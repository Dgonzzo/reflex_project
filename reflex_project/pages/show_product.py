import reflex as rx

def show_product_page() -> rx.Component:
    return rx.container(
        foreach_table_example(),
    )


def show_person(products: list):
    """Show a person in a table row."""

    # ! This is a placeholder for the actual implementation
    return rx.table.row(
        rx.table.cell(products[0]),
        rx.table.cell(products[1]),
        rx.table.cell(products[2]),
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
            # rx.foreach(
            #     # ! Replace with your data source
            # )
        ),
        width="100%",
    )