# lets make a qr code
# lets install a package named qr code
import qrcode
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants. ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcodeimage01.png")

url = input("Enter your URL:")
generate_qrcode(url)


# Must be a bug 