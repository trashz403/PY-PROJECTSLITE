import pyqrcode
from pyqrcode import QRCode


# Content which should be Turned into QRCode
s = "TRASHZ403"

# Generate QR code 
url = pyqrcode.create(s)

url.svg("shit.svg", scale = 8)