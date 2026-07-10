class PasswordManager:
    @staticmethod
    def validate_length(password, min_length):
        if len(password) >= min_length:
            return True

        return False
    @staticmethod
    def has_uppercase(password):
        for char in password:
            if char.isupper():
                return True

        return False
    @staticmethod
    def has_special_char(password):
        for char in password:
            if char in "!@#$%^&*":
                return True

        return False
    @staticmethod
    def get_strength_score(password):
        i = 0
        length = PasswordManager.validate_length(password,8)
        if length:
            i += 1
        uppercase = PasswordManager.has_uppercase(password)
        if uppercase:
            i += 1

        special = PasswordManager.has_special_char(password)
        if special:

            i += 1

        if any(char.isdigit() for char in password):
            i += 1

        return i

print(PasswordManager.get_strength_score("#Mandatory788!"))