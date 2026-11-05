from typing import *
import random
import time

from .Templates import Sort, InsertSort, QuickSort, BubbleSort
from .Con_Manager import Connection_Manager as connect


class OP_Manager:
    # Stats

    initData: list[int] = []
    sorts: list[Sort] = []

    speed: float = 0.05

    isStart = False

    # Events
    sortInitEv = connect.getBindableEvent("sortInitEv")

    sortStartEv = connect.getBindableEvent("sortStartEv")
    sortPauseEv = connect.getBindableEvent("sortPauseEv")
    sortStepEv = connect.getBindableEvent("sortStepEv")
    sortSpeedEv = connect.getBindableEvent("sortSpeedEv")

    # 삽입, 퀵, 버블 순
    sort1Ev = connect.getBindableEvent("sort1Ev")
    sort2Ev = connect.getBindableEvent("sort2Ev")
    sort3Ev = connect.getBindableEvent("sort3Ev")

    # Tkinter 전용 기다리기
    waitEv = connect.getBindableEvent("waitEv")

    # -------------------------------------------------------- Main

    def sortAll():
        work = False

        if not OP_Manager.sorts[0].ended:
            inst1 = OP_Manager.sorts[0].act()
            work = True
            OP_Manager.sort1Ev.fire(inst1)

        if not OP_Manager.sorts[1].ended:
            inst2 = OP_Manager.sorts[1].act()
            work = True
            OP_Manager.sort2Ev.fire(inst2)

        if not OP_Manager.sorts[2].ended:
            inst3 = OP_Manager.sorts[2].act()
            work = True
            OP_Manager.sort3Ev.fire(inst3)

        return work

    # --------------------------------------------------------

    def sortInitEvFilter(requestorName, data):

        if data["dataRange"] < 2 or data["dataRange"] > 500:
            return False
        if data["dataAmount"] < 2 or data["dataAmount"] > 100:
            return False
        if data["sortType"] not in ["Random", "Order", "Reverse"]:
            return False
        else:
            return True

    def sortInitEvCallback(requestorName, data):

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

        OP_Manager.sorts.append(InsertSort(OP_Manager.initData[:]))
        OP_Manager.sorts.append(QuickSort(OP_Manager.initData[:]))
        OP_Manager.sorts.append(BubbleSort(OP_Manager.initData[:]))

        print(
            f"< 초기 데이터 > [ 데이터 범위 : 1 ~ {data['dataRange']} / 데이터 개수 : {data['dataAmount']} / 데이터 형식 : {data['sortType']} ]\n{OP_Manager.initData}"
        )

    sortInitEv.eventFilter = sortInitEvFilter
    sortInitEv.eventCallback = sortInitEvCallback

    def adjustSpeed(requestorName, data):
        OP_Manager.speed = data

    sortSpeedEv.eventCallback = adjustSpeed

    def stopSort(requestorName, data):
        OP_Manager.isStart = False

    def stepSort(requestorName, data):
        isWork = OP_Manager.sortAll()
        if not isWork:
            OP_Manager.sortPauseEv.fire(1)

    def autoSort(requestorName, data):
        OP_Manager.isStart = True
        while OP_Manager.isStart:
            isWork = OP_Manager.sortAll()
            if not isWork:
                OP_Manager.sortPauseEv.fire(1)
                break
            initTime = time.perf_counter()
            while True:
                OP_Manager.waitEv.fire(0.001)
                if (
                    time.perf_counter() - initTime >= OP_Manager.speed
                    or not OP_Manager.isStart
                ):
                    break

    sortPauseEv.eventCallback = stopSort
    sortStepEv.eventCallback = stepSort
    sortStartEv.eventCallback = autoSort
