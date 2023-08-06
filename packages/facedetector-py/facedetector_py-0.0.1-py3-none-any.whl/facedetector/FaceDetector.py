from .util import ( detector, align, geometry )

def detect(img):
  output = []
  faces = detector.detect(img)
  for face in faces:
    score, orig_bbox, landmarks = face
    landmarks = add_landmarks(landmarks)
    pivot = landmarks['eyes_center']
    angle = align.calc_angle(landmarks)

    eye_line = [landmarks['left_eye'], landmarks['right_eye']]
    face_line = [landmarks['eyes_center'], landmarks['mouth_center']]
    face_line_length = geometry.distance(face_line)
    eye_line_length = geometry.distance(eye_line)
    max_length = max(face_line_length, eye_line_length)

    bbox_size = int(max_length / .30)
    bbox_offset_x = int(bbox_size / 2)
    bbox_offset_y = int(bbox_size * .55)
    bbox = [(0-bbox_offset_x,0-bbox_offset_y),(bbox_size-bbox_offset_x,0-bbox_offset_y),(bbox_size-bbox_offset_x,bbox_size-bbox_offset_y),(0-bbox_offset_x,bbox_size-bbox_offset_y)]
    bbox = geometry.move(bbox, (pivot[0], pivot[1]+face_line_length/2))
    bbox = geometry.rotate(bbox, pivot, angle)

    output.append({
      "score": score,
      "angle": angle,
      "size": bbox_size,
      "pivot": landmarks["face_center"],
      "bounding_box": bbox,
      "landmarks": landmarks
    })

  return output

def add_landmarks(landmarks):
  #left eye is the eye appearing on the left (right eye of the person)
  left_eye_x, left_eye_y = landmarks["right_eye"]
  right_eye_x, right_eye_y = landmarks["left_eye"]
  left_mouth_x, left_mouth_y = landmarks["mouth_right"]
  right_mouth_x, right_mouth_y = landmarks["mouth_left"]

  eyes_center_x, eyes_center_y = (int((left_eye_x + right_eye_x) / 2), int((left_eye_y + right_eye_y) / 2))
  mouth_center_x, mouth_center_y = (int((left_mouth_x + right_mouth_x) / 2), int((left_mouth_y + right_mouth_y) / 2))
  landmarks['eyes_center'] = (eyes_center_x, eyes_center_y)
  landmarks['mouth_center'] = (mouth_center_x, mouth_center_y)
  landmarks['face_center'] = (int((eyes_center_x + mouth_center_x) / 2), int((eyes_center_y + mouth_center_y) / 2))

  return landmarks