NAME = "ESP32_S3_pro"

from machine import Pin

# Left
GPIO35 = D35 = SPI_MOSI = Pin(35)
GPIO37 = D37 = SPI_MISO = Pin(37)
GPIO36 = D36 = SPI_SCK = Pin(36)
GPIO34 = D34 = Pin(34)
GPIO9 = D9 = A8 = I2C_SCL = Pin(9)
GPIO8 = D8 = A7 = I2C_SDA = Pin(8)
GPIO7 = D7 = A6 = Pin(7)
GPIO6 = D6 = A5 = Pin(6)

GPIO43 = D43 = UART_TX = Pin(43)
GPIO44 = D44 = UART_RX = Pin(44)
GPIO38 = D38 = Pin(38)
GPIO39 = D39 = Pin(39)
GPIO40 = D40 = Pin(40)
GPIO41 = D41 = Pin(41)
GPIO42 = D42 = Pin(42)

# Right
RGB_LED_DATA = Pin(18)
DETECT_5V_PRESENT = Pin(33)
BATTERY_VOLTAGE = Pin(10)
LD02_PWR_EN = Pin(17)

GPIO1 = D1 = A0 = Pin(1)
GPIO2 = D2 = A1 = Pin(2)
GPIO3 = D3 = A2 = Pin(3)
GPIO4 = D4 = A3 = Pin(4)
GPIO5 = D4 = A3 = Pin(5)
GPIO21 = D21 = Pin(21)
GPIO0 = D0 = Pin(0)

GPIO16 = D16 = A15 = Pin(16)
GPIO15 = D15 = A14 = Pin(15)
GPIO14 = D14 = A13 = Pin(14)
GPIO13 = D13 = A12 = Pin(13)
GPIO12 = D12 = A11 = Pin(12)

# ordered as spiId, sckId, mosiId, misoId
SPI_PORTS = ({"ID": 1, "SPI_SCK": SPI_SCK, "SPI_MOSI": SPI_MOSI, "SPI_MISO": SPI_MISO},)

# ordered as uartId, txId, rxId
UART_PORTS = ({"ID": 0, "UART_TX": UART_TX, "UART_RX": UART_RX},)

# ordered as scl, sda
I2C_PORTS = ({"ID": 0, "I2C_SCL": I2C_SCL, "I2C_SDA": I2C_SDA},)
