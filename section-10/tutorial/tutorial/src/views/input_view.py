from flet import * 

def input_view():
    return View(
        route="/forms",
        bgcolor=Colors.random(),
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
                borde,
                border = border.all(5, Colors.YELLOW)
            )
        ]
    )