from faker import Faker


fake = Faker()


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self._length=len(self.first_name) + len(self.last_name) + 1

    def __str__(self):
        return f"First name:{self.first_name}, Last name:{self.last_name}, phone:{self.phone_number}, e-mail:<{self.email}>"

    def contact(self):
        return f"Wybieram numer + 48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return self._length


class BusinessContact(BaseContact):
    def __init__(self, work_phone, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone = work_phone
        self.company = company
        self.job = job

    def contact(self):
        return f"Wybieram numer + 48 {self.work_phone} i dzwonię do {self.first_name} {self.last_name}"



def create_contacts(kind, quantity):
    if kind == 1:
        for _ in range(quantity):
            x = BaseContact(
                fake.unique.first_name(),
                fake.unique.last_name(),
                fake.phone_number(),
                fake.email(),
            )
            list_BaseContact_faker.append(x)
            print(x)
    elif kind == 2:
        for _ in range(quantity):
            y = BusinessContact(
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                company=fake.company(),
                job=fake.job(),
                work_phone=fake.phone_number(),
            )
            list_BusinessContact_faker.append(y)
            print(y)
    return 'Done!'



def display_len(list_BaseContact_faker):
    print("Length of name and surname:")
    for x in list_BaseContact_faker:
        print(f"{x.label_length}= {x.first_name} {x.last_name}")


def display_contact_private(list_BaseContact_faker):
    print("List of private contacts from BaseContact list:")
    for x in list_BaseContact_faker:
        print(x.contact())


# def display_contact_business(list_BusinessContact_faker):
#     print("List of BusinessContacts:")
#     for x in list_BusinessContact_faker:
#         print(x.contact())


def display_len_business(list_BusinessContact_faker):
    print("Length of name and surname in BsinessContacts:")
    for x in list_BusinessContact_faker:
        print(f"{x.label_length}= {x.first_name} {x.last_name}")


def display_contact_private_business(list_BusinessContact_faker):
    print("List of private contacts from BusinessContact list:")
    for x in list_BusinessContact_faker:
        print(x.contact())


if __name__ == "__main__":
    list_BaseContact_faker = []
    list_BusinessContact_faker = []
    print(
        "\n\n---------------------------------------------------------------------------------------"
    )
    kind = int(
        input(
            "Which kind of contacts do you need: 1. BaseContact or 2. BusinessContact.\n Enter number:"
        )
    )
    quantity = int(input("Enter quantity of contacts which you need generate:"))
    print(
        "\n\n---------------------------------------------------------------------------------------"
    )
    print(create_contacts(kind, quantity))
    if kind == 1:
        print("\n\nInformation about people from BaseContact list:")
        print("\n---------------------------------------------------")
        display_contact_private(list_BaseContact_faker)
        print("\n---------------------------------------------------")
        display_len(list_BaseContact_faker)
    elif kind == 2:
        print("\nInformation about people from BusinessContact list:")
        print("\n---------------------------------------------------")
        display_contact_private_business(list_BusinessContact_faker)
        print("\n---------------------------------------------------")
        # display_contact_business(list_BusinessContact_faker)
        print("\n---------------------------------------------------")
        display_len_business(list_BusinessContact_faker)
