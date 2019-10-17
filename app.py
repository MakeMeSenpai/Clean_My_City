#Camera controls! Thanks Ryan Keys for the help and Stack Overflow
from cv2 import cv2

cv2.namedWindow("Hello")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Hello", frame)
    rval, frame = vc.read()
    frame = cv2.flip(frame,1)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
vc.release()
cv2.destroyWindow("Hello")

#TODO: Skateboard- Users are able to create, edit, and delete tickets (CRUD)
    
# Class for tickets
class Ticket():
    def __init__(self):
        pass

    # Creates a ticket
    def create(self):
        pass

    # Read a ticket (the ability to view a ticket)
    def read(self):
        pass

    # lets user edit a ticket
    def edit(self):
        pass

    # lets user update a ticket
    def update(self):
        pass

    # let the user delete a ticket
    def delete(self):
        pass

    # cancles the creation of a ticket
    def cancle(self):
        pass

#TODO: Bike - Users will be able to switch between cleaned and pollution tabs in which they can leave 
        # comments
    # 1. Create a way for the user to be able to use their camera - edit camera code
    # 2. Create templates for html- base.html etc
    # 3. Create routes for different pages- @route home, polution page, cleaned page
    # 4. Create a way for users to leave comments on tickets-class comment
    # 5. Create a cleaner UI on all of your pages
class Comment(object):
    def __init__(self):
        pass

    # create a comment
    def create(self):
        pass

    # deletes a ticket
    def delete(self):
        pass

#TODO: Car
    # Users will be able to message one another, send each other money, and join larger events. 
        # Final stages will include the ability to sign into their own accounts.
    # 1. Make it so that people can post completed cleans next to before picture - more camera editing
class after(object):
    def __init__(self):
        pass
    
    #takes ticket object and posts after picture next to area
    def create(self):
        pass

    #lets users edit after posts
    def edit(self):
        pass
    # 2. User Authentification - do more research!!!!
    # 3. Make it so that users can join larger events - make a reclickable button that toggles on/off

#TODO: Stretch Challenges and other
    # 1. re-examine and clean up site/app based off user feedback
    # 2. Make it so that users can message one another class private message
    # 3. Make it so that users can send money to one another (with the ability to accept or decline)
    # 4. Make events better preforming and donation option available - revert to 3 
    # 5. Ship app to every app store