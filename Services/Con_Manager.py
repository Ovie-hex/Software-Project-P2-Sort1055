from __future__ import annotations
from typing import *
import secrets
from copy import *

# eventFilter 및 eventCallback 함수 작성시 매게변수로 requestor의 이름과 data를 받아야합니다.


class Connection:
    _connections: list[Connection] = []

    @staticmethod
    def getConnection(name: str):
        return next((c for c in Connection._connections if c.name == name), None)

    # Information

    def __init__(self, name: str, firstevent: BindableEvent):
        self._name: str = name

        self._events: dict[
            BindableEvent,
            dict[str, Callable[[str, Any], None] | Callable[[str, Any], bool]],
        ] = {}
        self._count = 0
        self._onlinked: bool = False

        # Initalize
        Connection._connections.append(self)

        self._events[firstevent] = {"eventFilter": None, "eventCallback": None}
        firstevent._connection = self
        self._count += 1

    def __str__(self):
        return self._name

    # Read Only
    @property
    def name(self) -> str:
        return self._name

    # Member Methods

    def addLink(self, event: BindableEvent) -> None:
        if event in self._events:
            return

        self._events[event] = {"eventFilter": None, "eventCallback": None}
        event._connection = self
        self._count += 1

        if self._count >= 2:
            self._onlinked = True

    def removeLink(self, event: BindableEvent) -> None:
        if event not in self._events or event._connection != self:
            return

        self._events.pop(event)
        self._count -= 1
        if self._count < 2:
            self._onlinked = False
        if self._count < 0:
            Connection._connections.remove(self)

    def adjustFilter(
        self, event: BindableEvent, func: Callable[[str, Any], bool]
    ) -> None:
        if event not in self._events or event._connection != self:
            return

        event._connection._events[event]["eventFilter"] = func

    def adjustCallback(
        self, event: BindableEvent, func: Callable[[str, Any], None]
    ) -> None:
        if event not in self._events or event._connection != self:
            return

        event._connection._events[event]["eventCallback"] = func

    def send(self, requestor: BindableEvent, data: Any) -> None:
        if self._onlinked:
            for event in self._events:
                if event.name != requestor.name:
                    if event.eventFilter(requestor.name, deepcopy(data)) == False:
                        continue
                    else:
                        event.eventCallback(requestor.name, deepcopy(data))


class BindableEvent:
    _bindableEvents: list[BindableEvent] = []

    # Information
    def _nothing(reqName: str, data: Any):
        return True

    def __init__(self, name):
        self._name: str = str(hash(name + secrets.token_hex(67)))
        self._connection: Connection = None

    def __str__(self):
        return f"BindableEvent : {self._name}, Connection : {self._connection.name}"

    # Can Adjust
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if name not in (b.name for b in BindableEvent._bindableEvents):
            self._name = name

    @property
    def eventFilter(self) -> Callable[[str, Any], bool]:
        return self._connection._events[self]["eventFilter"]

    @eventFilter.setter
    def eventFilter(self, func) -> None:
        self._connection.adjustFilter(self, func)

    @property
    def eventCallback(self) -> Callable[[str, Any], None]:
        return self._connection._events[self]["eventCallback"]

    @eventCallback.setter
    def eventCallback(self, func) -> None:
        self._connection.adjustCallback(self, func)

    # Member Methods

    def fire(self, data: Any) -> None:
        self._connection.send(self, data)

    def destroy(self) -> None:
        if self not in BindableEvent._bindableEvents:
            return

        self._connection.removeLink(self)
        BindableEvent._bindableEvents.remove(self)


class Connection_Manager:
    @staticmethod
    def getBindableEvent(name: str) -> BindableEvent | None:

        name = name.strip()
        event: BindableEvent = BindableEvent(name)

        con = Connection.getConnection(name)

        if con == None:
            con = Connection(name, event)
            con.adjustFilter(event, BindableEvent._nothing)
            con.adjustCallback(event, BindableEvent._nothing)
        else:
            con.addLink(event)
            con.adjustFilter(event, BindableEvent._nothing)
            con.adjustCallback(event, BindableEvent._nothing)
        return event
