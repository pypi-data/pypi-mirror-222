import json
from time import time

import aiohttp

PORT = 6095
TIMEOUT = 4


class Source:
    HDMI1 = "hdmi1"
    HDMI2 = "hdmi2"


class Key:
    POWER = "power"
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    ENTER = "enter"
    MENU = "menu"
    BACK = "back"
    HOME = "home"
    VOLUME_UP = "volumeup"
    VOLUME_DOWN = "volumedown"


class SystemState:
    def __init__(self, data: dict) -> None:
        self.name: str = data["devicename"]
        self.ip_address: str = data["ip"].split(":")[0]
        self.port: int = int(data["ip"].split(":")[1])
        self.features: list[str] = data["feature"]
        self.platform: int = data["platform"]
        self.build: int = data["build"]
        self.version: int = data["version"]


class SystemInfo:
    def __init__(self, data: dict) -> None:
        self.name: str = data["devicename"]
        self.id: str = data["deviceid"]
        self.platform: int = data["ptf"]
        self.code_version: int = data["codever"]
        self.wifi_mac: str = data["wifimac"]
        self.eth_mac: str = data["ethmac"]


class App:
    def __init__(self, data: dict) -> None:
        self.name: str = data["AppName"]
        self.id: str = data["PackageName"]
        self.icon_url: str = data["IconURL"]
        self.order: int = data["Order"]


class XiaomiTV:
    _session: aiohttp.ClientSession | None = None
    _volume_set_time: float | None = None

    def __init__(
        self,
        host: str,
        *,
        port: int = PORT,
        timeout: int = TIMEOUT,
    ) -> None:
        self._session = aiohttp.ClientSession(
            f"http://{host}:{port}",
            timeout=aiohttp.ClientTimeout(timeout),
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.async_close()

    async def _async_send_request(self, string: str) -> dict:
        try:
            async with self._session.get(string) as response:
                return json.loads(await response.text())["data"]
        except Exception as exc:
            raise RequestError("Request failed") from exc

    async def async_close(self):
        """Close."""
        await self._session.close()

    async def async_get_system_state(self) -> SystemState:
        """Get the system state."""
        data = await self._async_send_request("/request?action=isalive")
        return SystemState(data)

    async def async_get_system_info(self) -> SystemInfo:
        """Get the system info."""
        data = await self._async_send_request("/controller?action=getsysteminfo")
        return SystemInfo(data)

    async def async_get_apps(self) -> list[App]:
        """Get the installed apps."""
        string = "/controller?action=getinstalledapp&count=999&changeIcon=1"
        data = await self._async_send_request(string)
        return [App(info) for info in data["AppInfo"]]

    async def async_get_volume(self) -> int:
        """Get the volume."""
        string = "/controller?action=getvolume"
        data = await self._async_send_request(string)
        return data["volume"]

    async def async_press_key(self, key: Key) -> None:
        """Press a key."""
        string = f"/controller?action=keyevent&keycode={key}"
        await self._async_send_request(string)

    async def async_start_app(self, app_id: str) -> None:
        """Start a app."""
        string = f"/controller?action=startapp&type=packagename&packagename={app_id}"
        await self._async_send_request(string)

    async def async_change_source(self, source: Source) -> None:
        """Change the source."""
        string = f"/controller?action=changesource&source={source}"
        await self._async_send_request(string)

    async def async_set_volume(self, volume: int):
        """Set the volume."""
        self._volume_set_time = set_time = time()
        diff = await self.async_get_volume() - volume

        while self._volume_set_time == set_time and diff != 0:
            if diff < 0:
                await self.async_press_key(Key.VOLUME_UP)
                diff += 1
            else:
                await self.async_press_key(Key.VOLUME_DOWN)
                diff -= 1


class RequestError(Exception):
    """Error to indicate a request failed."""
