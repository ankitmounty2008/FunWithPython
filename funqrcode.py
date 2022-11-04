import qrcode
img = qrcode.make("Scan This QR")
img.save("AnyImage.jpg")
