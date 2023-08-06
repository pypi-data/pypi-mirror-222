NAME = "RP2040"

from machine import Pin

GP0 = Pin(0)
GP1 = Pin(1)
GP2 = Pin(2)
GP3 = Pin(3)
GP4 = Pin(4)
GP5 = Pin(5)
GP6 = Pin(6)
GP7 = Pin(7)
GP8 = Pin(8)
GP9 = Pin(9)
GP10 = Pin(10)
GP11 = Pin(11)
GP12 = Pin(12)
GP13 = Pin(13)
GP14 = Pin(14)
GP15 = Pin(15)
GP16 = Pin(16)
GP17 = Pin(17)
GP18 = Pin(18)
GP19 = Pin(19)
GP20 = Pin(20)
GP21 = Pin(21)
GP22 = Pin(22)
GP23 = Pin(23)
GP24 = Pin(24)
GP25 = Pin(25)
GP26 = Pin(26)
GP27 = Pin(27)
GP28 = Pin(28)
GP29 = Pin(29)

# ordered as spiId, sckId, mosiId (tx}, misoId (rx)
SPI_PORTS = (
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP3, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP3, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP3, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP7, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP7, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP7, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP19, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP19, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP2, "SPI_MOSI": GP19, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP3, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP3, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP3, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP7, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP7, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP7, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP19, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP19, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP6, "SPI_MOSI": GP19, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP3, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP3, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP3, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP7, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP7, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP7, "SPI_MISO": GP16},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP19, "SPI_MISO": GP0},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP19, "SPI_MISO": GP4},
    {"ID": 0, "SPI_SCK": GP18, "SPI_MOSI": GP19, "SPI_MISO": GP16},
    {"ID": 1, "SPI_SCK": GP10, "SPI_MOSI": GP11, "SPI_MISO": GP8},
    {"ID": 1, "SPI_SCK": GP10, "SPI_MOSI": GP11, "SPI_MISO": GP12},
    {"ID": 1, "SPI_SCK": GP10, "SPI_MOSI": GP15, "SPI_MISO": GP8},
    {"ID": 1, "SPI_SCK": GP10, "SPI_MOSI": GP15, "SPI_MISO": GP12},
    {"ID": 1, "SPI_SCK": GP14, "SPI_MOSI": GP11, "SPI_MISO": GP8},
    {"ID": 1, "SPI_SCK": GP14, "SPI_MOSI": GP11, "SPI_MISO": GP12},
    {"ID": 1, "SPI_SCK": GP14, "SPI_MOSI": GP15, "SPI_MISO": GP8},
    {"ID": 1, "SPI_SCK": GP14, "SPI_MOSI": GP15, "SPI_MISO": GP12},
)

# ordered as uartId, txId, rxId
UART_PORTS = (
    {"ID": 0, "UART_TX": GP0, "UART_RX": GP1},
    {"ID": 0, "UART_TX": GP0, "UART_RX": GP13},
    {"ID": 0, "UART_TX": GP12, "UART_RX": GP1},
    {"ID": 0, "UART_TX": GP12, "UART_RX": GP13},
    {"ID": 1, "UART_TX": GP4, "UART_RX": GP5},
    {"ID": 1, "UART_TX": GP4, "UART_RX": GP9},
    {"ID": 1, "UART_TX": GP8, "UART_RX": GP5},
    {"ID": 1, "UART_TX": GP8, "UART_RX": GP9},
)

# ordered as scl, sda
I2C_PORTS = (
    {"ID": 0, "SCL": GP1, "SDA": GP0},
    {"ID": 0, "SCL": GP1, "SDA": GP4},
    {"ID": 0, "SCL": GP1, "SDA": GP8},
    {"ID": 0, "SCL": GP1, "SDA": GP12},
    {"ID": 0, "SCL": GP1, "SDA": GP16},
    {"ID": 0, "SCL": GP1, "SDA": GP20},
    {"ID": 0, "SCL": GP1, "SDA": GP24},
    {"ID": 0, "SCL": GP1, "SDA": GP28},
    {"ID": 1, "SCL": GP3, "SDA": GP2},
    {"ID": 1, "SCL": GP3, "SDA": GP6},
    {"ID": 1, "SCL": GP3, "SDA": GP10},
    {"ID": 1, "SCL": GP3, "SDA": GP14},
    {"ID": 1, "SCL": GP3, "SDA": GP18},
    {"ID": 1, "SCL": GP3, "SDA": GP22},
    {"ID": 1, "SCL": GP3, "SDA": GP26},
    {"ID": 0, "SCL": GP5, "SDA": GP0},
    {"ID": 0, "SCL": GP5, "SDA": GP4},
    {"ID": 0, "SCL": GP5, "SDA": GP8},
    {"ID": 0, "SCL": GP5, "SDA": GP12},
    {"ID": 0, "SCL": GP5, "SDA": GP16},
    {"ID": 0, "SCL": GP5, "SDA": GP20},
    {"ID": 0, "SCL": GP5, "SDA": GP24},
    {"ID": 0, "SCL": GP5, "SDA": GP28},
    {"ID": 1, "SCL": GP7, "SDA": GP2},
    {"ID": 1, "SCL": GP7, "SDA": GP6},
    {"ID": 1, "SCL": GP7, "SDA": GP10},
    {"ID": 1, "SCL": GP7, "SDA": GP14},
    {"ID": 1, "SCL": GP7, "SDA": GP18},
    {"ID": 1, "SCL": GP7, "SDA": GP22},
    {"ID": 1, "SCL": GP7, "SDA": GP26},
    {"ID": 0, "SCL": GP9, "SDA": GP0},
    {"ID": 0, "SCL": GP9, "SDA": GP4},
    {"ID": 0, "SCL": GP9, "SDA": GP8},
    {"ID": 0, "SCL": GP9, "SDA": GP12},
    {"ID": 0, "SCL": GP9, "SDA": GP16},
    {"ID": 0, "SCL": GP9, "SDA": GP20},
    {"ID": 0, "SCL": GP9, "SDA": GP24},
    {"ID": 0, "SCL": GP9, "SDA": GP28},
    {"ID": 1, "SCL": GP11, "SDA": GP2},
    {"ID": 1, "SCL": GP11, "SDA": GP6},
    {"ID": 1, "SCL": GP11, "SDA": GP10},
    {"ID": 1, "SCL": GP11, "SDA": GP14},
    {"ID": 1, "SCL": GP11, "SDA": GP18},
    {"ID": 1, "SCL": GP11, "SDA": GP22},
    {"ID": 1, "SCL": GP11, "SDA": GP26},
    {"ID": 0, "SCL": GP13, "SDA": GP0},
    {"ID": 0, "SCL": GP13, "SDA": GP4},
    {"ID": 0, "SCL": GP13, "SDA": GP8},
    {"ID": 0, "SCL": GP13, "SDA": GP12},
    {"ID": 0, "SCL": GP13, "SDA": GP16},
    {"ID": 0, "SCL": GP13, "SDA": GP20},
    {"ID": 0, "SCL": GP13, "SDA": GP24},
    {"ID": 0, "SCL": GP13, "SDA": GP28},
    {"ID": 1, "SCL": GP15, "SDA": GP2},
    {"ID": 1, "SCL": GP15, "SDA": GP6},
    {"ID": 1, "SCL": GP15, "SDA": GP10},
    {"ID": 1, "SCL": GP15, "SDA": GP14},
    {"ID": 1, "SCL": GP15, "SDA": GP18},
    {"ID": 1, "SCL": GP15, "SDA": GP22},
    {"ID": 1, "SCL": GP15, "SDA": GP26},
    {"ID": 0, "SCL": GP17, "SDA": GP0},
    {"ID": 0, "SCL": GP17, "SDA": GP4},
    {"ID": 0, "SCL": GP17, "SDA": GP8},
    {"ID": 0, "SCL": GP17, "SDA": GP12},
    {"ID": 0, "SCL": GP17, "SDA": GP16},
    {"ID": 0, "SCL": GP17, "SDA": GP20},
    {"ID": 0, "SCL": GP17, "SDA": GP24},
    {"ID": 0, "SCL": GP17, "SDA": GP28},
    {"ID": 1, "SCL": GP19, "SDA": GP2},
    {"ID": 1, "SCL": GP19, "SDA": GP6},
    {"ID": 1, "SCL": GP19, "SDA": GP10},
    {"ID": 1, "SCL": GP19, "SDA": GP14},
    {"ID": 1, "SCL": GP19, "SDA": GP18},
    {"ID": 1, "SCL": GP19, "SDA": GP22},
    {"ID": 1, "SCL": GP19, "SDA": GP26},
    {"ID": 0, "SCL": GP21, "SDA": GP0},
    {"ID": 0, "SCL": GP21, "SDA": GP4},
    {"ID": 0, "SCL": GP21, "SDA": GP8},
    {"ID": 0, "SCL": GP21, "SDA": GP12},
    {"ID": 0, "SCL": GP21, "SDA": GP16},
    {"ID": 0, "SCL": GP21, "SDA": GP20},
    {"ID": 0, "SCL": GP21, "SDA": GP24},
    {"ID": 0, "SCL": GP21, "SDA": GP28},
    {"ID": 1, "SCL": GP23, "SDA": GP2},
    {"ID": 1, "SCL": GP23, "SDA": GP6},
    {"ID": 1, "SCL": GP23, "SDA": GP10},
    {"ID": 1, "SCL": GP23, "SDA": GP14},
    {"ID": 1, "SCL": GP23, "SDA": GP18},
    {"ID": 1, "SCL": GP23, "SDA": GP22},
    {"ID": 1, "SCL": GP23, "SDA": GP26},
    {"ID": 0, "SCL": GP25, "SDA": GP0},
    {"ID": 0, "SCL": GP25, "SDA": GP4},
    {"ID": 0, "SCL": GP25, "SDA": GP8},
    {"ID": 0, "SCL": GP25, "SDA": GP12},
    {"ID": 0, "SCL": GP25, "SDA": GP16},
    {"ID": 0, "SCL": GP25, "SDA": GP20},
    {"ID": 0, "SCL": GP25, "SDA": GP24},
    {"ID": 0, "SCL": GP25, "SDA": GP28},
    {"ID": 1, "SCL": GP27, "SDA": GP2},
    {"ID": 1, "SCL": GP27, "SDA": GP6},
    {"ID": 1, "SCL": GP27, "SDA": GP10},
    {"ID": 1, "SCL": GP27, "SDA": GP14},
    {"ID": 1, "SCL": GP27, "SDA": GP18},
    {"ID": 1, "SCL": GP27, "SDA": GP22},
    {"ID": 1, "SCL": GP27, "SDA": GP26},
    {"ID": 0, "SCL": GP29, "SDA": GP0},
    {"ID": 0, "SCL": GP29, "SDA": GP4},
    {"ID": 0, "SCL": GP29, "SDA": GP8},
    {"ID": 0, "SCL": GP29, "SDA": GP12},
    {"ID": 0, "SCL": GP29, "SDA": GP16},
    {"ID": 0, "SCL": GP29, "SDA": GP20},
    {"ID": 0, "SCL": GP29, "SDA": GP24},
    {"ID": 0, "SCL": GP29, "SDA": GP28},
)
