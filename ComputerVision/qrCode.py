'''
# Importing library
import qrcode
 
# Data to be encoded
#data = '- Facebook: https://www.facebook.com/sumbuilders\n- Instagram: https://www.instagram.com/sumbuilders\n- Youtube: https://www.youtube.com/@sumbuilders\n- Email: sumbuildersteam@gmail.com\n- WhatsApp Group: https://chat.whatsapp.com/HcL37cG0BjiK04rWqSTdkA'
data = 'https://chat.whatsapp.com/HcL37cG0BjiK04rWqSTdkA'
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('sumbuildersWhatsapp.png')
'''
import time
print("asd")
time.sleep(5)
print("LOOO")