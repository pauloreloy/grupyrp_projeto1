
import cv2
import sys
import base64
import numpy as np
import json

def detectFace(image, __name__ = None):

  # Carregando os modelos
  face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml')
  smile_cascade = cv2.CascadeClassifier('models/haarcascade_smile.xml')

  #Lendo a imagem
  if(__name__ == "__main__"):
    image = base64.decodebytes(image)
  image = np.frombuffer(image, dtype=np.uint8)
  img = cv2.imdecode(image, flags=1)

  # Convertendo pra grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Detectando as faces
  faces = face_cascade.detectMultiScale(gray,1.07,9)

  totalsmiles = 0
  totalfaces = 0
  for (x, y, w, h) in faces:
      totalfaces = totalfaces + 1
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      # Detectando sorrisos
      smiles = smile_cascade.detectMultiScale(roi_gray, 1.01, 6)
      if len(smiles) > 0:
        totalsmiles = totalsmiles + 1
        for (sx, sy, sw, sh) in smiles:
           cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 1),

  # Exibindo a Saida
  data = dict()
  resp = dict()
  data['totalfaces'] = str(totalfaces)
  data['smiling'] = str(totalsmiles)
  resp['result'] = data
  resp = json.dumps(resp)
  if(__name__ == "__main__"):
    return(resp, img)
  else:
    return resp

if __name__ == "__main__":
  image_path = sys.argv[1]
  with open(image_path, "rb") as img_file:
    img_str = base64.b64encode(img_file.read())
    result,img = detectFace(img_str, __name__)
    result = json.loads(result)
    totalfaces = result['result']['totalfaces']
    totalsmiling = result['result']['smiling']
    msg = f"Total de Pessoas: {totalfaces}\nTotal Sorrindo: {totalsmiling}"
    print(msg)
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()