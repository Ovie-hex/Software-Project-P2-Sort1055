from abc import ABC, abstractmethod

from typing import *

"""
GUI_Manager에 전달할 데이터 양식 (약간 2차원 배열 비스무리함)

[ 명령, 위치1, 위치2 ] : < list[list[str | int]] >

명령 종류 :

- comp
- swap
- pivot
- disable
- default
- end

ex )
[
 ["comp", 23, 44, ...],
 ["swap", 23, 44, ...],
 ["pivot", 1],
 ["disable", 5]
]
"""


class Sort(ABC):
    def __init__(self, data: list[int]):
        self._data = data[:]
        self._length = len(self._data)
        self.ended = False

    # Read Only
    @property
    @abstractmethod
    def data(self):
        return self._data

    @abstractmethod
    def act(self) -> list[list[str | int]]:
        # 이 함수 안에 데이터의 비교나 스왑 등을 수행하고 그 행위에 대한 기록을 반환해야한다.
        pass


class InsertSort(Sort):
    def __init__(self, data: list[int]):
        super().__init__(data)

        self._pos = 0
        self._current = 1
        self._NextStat = "comp"
        self._prevArg = []

    # Read Only
    @property
    def data(self):
        return super().data

    def act(self) -> list[list[str | int]]:
        inst = []
        if not self._pos + 1 >= self._length:
            if len(self._prevArg) > 0:
                inst.append(["default"] + self._prevArg[:])
            match self._NextStat:
                case "comp":
                    if self._current > 0:
                        if self.data[self._current] < self.data[self._current - 1]:
                            self._NextStat = "swap"

                        inst.append(["comp", self._current, self._current - 1])

                        self._prevArg.clear()
                        self._prevArg.append(self._current)
                        self._prevArg.append(self._current - 1)

                        if self._NextStat == "comp":
                            self._pos += 1
                            self._current = self._pos + 1

                case "swap":
                    temp = self.data[self._current - 1]
                    self.data[self._current - 1] = self.data[self._current]
                    self.data[self._current] = temp
                    inst.append(["swap", self._current, self._current - 1])

                    if self._current <= 1:
                        self._pos += 1
                        self._current = self._pos + 1
                    else:
                        self._current -= 1

                    self._NextStat = "comp"
        else:
            self.ended = True
            inst.append(["end"])
        return inst


# 퀵 정렬을 쓰기 위한 클래스
class Partition:
    def __init__(self, data: list[int], startPos: int, endPos: int):

        self._data: list[int] = data
        self._pivotValue: int = self._data[startPos]
        self._low: int = startPos + 1
        self._high: int = endPos

        self._left: Partition = None
        self._right: Partition = None

    # Read Only
    @property
    def data(self):
        return super().data

    # Member Method

    def act(self) -> Any:
        pass


class QuickSort(Sort):
    def __init__(self, data: list[int]):
        super().__init__(data)

        self._currentPartition: Partition = Partition(data, 0, self._length)

    # Read Only
    @property
    def data(self):
        return super().data

    # Member Method

    def act(self) -> list[list[str | int]]:
        pass


class BubbleSort(Sort):
    def __init__(self, data: list[int]):
        super().__init__(data)

        self._pos = 0
        self._roopCount = 0

    # Read Only
    @property
    def data(self):
        return super().data

    # Member Method

    def act(self) -> list[list[str | int]]:
        pass
