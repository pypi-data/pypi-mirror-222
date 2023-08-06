from retinaface import RetinaFace

def detect(path):
  results = RetinaFace.detect_faces(path, threshold = 0.95, allow_upscaling=False)

  faces = []
  if type(results) != dict:
    return faces

  for face in results.values():
    x1, y1, x2, y2 = face['facial_area']
    bbox = [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
    faces.append((face['score'], bbox, face['landmarks']))

  return faces