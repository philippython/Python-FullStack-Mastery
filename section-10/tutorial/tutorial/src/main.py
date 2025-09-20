from flet import *
from views.gallery_view import gallery_view
from views.home_view import home_view
from views.table_view import table_view
from views.input_view import input_view

def main(page: Page):
    page.title = "First flet App"
    page.bgcolor = Colors.BLUE_400


    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view())
        elif page.route == "/gallery":
            page.views.append(gallery_view())
        elif page.route == "/datatable":
            page.views.append(table_view())
        elif page.route == "/forms":
            page.views.append(input_view())
        page.update()


    page.on_route_change = route_change
    page.go("/")

app(main)

