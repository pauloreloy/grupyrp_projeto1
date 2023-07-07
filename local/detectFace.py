
import cv2
import sys

def detectFace(image):
  # Carregando os modelos
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

  #Lendo a imagem
  #img = cv2.imread(image)
  jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)

  img_np = cv2.imdecode(image, cv2.LOAD)

  # Convertendo pra grayscale
  gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

  # Detectando as faces
  faces = face_cascade.detectMultiScale(gray, 1.1, 2)

  # Detectando sorrisos
  totalsmiles = 0
  totalfaces = 0
  for (x, y, w, h) in faces:
      totalfaces = totalfaces + 1
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      smiles = smile_cascade.detectMultiScale(roi_gray, 1.3, 2)
      if len(smiles) > 0:
        totalsmiles = totalsmiles + 1
        for (sx, sy, sw, sh) in smiles:
           cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 1),

  # Exibindo a Saida
  print("Total Faces: " + str(totalfaces))
  print("Total Sorrindo: " + str(totalsmiles))
  cv2.imshow('img', img)
  cv2.waitKey()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  image_path = sys.argv[1]
  with open(image_path, encoding="utf8", errors='ignore') as f:
    #fd = open(image_path)
    image = f.read()
    #print(image)
    f.close()
    detectFace(image)
