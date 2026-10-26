from typing import *

from .Templates import Window, Page, Widget, Message
from .Con_Manager import Connection_Manager as connect


class GUI:
    """
    ------------------------------
                Values
    ------------------------------
    """

    # SettingPage Status
    startEnabled = True

    adjRange = False
    adjAmount = False

    dataRange = 2
    dataAmount = 2
    sortType = "Random"

    # visualPage Status
    initData: list[int] = []

    speed = 0.05  # (0.05초 마다 gui 반영, 처리 시간은 고려하지 않음)

    returnEnabled = True
    stepEnabled = True

    def __init__(self):
        """
        ------------------------------
                BindableEvent
        ------------------------------
        """
        sortInitEv = connect.getBindableEvent("sortInitEv")

        sortStatusEv = connect.getBindableEvent("sortStatusEv")

        sort1Ev = connect.getBindableEvent("sort1Ev")
        sort2Ev = connect.getBindableEvent("sort2Ev")
        sort3Ev = connect.getBindableEvent("sort3Ev")

        """
        ------------------------------
                     GUI
        ------------------------------
        """

        # Main Window
        window = Window(name="Sort Comparison Visualizer", size="400x300")

        # Setting
        settingPage = window.addPage("settingPage")
        settingPage.style = {"bg": "#CCCCCC"}

        dataRangeLabel = settingPage.addWidget(
            name="dataRangeLabel",
            widgetType="Label",
            placeType="place",
            style={
                "text": "랜덤 값 범위 [2 ~ 500]",
                "anchor": "w",
                "bg": "#CCCCCC",
                "font": ("맑은 고딕", 8, "bold"),
            },
            placeAttribute={"x": 20, "y": 10, "width": 300, "height": 20},
        )

        dataRangeBtn = settingPage.addWidget(
            name="dataRangeBtn",
            widgetType="Button",
            style={
                "text": GUI.dataRange,
                "font": ("맑은 고딕", 20, "bold"),
                "anchor": "w",
            },
            placeType="place",
            placeAttribute={"x": 20, "y": 30, "width": 260, "height": 60},
        )

        dataRangeEntry = settingPage.addWidget(
            name="dataRangeEntry",
            widgetType="Entry",
            style={
                "font": ("맑은 고딕", 20, "bold"),
            },
            placeType="place",
            placeAttribute={"x": 20, "y": 30, "width": 260, "height": 60},
        )

        dataRangeEntry.hideWidget()

        dataRangeAdjBtn = settingPage.addWidget(
            name="dataRangeAdjBtn",
            widgetType="Button",
            style={
                "text": "확인",
                "font": ("맑은 고딕", 16, "bold"),
            },
            placeType="place",
            placeAttribute={"x": 300, "y": 30, "width": 80, "height": 60},
        )

        dataAmountLabel = settingPage.addWidget(
            name="dataAmountLabel",
            widgetType="Label",
            placeType="place",
            style={
                "text": "데이터 개수 [2 ~ 100]",
                "anchor": "w",
                "bg": "#CCCCCC",
                "font": ("맑은 고딕", 8, "bold"),
            },
            placeAttribute={"x": 20, "y": 100, "width": 300, "height": 20},
        )

        dataAmountBtn = settingPage.addWidget(
            name="dataAmountBtn",
            widgetType="Button",
            style={
                "text": GUI.dataAmount,
                "font": ("맑은 고딕", 20, "bold"),
                "anchor": "w",
            },
            placeType="place",
            placeAttribute={"x": 20, "y": 120, "width": 260, "height": 60},
        )

        dataAmountEntry = settingPage.addWidget(
            name="dataAmountEntry",
            widgetType="Entry",
            style={
                "font": ("맑은 고딕", 20, "bold"),
            },
            placeType="place",
            placeAttribute={"x": 20, "y": 120, "width": 260, "height": 60},
        )

        dataAmountEntry.hideWidget()

        dataAmountAdjBtn = settingPage.addWidget(
            name="dataAmountAdjBtn",
            widgetType="Button",
            style={
                "text": "확인",
                "font": ("맑은 고딕", 16, "bold"),
            },
            placeType="place",
            placeAttribute={"x": 300, "y": 120, "width": 80, "height": 60},
        )

        randBtn = settingPage.addWidget(
            name="randBtn",
            widgetType="Button",
            style={
                "text": "랜덤",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#8FFF72",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={"x": 10, "y": 200, "width": 120, "height": 40},
        )
        orderBtn = settingPage.addWidget(
            name="orderBtn",
            widgetType="Button",
            style={
                "text": "정렬",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#797878",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={"x": 140, "y": 200, "width": 120, "height": 40},
        )
        reverseBtn = settingPage.addWidget(
            name="reverseBtn",
            widgetType="Button",
            style={
                "text": "역정렬",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#797878",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={"x": 270, "y": 200, "width": 120, "height": 40},
        )

        startBtn = settingPage.addWidget(
            name="startBtn",
            widgetType="Button",
            style={
                "text": "실행",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#8FFF72",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={"x": 10, "y": 250, "width": 380, "height": 40},
        )

        # visualPage
        visualPage = window.addPage("visualPage")
        visualPage.style = {"bg": "#CCCCCC"}

        interactFrame = visualPage.addWidget(
            name="interactFrame",
            widgetType="Frame",
            style={"bg": "#3d3d3d"},
            placeType="place",
            placeAttribute={"y": 740, "relwidth": 1, "height": 60},
        )

        backBtn = interactFrame.addChildWidget(
            name="backBtn",
            widgetType="Button",
            style={
                "text": "◀ 돌아가기",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#8FFF72",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={
                "x": 10,
                "y": 10,
                "width": 120,
                "height": 40,
            },
        )

        def backBtnSync(widget: Widget):
            if GUI.returnEnabled:
                widget.interactable = True
                widget.style = {
                    "bg": "#8FFF72",
                }
            else:
                widget.interactable = False
                widget.style = {
                    "bg": "#797878",
                }

        backBtn.sync = backBtnSync

        playBtn = interactFrame.addChildWidget(
            name="playBtn",
            widgetType="Button",
            style={
                "text": "▶",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#8FFF72",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={
                "x": 230,
                "y": 10,
                "width": 60,
                "height": 40,
            },
        )

        stopBtn = interactFrame.addChildWidget(
            name="stopBtn",
            widgetType="Button",
            style={
                "text": "❚❚",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#FF2222",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={
                "x": 230,
                "y": 10,
                "width": 60,
                "height": 40,
            },
        )

        stopBtn.hideWidget()
        stopBtn.interactable = False

        def stepBtnSync(self: Widget):
            if GUI.stepEnabled:
                self.interactable = True
                self.style = {
                    "bg": "#8FFF72",
                }
            else:
                self.interactable = False
                self.style = {
                    "bg": "#797878",
                }

        stepBtn = interactFrame.addChildWidget(
            name="stepBtn",
            widgetType="Button",
            style={
                "text": "→",
                "font": ("맑은 고딕", 14, "bold"),
                "bg": "#8FFF72",
                "fg": "#ffffff",
            },
            placeType="place",
            placeAttribute={
                "x": 300,
                "y": 10,
                "width": 60,
                "height": 40,
            },
        )

        stepBtn.sync = stepBtnSync

        speedBtn = interactFrame.addChildWidget(
            name="speedBtn",
            widgetType="Button",
            style={
                "text": f" {GUI.speed} / (초)",
                "font": ("맑은 고딕", 14, "bold"),
            },
            placeType="place",
            placeAttribute={
                "x": 370,
                "y": 20,
                "width": 160,
                "height": 30,
            },
        )
        speedLabel = interactFrame.addChildWidget(
            name="speedLabel",
            widgetType="Label",
            placeType="place",
            style={
                "text": "실행 간격 ( 0.05 ~ ... )",
                "anchor": "w",
                "font": ("맑은 고딕", 9, "bold"),
                "fg": "#ffffff",
                "bg": "#3d3d3d",
            },
            placeAttribute={"x": 370, "width": 160, "height": 20},
        )

        speedEntry = interactFrame.addChildWidget(
            name="speedEntry",
            widgetType="Entry",
            style={"font": ("맑은 고딕", 14, "bold"), "justify": "center"},
            placeType="place",
            placeAttribute={
                "x": 370,
                "y": 20,
                "width": 160,
                "height": 30,
            },
        )

        speedEntry.hideWidget()

        speedAdjBtn = interactFrame.addChildWidget(
            name="speedAdjBtn",
            widgetType="Button",
            style={
                "text": "확인",
                "font": ("맑은 고딕", 14, "bold"),
                "justify": "center",
            },
            placeType="place",
            placeAttribute={
                "x": 540,
                "y": 10,
                "width": 50,
                "height": 40,
            },
        )

        sortFrame1 = visualPage.addWidget(
            name="sortFrame1",
            widgetType="Frame",
            style={"bg": "#CCCCCC"},
            placeType="place",
            placeAttribute={"y": 0, "relwidth": 1, "height": 245},
        )
        sortFrame2 = visualPage.addWidget(
            name="sortFrame2",
            widgetType="Frame",
            style={"bg": "#CCCCCC"},
            placeType="place",
            placeAttribute={"y": 245, "relwidth": 1, "height": 245},
        )
        sortFrame3 = visualPage.addWidget(
            name="sortFrame3",
            widgetType="Frame",
            style={"bg": "#CCCCCC"},
            placeType="place",
            placeAttribute={"y": 490, "relwidth": 1, "height": 245},
        )

        def addSortComponents(frame: Widget):

            # 정렬 이름
            frame.addChildWidget(
                name="sortName",
                widgetType="Label",
                style={
                    "text": "정렬 이름",
                    "font": ("맑은 고딕", 14, "bold"),
                    "justify": "center",
                },
                placeType="place",
                placeAttribute={"x": 10, "y": 10, "width": 100, "height": 40},
            )

            # 정렬 통계
            frame.addChildWidget(
                name="sortStatus",
                widgetType="Label",
                style={
                    "text": "정렬 통계",
                    "font": ("맑은 고딕", 14, "bold"),
                    "anchor": "w",
                },
                placeType="place",
                placeAttribute={"x": 120, "y": 10, "width": 470, "height": 40},
            )

            # 정렬 그래프 프레임 (매우 중요!!!!!!!!😭😭😭😭😭)
            frame.addChildWidget(
                name="sortGraph",
                widgetType="Frame",
                placeType="place",
                placeAttribute={"x": 30, "y": 60, "width": 540, "height": 180},
            )

            # 데이터 최대 및 최소
            frame.addChildWidget(
                name="valueMax",
                widgetType="Label",
                style={
                    "text": "Max",
                    "font": ("맑은 고딕", 8, "bold"),
                    "bg": "#CCCCCC",
                    "fg": "#ffffff",
                    "anchor": "c",
                },
                placeType="place",
                placeAttribute={"x": 0, "y": 55, "width": 30, "height": 20},
            )

            frame.addChildWidget(
                name="valueMin",
                widgetType="Label",
                style={
                    "text": "Min",
                    "font": ("맑은 고딕", 8, "bold"),
                    "bg": "#CCCCCC",
                    "fg": "#ffffff",
                    "anchor": "c",
                },
                placeType="place",
                placeAttribute={"x": 0, "y": 230, "width": 30, "height": 20},
            )

        addSortComponents(sortFrame1)
        addSortComponents(sortFrame2)
        addSortComponents(sortFrame3)

        """
        ------------------------------
             GUI Func, Event Func
        ------------------------------
        """
        # Setting

        def enableStart():
            startBtn.interactable = True
            startBtn.style = {"bg": "#8FFF72"}

        def disableStart():
            startBtn.interactable = False
            startBtn.style = {"bg": "#797878"}

        # Visualizer

        # GUI Button Event ( Setting )
        def onEditRange(widget: Widget):
            widget.hideWidget()
            dataRangeEntry.removeText(dataRangeEntry.obj)
            dataRangeEntry.placeWidget()
            dataRangeAdjBtn.interactable = True
            GUI.adjRange = True
            disableStart()

        dataRangeBtn.event = onEditRange

        def onAdjustRange(widget: Widget):
            dataRangeAdjBtn.interactable = False
            try:
                text = dataRangeEntry.getText(dataRangeEntry.obj)
                if len(text.strip()) == 0:
                    GUI.dataRange = 2
                else:
                    value = int(text)
                    if value >= 2 and value <= 500:
                        GUI.dataRange = value
                    else:
                        Message.warn("값 범위를 벗어났습니다.")
            except ValueError:
                Message.error("숫자를 입력해주세요!")
            except Exception:
                Message.error("알 수 없는 오류가 발생하였습니다!")

            dataRangeBtn.style = {"text": GUI.dataRange}
            dataRangeEntry.hideWidget()
            dataRangeBtn.placeWidget()

            GUI.adjRange = False
            if not GUI.adjRange and not GUI.adjAmount:
                enableStart()

        dataRangeAdjBtn.event = onAdjustRange

        def onEditAmount(widget: Widget):
            widget.hideWidget()
            dataAmountEntry.removeText(dataAmountEntry.obj)
            dataAmountEntry.placeWidget()
            dataAmountAdjBtn.interactable = True
            GUI.adjAmount = True
            disableStart()

        dataAmountBtn.event = onEditAmount

        def onAdjustAmount(widget: Widget):
            dataAmountAdjBtn.interactable = False
            try:
                text = dataAmountEntry.getText(dataAmountEntry.obj)
                if len(text.strip()) == 0:
                    GUI.dataAmount = 2
                else:
                    value = int(text)
                    if value >= 2 and value <= 100:
                        GUI.dataAmount = value
                    else:
                        Message.warn("값 범위를 벗어났습니다.")
            except ValueError:
                Message.error("숫자를 입력해주세요!")
            except Exception:
                Message.error("알 수 없는 오류가 발생하였습니다!")

            dataAmountBtn.style = {"text": GUI.dataAmount}
            dataAmountEntry.hideWidget()
            dataAmountBtn.placeWidget()

            GUI.adjAmount = False
            if not GUI.adjRange and not GUI.adjAmount:
                enableStart()

        dataAmountAdjBtn.event = onAdjustAmount

        def onRandom(widget: Widget):
            GUI.sortType = "Random"
            randBtn.style = {"bg": "#8FFF72"}
            orderBtn.style = {"bg": "#797878"}
            reverseBtn.style = {"bg": "#797878"}

        def onOrder(widget: Widget):
            GUI.sortType = "Order"
            randBtn.style = {"bg": "#797878"}
            orderBtn.style = {"bg": "#8FFF72"}
            reverseBtn.style = {"bg": "#797878"}

        def onReverse(widget: Widget):
            GUI.sortType = "Reverse"
            randBtn.style = {"bg": "#797878"}
            orderBtn.style = {"bg": "#797878"}
            reverseBtn.style = {"bg": "#8FFF72"}

        def onStart(widget: Widget):
            sortInitEv.fire(
                {
                    "dataRange": GUI.dataRange,
                    "dataAmount": GUI.dataAmount,
                    "sortType": GUI.sortType,
                }
            )

        randBtn.event = onRandom
        orderBtn.event = onOrder
        reverseBtn.event = onReverse

        startBtn.event = onStart

        # GUI Button Event ( Visualizer )

        # 공통

        def goToSetting(self: Widget):
            window.size = "400x300"
            window.changePage("settingPage")

        backBtn.event = goToSetting

        # Bindable Event

        def graphInit(self: Widget, num: int):
            # sortName, sortStatus, sortGraph, valueMax, valueMin
            match num:
                case 1:
                    self.childWidgets["sortName"].style = {"text": "삽입 정렬"}
                case 2:
                    self.childWidgets["sortName"].style = {"text": "퀵 정렬"}
                case 3:
                    self.childWidgets["sortName"].style = {"text": "버블 정렬"}

            self.childWidgets["sortStatus"].style = {"text": " Comp : 0, Swap : 0"}

            length = len(GUI.initData)
            valueMax = max(GUI.initData)
            valueMin = min(GUI.initData)

            self.childWidgets["valueMax"].style = {"text": valueMax}
            self.childWidgets["valueMin"].style = {"text": valueMin}

            sortGraph = self.childWidgets["sortGraph"]
            sortGraph.removeAllChildWidget()

            # 겁나 매우 중요!!! (😭😭😭😭😭)
            for i in range(0, length):
                sortGraph.addChildWidget(
                    name=i,
                    widgetType="Frame",
                    style={"bg": "#3d3d3d"},
                    placeType="place",
                    placeAttribute={
                        "relx": 0 if i == 0 else i / length,
                        "rely": 1,
                        "relwidth": 1 / length,
                        "relheight": GUI.initData[i] / valueMax,
                        "anchor": "sw",
                    },
                )

        def goToVisualizer(requstorName, data):
            window.size = "600x800"
            GUI.initData = data[:]
            graphInit(sortFrame1, 1)
            graphInit(sortFrame2, 2)
            graphInit(sortFrame3, 3)
            window.changePage("visualPage")

        sortInitEv.eventCallback = goToVisualizer

        # MAIN ROOP
        window.changePage("settingPage")
        window.obj.mainloop()
