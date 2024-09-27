from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field


class SecChUaItemModel(BaseModel):
    """A model representing single item of the Sec-CH-UA HTTP header.

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA

    Attributes:
        brand: The browser name (e.g., "Google Chrome").
        significant_version: The significant version of the browser or engine (e.g., 75).
    """

    brand: str
    significant_version: int

    @property
    def value(self) -> str:
        """Returns the formatted value."""
        return f'"{self.brand}";v="{self.significant_version}"'


class SecChUaModel(BaseModel):
    """A model representing Sec-CH-UA HTTP header.

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA

    Attributes:
        uas: A list of `SecChUaItemModel` items representing the user-agent brands and versions.
    """

    uas: list[SecChUaItemModel]

    @property
    def header_value(self) -> str:
        """Returns the formatted value of the header."""
        return ', '.join(item.value for item in self.uas)


class SecChUaMobileModel(BaseModel):
    """A model representing Sec-CH-UA-Mobile HTTP header.

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Mobile

    Attributes:
        mobile: A boolean indicating if the client is mobile (`True` for mobile, `False` otherwise).
    """

    mobile: bool

    @property
    def header_value(self) -> str:
        return '?1' if self.mobile else '?0'


class SecChUaPlatformModel(BaseModel):
    """A model representing Sec-CH-UA-Platform HTTP header .

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Platform

    Attributes:
        platform: The platform name (e.g., "Windows").
    """

    platform: Literal['Android', 'Chrome OS', 'Chromium OS', 'iOS', 'Linux', 'macOS', 'Windows', 'Unknown']

    @property
    def header_value(self) -> str:
        """Returns the formatted value of the header."""
        return f'"{self.platform}"'


class UserAgentExtensionModel(BaseModel):
    """A model representing an extension part of the User-Agent HTTP header.

    Attributes:
        browser: The browser name (e.g., "Chrome").
        version: The browser version (e.g., "113.0.0.0").
    """

    browser: str
    version: str

    @property
    def value(self) -> str:
        """Returns the formatted value."""
        return f'{self.browser}/{self.version}'


class UserAgentModel(BaseModel):
    """A model representing User-Agent HTTP header.

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

    Attributes:
        compatibility_token: The compatibility token, often "Mozilla/5.0".
        system_information: Information about the system, including OS and architecture.
        platform: The browser engine or platform (e.g., "AppleWebKit/537.36").
        platform_details: Additional platform details (e.g., "KHTML, like Gecko").
        extensions: A list of extensions - browsers and their versions (e.g., "Chrome/113.0.0.0", "Safari/537.36").
    """

    compatibility_token: Annotated[str, Field(alias='compatibilityToken')]
    system_information: Annotated[str, Field(alias='systemInformation')]
    platform: str
    platform_details: Annotated[str, Field(alias='platformDetails')]
    extensions: list[UserAgentExtensionModel]

    def from_header_value(self, user_agent: str) -> UserAgentModel:
        """Parse a User-Agent string and return a UserAgentModel instance."""
        return None  # TODO

    @property
    def header_value(self) -> str:
        """Returns the formatted value of the header."""
        return f'{self.compatibility_token} ({self.system_information}) {self.platform} ({self.platform_details}) {self.extensions}'  # noqa: E501

    @property
    def sec_ch_ua(self) -> SecChUaModel:
        return None  # TODO

    @property
    def sec_ch_ua_mobile(self) -> SecChUaMobileModel:
        return None  # TODO

    @property
    def sec_ch_ua_platform(self) -> SecChUaPlatformModel:
        return None  # TODO


