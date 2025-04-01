import reflex as rx

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

class TableForEachState(rx.State):
    people: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Developer"],
        ["Zahra Ambessa", "zahra@example.com", "Admin"],
        ["Jasper Eriks", "jasper@example.com", "Developer"],
    ]
