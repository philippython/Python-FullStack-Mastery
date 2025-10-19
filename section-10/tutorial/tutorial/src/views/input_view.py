from flet import * 

def input_view():
    return View(
        route="/forms",
        bgcolor=Colors.WHITE,
        scroll=ScrollMode.ALWAYS,
        controls=[
            AutoComplete(
                suggestions=[
                    AutoCompleteSuggestion(key="Iowa", value="Iowa"),
                ],
            ),
            Text("AutoComplete field"),
            AutofillGroup(
                Column(
                    controls=[
                        TextField(
                            label="Name",
                            autofill_hints=AutofillHint.NAME,
                        ),
                        TextField(
                            label="Email",
                            autofill_hints=[AutofillHint.EMAIL],
                        ),
                        TextField(
                            label="Phone Number",
                            autofill_hints=[AutofillHint.TELEPHONE_NUMBER],
                        ),
                        TextField(
                            label="Street Address",
                            autofill_hints=AutofillHint.FULL_STREET_ADDRESS,
                        ),
                        TextField(
                            label="Postal Code",
                            autofill_hints=AutofillHint.POSTAL_CODE,
                        ),
                    ]
                )
            ),
            Checkbox(
                active_color=Colors.RED,
                check_color=Colors.BLUE,
                hover_color=Colors.WHITE,
                label="Are you loving this course",
                label_position=LabelPosition.LEFT,
                shape=CircleBorder(),
            ),
            RadioGroup(
                content=Column(
                    [
                        Radio(value="red", label="Red", adaptive=True),
                        Radio(value="green", label="Green", adaptive=True),
                        Radio(value="blue", label="Blue", adaptive=True),
                    ]
                ),
            ),
            Dropdown(
                bgcolor=Colors.GREY,
                color=Colors.GREEN,
                enable_search=True,
                editable=True,
                label="Cities",
                options= [
                    DropdownOption(
                        content=Text("Tokyo"),
                        key="Tokyo"
                    ),
                    DropdownOption(
                        content=Text("Yamanshi"),
                        key="Yamanshi"
                    ),
                    DropdownOption(
                        content=Text("Kofu"),
                        key="Kofu"
                    ),
                    DropdownOption(
                        content=Text("Osaka"),
                        key="Osaka"
                    ),
                    DropdownOption(
                        content=Text("Ogun"),
                        key="Ogun"
                    )
                ]
            ),
            RangeSlider(
                min=0,
                max=50,
                start_value=10,
                end_value=20
            ),
            SearchBar(
                autofocus=True,
                bar_bgcolor=Colors.WHITE,
                bar_hint_text="Search items..."
            ),
            Text("Slider with value:"),
            Slider(value=0.3),
            Text("Slider with a custom range and label:"),
            Slider(min=0, max=100, divisions=10, label="{value}%"),
            Switch(label="Unchecked switch", value=False, active_color=Colors.BLUE_400, adaptive=True),
            Switch(label="Checked switch", value=True, active_color=Colors.BLUE_400),
            Switch(label="Disabled switch", disabled=True, active_color=Colors.BLUE_400),
            TextField(label="Standard"),
            TextField(label="Disabled", disabled=True, value="First name"),
            TextField(label="Read-only", read_only=True, value="Last name"),
            TextField(label="With placeholder", hint_text="Please enter text here"),
            TextField(label="With an icon", icon=Icons.EMOJI_EMOTIONS)
        ]
    )