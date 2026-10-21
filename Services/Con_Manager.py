import inspect
from types import ModuleType, FunctionType


class BindableEvent:
    # Information

    def __init__(self, name: str):
        self._name: str = name

        self._link: list[ModuleType] = []
        self._eventFilter: list[FunctionType] = []
        self._eventCallback: list[FunctionType] = []
        self._onlinked: bool = False

    def __str__(self):
        return f"BindableEvent : {self._name}"

    # Read Only

    @property
    def name(self):
        return self._name

    @property
    def onlinked(self):
        return self._onlinked

    # Can Adjust

    @property
    def eventFilter(self) -> FunctionType:
        try:
            return self._eventFilter[
                self._link.index(inspect.getmodule(inspect.stack()[1].frame))
            ]
        except Exception as e:
            print(e)

    @eventFilter.setter
    def eventFilter(self, func):
        try:
            self._eventFilter[
                self._link.index(inspect.getmodule(inspect.stack()[1].frame))
            ] = func
        except Exception as e:
            print(e)

    @property
    def eventCallback(self) -> FunctionType:
        try:
            return self._eventCallback[
                self._link.index(inspect.getmodule(inspect.stack()[1].frame))
            ]
        except Exception as e:
            print(e)

    @eventCallback.setter
    def eventCallback(self, func):
        try:
            self._eventCallback[
                self._link.index(inspect.getmodule(inspect.stack()[1].frame))
            ] = func
        except Exception as e:
            print(e)

    # Inner Methods

    def _filter(data: any, filterFunc: FunctionType) -> bool:
        return filterFunc(data)

    def _callBack(data: any, callbackFunc: FunctionType) -> None:
        try:
            callbackFunc(data)
        except Exception as e:
            print(e)
            print("callBack has been broken")

    # Member Methods

    def _setLink(self, module: ModuleType) -> None:
        if len(self._link) < 2:
            self._link.append(module)
            self._eventFilter.append(None)
            self._eventCallback.append(None)

            if len(self._link) == 2:
                self._onlinked = True

    def fire(self, data: any) -> None:
        if self.onlinked:
            try:
                calledModule: ModuleType = inspect.getmodule(inspect.stack()[1].frame)
                funcPos = self._link.index(calledModule)

                filterFunc = None
                callbackFunc = None

                if funcPos == 0:
                    filterFunc = self._eventFilter[1]
                    callbackFunc = self._eventCallback[1]
                elif funcPos == 1:
                    filterFunc = self._eventFilter[0]
                    callbackFunc = self._eventCallback[0]

                if BindableEvent._filter(data, filterFunc):
                    BindableEvent._callBack(data, callbackFunc)
                else:
                    print("Event Fire has been Failed for Filtering")

            except Exception as e:
                print(e)
                print("Event Fire has been Failed for Unknown Error")
        else:
            print("Event is not linked")


class Connection_Manager:
    _bindableEvents: dict[str, BindableEvent] = {}

    @staticmethod
    def getBindableEvent(name: str) -> BindableEvent:
        calledModule: ModuleType = inspect.getmodule(inspect.stack()[1].frame)

        name = name.strip()

        if name not in Connection_Manager._bindableEvents:
            Connection_Manager._bindableEvents[name] = BindableEvent(name)
            event = Connection_Manager._bindableEvents[name]

            event._setLink(calledModule)

            return Connection_Manager._bindableEvents[name]
        else:
            event: BindableEvent = Connection_Manager._bindableEvents[name]

            if event._onlinked == False:
                event._setLink(calledModule)

                return event
            else:
                print(f"{event} is already linked")
                return None
