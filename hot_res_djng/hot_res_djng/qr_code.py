import get_ip
import qrcode
import wifi_qrcode_generator


def qr_code_gen(id):
    # img_name = "QR.png"

    data = "{}:8000/{}".format(get_ip.get_ip_address(), id)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # img.save(img_name)
    return img


def wifi_qr_code_gen(WIFI_name, WIFI_password):
    # WIFI_QR_code = "QR-WIFI.png"
    img = wifi_qrcode_generator.wifi_qrcode(WIFI_name, False, 'WPA', WIFI_password)
    # img.save(WIFI_QR_code)
    return img


qr_code_gen("5")
wifi_qr_code_gen('WIFI_name', 'WIFI_password')
