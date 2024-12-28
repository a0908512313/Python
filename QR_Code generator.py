import qrcode
qrcode = qrcode.make(input("Enter the link : "))
mode = int(input("Enter (1) for showing qrcode.\n      (2) for save the qrcode."))
if mode == 1:
    qrcode.show()
elif mode == 2:
    qrcode.save("qr_code.png")
