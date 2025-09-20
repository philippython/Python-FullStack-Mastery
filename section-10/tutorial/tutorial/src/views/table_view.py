from flet import *

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