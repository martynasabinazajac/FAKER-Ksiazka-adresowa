class Contact_list:

    
    def __init__(self, name, surname, company, job, email):
        self.name=name
        self.surname=surname
        self.company=company
        self.job=job
        self.email=email


    def __str__(self):
        return f'Name:{self.name}, Surname:{self.surname},e-mail:<{self.email}>'
    
    def contact(self):
        return f'Kontaktuję się z {self.name}, {self.surname}, {self.job}, {self.email}'
    
    @property
    def sum_of_name_and_surname(self):
        len_ns= len(self.name) + len(self.surname) + 1
        return f'{len_ns}'


        
    

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

#by_name=sorted(list, key=lambda x: x.name)
#by_surname=sorted(list, key=lambda x: x.surname)
#by_email=sorted(list, key=lambda x: x.email)

#def display_list_by_name():
#    for x in by_name:
#        print(x)

#def display_list_by_surname():
#    for x in by_surname:
#        print(x)

#def display_list_by_email():
#    for x in by_email:
#        print(x) 

#display_list_by_name()
#display_list_by_surname()
#display_list_by_email()

def display_contact():
    for x in list:
        print(x.contact())

def display_len():
    for x in list:
        print(x.sum_of_name_and_surname)

display_contact()
display_len()