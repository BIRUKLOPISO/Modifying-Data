class User:
    def __init__(self,email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,new_email):
        if not isinstance(new_email,str):
            raise ValueError("Email is not a string.")
        if new_email.count("@") != 1:
            raise ValueError("Email must contain exactly one @.")
        if len(new_email.split(".")[-1]) < 3:
            raise ValueError("Must have at least 3 characters after last dot")

        self._email = new_email



user = User("john@gmail.com")
print(user.email)  # john@gmail.com

user.email = "jane@yahoo.com"  # Works

user.email = "notanemail"       # ❌ ValueError: Must contain @ symbol

user.email = 123                 # ❌ ValueError: Email must be string