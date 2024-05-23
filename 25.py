import cv2
import numpy as np

# Resmi yükle
image_path = 'gul.jpg'
image = cv2.imread(image_path)

# Resmi RGB formatına çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# HSV formatına çevir
hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# Kırmızı rengin HSV aralığını belirle
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# İki maskeyi birleştir
mask = mask1 | mask2

# Gülü mor renge çevir (R ve B kanallarını değiştir)
purple_rose = image_rgb.copy()
purple_rose[mask != 0, 0], purple_rose[mask != 0, 2] = purple_rose[mask != 0, 2], purple_rose[mask != 0, 0]

# Arka planı siyah yap
background = np.zeros_like(image_rgb)

# Maskeyi kullanarak iki resmi birleştir
result = np.where(mask[:, :, np.newaxis] != 0, purple_rose, background)

# Sonucu BGR formatına çevir ve kaydet
result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
output_path = 'mor_gul_siyaharkaplan2.jpg'
cv2.imwrite(output_path, result_bgr)

output_path
