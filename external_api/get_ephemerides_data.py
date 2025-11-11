import httpx

from external_api.api import SSD_JPL_NASA_URL, USER_AGENT


async def get_ephemerides_data():
    """Fetches ephemerides data from the external API."""
    async with httpx.AsyncClient() as client:
        try:
            headers = {
                "User-Agent": USER_AGENT,
            }
            params = {
                "format": "json",
                "EPHEM_TYPE": "OBSERVER",
                "CENTER": "g@399",
                "START_TIME": "2025-11-09",
                "STOP_TIME": "2025-11-10",
                "STEP_SIZE": "1d",
                "COMMAND": -31,
            }
            response = await client.get(
                SSD_JPL_NASA_URL, headers=headers, params=params
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            raise TimeoutError("External API request timed out")
        except httpx.HTTPStatusError as e:
            raise Exception(
                f"External API request failed with status code {e.response.status_code}"
            )
        except Exception as e:
            raise Exception("An error occurred while fetching ephemerides data", e)
