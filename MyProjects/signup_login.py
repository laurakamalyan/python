import hashlib
import os


class User:
    def __init__(self):
        self.__name = ""
        self.__surname = ""
        self.__age = ""
        self.__email = ""
        self.__password = ""

    def start(self):
        print("Welcome")
        start_input = input("Press 1 to log in and 2 to register. ")
        if start_input == '1':
            self.log_in()
        elif start_input == '2':
            self.sign_up()

    def log_in(self):
        self.__email = input("Input your email: ")
        self.__password = input("Input your password: ")
        hash_password = hashlib.md5(self.__password.encode()).hexdigest()

        filename = "users"

        with open(filename, 'r') as file:
            user = file.readline()
            user_find = False

            while user:
                email_in_file = ""
                password_in_file = ""
                for i in range(user.find("email: ") + 7, user.find("password") - 2):
                    email_in_file += user[i]

                for i in range(user.find("password: ") + 10, user.find("\n")):
                    password_in_file += user[i]

                if self.__email == email_in_file:
                    if hash_password == password_in_file:
                        name_in_file = ""
                        surname_in_file = ""
                        age_in_file = ""

                        for i in range(6, user.find(",")):
                            name_in_file += user[i]
                        for i in range(user.find("surname: ") + 9, user.find("age") - 2):
                            surname_in_file += user[i]
                        for i in range(user.find("age: ") + 5, user.find("email") - 2):
                            age_in_file += user[i]

                        print(f"\nWelcome {name_in_file} to your page!\n")

                        print("Name: ", name_in_file)
                        print("Surname: ", surname_in_file)
                        print("Age: ", age_in_file)
                        print("Email: ", email_in_file)
                    else:
                        print("Wrong password.")

                    user_find = True
                    return

                else:
                    user_find = False

                user = file.readline()

            if not user_find:
                print("Account could not be found.")

    def sign_up(self):
        self.__name = input("Input your name: ")
        self.__surname = input("Input your surname: ")
        self.__age = int(input("Input your age: "))
        self.__email = input("Input your email: ")
        self.__password = input("Input your password: ")

        hash_password = hashlib.md5(self.__password.encode()).hexdigest()

        user = f"name: {self.__name}, surname: {self.__surname}, age: {self.__age}, email: {self.__email}, " \
               f"password: {hash_password}"

        filename = "users"

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                user_in_file = file.readline()
                while user_in_file:
                    email_in_file = ""
                    for i in range(user_in_file.find("email: ") + 7, user_in_file.find("password") - 2):
                        email_in_file += user_in_file[i]

                    if self.__email == email_in_file:
                        print("\nEmail already exist.")
                        return

                    user_in_file = file.readline()

        with open(filename, 'a') as file:
            file.write(user)
            file.write("\n")

        print("Thank you for registration!")


user1 = User()
user1.start()

