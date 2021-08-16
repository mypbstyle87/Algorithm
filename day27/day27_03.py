# 체인법으로 해시 함수 구하기

from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    # 해시를 구성하는 노드

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        # 초기화
        self.key = key
        self.value = value
        self.next = next
