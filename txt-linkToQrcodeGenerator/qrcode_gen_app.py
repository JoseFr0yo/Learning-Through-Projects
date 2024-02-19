# install qrcode & Image libraries
# create a function that collects text and converts to qrcode
# save the qrcode as img
# run the function

import qrcode
import image


def qr_gen(text):  # function to generate qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("myqrcode.png")


qr_gen("www.soyandyleal.com")
