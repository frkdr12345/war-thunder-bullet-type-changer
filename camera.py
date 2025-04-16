
import cv2
import keyboard


cap = cv2.VideoCapture(0)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

i_pressed = False
ö_pressed = False
x_pressed = False
l_pressed = False

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
    cx = int(width / 2)
    cy = int(height / 2)

    
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]
    Value_value = pixel_center[0]

    color = "Undefined"
    if Value_value < 5:
        color = "siyah"
        i_pressed = False
        ö_pressed = False
        x_pressed = False
        l_pressed = False

        if not Value_value < 1:
         if hue_value < 20:
          color = "red"
          ö_pressed = False
          x_pressed = False
          l_pressed = False
          if not i_pressed:  
           keyboard.press('1')
           keyboard.release('1')
           i_pressed = True
         print("1 pressed")
    elif hue_value < 33:
        i_pressed = False
        ö_pressed = False
        l_pressed = False
        if not x_pressed:  
         keyboard.press('2')
         keyboard.release('2')
         x_pressed = True
         print("2 pressed")
        color = "yellow"
    elif hue_value < 78:
         x_pressed = False
         i_pressed = False
         l_pressed = False
         color = "green"
         if not ö_pressed:
          keyboard.press('3')
          keyboard.release('3')
          ö_pressed = True
          print("3 basıldı")
    elif hue_value < 170:
        color = "blue"
        i_pressed = False
        x_pressed = False
        ö_pressed = False
        if not l_pressed:  
         keyboard.press('4')
         keyboard.release('4')
         l_pressed = True
         print("4 basıldı")
    else:
        color = "siyah"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

cap.release()
cv2.destroyAllWindows()
