from faker import Faker


fake=Faker()

class BaseContact:

    
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email


    def __str__(self):
        return f'First name:{self.first_name}, Last name:{self.last_name}, phone:{self.phone_number}, e-mail:<{self.email}>'
    

    def contact_private(self):
        return f'Wybieram numer + 48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'
    
    @property
    def label_length(self):
        len_ns= len(self.first_name) + len(self.last_name) + 1
        return f'{len_ns} = {self.first_name} {self.last_name}'

class BusinessContact(BaseContact):

    
    def __init__(self, work_phone, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone=work_phone
        self.company=company
        self.job=job
    
    def contact(self):
        return f'Wybieram numer + 48 {self.work_phone} i dzwonię do {self.first_name} {self.last_name}'
    
        
    

list_BaseContact=[]
contact1=BaseContact("Adam", "Kot", "974793749", "Adam.K@dayrep.com")
contact2=BaseContact("Michał", "Wiśnia", "34798084", "M.W@teleworm.us")
contact3=BaseContact("Wilchelm", "Rudy", "0873974334", "Wi.R@jourrapide.com")
contact4=BaseContact("Carlos", "Blok", "0212489754", "Car.B@dayrep.com")
contact5=BaseContact("Alicja", "Gray", "283498857", "A.Gray@armyspy.com")

list_BusinessContact=[]
contact1_b=BusinessContact(first_name="Charles", last_name= "L. Piper", phone_number="232357686", email="CharlesLPiper@dayrep.com", work_phone="29357393687", company="Perisolution", job="Plating and coating machine tender")
contact2_b=BusinessContact(first_name="Michael", last_name="P. Armour", phone_number="56356887", email="MichaelPArmour@teleworm.us", work_phone="35774360902",company="Pay'N Takeit",job="Etcher")
contact3_b=BusinessContact(first_name="William", last_name="E. McCoy", phone_number="54658090", email="WilliamEMcCoy@jourrapide.com", work_phone="3754378090", company="Price Club",job="Portfolio manager")
contact4_b=BusinessContact(first_name="Carlos", last_name="J. Bright", phone_number="134557689", email="CarlosJBright@dayrep.com", work_phone="2094754876",company="Luria's", job="Engraver set-up operator")
contact5_b=BusinessContact(first_name="George", last_name="A. Gray", phone_number="983674587", email="GeorgeAGray@armyspy.com", work_phone="46778799780", company="The Sample", job="Merchandise manager")

list_BaseContact.append(contact1)
list_BaseContact.append(contact2)
list_BaseContact.append(contact3)
list_BaseContact.append(contact4)
list_BaseContact.append(contact5)

list_BusinessContact.append(contact1_b)
list_BusinessContact.append(contact2_b)
list_BusinessContact.append(contact3_b)
list_BusinessContact.append(contact4_b)
list_BusinessContact.append(contact5_b)


list_BusinessContact.sort(key=lambda x: x.first_name)
list_BusinessContact.sort(key=lambda x: x.last_name)
list_BusinessContact.sort(key=lambda x: x.email)

list_BaseContact.sort(key=lambda x: x.first_name)
list_BaseContact.sort(key=lambda x: x.last_name)
list_BaseContact.sort(key=lambda x: x.email)

def display_contact_business():
    print('List of BusinessContacts:')
    for x in list_BusinessContact:
        print(x.contact())    

def display_len_business():
    print('Length of name and surname in BsinessContacts:')
    for x in list_BusinessContact:
        print(f'{x.label_length}')

def display_contact_private_business():
    print('List of private contacts from BusinessContact list:')
    for x in list_BusinessContact:
        print(x.contact_private())


# funkcje dla wizytówek prywatnych
def display_len():
    print('Length of name and surname:')
    for x in list_BaseContact:
        print(f'{x.label_length}')

def display_contact_private():
    print('List of private contacts from BaseContact list:')
    for x in list_BaseContact:
        print(x.contact_private())

print('\nInformation about people from BusinessContact list:')
print('\n---------------------------------------------------')
display_contact_private_business()
print('\n---------------------------------------------------')
display_contact_business()
print('\n---------------------------------------------------')
display_len_business()

print('\n\nInformation about people from BaseContact list:')
print('\n---------------------------------------------------')
display_contact_private()
print('\n---------------------------------------------------')
display_len()

#funkcja do generowania losowych wizytówek:

list_BaseContact_faker=[]
list_BusinessContact_faker=[]

def create_contacts(kind, quantity):
    if kind==1:
        for _ in range(quantity):
            x = BaseContact(fake.unique.first_name(), fake.unique.last_name(), fake.phone_number(), fake.email())
            list_BaseContact_faker.append(x)
            print(x)
        return 'Done!'
    if kind==2:
        for _ in range(quantity):
            y= BusinessContact(first_name=fake.unique.first_name(), last_name=fake.unique.last_name(), phone_number=fake.phone_number(), email=fake.email(), company=fake.company(), job=fake.job(), work_phone=fake.phone_number())
            list_BusinessContact_faker.append(y)
            print(y)
        return 'Done!'

if __name__=="__main__":
    print('\n\n---------------------------------------------------------------------------------------')
    kind=int(input('Which kind of contacts do you need: 1. BaseContact or 2. BusinessContact.\n Enter number:'))
    quantity=int(input('Enter quantity of contacts which you need generate:'))
    Contact_faker= create_contacts(kind, quantity)
    print(Contact_faker)
