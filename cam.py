import cv2
import tkinter as tk
from PIL import Image, ImageTk

def cam_app():
    # Create a window
    window = tk.Tk()
    window.title("Search by camera")
    window.configure(bg="white")
    # Create a canvas to display the camera video
    canvas = tk.Canvas(window, width=480, height=380, bg="white")
    canvas.pack(side=tk.TOP)
    # Create a frame on the top side for the logo
    logo_frame = tk.Frame(window, width=200, height=200, bg="white")
    logo_frame.pack(side=tk.TOP)
    # Load the logo image
    logo_image = Image.open("logo.png")
    logo_image = logo_image.resize((100, 100))  # size of the logo
    logo_photo = ImageTk.PhotoImage(logo_image)
    # Create a label to display the logo
    logo_label = tk.Label(logo_frame, image=logo_photo, bg="white")
    logo_label.pack(pady=20)  # padding 
    # Open the camera
    camera = cv2.VideoCapture(0)
    def update_frame():
        # Read a frame from the camera
        ret, frame = camera.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Create an ImageTk object from the frame
            image = Image.fromarray(frame_rgb)
            image_tk = ImageTk.PhotoImage(image)
            # Display the frame on the canvas
            canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
            canvas.image = image_tk
        # Schedule the next frame update
        window.after(15, update_frame)
    # Start updating the frames
    update_frame()
    # Create a frame to hold the buttons
    button_frame = tk.Frame(window, bg="white")
    button_frame.pack(side=tk.BOTTOM, pady=20)
    # Function to capture a frame from the camera
    def capture_frame():
        # Read a frame from the camera
        ret, frame = camera.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Create an ImageTk object from the frame
            image = Image.fromarray(frame_rgb)
            image.save("captured_image.jpg")  # Save the captured image as a file
    # Function to exit the application
    def exit_application():
        # Release the camera
        camera.release()
        # Close the window
        window.destroy()
    # Create a button to capture the frame
    capture_button = tk.Button(button_frame, text="Capture", command=capture_frame, width=10, height=2, bg="cyan", relief="raised", bd=2, font=("Arial", 14), padx=10)
    capture_button.pack(side=tk.LEFT, padx=10)
    # Create a button to exit the application
    exit_button = tk.Button(button_frame, text="Exit", command=exit_application, width=10, height=2, bg="cyan", relief="raised", bd=2, font=("Arial", 14), padx=10)
    exit_button.pack(side=tk.RIGHT, padx=10)
    # Start the tkinter event loop
    window.mainloop()
    # Release the camera
    camera.release()

cam_app()