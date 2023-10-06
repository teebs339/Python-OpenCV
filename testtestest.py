class Base:
    def __init__(self):
        self._protected_var = 10  # Protected attribute

    def protected_method(self):
        print("This is a protected method")

class Derived(Base):
    def access_protected(self):
        print(self._protected_var)  # Accessing protected attribute
        self.protected_method()  # Accessing protected method

# Example usage
obj = Derived()
obj.access_protected()  # Accessing protected attribute and method in a subclass
