# Tkinter Widgets Used in Login System

This document lists and explains all the tkinter widgets used in the mini login system.

---

## Widget Summary

| Widget | Count | Purpose |
|--------|-------|---------|
| `Tk` | 1 | Main application window |
| `Label` | Multiple | Display text and images |
| `Entry` | 2 | Username and password input fields |
| `Button` | 2 | Login and Logout buttons |
| `Frame` | Multiple | Container/grouping for layout |
| `messagebox` | 3 | Alert dialogs for errors and confirmation |

---

## Detailed Widget Usage

### 1. **Tk (Root Window)**

```python
root = tk.Tk()
```

**Purpose:** The main application window container

**Properties Used:**
- `title()` - Sets window title ("Login System")
- `geometry()` - Sets window size (e.g., "400x300", "700x700")
- `resizable()` - Controls if window can be resized (False, False)
- `mainloop()` - Starts the event loop to display the window

**Where Used:**
- Created once at program start
- Modified during login/logout to change size

---

### 2. **Label Widget**

```python
tk.Label(parent, text="...", font=(...), bg="...")
```

**Purpose:** Display static text or images

**Instances in the System:**

#### a) Title Labels
```python
title_label = tk.Label(self.root, text="Login System", font=("Arial", 24, "bold"))
title_label.pack(pady=30)
```
- Displays "Login System" on login page
- Displays "Profile Details" on profile page
- Uses large bold font (24pt Arial)

#### b) Form Labels
```python
tk.Label(username_frame, text="Username:", font=("Arial", 12))
tk.Label(password_frame, text="Password:", font=("Arial", 12))
```
- Labels for input fields
- Standard 12pt font

#### c) Profile Picture Label
```python
img_label = tk.Label(self.root, image=photo)
img_label.image = photo  # Keep reference
```
- Displays user's profile image
- Uses PIL/Pillow to load and resize image
- Fallback label if image not found

#### d) Profile Data Labels
```python
label = tk.Label(row_frame, text=label_text, font=("Arial", 12, "bold"), 
                bg="#f0f0f0", width=25, anchor=tk.W)
value = tk.Label(row_frame, text=value_text, font=("Arial", 12), 
                bg="#f0f0f0", anchor=tk.W)
```
- Two labels per profile field (label + value)
- 6 fields total = 12 labels
- Gray background (#f0f0f0)
- Left-aligned (anchor=tk.W)

---

### 3. **Entry Widget**

```python
tk.Entry(parent, font=(...), width=..., show="...")
```

**Purpose:** Text input fields for user data

**Instances:**

#### a) Username Entry
```python
self.username_entry = tk.Entry(username_frame, font=("Arial", 12), width=20)
```
- Input field for username
- 20 characters wide
- Stored as instance variable to retrieve value

#### b) Password Entry
```python
self.password_entry = tk.Entry(password_frame, font=("Arial", 12), width=20, show="*")
```
- Input field for password
- `show="*"` masks password characters
- Can be cleared with `.delete(0, tk.END)`

**Methods Used:**
- `.get()` - Retrieve entered text
- `.delete(0, tk.END)` - Clear the field

---

### 4. **Button Widget**

```python
tk.Button(parent, text="...", font=(...), bg="...", fg="...", command=...)
```

**Purpose:** Clickable buttons that trigger actions

**Instances:**

#### a) Login Button
```python
login_btn = tk.Button(self.root, text="Login", font=("Arial", 14, "bold"), 
                     bg="#4CAF50", fg="white", width=15, command=self.login)
```
- Green background (#4CAF50)
- White text
- Calls `self.login()` when clicked
- 15 characters wide

#### b) Logout Button
```python
logout_btn = tk.Button(self.root, text="Logout", font=("Arial", 12, "bold"), 
                      bg="#f44336", fg="white", width=15, command=self.logout)
```
- Red background (#f44336)
- White text
- Calls `self.logout()` when clicked
- Shows confirmation dialog before logout

**Properties:**
- `command` - Function to call on click
- `bg` - Background color
- `fg` - Foreground (text) color

---

### 5. **Frame Widget**

```python
tk.Frame(parent, bg="...")
```

**Purpose:** Container widget for grouping and organizing other widgets

**Instances:**

#### a) Username Frame
```python
username_frame = tk.Frame(self.root)
```
- Groups username label and entry field
- Allows horizontal layout (side=tk.LEFT)

#### b) Password Frame
```python
password_frame = tk.Frame(self.root)
```
- Groups password label and entry field
- Same layout as username frame

#### c) Profile Information Frame
```python
info_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
```
- Main container for all profile data
- Gray background (#f0f0f0)
- Internal padding (20px all sides)

#### d) Row Frames (Multiple)
```python
row_frame = tk.Frame(info_frame, bg="#f0f0f0")
```
- One frame per profile field (6 total)
- Contains label and value for each field
- Consistent gray background

---

### 6. **messagebox Module**

```python
from tkinter import messagebox
```

**Purpose:** Display popup dialog boxes for alerts and confirmations

**Instances:**

#### a) Login Error
```python
messagebox.showerror("Login Failed", "Invalid username or password!")
```
- Shows error icon
- Title: "Login Failed"
- Displayed when credentials are wrong

#### b) Logout Confirmation
```python
messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
```
- Shows question icon
- Returns True if "Yes" clicked, False if "No"
- Prevents accidental logout

**Message Box Types Used:**
- `showerror()` - Error messages (red X icon)
- `askyesno()` - Yes/No question dialogs

---

## Layout Methods Used

### 1. **pack()**
```python
widget.pack(pady=10, padx=5, side=tk.LEFT, anchor=tk.W)
```

**Used for:** All widgets in this system

**Common Parameters:**
- `pady` - Vertical padding (space above/below)
- `padx` - Horizontal padding (space left/right)
- `side` - Positioning (tk.LEFT, tk.RIGHT, tk.TOP, tk.BOTTOM)
- `anchor` - Alignment (tk.W=West/Left, tk.E=East/Right)
- `fill` - Expand to fill space (tk.X, tk.Y, tk.BOTH)
- `expand` - Allow widget to grow (True/False)

**Examples in Code:**
```python
title_label.pack(pady=30)                    # Vertical spacing
username_frame.pack(pady=10)                 # Vertical spacing
self.username_entry.pack(side=tk.LEFT, padx=5)  # Horizontal layout
info_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)  # Fill space
```

---

## Widget Destruction

### Clearing All Widgets
```python
for widget in self.root.winfo_children():
    widget.destroy()
```

**Purpose:** Remove all widgets from window before switching screens

**Used When:**
- Switching from login to profile page
- Switching from profile back to login page

---

## Event Binding

### Enter Key Binding
```python
self.root.bind('<Return>', lambda event: self.login())
```

**Purpose:** Allows pressing Enter key to submit login

**Unbinding:**
```python
self.root.unbind('<Return>')
```
- Removed on profile page to prevent accidental actions

---

## Additional Libraries

### PIL/Pillow (Image Handling)
```python
from PIL import Image, ImageTk

img = Image.open(image_path)
img = img.resize((150, 150), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(img)
```

**Purpose:** Load and display profile picture

**Methods:**
- `Image.open()` - Load image file
- `.resize()` - Change image dimensions
- `ImageTk.PhotoImage()` - Convert for tkinter display
- `Resampling.LANCZOS` - High-quality resizing algorithm

---

## Color Scheme

| Element | Color Code | Color Name |
|---------|-----------|------------|
| Login Button | `#4CAF50` | Green |
| Logout Button | `#f44336` | Red |
| Profile Background | `#f0f0f0` | Light Gray |
| Fallback Image BG | `#ddd` | Gray |
| Button Text | `white` | White |

---

## Font Usage

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Page Titles | Arial | 24pt | Bold |
| Buttons | Arial | 12-14pt | Bold |
| Labels | Arial | 12pt | Bold |
| Values | Arial | 12pt | Normal |

---

## Summary

**Total Widget Types:** 6 (Tk, Label, Entry, Button, Frame, messagebox)

**Total Widget Instances:** ~25+ widgets created dynamically

**Layout System:** pack() geometry manager

**Special Features:**
- Image display with PIL/Pillow
- Password masking with `show="*"`
- Event binding for Enter key
- Dynamic screen switching by destroying/recreating widgets
