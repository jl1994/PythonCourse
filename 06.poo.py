class User:  # The first letter is capitalized for classes
    def __init__(self, username, name, lastname, id):
        self.username = username
        self.name = name
        self.lastname = lastname
        self.id = id


# We instantiate an object of the User class
user1 = User("johan.luna", "Johan", "Luna", 1143966442)
user2 = User("ederlien.bermeo", "Ederlien", "Bermeo", 1143966440)

print(user1.username, "\t", user2.username)
# print(type(User))


class AmazonSES:
    check_service = "Check Endpoint SMTP"
    send_emails = "Send Emails"
    gen_reports = "Generating Reports"


check_service_finkargo = AmazonSES()

# print(check_service_finkargo.check_service,
#       "\n", check_service_finkargo.send_emails)


class Scanner:
    scanning_ports = ""

# Examples


class store:
    open_store = ""
    close_store = ""
    sell_product = ""
    manage_inventory = ""


class bank:
    open_account = ""
    close_account = ""
    insert_money = ""
    take_out_money = ""


class book:
    read = ""
    lend = ""
    return_book = ""


class Car:
    speed = ""
    curb = ""
    spin = ""


class Person:
    talk = ""
    walk = ""
    eat = ""
