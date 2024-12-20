from flet import *


def main(page: Page):
    page.title = "Todo APP"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = MainAxisAlignment.CENTER

    def add_task(e):
        new_task_value = new_task.value
        page.add(Checkbox(label=new_task_value))
        new_task.value = ''
        page.update()

    new_task = TextField(hint_text="Please enter the task")

    page.add(new_task,
             FloatingActionButton(
                 icon=icons.ADD,
                 on_click=add_task)
             )


app(target=main)
