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

    # visualPage Status
    returnEnabled = True

    # 전달할거
    dataRange = 2
    dataAmount = 2
    sortType = "Random"

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
            style={},
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
                    "text": "◀ 돌아가기",
                    "font": ("맑은 고딕", 14, "bold"),
                    "bg": "#8FFF72",
                    "fg": "#ffffff",
                }
            else:
                widget.interactable = False
                widget.style = {
                    "text": "◀ 돌아가기",
                    "font": ("맑은 고딕", 14, "bold"),
                    "bg": "#FC3A3A",
                    "fg": "#ffffff",
                }

        backBtn.sync = backBtnSync

        # playBtn = interactFrame.addChildWidget()
        # stopBtn = interactFrame.addChildWidget()
        # stepBtn = interactFrame.addChildWidget()
        # speedBtn = interactFrame.addChildWidget()
        # speedEntry = interactFrame.addChildWidget()
        # speedAdjBtn = interactFrame.addChildWidget()

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
            startBtn.style = {"bg": "#FC3A3A"}

        # Visualizer

        # GUI
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

        # 비주얼라이저쪽 버튼 이벤트

        def goToSetting(self: Widget):
            window.size = "400x300"
            window.changePage("settingPage")

        backBtn.event = goToSetting

        # Bindable Event

        def goToVisualizer(requstorName, data):
            window.size = "600x800"
            print(f"[초기 데이터]\n{data}")
            window.changePage("visualPage")

        sortInitEv.eventCallback = goToVisualizer

        # MAIN ROOP
        window.changePage("settingPage")
        window.obj.mainloop()
