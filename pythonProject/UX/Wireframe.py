import tkinter as tk


def show_home():
    # Hide other frames
    features_frame.pack_forget()

    # Show home frame
    home_frame.pack(fill=tk.BOTH, expand=True)


def show_features():
    # Hide other frames
    home_frame.pack_forget()

    # Show features frame
    features_frame.pack(fill=tk.BOTH, expand=True)


# Create the main window
root = tk.Tk()
root.title("Website Wireframe")

# Navigation bar
navbar = tk.Frame(root, bg="lightblue")
navbar.pack(fill=tk.X, side=tk.TOP)

home_button = tk.Button(navbar, text="Home", command=show_home)
home_button.pack(side=tk.LEFT, padx=10, pady=10)

features_button = tk.Button(navbar, text="Features", command=show_features)
features_button.pack(side=tk.LEFT, padx=10, pady=10)

# Home Page Frame
home_frame = tk.Frame(root, bg="lightgrey")

home_label = tk.Label(home_frame, text="Welcome to the Home Page!", bg="lightgrey", font=("Arial", 24))
home_label.pack(pady=100)

# Features Page Frame
features_frame = tk.Frame(root, bg="lightgreen")

features_label = tk.Label(features_frame, text="Our Amazing Features", bg="lightgreen", font=("Arial", 24))
features_label.pack(pady=40)

feature1_label = tk.Label(features_frame, text="Feature 1: ...", bg="lightgreen")
feature1_label.pack(pady=20)

feature2_label = tk.Label(features_frame, text="Feature 2: ...", bg="lightgreen")
feature2_label.pack(pady=20)

# Show the home frame by default
show_home()

# Run the main loop to display the GUI
root.mainloop()
