import get_ip
import qrcode


def qr_code_gen(id):
    # img_name = "QR.png"

    data = "{}:8000/{}".format(get_ip.get_ip_address(), id)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # img.save(img_name)
    return img


qr_code_gen("5")
