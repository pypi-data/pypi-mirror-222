from typing import Optional

from vessim.core.consumer import PowerMeter
from vessim.sil.http_client import HTTPClient
from vessim.sil.stoppable_thread import StoppableThread


class HttpPowerMeter(PowerMeter):
    """Power meter for an external node that implements the vessim node API.

    This class represents a power meter for an external node. It creates a thread
    that updates the power demand from the node API at a given interval.

    Args:
        interval: The interval in seconds to update the power demand.
        server_address: The IP address of the node API.
        port: The IP port of the node API.
        name: The name of the power meter.
    """

    def __init__(
        self,
        interval: float,
        server_address: str,
        port: int = 8000,
        name: Optional[str] = None
    ) -> None:
        super().__init__(name)
        self.http_client = HTTPClient(f"{server_address}:{port}")
        self.power = 0.0
        self.update_thread = StoppableThread(self._update_power, interval)
        self.update_thread.start()

    def _update_power(self) -> None:
        """Gets the power demand every `interval` seconds from the API server."""
        self.power = float(self.http_client.get("/power")["power"])

    def measure(self) -> float:
        """Returns the current power demand of the node."""
        return self.power

    def finalize(self) -> None:
        """Terminates the power update thread when the instance is finalized."""
        self.update_thread.stop()
        self.update_thread.join()
