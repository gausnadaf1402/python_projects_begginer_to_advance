import qrcode

def generate__qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2
    )

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="yellow",back_color="black")
    img.save("qrimg.png")

url=input("Enter your url:")
generate__qrcode(url)
