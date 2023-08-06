from dataclasses import dataclass
from enum import Enum


class BannerAdSize(Enum):
    normal = "normal"
    large = "large"
    extraLarge = "extraLarge"
    anchoredAdaptive = "anchoredAdaptive"


@dataclass(frozen=True)
class BannerAdContent:
    size: BannerAdSize
    __identifier = "__banner_ad__"

    @property
    def type(self) -> str:
        return self.__identifier
