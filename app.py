import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
vc.release()
cv2.destroyWindow("preview")

#TODO: Skateboard
    # Users are able to create, edit, and delete tickets (CRUD)
    # 1. review playlister & superheroes.py
    # 2. Conduct some extra research
    # 3. Make a class for tickets
    # 4. create methods that let the user create a ticket
    # 5. create methods that let the user read a ticket
    # 6. create methods that let the user update/edit a ticket
    # 7. creat methods that let the user delete a ticket

#TODO: Bike
    # Users will be able to switch between cleaned and pollution tabs in which they can leave 
        # comments
    # 1. Create a way for the user to be able to use their camera
    # 2. Create templates for html
    # 3. Create routes for different pages
    # 4. Create a way for users to leave comments on tickets
    # 5. Create a cleaner UI on all of your pages

#TODO: Car
    # Users will be able to message one another, send each other money, and join larger events. 
        # Final stages will include the ability to sign into their own accounts.
    # 1. Make it so that people can post completed cleans next to before picture
    # 2. User Authentification
    # 3. Make it so that users can join larger events

#TODO: Stretch Challenges and other
    # 1. re-examine and clean up site/app based off user feedback
    # 2. Make it so that users can message one another
    # 3. Make it so that users can send money to one another (with the ability to accept or decline)
    # 4. Make events better preforming and donation option available
    # 5. Ship app to every app store