## mainLED.py ##

import cv2
import mediapipe as mp
import time
import pyfirmata

time.sleep(2.0)

mp_draw=mp.solutions.drawing_utils #use function drawing_utils to draw straight connect landmark point
mp_hand=mp.solutions.hands #use function hands to find hand on camera


tipIds=[4,8,12,16,20] # media-pipe position  of fingertips

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        # print("Input is an integer number. Number = ", val)
        bv = True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print("Input is a float  number. Number = ", val)
            bv = True
        except ValueError:
            # print("No.. input is not a number. It's a string")
            bv = False
    return bv

cport = input('Enter the camera port: ')
while not (check_user_input(cport)):
    print('Please enter a number not string')
    cport = input('Enter the camera port: ')

comport = input('Enter the arduino board COM port: ')
while not (check_user_input(comport)):
    print('Please enter a number not string')
    comport = input('Enter the arduino board COM port: ')

board=pyfirmata.Arduino('COM'+comport)#เชื่อมaduino กับ python
led_1=board.get_pin('d:13:o') #Set pin to output
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')#digital:port:output

cap = cv2.VideoCapture(0)
def led(total,led_1,led_2,led_3,led_4,led_5):#creat condition to controll digital out put
    return 0
    #เอา code ระบุนิ้วมาวาง
# Nfing = 5
    


#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h) #lm คือตำแหน่ง
                if id == 20:
                    id20 = int(id)
                    cx20 = cy
                if id == 18:
                    id18 = int(id)
                    cx18 = cy
                if id == 16:
                    id16 = int(id)
                    cx16 = cy
                if id == 14:
                    id14 = int(id)
                    cx14 = cy
                if id == 12:
                    id12 = int(id)
                    cx12 = cy
                if id == 10:
                    id10 = int(id)
                    cx10 = cy
                if id == 8:
                    id8 = int(id)
                    cx8 = cy
                if id == 6:
                    id6 = int(id)
                    cx6 = cy
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
            
            finger = ["THUMB", "Index finger","Middle finger","Ring finger","Pinky Finger"]   
            if cx20 < cx18 :
                led_5.write(1)
                cv2.putText(img, str(finger[4]),(10, 250), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            else:
                led_5.write(0)
            if cx16 < cx14:
                led_4.write(1)
                cv2.putText(img, str(finger[3]),(10, 300 ), cv2.FONT_HERSHEY_PLAIN,2,
                (135, 206, 250), 3)
            else:
                led_4.write(0)
            if cx12 < cx10 :
                led_3.write(1)
                cv2.putText(img, str(finger[2]),(10, 350), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            else:
                led_3.write(0)
            if cx8 < cx6 :
                led_2.write(1)
                cv2.putText(img, str(finger[1]),(10, 400), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            else:
                led_2.write(0)
            if cx4 > cx3:
                led_1.write(1)
                cv2.putText(img, str(finger[0]),(10, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            else:
                led_1.write(0)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
