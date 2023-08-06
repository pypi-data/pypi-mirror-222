import asyncio
import logging
import os

import aiohttp
from aiohttp import ClientTimeout

NEWS_TOOLKIT_REQUEST_TIMEOUT = int(os.getenv("NEWS_TOOLKIT_REQUEST_TIMEOUT", 60))


async def fetch_content(url: str) -> str | None:
    try:
        async with aiohttp.ClientSession(
            timeout=ClientTimeout(NEWS_TOOLKIT_REQUEST_TIMEOUT)
        ) as session:
            async with session.get(url) as res:
                res.raise_for_status()
                return await res.text()
    except aiohttp.ClientError as e:
        logging.error(f"Error fetching the url {url}: {e}")
        return None
    except asyncio.TimeoutError:
        logging.error(f"Timeout while fetching the url {url}.")
        return None
