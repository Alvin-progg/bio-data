import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from abc import ABC, abstractmethod

# ABSTRACTION: Abstract base class defining the contract for authentication systems
class AuthenticationSystem(ABC):
    """Abstract base class for authentication systems"""
    
    @abstractmethod
    def authenticate(self, username, password):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_user_data(self):
        """Abstract method to retrieve user data"""
        pass

# INHERITANCE: User class inheriting from AuthenticationSystem
class User(AuthenticationSystem):
    """User class demonstrating Encapsulation and Inheritance"""
    
    # ENCAPSULATION: Private attributes (using name mangling)
    def __init__(self, username, password, profile_data):
        self.__username = username  # Private attribute
        self.__password = password  # Private attribute
        self.__profile_data = profile_data  # Private attribute
        self.__is_authenticated = False  # Private attribute
    
    # ENCAPSULATION: Public methods to access private data (getters)
    def get_username(self):
        """Getter for username"""
        return self.__username
    
    def get_profile_data(self):
        """Getter for profile data"""
        return self.__profile_data
    
    def is_logged_in(self):
        """Check authentication status"""
        return self.__is_authenticated
    
    # ABSTRACTION: Implementation of abstract method
    def authenticate(self, username, password):
        """Authenticate user credentials"""
        if username == self.__username and password == self.__password:
            self.__is_authenticated = True
            return True
        return False
    
    # ABSTRACTION: Implementation of abstract method
    def get_user_data(self):
        """Get user profile data if authenticated"""
        if self.__is_authenticated:
            return self.__profile_data
        return None
    
    def logout(self):
        """Logout user"""
        self.__is_authenticated = False

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window(400, 300)
        
        # ENCAPSULATION & POLYMORPHISM: Create user objects
        profile_data = [
            ("Name:", "Dela Cruz Eugene Kim A."),
            ("Age:", "19"),
            ("Where do I live:", "Manghinao Proper Bauan Batangas"),
            ("High school graduated:", "Bauan Technical Integrated High School"),
            ("Current School:", "BSU Mabini Campus"),
            ("Hobby:", "Gaming, Workout, Game Programming")
        ]
        
        # Regular user
        self.regular_user = User("eugene", "123456", profile_data)
        
        
        self.current_user = None  # Track currently logged in user
        
        self.create_login_page()
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        # ENCAPSULATION: Create user object
        profile_data = [
            ("Name:", "Dela Cruz Eugene Kim A."),
            ("Age:", "19"),
            ("Where do I live:", "Manghinao Proper Bauan Batangas"),
            ("High school graduated:", "Bauan Technical Integrated High School"),
            ("Current School:", "BSU Mabini Campus"),
            ("Hobby:", "Gaming, Workout, Game Programming")
        ]
        
        # User object
        self.user = User("eugene", "123456", profile_data)
        
        self.current_user = None  # Track currently logged in user
        # Password
        password_frame = tk.Frame(self.root)
        password_frame.pack(pady=10)
        tk.Label(password_frame, text="Password:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.password_entry = tk.Entry(password_frame, font=("Arial", 12), width=20, show="*")
        self.password_entry.pack(side=tk.LEFT, padx=5)
        
        # Login button
        login_btn = tk.Button(self.root, text="Login", font=("Arial", 14, "bold"), 
                             bg="#4CAF50", fg="white", width=15, command=self.login)
        login_btn.pack(pady=30)
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.login())
    
    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        
        # ENCAPSULATION: Use authenticate method
        if self.user.authenticate(entered_username, entered_password):
            self.current_user = self.user
            self.show_profile()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
            self.password_entry.delete(0, tk.END)
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Resize window for profile
        self.root.geometry("700x700")
        self.center_window(700, 700)
        self.root.unbind('<Return>')
        
        # Title
        title_label = tk.Label(self.root, text="Profile Details", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Profile Picture
        try:
            image_path = os.path.join(os.path.dirname(__file__), "Kim.png")
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(self.root, image=photo)
            img_label.image = photo  # Keep a reference
            img_label.pack(pady=10)
        except Exception as e:
            tk.Label(self.root, text="[Profile Picture]", font=("Arial", 12), 
                    bg="#ddd", width=20, height=8).pack(pady=10)
        
        # Profile Information Frame
        info_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        info_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
        
        # ENCAPSULATION & POLYMORPHISM: Get data through encapsulated method
        # Different user types return different data (polymorphism)
        profile_data = self.current_user.get_user_data()
        
        for label_text, value_text in profile_data:
            row_frame = tk.Frame(info_frame, bg="#f0f0f0")
            row_frame.pack(anchor=tk.W, pady=8)
            
            label = tk.Label(row_frame, text=label_text, font=("Arial", 12, "bold"), 
                           bg="#f0f0f0", width=25, anchor=tk.W)
            label.pack(side=tk.LEFT)
            
            value = tk.Label(row_frame, text=value_text, font=("Arial", 12), 
                           bg="#f0f0f0", anchor=tk.W)
            value.pack(side=tk.LEFT)
        
        # Logout button
        logout_btn = tk.Button(self.root, text="Logout", font=("Arial", 12, "bold"), 
                              bg="#f44336", fg="white", width=15, command=self.logout)
        logout_btn.pack(pady=20)
    
    def logout(self):
        # Confirmation dialog before logout
        result = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
        
        if result:  # If user clicked "Yes"
            # ENCAPSULATION: Use encapsulated logout method
            if self.current_user:
                self.current_user.logout()
                self.current_user = None
            
            self.root.geometry("400x300")
            self.center_window(400, 300)
            self.create_login_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()
