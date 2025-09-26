from datetime import datetime

# Bad Way to access and modify attributes
"""
class User:
    def __init__(self, username, email , password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username} Hi {user.username}, its {self.username}!")

user1 = User("Alice", "alice@example.com", "alice123")
user2 = User("Danny", "danny@hotmail.com", "abc")
user1.say_hi_to_user(user2)


print(user1.email)
user1.email = "dan"
print(user1.email)
"""

# 1st Good way , Traditional method: make data private and use getters and setters

"""
class User:
    def __init__(self, username, email , password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username} Hi {user.username}, its {self.username}!")

user1 = User("Alice", "alice@example.com", "alice123")
user2 = User("Danny", "danny@hotmail.com", "abc")

print(user1.get_email())
user1.set_email("danny@hotmail.com")
print(user1.get_email()) 
"""

# 2nd Good way, python mordern property decorator

class User:
    def __init__(self, username, email , password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email

user1 = User("Alice", "alice@example.com", "alice123")
user2 = User("Danny", "danny@hotmail.com", "abc")

print(user1.email)
user1.email = "abc@def.com"
print(user1.email)

