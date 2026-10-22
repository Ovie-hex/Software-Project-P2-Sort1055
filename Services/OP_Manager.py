from types import FunctionType
from typing import Any

from .Templates import InsertSort, QuickSort, BubbleSort
from .Con_Manager import Connection_Manager as connect


class OP_Manager:
    ev1 = connect.getBindableEvent("tt")
    ev2 = connect.getBindableEvent("tt")

    def filt(requestorName: str, data: Any) -> bool:
        if data != 67:
            print("not 67 ;-;")
            return False
        else:
            return True

    def callb(requestorName: str, data: Any) -> None:
        if requestorName == "FromGUI":
            print("HOW")
        print("\\67/")

    def callb2(requestorName: str, data: Any) -> None:
        print("Huh")

    ev1.eventCallback = callb
    ev1.eventFilter = filt

    ev2.eventCallback = callb2
