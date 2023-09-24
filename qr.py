import qrcode

image = qrcode.make("https://127.0.0.0:8000")
image.save("qr.png")
