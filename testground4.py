import cv2
from utils import *

folder = './demo_image/'
filename = 'demodemo2.jpg'

img = cv2.imread(folder+filename)
img_d, sf = imresize(img) # downscale, remember scaling factor
# resize를 하고 돌리면 integer coordinate가 나옴 (정확한 이유 불명)

img_ = img.copy()  # backup
img_d_ = img_d.copy() # backup

print(type(img_))

from paddleocr import PaddleOCR,draw_ocr
import inspect
print(inspect.getfile(PaddleOCR)) # make sure that local PaddleOCR module is imported, not global (site-packages)

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=False, lang='en', use_gpu=True) # need to run only once to download and load model into memory
result = ocr.ocr(img_, cls=True)
for line in result:
    print(line)


# draw result
from PIL import Image
image = Image.open(folder+filename).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')
