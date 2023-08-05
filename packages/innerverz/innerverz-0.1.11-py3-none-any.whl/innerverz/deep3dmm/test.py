import cv2
from innerverz import Data_Process

image_path = 'sample.png'
DP = Data_Process()

"""
        face alignment usage
"""
from innerverz import FaceAligner
FA = FaceAligner(align_style='ffhq')
cv2_image = cv2.imread(image_path)
aligned_face, tfm, tfm_inv, lms_5, lms_106, face_bool = FA.get_face(cv2_image)
face_bool, lms_106, lms_5 = FA.detect_lmk(cv2_image)
aligned_face, tfm, tfm_inv = FA.align_face_from_5(cv2_image, lms_5)


"""
        Deep3dmm usage
"""
from innerverz import Deep3DMM
D3 = Deep3DMM()

ts_256_aligned_face = DP.image_pp(aligned_face, 256, normalize=True)
coeffs, lms_68 = D3(ts_256_aligned_face)