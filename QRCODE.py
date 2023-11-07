#install libraries needed
#create a function that collects text and converts it to QRcode
#save the QR code as an image 
#run the function


import qrcode
import os

def generate_QR_code(text):
    QR=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)
    QR.add_data(text)
    QR.make(fit=True)
    QR_image=QR.make_image(fill_color='black',back_color="white")

    #providing the absolute path where we can save the file
    save__path=os.path.join(os.getcwd(),'QR_code.png')
    QR_image.save(save__path)

text=input("enter a text to encode")
generate_QR_code(text)
print(os.path.join(os.getcwd(),'QR_code.png'))