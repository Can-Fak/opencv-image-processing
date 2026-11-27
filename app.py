import cv2

goruntu = cv2.imread("kirmizi_kalem.jpg")

if goruntu is None:
    print("Görüntü okunamadı. Dosya adını ve konumunu kontrol et.")
else:
    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

    maske1 = cv2.inRange(hsv, (0, 100, 120), (5, 255, 255))
    maske2 = cv2.inRange(hsv, (175, 100, 120), (179, 255, 255))
    maske = cv2.bitwise_or(maske1, maske2)
    sonuc = cv2.bitwise_and(goruntu, goruntu, mask=maske)
    cv2.imwrite("kalem_maske.png", maske)
    cv2.imwrite("kalem_sonuc.png", sonuc)
    cv2.imshow("Giris Goruntusu", goruntu)
    cv2.imshow("Kirmizi Maskesi", maske)
    cv2.imshow("Tespit Edilen Kirmizi Bolgeler", sonuc)

    cv2.waitKey(0)
    cv2.destroyAllWindows()