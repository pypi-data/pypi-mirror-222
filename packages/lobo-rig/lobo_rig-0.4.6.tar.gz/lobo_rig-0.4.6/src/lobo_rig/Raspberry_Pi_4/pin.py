"""Raspberry_Pi_4"""

"""RP Pi 4 pins"""

NAME = "Raspberry_Pi_4"

from machine import Pin

# Left
GPIO2 = Pin(2)
GPIO3 = Pin(3)
GPIO4 = Pin(4)

GPIO17 = Pin(17)
GPIO27 = Pin(27)
GPIO22 = Pin(22)

GPIO10 = Pin(10)
GPIO9 = Pin(9)
GPIO11 = Pin(11)

GPIO0 = Pin(0)
GPIO5 = Pin(5)
GPIO6 = Pin(6)
GPIO13 = Pin(13)
GPIO19 = Pin(19)
GPIO26 = Pin(26)

# Right
GPIO14 = Pin(14)
GPIO15 = Pin(15)
GPIO18 = Pin(18)

GPIO23 = Pin(23)
GPIO24 = Pin(24)

GPIO25 = Pin(25)
GPIO8 = Pin(8)
GPIO7 = Pin(7)
GPIO1 = Pin(1)

GPIO12 = Pin(12)

GPIO16 = Pin(16)
GPIO20 = Pin(20)
GPIO21 = Pin(21)

PWM = (GPIO12, GPIO13, GPIO18, GPIO19)

SPI_PORTS = (
    {
        "ID": 0,
        "SPI_MOSI": GPIO10,
        "SPI_MISO": GPIO9,
        "SPI_SCK": GPIO11,
        "SPI_CE0": GPIO8,
        "SPI_CE1": GPIO7,
    },
    {
        "ID": 1,
        "SPI_MOSI": GPIO20,
        "SPI_MISO": GPIO19,
        "SPI_SCK": GPIO21,
        "SPI_CE0": GPIO18,
        "SPI_CE1": GPIO17,
        "SPI_CE2": GPIO16,
    },
)

UART_PORTS = ({"ID": 0, "UART_TX": GPIO14, "UART_RX": GPIO15},)

I2C_PORTS = (
    {"ID": 0, "I2C_SDA": GPIO2, "I2C_SCL": GPIO3},
    {"ID": 1, "I2C_SDA": GPIO0, "I2C_SCL": GPIO1},
)
