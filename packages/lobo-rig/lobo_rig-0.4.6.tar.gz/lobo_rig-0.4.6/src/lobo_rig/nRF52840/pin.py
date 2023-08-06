NAME = "nRF52840"

from machine import Pin

# Left
D0 = A0 = Pin(2)
D1 = A1 = Pin(3)
D2 = A2 = Pin(28)
D3 = A3 = Pin(29)
D4 = A4 = I2C_SDA = Pin(4)
D5 = A5 = I2C_SCL = Pin(5)
D6 = UART_TX = Pin(43)

# Right
D10 = SPI_MOSI = Pin(10)
D9 = SPI_MISO = Pin(9)
D8 = SPI_SCK = Pin(8)
D7 = UART_RX = Pin(44)

# LEDs ~NOT.value()
RED = Pin.board.P26
GREEN = Pin.board.P30
BLUE = Pin.board.P6

# ordered as spiId, sckId, mosiId, misoId
SPI_PORTS = ({"ID": 3, "SPI_SCK": SPI_SCK, "SPI_MOSI": SPI_MOSI, "SPI_MISO": SPI_MISO},)

# ordered as uartId, txId, rxId
UART_PORTS = ({"ID": 0, "UART_TX": UART_TX, "UART_RX": UART_RX},)

# ordered as scl, sda
I2C_PORTS = ({"ID": 0, "I2C_SCL": I2C_SCL, "I2C_SDA": I2C_SDA},)

"""
As you can see in the table, the SPI and the TWI=I2C shares ID's so if you want to use SPI and TWI at the same time you'll need to use SPI0 and TWI1 for example.

If I read the table correctly you have 3 SPI/TWI available so you could use any of the following combinations:
3 SPI / 0 TWI=I2C
2 SPI / 1 TWI=I2C
1 SPI / 2 TWI=I2C
0 SPI / 3 TWI=I2C
"""
