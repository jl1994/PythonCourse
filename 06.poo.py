class User:  # The first letter is capitalized for classes
    def __init__(self, username, name, lastname, id, email):
        self.username = username
        self.name = name
        self.lastname = lastname
        self.id = id
        self.email = email

    # New methods
    def change_password(self):
        print(f'Change password to {self.username}')

    def create_user(self):
        print(f'Creating the new user to {self.username}')

    # Print all properties
    def list_user(self):
        print(
            f'\n--- User Team --- \n\n{self.username}\n{self.name}\n{self.lastname}\n{self.id}\n{self.email}')


# We instantiate an object of the User class
user1 = User("johan.luna", "Johan", "Luna",
             1143966442, "johanluna777@gmail.com")
user2 = User("ederlien.bermeo", "Ederlien", "Bermeo",
             1143966440, "ederlien.bermeo@gmail.com")

user1.change_password()
user2.create_user()

# Self, Add, Delete properties

user1.username = "johan.luna1994"
# del user1.username
# del user1
user1.list_user()

### INHERITANCE ###


class DevOps(User):
    def superList(self):
        print(
            f'\n--- DevOps Team --- \n\n{self.username}\n{self.name}\n{self.lastname}\n{self.id}\n{self.email}')


devops1 = DevOps("johan.luna", "Johan", "Luna",
                 1143966442, "johan.luna@mycompany.com")

devops1.list_user()
devops1.superList()


# class AmazonSES:
#     check_service = "Check Endpoint SMTP"
#     send_emails = "Send Emails"
#     gen_reports = "Generating Reports"
# check_service_finkargo = AmazonSES()

# # print(check_service_finkargo.check_service,
# #       "\n", check_service_finkargo.send_emails)


# class Scanner:
#     scanning_ports = ""

# # Examples


# class store:
#     open_store = ""
#     close_store = ""
#     sell_product = ""
#     manage_inventory = ""


# class bank:
#     open_account = ""
#     close_account = ""
#     insert_money = ""
#     take_out_money = ""


# class book:
#     read = ""
#     lend = ""
#     return_book = ""


# class Car:
#     speed = ""
#     curb = ""
#     spin = ""


# class Person:
#     talk = ""
#     walk = ""
#     eat = ""
