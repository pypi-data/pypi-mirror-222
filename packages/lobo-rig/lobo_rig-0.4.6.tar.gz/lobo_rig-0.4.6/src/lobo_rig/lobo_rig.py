# (c) Lukasz Lobocki

import sys

if __name__ == "__main__":
    print(sys.implementation._machine)

if sys.implementation.name == "micropython":
    if sys.implementation._machine == "ESP32C3 module with ESP32C3":
        from .ESP32_C3.pin import *
    elif sys.implementation._machine == "XIAO nRF52840 Sense with NRF52840":
        from .nRF52840.pin import *
    elif sys.implementation._machine == "Raspberry Pi Pico W with RP2040":
        from .RP2040.pin import *
    elif sys.implementation._machine == "ProS3 with ESP32-S3":
        from .ESP32_S3_pro.pin import *
    elif sys.implementation._machine == "ESP32S3 module (spiram) with ESP32S3":
        from .ESP32_S3_mini.pin import *
    else:
        raise NotImplementedError(
            "Unknown board. Implementation: {i}. Machine: {m}.".format(
                i=sys.implementation.name, m=sys.implementation._machine
            )
        )
else:
    raise NotImplementedError(
        "Unknown board. Implementation: {i}. Machine: {m}.".format(
            i=sys.implementation.name, m=sys.implementation._machine
        )
    )
