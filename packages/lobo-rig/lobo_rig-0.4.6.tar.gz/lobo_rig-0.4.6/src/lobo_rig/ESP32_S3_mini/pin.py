NAME = "ESP32_S3_mini"

from machine import Pin

# Left
GPIO18 = A0 = Pin(18)
GPIO17 = A1 = Pin(17)
GPIO16 = A2 = Pin(16)
GPIO15 = A3 = Pin(15)
GPIO14 = A4 = Pin(14)
GPIO8 = A5 = Pin(8)
GPIO36 = SPI_SCK = Pin(36)
GPIO35 = SPI_MOSI = Pin(35)
GPIO37 = SPI_MISO = Pin(37)
GPIO38 = UART_RX = Pin(38)
GPIO39 = UART_TX = Pin(39)

# Right
GPIO13 = D13 = Pin(13)
GPIO12 = D12 = Pin(12)
GPIO11 = D11 = Pin(11)
GPIO10 = D10 = Pin(10)
GPIO9 = D9 = Pin(9)
GPIO6 = D6 = Pin(6)
GPIO5 = D5 = Pin(5)
GPIO4 = I2C_SCL = Pin(4)
GPIO3 = I2C_SDA = Pin(3)

GPIO21 = NEOPIXEL_POWER = Pin(21)
GPIO33 = NEOPIXEL = Pin(33)

# ordered as spiId, sckId, mosiId, misoId
SPI_PORTS = ({"ID": 2, "SPI_SCK": SPI_SCK, "SPI_MOSI": SPI_MOSI, "SPI_MISO": SPI_MISO},)

# ordered as uartId, txId, rxId
UART_PORTS = ({"ID": 0, "UART_TX": UART_TX, "UART_RX": UART_RX},)

# ordered as scl, sda
I2C_PORTS = ({"ID": 0, "I2C_SCL": I2C_SCL, "I2C_SDA": I2C_SDA},)
