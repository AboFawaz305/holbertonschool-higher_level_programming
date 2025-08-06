#!/usr/bin/python3
class VerboseList(list):
    def append(self, object, /) -> None:
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable, /) -> None:
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)

    def remove(self, value, /) -> None:
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index=-1, /):
        r = super().pop(index)
        print(f"Popped [{r}] from the list.")
        return r
