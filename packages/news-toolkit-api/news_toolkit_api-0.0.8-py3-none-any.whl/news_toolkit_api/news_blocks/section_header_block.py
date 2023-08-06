from dataclasses import dataclass


@dataclass(frozen=True)
class SectionHeaderBlock:
    title: str
    __identifier = "__section_header__"

    @property
    def type(self) -> str:
        return self.__identifier
