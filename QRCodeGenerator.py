import qrcode


def QRCodeGenerator():

    # instance of qrcode
    qr = qrcode.QRCode(
        version=2,  # 1 to 40 - higher the number, more complex is QR
        box_size=10,  # size of the qr-code
        border=1  # same as css padding
    )

    # to convert URL to QRCode, place the URL as function argument
    qr.add_data(getUserData())
    qr.make(fit=True)
    qr.make_image().save('qr.jpg')


def getUserData():
    name = input('Please enter you name: ')
    mobileNumber = input('Please enter your mobile number: ')
    email = input('Please enter your email ID: ')
    return f'Name = {name}\nMobile Number = +1 {mobileNumber}\nEmail = {email}'


QRCodeGenerator()
