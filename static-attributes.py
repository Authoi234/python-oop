# Static Attributes

class User:
    user_count = 0  # Static attribute to keep track of user count

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1  # Inc rement user count when a new user is created

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user1 = User("Abdulaziz", "abdulaziz@example.com")
user2 = User("Danny", "danny@hotmail.com")

print(User.user_count)  # Accessing static attribute without creating an instance
print(user1.user_count)  # Accessing static attribute via instance
print(user2.user_count)  # Accessing static attribute via instance