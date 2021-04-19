from IPython.display import clear_output

class garage():
    def __init__(self,ticket_space,status):
        self.ticket_space = list(range(1,ticket_space))
        self.status = status 
    """ 
    garage class(ticket,space,status):
        ticket = int number of tickets turned into list 
        status = dict whose key=ticket number and corresponding value indicates whether in use or paid,
    """
    #Method to take ticket
    def takeTicket(self):
        clear_output
        if self.ticket_space != []:
            ticket = self.ticket_space.pop(0)
            self.status[ticket]= ""
            print(f'You have ticket number {ticket}')
            print(self.ticket_space)
            print(self.status)
        else:
            print("unfortunately we do no have any space available")
        
            
        

    #method to pay for parking
    def payForParking(self):
        clear_output
        ticket_number = input("Welcome to the payment kiosk, what is your ticket number? Enter 'b' for back \n")
        if ticket_number.lower() == "b":
            pass
        elif int(ticket_number) in self.status:
            self.status[int(ticket_number)] = "paid"
            print("Please proceed to the exit booth, your ticket has been paid.")
        else:
            print("Please enter a valid number")
        
        
            
    #method to leave garage
    def leaveGarage(self):
        clear_output
        leave = input("Please enter your ticket number. Enter 'b' for back \n")
        if leave.lower() == "b":
            pass
        elif int(leave) in self.status:
            if self.status[int(leave)] == "paid":
                self.ticket_space.append(int(leave))
                self.ticket_space.sort()
                del self.status[int(leave)]
                print("Thank you for parking at the Marina Towers!")
            else:
                print("You can't leave unless you have paid, please visit the payment kiosk") 
        elif leave not in self.status :
            print("Please enter a valid number")
        
        
            


def run():
    Marina_Towers= garage(3,{})
    while True:
        question = (f"Welcome to Marina Towers garage.There are currently {len(Marina_Towers.ticket_space)} spaces.")
        question += ('\n What would you like to do ?: park/pay/leave/quit \n')
        ask = input(question)
        if ask.lower() == "park":
            Marina_Towers.takeTicket()
        elif ask.lower() == "pay":
            Marina_Towers.payForParking()
        elif ask.lower() == "leave":
            Marina_Towers.leaveGarage()
        elif ask.lower() == "quit":
            break

run()
