from faker import Faker


fake = Faker()


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self._length = len(self.first_name) + len(self.last_name) + 1

    def __repr__(self):
        return f"BaseContact(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, email={self.email})"

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

    def __repr__(self):
        return f"BusinessContact(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, email={self.email}, work_phone={self.work_phone}, company={self.company}, job={self.job})"

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
    return "Done!"


def display_len(list):
    for y in list:
        print(f"{y.label_length}= {y.first_name} {y.last_name}")
    return "Done!"


def display_contact(list):
    for x in list:
        print(x.contact())
    return "Done!"


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
        print("\n---------------------------------------------------")
        list_BaseContact_faker.sort(key=lambda x: x.first_name)
        print(list_BaseContact_faker)
        print("\n\nInformation about people from BaseContact list:")
        print("-----------------------------------------------------")
        print("List of private contacts from BaseContact list:")
        display_contact(list_BaseContact_faker)
        print("\n---------------------------------------------------")
        print("Length of name and surname in BaseContacts:")
        display_len(list_BaseContact_faker)
    elif kind == 2:
        print("\n---------------------------------------------------")
        list_BusinessContact_faker.sort(key=lambda x: x.first_name)
        print(list_BusinessContact_faker)
        print("\nInformation about people from BusinessContact list:")
        print("------------------------------------------------------")
        print("List of BusinessContacts:")
        display_contact(list_BusinessContact_faker)
        print("\n---------------------------------------------------")
        print("Length of name and surname in BsinessContacts:")
        display_len(list_BusinessContact_faker)
