from typing import *

from .Templates import Window, Page, Widget, Message
from .Con_Manager import Connection_Manager as connect


class GUI:
    # SettingPage Status
    startEnabled = True

    adjRange = False
    adjAmount = False

    # visualPage Status
    returnEnabled = True

    # 전달할거
    dataRange = 1
    dataAmount = 2
    sortType = "Random"

    def __init__(self):
        """
        ------------------------------
                    Values
        ------------------------------
        """

        """
        ------------------------------
                BindableEvent
        ------------------------------
        """
        # 데이터 설정 후 그 설정 값을 op에 보내고 초기화를 통해 비주얼 라이저 화면으로 넘어감
        sortInitEv = connect.getBindableEvent("sortInitEv")

        # Act할 때 마다 callback 호출하여 gui 동기화
        sort1Ev = connect.getBindableEvent("sort1Ev")
        sort2Ev = connect.getBindableEvent("sort2Ev")
        sort3Ev = connect.getBindableEvent("sort3Ev")

        # 비주얼라이저 화면에서 스탭, 재생, 정지 버튼 전달
        sortStatusEv = connect.getBindableEvent("sortStatusEv")

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
                "text": "랜덤 값 범위 [1 ~ 500]",
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

        """
        ------------------------------
             GUI Func, Event Func
        ------------------------------
        """

        def EnableStart():
            startBtn.interactable = True
            startBtn.style = {"bg": "#8FFF72"}

        def disableStart():
            startBtn.interactable = False
            startBtn.style = {"bg": "#FC3A3A"}

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
                    GUI.dataRange = 1
                else:
                    value = int(text)
                    if value >= 1 and value <= 500:
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
                EnableStart()

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
                EnableStart()

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
            print(67)

        randBtn.event = onRandom
        orderBtn.event = onOrder
        reverseBtn.event = onReverse

        startBtn.event = onStart

        # Bindable Event

        # MAIN ROOP
        window.changePage("settingPage")
        window.obj.mainloop()
