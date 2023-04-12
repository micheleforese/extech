# Extech Devices

## Light Meter 407026

<!-- ```{.Python, .copy} -->

```py
import extech

lux_meter = extech.LightMeter(device_port="/dev/ttyUSB1")
data: int | None = lux_meter.read()
print(data)
```
