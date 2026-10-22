from abc import ABC, abstractmethod

from types import FunctionType
from typing import Any

"""
GUI_Manager에 전달할 데이터 딕셔너리 양식
{
 IDK
}
"""


class Sort(ABC):
    def __init__(self, data: list[int]):
        self._data = data[:]
        self._length = len(self._data)

    # Read Only
    @property
    @abstractmethod
    def data(self):
        return self.data

    # Member Method
    # act 함수 위에 _swap(self), _comp(self) 등을 정의하면 된다.

    @abstractmethod
    def act(self) -> dict[str, any]:
        # 이 함수 안에 데이터의 비교나 스왑 등을 수행하고 그 행위에 대한 기록을 반환해야한다.
        pass


class InsertSort(Sort):
    def __init__(self, data):
        super().__init__(data)

        self._pos = 0

    # Read Only
    @property
    def data(self):
        return super().data


class QuickSort(Sort):
    def __init__(self, data):
        super().__init__(data)

    # Member Method

    # Read Only
    @property
    def data(self):
        return super().data


class BubbleSort(Sort):
    def __init__(self, data):
        super().__init__(data)

        self._pos = 0

    # Read Only
    @property
    def data(self):
        return super().data
