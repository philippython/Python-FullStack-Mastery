from flet import *

gallery_grid = GridView(
        auto_scroll=False,
        expand=1,
        child_aspect_ratio=2.0,
        run_spacing= 10,
        spacing=5,
        runs_count= 3,
    )

for i in range(0, 60):
    gallery_grid.controls.append(
        Image(
            src=f"https://picsum.photos/150/150?{i}",
            fit=ImageFit.NONE,
            repeat=ImageRepeat.NO_REPEAT,
            border_radius= border_radius.all(10),
        )
    )

def gallery_view():
        return View(
            route="/gallery",
            bgcolor=Colors.BLACK54,
            scroll = ScrollMode.ALWAYS,
            controls=[gallery_grid]
        )