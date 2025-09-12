from turtle import color
from flet import *

def main(page: Page):
    page.title = "First flet App"
    page.bgcolor = Colors.BLUE_400

    gallery_grid = GridView(
        auto_scroll=False,
        expand=1,
        child_aspect_ratio=2.0,
        run_spacing= 10,
        spacing=5,
        runs_count= 3,
    )

    def home_view():
        return View(
            route="/",
            bgcolor="blue400",
            scroll=ScrollMode.ALWAYS,
            controls=[
                Tabs(
                    animation_duration=10,
                    indicator_color=Colors.RED,
                    divider_color=Colors.BLACK,
                    tabs=[
                        Tab(
                            text="configuration",
                            content=ListView(
                                auto_scroll=True,
                                spacing=10,
                                controls=[
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 8GB - 2.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 16GB - 3.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 20GB - 4.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 24GB - 5.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 28GB - 6.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 30GB - 7.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 32GB - 8.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 36GB - 9.5 virtual Mahine")),
                                    Container(bgcolor=Colors.WHITE, padding=10, content=Text("RAM 50GB - 10.5 virtual Mahine"))
                                ]
                            )
                        ),
                        Tab(
                            text="console",
                            content=Container(height=200, width=400, content=Text("root:/"))
                        ),
                        Tab(
                            text="Settings",
                            content=Tabs(
                                is_secondary=True,
                                tabs=[
                                    Tab(text="Freeze server", content=Text("Click here to freeze server")),
                                    Tab(text="Delete server", content=Text("Click here to delete server")),
                                ]
                            )
                        )
                    ]
                )
            ]
        )

    def gallery_view():
        return View(
            route="/gallery",
            bgcolor=Colors.BLACK54,
            scroll = ScrollMode.ALWAYS,
            controls=[gallery_grid]
        )

    def table_view():
        return View(
            route="/datatable",
            scroll = ScrollMode.ALWAYS,
            controls = [
                Dismissible(
                    content=Text("Sofascore Notification"),
                    secondary_background=Container(bgcolor=Colors.RED_800),
                    dismiss_direction=DismissDirection.HORIZONTAL,
                    dismiss_thresholds={
                        DismissDirection.HORIZONTAL: 0.1,
                    }
                ),
                Row(
                    controls = [
                        DataTable(
                            bgcolor = Colors.GREEN_600,
                            border = border.all(5, Colors.YELLOW_500),
                            border_radius = border_radius.all(20),
                            columns = [
                                DataColumn(label=Text("State")),
                                DataColumn(label=Text("School name")),
                                DataColumn(label=Text("Location"))
                            ],
                            rows = [
                                DataRow(
                                    cells=[
                                        DataCell(
                                            Text("Indiana")
                                        ),
                                        DataCell(
                                            Text("Ball State University")
                                        ),
                                        DataCell(
                                            Text("Muncie")
                                        )
                                    ]
                                ),
                                DataRow(
                                    cells=[
                                        DataCell(
                                            Text("South Dakota")
                                        ),
                                        DataCell(
                                            Text("University of South Dakota")
                                        ),
                                        DataCell(
                                            Text("Vermillion")
                                        )
                                    ]
                                ),
                                DataRow(
                                    cells=[
                                        DataCell(
                                            Text("North Dakota")
                                        ),
                                        DataCell(
                                            Text("North Dakota State University")
                                        ),
                                        DataCell(
                                            Text("Fargo")
                                        )
                                    ]
                                )
                            ]
                        ),
                        Placeholder(expand=True, color=Colors.random())
                    ]
                ),
                ExpansionPanelList(
                    controls = [
                        ExpansionPanel(
                            header = Text("When should i expect to hearback from the school ?"),
                            bgcolor=Colors.BLUE_400,
                            can_tap_header=True,
                            content=Text("2 months from application deadline")
                        ),
                        ExpansionPanel(
                            header= Text("How long is it from Sious Falls to Vermillion"),
                            bgcolor=Colors.BROWN_400,
                            can_tap_header=True,
                            content=Text("1hr 20mins drive from Sious Falls")

                        ),
                        ExpansionPanel(
                            header= Text("Does Nigerian internation students require IELTS test scores"),
                            bgcolor=Colors.ORANGE_400,
                            can_tap_header=True,
                            content=Text("Nigerian graduates do not need IELTS test scores")
                        )
                    ],
                    expanded_header_padding=30,
                    divider_color=Colors.BLACK
                ),
                ReorderableListView(
                    controls=[
                        Container(width=50, height=50,bgcolor = Colors.random()),
                        Container(width=50, height=50,bgcolor = Colors.random()),
                        Container(width=50, height=50,bgcolor = Colors.random()),
                        Container(width=50, height=50,bgcolor = Colors.random()),
                        Container(width=50, height=50,bgcolor = Colors.random())
                    ],
                    horizontal=False
                )
            ]
        )

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view())
        elif page.route == "/gallery":
            page.views.append(gallery_view())
        elif page.route == "/datatable":
            page.views.append(table_view())
        page.update()

    for i in range(0, 60):
        gallery_grid.controls.append(
            Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius= border_radius.all(10),
            )
        )
    page.on_route_change = route_change
    page.go("/")

app(main)


# controls=[
#             Column(
#                 scroll = ScrollMode.ALWAYS,
#                 wrap = True,
#                 height= 600,
#                 alignment= MainAxisAlignment.END,
#                 run_spacing = 10,
#                 controls=[
#                     Container(bgcolor=Colors.RED, width=100, height=100),
#                     Container(bgcolor=Colors.BLUE, width=100, height=100),
#                     Container(bgcolor=Colors.GREEN, width=100, height=100),
#                     Container(bgcolor=Colors.YELLOW, width=100, height=100),
#                     Container(bgcolor=Colors.PINK, width=100, height=100),
#                     Container(bgcolor=Colors.WHITE, width=100, height=100),
#                     Container(bgcolor=Colors.BLACK, width=100, height=100),
#                     Container(bgcolor=Colors.LIGHT_BLUE_200, width=100, height=100),
#                     Container(bgcolor=Colors.CYAN, width=100, height=100),
#                     Container(bgcolor=Colors.BROWN, width=100, height=100),
#                     Container(bgcolor=Colors.GREEN, width=100, height=100),
#                     Container(bgcolor=Colors.YELLOW, width=100, height=100),
#                     Container(bgcolor=Colors.PINK, width=100, height=100, on_click=lambda e: print("Clickable without Ink clicked!"),),
#                 ]
#             ),
#             ResponsiveRow([
#                 Column(col={"xs": 12,"sm": 6, "md" : 6, "lg": 3}, controls=[Container(bgcolor=Colors.YELLOW, width=100, height=100)]),
#                 Column(col={"xs": 12,"sm": 6, "md" : 6, "lg": 3}, controls=[Container(bgcolor=Colors.LIGHT_BLUE_200, width=100, height=100)]),
#                 Column(col={"xs": 12,"sm": 6, "md" : 6, "lg": 3}, controls=[Container(bgcolor=Colors.YELLOW, width=100, height=100)]),
#                 Column(col={"xs": 12,"sm": 6, "md" : 6, "lg": 3}, controls=[Container(bgcolor=Colors.LIGHT_BLUE_200, width=100, height=100)])
#             ])
#         ]