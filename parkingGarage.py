class garage():
    def __init__(self,ticket_space,status):
        self.ticket_space = ticket_space
        self.status = status 
""" 
garage class(ticket,space,status):
    ticket = int number of tickets turned into list 
    space = int number of spaces turned into list
    status = dict whose key=ticket number and corresponding value indicates whether in use or paid,
"""
#Method to take ticket
    def takeTicket(self):
        if self.ticket_space != []:
            ticket = self.ticket_space.pop(0)
            self.status[ticket]= ""
        if self.ticket_space == []:
            print("unfortunately we do no have any space available")
    
    def payForParking(self):
        ticket_number = input("Welcome to the payment kiosk, what is your ticket number? ")
        if ticket_number in status:
            self.status[ticket]= "paid"
        if ticket_number not in status:
            print("Please enter a valid number?")

                

        
        

    def payForParking(self):

    def leaveGarage(self):

def run():
    Marina_Towers= garage(10,{})
        space = list in range(Marina_Towers.ticket)
