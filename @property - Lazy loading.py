import time


class Profile:
    def __init__(self,username ):
        self.username = username
        self._picture_data = None


    def _load_picture(self):
        print(f"Getting picture data for {self.username}")
        time.sleep(2)
        self._picture_data = "📸 profile.jpg data"
        print("The picture data is available.")

    @property
    def picture(self):
        if self._picture_data is None:
            self._load_picture()
        return self._picture_data

user = Profile("john_doe")
print("User created")
print("Doing other things...")

# First access - loads picture
print(user.picture)  # Should show loading message, delay, then picture data

# Second access - instant
print(user.picture)  # No loading message, instant return