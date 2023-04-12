from __future__ import annotations

from typing import Self

import serial


class LightMeter:
    device: serial.Serial

    def __init__(self: Self, device_port: str) -> None:
        self.device = serial.Serial(device_port, baudrate=9600)

        if not self.device.is_open:
            self.device.open()

    def __del__(self: Self) -> None:
        if not self.device.closed:
            self.device.close()

    def read(self: Self) -> int:
        self.device.reset_input_buffer()
        data: str = self.device.read_until(b"\r").decode()

        lux = int(data[-5:])

        if data[-6] == "0":
            lux *= 10
        if data[-7] == "0":
            lux *= 10

        return lux
