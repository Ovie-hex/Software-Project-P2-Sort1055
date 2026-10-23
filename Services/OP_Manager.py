from typing import *
import random

from .Templates import Sort, InsertSort, QuickSort, BubbleSort
from .Con_Manager import Connection_Manager as connect


class OP_Manager:
    # Stats

    initData: list[int] = []
    sorts: list[Sort] = []

    # Events
    sortInitEv = connect.getBindableEvent("sortInitEv")

    sortStatusEv = connect.getBindableEvent("sortStatusEv")

    sort1Ev = connect.getBindableEvent("sort1Ev")
    sort2Ev = connect.getBindableEvent("sort2Ev")
    sort3Ev = connect.getBindableEvent("sort3Ev")

    def sortInitEvFilter(requstorName, data):
        if data["dataRange"] < 2 or data["dataRange"] > 500:
            return False
        if data["dataAmount"] < 2 or data["dataAmount"] > 100:
            return False
        if data["sortType"] not in ["Random", "Order", "Reverse"]:
            return False
        else:
            return True

    def sortInitEvCallback(requstorName, data):

        OP_Manager.initData.clear()
        OP_Manager.sorts.clear()

        for i in range(0, data["dataAmount"]):
            OP_Manager.initData.append(random.randint(1, data["dataRange"]))

        if data["sortType"] == "Random":
            OP_Manager.sortInitEv.fire(OP_Manager.initData)
        elif data["sortType"] == "Order":
            OP_Manager.initData.sort()
            OP_Manager.sortInitEv.fire(OP_Manager.initData)
        elif data["sortType"] == "Reverse":
            OP_Manager.initData.sort(reverse=True)
            OP_Manager.sortInitEv.fire(OP_Manager.initData)

    sortInitEv.eventFilter = sortInitEvFilter
    sortInitEv.eventCallback = sortInitEvCallback
