# install the open cv module of python from google
import winsound
import pygame
import cv2
x="Aleart , Chor aa Gya"
def load(name):
    return pygame.image.load(name)
    alert_message=load(chor_message.png)
    # screen.blit(chor_message.png)




cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1=cam.read()
    ret,frame2=cam.read()
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _, thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    for c in contours:

        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

        winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
# def load(name):
#  return pygame.image.load(name)
#   alert_message=load(chor_message.png)

#                pygame.event.get()
#           screen.blit(chor_message.png,[0,0])
#                 pygame.display.update()

        # def show_message (x):
        #  font = pygame.font.SysFont('Comic Sans MS', 30)
        #  show_message =  str(x)
        #  text = font.render(x, True)
        #  screen.blit('x', [20, 10])




    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow('Rider Infinity Securities',frame1)


