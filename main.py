import cv2
import qrcode

# x = qrcode.make("https://www.javatpoint.com/javascript-oops-static-method")
# x.save("tut.jpg")

x = qrcode.make("Hello World")
x.save("t.jpg")


d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread('t.jpg'))
print(val)
