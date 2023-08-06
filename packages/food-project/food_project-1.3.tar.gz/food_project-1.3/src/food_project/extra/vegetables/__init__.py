from typing import Any


class Vegetables:
    print("огурцы")

    def __init__(self) -> None:
        print("салат")
    
    def __str__(self):
        return "лук"

    def __call__(self, letter: str) -> Any:
        assert len(letter) <= 1
        print(letter, self)