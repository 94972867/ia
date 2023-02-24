import cv2

# Charger l'image
img = cv2.imread("D:/ia/pantalon.jpg")

# Convertir l'image en niveau de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer un filtre de Canny pour détecter les contours
edges = cv2.Canny(gray, 50, 150)

# Trouver les contours dans l'image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner les contours sur l'image d'origine
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Mesurer la longueur et la largeur de l'objet en pixels
x, y, w, h = cv2.boundingRect(contours[0])
longueur_pixels = w
largeur_pixels = h

# Définir l'échelle de l'image (en cm/pixel)
echelle = 0.2

# Convertir les mesures en pixels en unités physiques
longueur_cm = longueur_pixels * echelle
largeur_cm = largeur_pixels * echelle

# Afficher les résultats
print("Longueur : ", longueur_cm, "cm")
print("Largeur : ", largeur_cm, "cm")

# Afficher l'image avec les contours détectés
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
