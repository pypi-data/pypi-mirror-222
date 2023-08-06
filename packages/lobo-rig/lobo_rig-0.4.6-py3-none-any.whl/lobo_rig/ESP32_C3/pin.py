NAME = "ESP32_C3"

from machine import Pin

# Left
GPIO2 = D0 = A0 = Pin(2)
GPIO3 = D1 = A1 = Pin(3)
GPIO4 = D2 = A2 = Pin(4)
GPIO5 = D3 = A3 = Pin(5)
GPIO6 = D4 = I2C_SDA = Pin(6)
GPIO7 = D5 = I2C_SCL = Pin(7)
GPIO21 = D6 = UART_TX = Pin(21)

# Right
GPIO10 = D10 = SPI_MOSI = Pin(10)
GPIO9 = D9 = SPI_MISO = Pin(9)
GPIO8 = D8 = SPI_SCK = Pin(8)
GPIO20 = D7 = UART_RX = Pin(20)

# ordered as spiId, sckId, mosiId, misoId
SPI_PORTS = ({"ID": 0, "SPI_SCK": SPI_SCK, "SPI_MOSI": SPI_MOSI, "SPI_MISO": SPI_MISO},)

# ordered as uartId, txId, rxId
UART_PORTS = ({"ID": 0, "UART_TX": UART_TX, "UART_RX": UART_RX},)

# ordered as scl, sda
I2C_PORTS = ({"ID": 0, "I2C_SCL": I2C_SCL, "I2C_SDA": I2C_SDA},)
