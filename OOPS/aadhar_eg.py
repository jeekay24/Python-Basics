class Employee:
    def __init__(self, fname, aadhar):
        self.name = fname
        self.ano = aadhar

    def bank_details(self):
        print(f"Hi {self.name}, please give me your aadhar number: {self.ano} ")

    def office_details(self):
        print(f"Hi {self.name}, please provide your aadhar number: {self.ano}")


e = Employee("Ganesh Kumar", "2174-2127-2433")
e.bank_details()
e.office_details()
