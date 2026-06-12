class AccountLockedError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.__password = "python@123"
        self.__attempts = 3

    def login(self, password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("Account is locked")

            if password == self.__password:
                print("Login successful!")

            else:
                self.__attempts -= 1
                print("Wrong password")
                print("Remaining attempts:", self.__attempts)

                if self.__attempts == 0:
                    raise AccountLockedError("Account Locked")

        except AccountLockedError as e:
            print(e)

        finally:
            print("Login process finished")



obj = LoginSystem()

obj.login("abc123")
obj.login("test")
obj.login("hello")
obj.login("python@123")