import asyncio
import winsdk.windows.devices.geolocation as wdg
from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float


async def getCoords() -> Coordinates:
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return Coordinates(latitude=pos.coordinate.latitude, longitude=pos.coordinate.longitude)


def get_loc():

    print('Getting your current coordinates...')

    try:
        return asyncio.run(getCoords())
    except PermissionError:
        print("ERROR: You need to allow applications to access you location in Windows settings")