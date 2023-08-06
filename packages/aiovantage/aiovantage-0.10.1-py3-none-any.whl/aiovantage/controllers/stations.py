"""Controller holding and managing Vantage stations."""

from aiovantage.models import StationObject

from .base import BaseController


class StationsController(BaseController[StationObject]):
    """Controller holding and managing Vantage stations."""

    vantage_types = (
        "Dimmer",
        "DualRelayStation",
        "EqCtrl",
        "EqUX",
        "Keypad",
        "ScenePointRelay",
        "Vantage.DmxDaliGateway",
    )
    """The Vantage object types that this controller will fetch."""
