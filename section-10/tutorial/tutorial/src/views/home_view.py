from flet import *

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

