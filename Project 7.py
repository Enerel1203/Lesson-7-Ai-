import cv2

image = cv2.imread('image.jpg')

if image is None:
    print("Error: Image not found")
    exit()

sizes = [
    (100, 100),
    (300, 300),
    (500, 500)
]

for size in sizes:
    resized = cv2.resize(image, size)
    
    cv2.imshow(f"Resized {size}", resized)
    
    filename = f"resized_{size[0]}x{size[1]}.jpg"
    cv2.imwrite(filename, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()