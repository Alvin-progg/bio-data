# OOP Concepts Demonstrated in Login System

This document explains where and how the four main Object-Oriented Programming (OOP) concepts are implemented in the login system.

---

## 1. **Encapsulation** 🔒

**Definition**: Bundling data (attributes) and methods that operate on that data within a single unit (class), and restricting direct access to some components.

### Where it's used:

#### In `User` class:
```python
class User(AuthenticationSystem):
    def __init__(self, username, password, profile_data):
        self.__username = username        # Private attribute
        self.__password = password        # Private attribute
        self.__profile_data = profile_data # Private attribute
        self.__is_authenticated = False   # Private attribute
```

**Key Points:**
- **Private attributes** use double underscore `__` prefix (e.g., `__username`, `__password`)
- These attributes cannot be accessed directly from outside the class
- Access is provided through **public methods** (getters):
  - `get_username()` - safely returns username
  - `get_profile_data()` - safely returns profile data
  - `is_logged_in()` - checks authentication status
- **Benefits**: Protects sensitive data (like passwords) from direct external access

#### Example:
```python
user = User("eugene", "123456", profile_data)
# user.__username  # This would cause an error (private)
username = user.get_username()  # Correct way to access
```

---

## 2. **Inheritance** 👨‍👦

**Definition**: A mechanism where a new class (child) derives properties and behaviors from an existing class (parent).

### Where it's used:

#### Class Hierarchy:
```
AuthenticationSystem (Abstract Base Class)
    ↓
User (inherits from AuthenticationSystem)
    ↓
AdminUser (inherits from User)
```

#### In `User` class:
```python
class User(AuthenticationSystem):
    # User inherits from AuthenticationSystem
    # Must implement abstract methods: authenticate() and get_user_data()
```

#### In `AdminUser` class:
```python
class AdminUser(User):
    def __init__(self, username, password, profile_data, admin_level):
        super().__init__(username, password, profile_data)  # Inherit parent's initialization
        self.__admin_level = admin_level
```

**Key Points:**
- `User` inherits the abstract contract from `AuthenticationSystem`
- `AdminUser` inherits all attributes and methods from `User`
- `super()` is used to call parent class methods
- **Benefits**: Code reusability, creates logical hierarchies

---

## 3. **Polymorphism** 🎭

**Definition**: The ability of different classes to be treated as instances of the same class through inheritance, and the ability to override methods.

### Where it's used:

#### Method Overriding in `AdminUser`:

**Original method in `User`:**
```python
def authenticate(self, username, password):
    if username == self.__username and password == self.__password:
        self.__is_authenticated = True
        return True
    return False
```

**Overridden method in `AdminUser`:**
```python
def authenticate(self, username, password):
    result = super().authenticate(username, password)  # Call parent method
    if result:
        print(f"Admin user '{username}' logged in with level {self.__admin_level}")
    return result
```

**Key Points:**
- Same method name (`authenticate`) behaves differently in child class
- Admin login adds extra logging functionality
- `get_user_data()` also overridden to include admin level

#### In `LoginSystem`:
```python
def login(self):
    # POLYMORPHISM: Different user types authenticate differently
    if self.regular_user.authenticate(entered_username, entered_password):
        self.current_user = self.regular_user
    elif self.admin_user.authenticate(entered_username, entered_password):
        self.current_user = self.admin_user
```

**Benefits**: 
- Same interface (`authenticate`) works for different user types
- Can add new user types without changing the login logic
- Flexible and extensible code

---

## 4. **Abstraction** 🎨

**Definition**: Hiding complex implementation details and showing only the necessary features. Using abstract classes to define a template.

### Where it's used:

#### In `AuthenticationSystem` abstract base class:
```python
from abc import ABC, abstractmethod

class AuthenticationSystem(ABC):
    @abstractmethod
    def authenticate(self, username, password):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_user_data(self):
        """Abstract method to retrieve user data"""
        pass
```

**Key Points:**
- Uses Python's `ABC` (Abstract Base Class) module
- Defines a **contract** that all authentication systems must follow
- Methods decorated with `@abstractmethod` **must** be implemented by child classes
- Cannot create instances of `AuthenticationSystem` directly
- **Benefits**: Ensures consistent interface across different implementations

#### Implementation in child classes:
```python
class User(AuthenticationSystem):
    # MUST implement these methods
    def authenticate(self, username, password):
        # Implementation here
        
    def get_user_data(self):
        # Implementation here
```

---

## Summary Table

| OOP Concept | Class/Location | Purpose |
|-------------|----------------|---------|
| **Encapsulation** | `User` class | Protects private data (`__username`, `__password`) with getter methods |
| **Inheritance** | `User` → `AuthenticationSystem`<br>`AdminUser` → `User` | Reuses code and creates class hierarchy |
| **Polymorphism** | `AdminUser.authenticate()`<br>`AdminUser.get_user_data()` | Same method name, different behavior for admin users |
| **Abstraction** | `AuthenticationSystem` (ABC) | Defines contract that all auth systems must follow |

---

## Testing the Concepts

### Login Credentials:

1. **Regular User:**
   - Username: `eugene`
   - Password: `123456`
   - Shows standard profile

2. **Admin User:**
   - Username: `admin`
   - Password: `admin123`
   - Shows profile + admin level
   - Prints admin login message to console

---

## Benefits of Using OOP

1. **Code Reusability**: Inheritance prevents code duplication
2. **Security**: Encapsulation protects sensitive data
3. **Flexibility**: Polymorphism allows easy extension
4. **Maintainability**: Abstraction provides clear contracts
5. **Scalability**: Easy to add new user types (StudentUser, TeacherUser, etc.)
