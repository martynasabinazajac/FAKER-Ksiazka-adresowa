class Contact_list:

    
    def __init__(self, name, surname, company, position, e_mail):
        self.name=name
        self.surname=surname
        self.company=company
        self.position=position
        self.e_mail=e_mail


    def __str__(self):
        return f'Name:{self.name}, Surname:{self.surname},e-mail:<{self.e_mail}>'
        
    

list=[]
contact1=Contact_list("Charles", "L. Piper", "Perisolution","Plating and coating machine tender","CharlesLPiper@dayrep.com")
contact2=Contact_list("Michael", "P. Armour", "Pay'N Takeit","Etcher","MichaelPArmour@teleworm.us")
contact3=Contact_list("William", "E. McCoy", "Price Club","Portfolio manager","WilliamEMcCoy@jourrapide.com")
contact4=Contact_list("Carlos", "J. Bright", "Luria's","Engraver set-up operator","CarlosJBright@dayrep.com")
contact5=Contact_list("George", "A. Gray", "The Sample","Merchandise manager","GeorgeAGray@armyspy.com")

list.append(contact1)
list.append(contact2)
list.append(contact3)
list.append(contact4)
list.append(contact5)

def display_list():
    for x in list:
        print(x)

display_list()