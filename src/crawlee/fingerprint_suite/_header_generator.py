from __future__ import annotations

import random
from typing import TYPE_CHECKING

from crawlee.fingerprint_suite._consts import COMMON_ACCEPT, COMMON_ACCEPT_LANGUAGE, USER_AGENT_POOL

if TYPE_CHECKING:
    from collections.abc import Mapping


class HeaderGenerator:
    """Generates common headers for HTTP requests."""

    def get_common_headers(
        self,
        *,
        include_random_user_agent: bool = True,
    ) -> Mapping[str, str]:
        """Get common headers for HTTP requests.

        We do not modify the 'Accept-Encoding', 'Connection' and other headers. They should be included and handled
        by the HTTP client.

        Args:
            include_random_user_agent: Whether to include a random User-Agent header.

        Returns:
            Dictionary containing common headers.
        """
        headers = {
            'Accept': COMMON_ACCEPT,
            'Accept-Language': COMMON_ACCEPT_LANGUAGE,
        }

        if include_random_user_agent:
            headers['User-Agent'] = random.choice(USER_AGENT_POOL)

        return headers
