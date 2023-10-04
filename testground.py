ip = '128.61.117.190'

import pygame
import cv2
import numpy as np

pygame.init()
pygame.display.set_caption("Camera Braille Translation")
surface = pygame.display.set_mode([1280, 720])

cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture('http://'+ip+':4747/mjpegfeed')

# fps = cap.get(cv2.CAP_PROP_FPS)
# print("fps:", fps)


# cap.set(cv2.CAP_PROP_FPS, 60)

while True:
    try: 

        success, frame = cap.read()
        if not success: 
            print("not success")

        # for some reasons the frames apear inverted
        frame = np.fliplr(frame)
        frame = np.rot90(frame)

        # The video uses BGR colors and pygame likes RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        surf = pygame.surfarray.make_surface(frame)

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYUP:
        #         background_color = 'red'
        #         surface.fill(background_color)
        #         pygame.display.update()
        
        # # show the surface
        surface.blit(surf, (0,0))
        pygame.display.flip()
    except Exception: pass


# https://stackoverflow.com/questions/59948996/how-to-use-webcam-as-a-screen-of-pygame