from cv2 import cv2
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
#TODO: Bike - Users will be able to switch between cleaned and pollution tabs in which they can leave 
        # comments
    # 1. Create a way for the user to be able to use their camera
    # 2. Create templates for html- base.html etc
    # 3. Create routes for different pages- @route home, polution page, cleaned page
    # 4. Create a way for users to leave comments on tickets-class comment
    # 5. Create a cleaner UI on all of your pages

# Class for tickets
class Ticket():
    def __init__(self):
        self.ticket_name = ""
        self.description = ""
        self.img_name = ""
        self.img_counter = 0 # helps name our imgs

    # Creates a ticket
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

        #access cancle method to determine if user wants to save or not
        while True:
            save = input("Would you like to save?(y/n): ")
            if save == 'y':
                return False
            elif save == 'n':
                self.cancle()
                return False

    # Read a ticket (the ability to view a ticket)
    def read(self):
        # cv2.imshow(self.ticket_name)
        # cv2.imread(self.img_name)
        print(self.ticket_name)
        print(self.description)

    # lets user edit a ticket
    def edit(self):
        self.ticket_name = input("Rename Ticket: ")
        self.description = input("New Description: ")

    # lets user update a ticket
    def update(self):
        self.ticket_name += " *Cleaned!*"
        self.description += " *Post Description*"
        self.description += input("Clean up description: ")

    # let the user delete a ticket
    def delete(self):
        self.ticket_name = ""
        self.description = ""

    # cancles the creation of a ticket
    def cancle(self):
        self.ticket_name = ""
        self.description = ""
        print("No problem. Nothing was saved!")

# Camera controls! Thanks Ryan Keys for the help and Stack Overflow. This function also runs our program
def run():
    new_ticket = Ticket() # creates new ticket object
    Ticket.create(new_ticket) # lets user create a ticket!
    #Gives user other controls involving CRUD
    while True: 
        opt = input("What would you like to do?(type c, r, e, u, d, or q): ")
        if opt == 'c':
            Ticket.create(new_ticket)
        elif opt == 'r':
            Ticket.read(new_ticket)
        elif opt == 'e':
            Ticket.edit(new_ticket)
        elif opt == 'u':
            Ticket.update(new_ticket)
        elif opt == 'd':
            Ticket.delete(new_ticket)
        elif opt == 'q':
            return False
        else:
            print("Sorry, What was that?")
            
run() #runs our program

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