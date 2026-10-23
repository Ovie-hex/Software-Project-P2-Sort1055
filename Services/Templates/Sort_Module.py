from abc import ABC, abstractmethod

from typing import *

"""
GUI_Manager에 전달할 데이터 양식 (약간 2차원 배열 비스무리함)

[ 명령, 위치1, 위치2 ] : < list[list[str | int]] >

명령 종류 :
# 공통
- comp
- swap

# 퀵정렬 전용
- pivot
- disable
- enable

ex )
[
 []
]
"""


class Sort(ABC):
    def __init__(self, data: list[int]):
        self._data = data[:]
        self._length = len(self._data)
        self._step = 0

    # Read Only
    @property
    @abstractmethod
    def data(self):
        return self.data

    # Member Method
    # act 함수 위에 _swap(self), _comp(self) 등을 정의하면 된다.

    @abstractmethod
    def act(self) -> list[list[str | int]]:
        # 이 함수 안에 데이터의 비교나 스왑 등을 수행하고 그 행위에 대한 기록을 반환해야한다.
        pass


class InsertSort(Sort):
    def __init__(self, data: list[int]):
        super().__init__(data)

        self._pos = 0

    # Read Only
    @property
    def data(self):
        return super().data

    # Member Method

    def _comp(self):
        pass

    def _swap(self):
        pass

    def act(self) -> list[list[str | int]]:
        pass


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

    def _comp(self):
        pass

    def _swap(self):
        temp = self.data[self._low]
        self.data[self._low] = self.data[self._high]
        self.data[self._high] = temp

    def _divide(self):
        pass

    def act(self) -> Any:
        pass


"""
# 먼저 전체 리스트를 파티션 클래스로 래핑하고 이후
# 그 안에 left, right를 할당하여 left가 없는 경우 먼저 있다는 소리이고,
# right가 없는 경우는 리스트의 끝자리에 있다는 소리다.
# 양쪽 없는 경우 단일 리스트라는 의미이다
"""


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

    def _comp(self):
        pass

    def _swap(self):
        pass

    def act(self) -> list[list[str | int]]:
        pass
