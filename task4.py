class UnderAgeError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class AgeVerification:

    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative")

            elif age < 18:
                raise UnderAgeError("Person is under age")

            elif age > 100:
                raise InvalidAgeError("Invalid age entered")

            else:
                print("Valid age!")

        except ValueError as e:
            print("ValueError :", e)

        except UnderAgeError as e:
            print("UnderAgeError :", e)

        except InvalidAgeError as e:
            print("InvalidAgeError :", e)

        finally:
            print("Verification completed")



obj = AgeVerification()

obj.set_age(-5)
obj.set_age(15)
obj.set_age(120)
obj.set_age(25)