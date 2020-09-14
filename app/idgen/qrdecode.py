from PIL import Image

from pyzbar.pyzbar import decode


def decode_qr(filename='test_card.jpeg'):
    """
    Returns dictionary with key, value pair

    Parameters
    ----------
        filename: qrcode file path

    Return
    ------
        dict: key value pair

    """
    d = decode(Image.open(filename))
    data = d[0].data.decode('ascii')
    data = data.replace(':', '').split()
    dict = {data[i]: data[i+1] for i in range(0, len(data), 2)}
    return dict


print(decode_qr())
