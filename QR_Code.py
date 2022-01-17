import qrcode
import image

qr_code = qrcode.QRCode(version = 15 , box_size = 10 , border = 5)
data = "HelloWorld"
qr_code.add_data(data)
qr_code.make(fit = True)
img = qr_code.make_image(fill = "black" , back_color = "white")
img.save("test.png")
