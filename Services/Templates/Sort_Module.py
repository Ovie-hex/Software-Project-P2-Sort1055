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

        self._startPos = startPos
        self._endPos = endPos
        self._length = endPos - startPos + 1

        self._low: int = startPos + 1
        self._lowComplted = False

        self._high: int = endPos
        self._highComplted = False

        self._left: Partition = None
        self._right: Partition = None

        self._ended = False

        self._prevArg = []

    # Read Only
    @property
    def data(self):
        return super()._data

    # Member Method

    def act(self) -> list[list[str | int]]:

        inst = []
        inst.append(["pivot", self._startPos])

        print(self._length)

        if len(self._prevArg) > 0:
            inst.append(["default"] + self._prevArg[:])

        match self._length:
            case 1:
                inst.append(["disable"] + [self._startPos])
                self._ended = True
            case 2:
                if self._data[self._startPos] > self._data[self._startPos + 1]:
                    temp = self._data[self._startPos]
                    self._data[self._startPos] = self._data[self._startPos + 1]
                    self._data[self._startPos + 1] = temp
                    inst.append(["comp", self._startPos, self._startPos + 1])
                    inst.append(["swap", self._startPos, self._startPos + 1])
                    inst.append(["disable", self._startPos, self._startPos + 1])
                    self._prevArg.clear()
                    self._ended = True
                else:
                    inst.append(["comp", self._startPos, self._startPos + 1])
                    inst.append(["disable", self._startPos, self._startPos + 1])
                    self._ended = True
            case _:
                if not self._lowComplted:
                    inst.append(["comp", self._low])
                    if self._data[self._low] > self._pivotValue:
                        self._lowComplted = True
                    else:
                        if self._low == self._endPos:
                            temp = self._data[self._startPos]
                            self._data[self._startPos] = self._data[self._low]
                            self._data[self._low] = temp
                            inst.append(["swap", self._startPos, self._low])
                            inst.append(["default"] + [self._startPos])
                            inst.append(["disable"] + [self._low])
                            self._prevArg.clear()

                            self._left = Partition(
                                self._data, self._startPos, self._high - 1
                            )
                            self._left._right = Partition(
                                self._data, self._endPos, self._endPos
                            )

                            if self._right != None:
                                self._left._right._right = self._right

                            self._ended = True

                        else:
                            self._prevArg.clear()
                            self._prevArg.append(self._low)
                            self._low += 1

                elif not self._highComplted:
                    inst.append(["comp", self._high])
                    if self._data[self._high] < self._pivotValue:
                        self._highComplted = True
                    else:
                        if self._high == self._startPos:
                            inst.append(["disable"] + [self._startPos])
                            self._startPos += 1
                            self._length -= 1
                            self._pivotValue = self._data[self._startPos]
                            self._low = self._startPos + 1
                            self._high = self._endPos
                            self._lowComplted = False
                            self._prevArg.clear()

                        else:
                            self._prevArg.clear()
                            self._prevArg.append(self._high)
                            self._high -= 1

                else:
                    if self._low > self._high:
                        temp = self._data[self._startPos]
                        self._data[self._startPos] = self._data[self._high]
                        self._data[self._high] = temp
                        inst.append(["swap", self._startPos, self._high])
                        inst.append(["default"] + [self._startPos, self._low])
                        inst.append(["disable"] + [self._high])

                        self._left = Partition(
                            self._data, self._startPos, self._high - 1
                        )
                        self._left._right = Partition(
                            self._data, self._high + 1, self._endPos
                        )

                        if self._right != None:
                            self._left._right._right = self._right

                        self._ended = True
                    else:
                        temp = self._data[self._low]
                        self._data[self._low] = self._data[self._high]
                        self._data[self._high] = temp
                        inst.append(["swap", self._low, self._high])

                        self._prevArg.clear()
                        self._prevArg.append(self._low)
                        self._prevArg.append(self._high)

                        self._low += 1
                        self._lowComplted = False
                        self._high -= 1
                        self._highComplted = False

        return inst


class QuickSort(Sort):
    def __init__(self, data: list[int]):
        super().__init__(data)

        self._currentPartition: Partition = Partition(self.data, 0, self._length - 1)

        self.ended = False

    # Read Only
    @property
    def data(self):
        return super().data

    # Member Method

    def act(self) -> list[list[str | int]]:
        inst = []
        if self._currentPartition._ended:
            if self._currentPartition._left != None:
                self._currentPartition = self._currentPartition._left
                inst = inst + self._currentPartition.act()
            elif self._currentPartition._right != None:
                self._currentPartition = self._currentPartition._right
                inst = inst + self._currentPartition.act()
            else:
                self.ended = True
                inst.append(["end"])
        else:
            inst = inst + self._currentPartition.act()
        return inst


class BubbleSort(Sort):
    def __init__(self, data: list[int]):
        super().__init__(data)

        self._pos = 0
        self._roopCount = 0
        self._NextStat = "comp"
        self._prevArg = []

    # Read Only
    @property
    def data(self):
        return super().data

    # Member Method

    def act(self) -> list[list[str | int]]:
        inst = []
        if not self._roopCount >= self._length - 1:
            if len(self._prevArg) > 0:
                inst.append(["default"] + self._prevArg[:])
            match self._NextStat:
                case "comp":
                    if self._pos >= self._length - 1 - self._roopCount:
                        inst.append(["disable", self._pos])
                        self._roopCount += 1
                        self._pos = 0

                    if self.data[self._pos] > self.data[self._pos + 1]:
                        self._NextStat = "swap"

                    inst.append(["comp", self._pos, self._pos + 1])

                    self._prevArg.clear()
                    self._prevArg.append(self._pos)
                    self._prevArg.append(self._pos + 1)

                    if self._NextStat == "comp":
                        self._pos += 1

                case "swap":
                    temp = self.data[self._pos + 1]
                    self.data[self._pos + 1] = self.data[self._pos]
                    self.data[self._pos] = temp
                    inst.append(["swap", self._pos, self._pos + 1])

                    self._pos += 1

                    self._NextStat = "comp"
        else:
            self.ended = True
            inst.append(["end"])
        return inst
