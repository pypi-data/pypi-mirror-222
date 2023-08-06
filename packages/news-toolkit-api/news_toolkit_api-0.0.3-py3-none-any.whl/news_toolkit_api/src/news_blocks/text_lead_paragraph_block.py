from dataclasses import dataclass


@dataclass(frozen=True)
class TextLeadParagraphBlock:
    text: str
    __identifier = "__text_lead_paragraph__"

    @property
    def type(self) -> str:
        return self.__identifier
