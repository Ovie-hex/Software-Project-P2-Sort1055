from types import FunctionType
from typing import Any

from .Templates import Window, Page, Widget
from .Con_Manager import Connection_Manager as connect


class GUI:
    def __init__(self):
        win = Window(name="test", size="200x200")
        frame = win.addPage(name="str")
        Widget = frame.addWidget(
            name="Btn",
            widgetType="Button",
            placeType="place",
            placeAttribute={"x": 50, "y": 100, "anchor": "center"},
        )

        ev1 = connect.getBindableEvent("tt")
        ev1.name = "FromGI"

        def onClick(widget):
            ev1.fire(67)

        Widget.event = onClick

        win.changePage("str")

        win.obj.mainloop()
