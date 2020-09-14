# import pyqrcode

# qr = pyqrcode.create('hello')

# print(qr)

# qr.png('abc.png', scale=8)



# Read QR code

from pyzbar.pyzbar import decode

from PIL import Image

d = decode(Image.open('test_card.jpeg'))

print(d[0].data.decode('ascii'))


# import qrcode
# from PIL import Image, ImageDraw

# qr = qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# qr.add_data('Sudip Bhujel \
#     Random alskdnf ajfals\
#         askdjflaksndf;asndkf \
#             alskdjf;lasjdf;lkasjdfl;jas')
# qr.make(fit=True)

# img = qr.make_image(fill_color='black', back_color='white')

# img.thumbnail((150, 150), Image.ANTIALIAS)

# print(img.size)

# background_image = Image.new('RGB', (500,500), 'rgb(255,255,255)')

# background_image.paste(img, (0,0))

# draw = ImageDraw.Draw(background_image)

# draw.text((200,200), 'Sudip Bhujel', fill='rgb(0,0,0)')

# background_image.save('pase.png')