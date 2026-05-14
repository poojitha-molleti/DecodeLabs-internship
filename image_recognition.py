import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("sample.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

text = pytesseract.image_to_string(gray)

print("\n📝 Extracted Text:\n")
print(text)

cv2.imshow("Input Image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()