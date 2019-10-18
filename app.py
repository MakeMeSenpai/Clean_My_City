import os
import numpy as np
from cv2 import cv2
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
# Camera controls! Thanks Ryan Keys for the help and Stack Overflow. This function also runs our program
#TODO: Bike - Users will be able to switch between cleaned and pollution tabs in which they can leave 
        # comments
    # 1. Create a way for users to leave comments on tickets-class comment
    # 2. Make it work with flask
    # 3. Create a cleaner UI on all of your pages
    

# Class for tickets
@app.route('/home') # uselessly runs flask after quiting terminal commands! 
class Ticket():
    def __init__(self):
        self.ticket_name = ""
        self.description = ""
        self.img_name = ""
        self.new_img = ""
        self.imgs = []
        self.img_counter = 0 # helps name our imgs

    # Creates a ticket
    @app.route('/polution')
    def create(self):
        cv2.namedWindow(self.ticket_name) # names our camera window
        vc = cv2.VideoCapture(0) #looks at first frame 

        #detects if the camera is on or not
        if vc.isOpened(): 
            rval, frame = vc.read()  # Shows camera feed
        else:
            rval = False

        while rval: # keeps camera on
            cv2.imshow(self.ticket_name, frame) # shows camera feed
            rval, frame = vc.read() # shows camera feed
            frame = cv2.flip(frame,1) # inverts camera
            key = cv2.waitKey(20) # sets keyboard commands later, but here it waits 20ms for each frame
            if key == 27: # exit on ESC - this is an emergancy exit
                break 
            elif key%256 == 32: # SPACE pressed - takes a picture!
                self.img_name = "pics/ticket_{}.png".format(self.img_counter) # writes file name, in pics path
                cv2.imread(self.img_name,1) # shows us tour picture *sometimes late*
                cv2.imwrite(self.img_name, frame) # creates img file
                print("{} written!".format(self.img_name)) #terminal output to help us
                self.img_counter += 1 # helps name imgs
                rval = False

        vc.release() # stops capturing images
        cv2.destroyWindow(self.ticket_name) # destroys cv2 window
        self.ticket_name = input("Name of Ticket: ")
        self.description = input("Location and Description: ")
        self.imgs.append(self.img_name)

        #access cancle method to determine if user wants to save or not
        while True:
            save = input("Would you like to save?(y/n): ")
            if save == 'y':
                return False
            elif save == 'n':
                self.cancle()
                return False

    # lets user update a ticket
    @app.route('/cleaned')
    def update(self):
        #creates new image
        cv2.namedWindow(self.ticket_name) # names our camera window
        vc = cv2.VideoCapture(0) #looks at first frame 

        #detects if the camera is on or not
        if vc.isOpened(): 
            rval, frame = vc.read()  # Shows camera feed
        else:
            rval = False

        while rval: # keeps camera on
            cv2.imshow(self.ticket_name, frame) # shows camera feed
            rval, frame = vc.read() # shows camera feed
            frame = cv2.flip(frame,1) # inverts camera
            key = cv2.waitKey(20) # sets keyboard commands later, but here it waits 20ms for each frame
            if key == 27: # exit on ESC - this is an emergancy exit
                break 
            elif key%256 == 32: # SPACE pressed - takes a picture!
                self.new_img = "pics/after_{}.png".format(self.img_counter) # writes file name, in pics path
                cv2.imread(self.new_img,1) # shows us tour picture *sometimes late*
                cv2.imwrite(self.new_img, frame) # creates img file
                print("{} written!".format(self.new_img)) #terminal output to help us
                rval = False

        vc.release() # stops capturing images
        cv2.destroyWindow(self.ticket_name) # destroys cv2 window

        #combineds images thanks to https://answers.opencv.org/question/175912/how-to-display-multiple-images-in-one-window/
        before = cv2.imread(self.img_name) #opens images
        after = cv2.imread(self.new_img)

        #thx https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/ for the help
        # before = cv2.resize(self.img_name,None,fx=0.5,fy=0.95) #resizes imgs 
        # after = cv2.resize(self.new_img,None,fx=0.5,fy=0.95)

        numpy_horizontal_concat = np.concatenate((before, after), axis=1) #sorts the row
        cv2.imwrite(self.img_name, numpy_horizontal_concat)
        cv2.imshow(self.ticket_name + " *Cleaned!*", numpy_horizontal_concat)

        cv2.waitKey(5000)
        cv2.destroyWindow(self.ticket_name)

        #makes final changes
        self.ticket_name += " *Cleaned!*"
        self.description += " *Post Description*"
        self.description += input("Clean up description: ")

    # Read a ticket (the ability to view a ticket)
    def read(self):
        for i in self.imgs:
            img = cv2.imread(i) #Read Image
            cv2.imshow(self.ticket_name,img) #Display Image
            cv2.waitKey(5000)
            cv2.destroyWindow(self.ticket_name)
            print(self.ticket_name)
            print(self.description)

    # lets user edit a ticket
    def edit(self):
        self.ticket_name = input("Rename Ticket: ")
        self.description = input("New Description: ")


    # let the user delete a ticket
    def delete(self):
        self.img_name = ""
        self.new_img = ""
        self.ticket_name = ""
        self.description = ""
        self.img_counter -= 1

    # cancles the creation of a ticket
    def cancle(self):
        self.img_name = ""
        self.new_img = ""
        self.ticket_name = ""
        self.description = ""
        print("No problem. Nothing was saved!")

# class Comment(object):
#     def __init__(self, object):
#         self.comment = ""
#         self.comments = []

#     # create a comment
#     def create(self):
#         self.comment = input("Leave a comment: ")
#         self.comments.append(self.comment)
#         for i in self.comments:
#             print(i)
#         self.run()

#     # deletes a ticket
#     def delete(self):
#         self.comments.remove(self.comment)
#         self.run()

#     #runs program else where with z
#     def run(self):
#         what = input("What would you like to do?(c, d, or q): ")
#         while True:
#             if what == 'c':
#                 self.create()
#             elif what == 'd':
#                 self.delete()
#             elif what == 'q':
#                 for i in self.comments:
#                     object.description += f" #Comment: {i}"
#                 run()
#                 return False
#             else:
#                 print("what? ")
#                 return True


#runs code
@app.route('/')
def run():
    new_ticket = Ticket() # creates new ticket object
    #Gives user other controls involving CRUD
    while True: 
        opt = input("What would you like to do?(type c, r, e, u, d, or q): ") #add z for comments but can't figure out how to add comments to a separate object rn becuase I'm tired
        if opt == 'c':
            new_ticket.create()
        elif opt == 'r':
            new_ticket.read()
        elif opt == 'e':
            new_ticket.edit()
        elif opt == 'u':
            new_ticket.update()
        elif opt == 'd':
            new_ticket.delete()
        # elif opt == 'z':
        #     new_comment = Comment(new_ticket)
        #     new_comment.run()
        elif opt == 'q':
            return False
        else:
            print("Sorry, What was that?")
            
run() #runs our program

#TODO: Car with stretch limo (stretch challenges)
    # Users will be able to message one another, send each other money, and join larger events. 
        # Final stages will include the ability to sign into their own accounts.
    # 1. User Authentification - do more research!!!!
    # 2. Make it so that users can join larger events - make a reclickable button that toggles on/off
    # 3. Make it so that users can message one another class private message
    # 4. Make it so that users can send money to one another (with the ability to accept or decline)
    # 5. Make events better preforming and donation option available - revert to 3 
    # 6. Ship app to every app store
    # 7. re-examine and clean up site/app based off user feedback