from __future__ import annotations

from typing import TYPE_CHECKING

from crawlee.fingerprint_suite._consts import (
    PW_CHROMIUM_HEADLESS_DEFAULT_SEC_CH_UA,
    PW_CHROMIUM_HEADLESS_DEFAULT_SEC_CH_UA_MOBILE,
    PW_CHROMIUM_HEADLESS_DEFAULT_SEC_CH_UA_PLATFORM,
    PW_CHROMIUM_HEADLESS_DEFAULT_USER_AGENT,
    PW_FIREFOX_HEADLESS_DEFAULT_USER_AGENT,
    PW_WEBKIT_HEADLESS_DEFAULT_USER_AGENT,
)
from crawlee.fingerprint_suite._header_generator import HeaderGenerator

if TYPE_CHECKING:
    from collections.abc import Mapping

    from playwright.async_api import Request, Route

    from crawlee.browsers._types import BrowserType


class FingerprintInjector:
    """Injects a fingerprint into the request headers."""

    _DEFAULT_HEADER_GENERATOR = HeaderGenerator()

    def __init__(
        self,
        header_generator: HeaderGenerator = _DEFAULT_HEADER_GENERATOR,
    ) -> None:
        self._header_generator = header_generator

    async def inject_fingerprint(
        self,
        route: Route,
        request: Request,
        browser_type: BrowserType,
    ) -> None:
        """Injects a fingerprint into the request headers."""
        common_headers = self._header_generator.get_common_headers(include_random_user_agent=False)
        user_agent_headers = self._get_user_agent_headers(browser_type=browser_type)

        headers = {
            **request.headers,
            **common_headers,
            **user_agent_headers,
        }

        # Continue the request with modified headers
        await route.continue_(headers=headers)

    def _get_user_agent_headers(
        self,
        browser_type: BrowserType,
    ) -> Mapping[str, str]:
        headers = {}

        if browser_type == 'chromium':
            headers['User-Agent'] = PW_CHROMIUM_HEADLESS_DEFAULT_USER_AGENT
            headers['Sec-Ch-Ua'] = PW_CHROMIUM_HEADLESS_DEFAULT_SEC_CH_UA
            headers['Sec-Ch-Ua-Mobile'] = PW_CHROMIUM_HEADLESS_DEFAULT_SEC_CH_UA_MOBILE
            headers['Sec-Ch-Ua-Platform'] = PW_CHROMIUM_HEADLESS_DEFAULT_SEC_CH_UA_PLATFORM

        elif browser_type == 'firefox':
            headers['User-Agent'] = PW_FIREFOX_HEADLESS_DEFAULT_USER_AGENT

        elif browser_type == 'webkit':
            headers['User-Agent'] = PW_WEBKIT_HEADLESS_DEFAULT_USER_AGENT

        else:
            raise ValueError(f'Unsupported browser type: {browser_type}')

        return headers
