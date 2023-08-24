import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import customtkinter
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
import cv2
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("TerrainVisionX")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="TerrainVisionX", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, height=500)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("Home")
        self.tabview.add("Normal View")
        self.tabview.add("Normal & Segmentation View")
        self.tabview.add("Camera View")
        self.tabview.add("All")
        
            # Grid configuration
        self.tabview.tab("Home").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("Home").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Normal View").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Normal View").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Normal & Segmentation View").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Normal & Segmentation View").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Normal & Segmentation View").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Camera View").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Camera View").grid_rowconfigure(1, weight=1)
        
            # Create textbox
        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("Home"))
        self.textbox.grid(row=0, column=0, sticky="nsew")
            # Create Normal View's video player
        self.video_player_n = TkinterVideo(self.tabview.tab("Normal View"))
        self.video_player_n.grid(row=0, column=0, sticky="nsew")
        self.video_player_n.load(".\\assets\Los Angeles 720p - California Glow.mp4")
            # Create Framesx2 for Noraml & Segmentation View's video players
        self.video_frame_l = customtkinter.CTkFrame(self.tabview.tab("Normal & Segmentation View"), corner_radius=0)
        self.video_frame_l.grid(row=0, column=0, sticky="nsew")
        self.video_frame_l.grid_rowconfigure(0, weight=1)
        self.video_frame_l.grid_columnconfigure(0, weight=1)
        # self.video_frame_l.grid_columnconfigure(1, weight=1)
        
        self.video_frame_r = customtkinter.CTkFrame(self.tabview.tab("Normal & Segmentation View"), corner_radius=0)
        self.video_frame_r.grid(row=0, column=1, sticky="nsew")
        self.video_frame_r.grid_rowconfigure(0, weight=1)
        self.video_frame_r.grid_columnconfigure(0, weight=1)
            
            # Create Noraml & Segmentation View's video players
        self.video_player_ns_n = TkinterVideo(self.video_frame_l)
        self.video_player_ns_n.grid(row=0, column=0, sticky="nsew")
        self.video_player_ns_n.load(".\\assets\Los Angeles 720p - California Glow.mp4")
        
        self.video_player_ns_s = TkinterVideo(self.video_frame_r)
        self.video_player_ns_s.grid(row=0, column=0, sticky="nsew")
        self.video_player_ns_s.load(".\\assets\Segmentation_for_Autonomous_Driving.mp4")
        # self.video_player.load(".\\assets\Segmentation_for_Autonomous_Driving.mp4")
        
        # Camera
        # self.camera_frame = ttk.LabelFrame(self.tabview.tab("Camera View"), text="Camera Feed")
        # self.camera_frame.grid(row = 0, column = 0, sticky='nsew')
        # self.start_button = ttk.Button(self.tabview.tab("Camera View"), text="Start", command=self.start_camera_recording)
        # self.start_button.grid(row = 1, column = 0)
        # self.canvas = customtkinter.CTkCanvas(self.camera_frame)
        # self.canvas.grid(row = 0, column = 0, sticky='nsew')
        
        
        # self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)        
        
        # self.recording = False
        # self.writer = None
        # self.update()

        # Create footbar frame
        self.footbar_frame = customtkinter.CTkFrame(self, width=140, height=40, corner_radius=0)
        self.footbar_frame.grid(row=4, column=1, columnspan=2, padx=(20, 20), pady=(10,0), sticky="nsew")
        self.footbar_frame.grid_columnconfigure(2, weight=1)

        self.play_button = customtkinter.CTkButton(master=self.footbar_frame, text="Play", command=self.play_button_event)
        self.play_button.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.stop_button = customtkinter.CTkButton(master=self.footbar_frame, text="Stop", command=self.stop_button_event)
        self.stop_button.grid(row=0, column=1, padx=(20, 20), pady=(10, 10))
        self.load_button = customtkinter.CTkButton(master=self.footbar_frame, text="Load", command=self.load_button_event, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.load_button.grid(row=0, column=3, padx=(20, 20), pady=(10, 10))
        self.live_button = customtkinter.CTkButton(master=self.footbar_frame, text="Live", command=None, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.live_button.grid(row=0, column=4, padx=(20, 20), pady=(10, 10))
        
        
        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "Welcome to TerrainVisionX\n\n" + "Here's gonna be readme or instructions guide.\n\n")
        self.textbox.configure(state='disabled')

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def play_button_event(self):
        if self.tabview.get() == 'Normal & Segmentation View':
            self.video_player_ns_n.play()
            self.video_player_ns_s.play()
        else:
            self.video_player_n.play()
    
    def stop_button_event(self):
        self.video_player_n.stop()
        self.video_player_ns_n.stop()
        self.video_player_ns_s.stop()
    
    # Open a file dialog box and allow the user to select a video file to load into the video player
    def load_button_event(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
        self.video_player.load(file_path)
    
    def live_button_event(self):
        pass
    
    def start_camera_recording(self):
        self.recording = True
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        self.writer = cv2.VideoWriter("recording1.mp4", fourcc, 30.0, (1080, 720))
        
    def stop_camera_recording(self):
        self.recording = False
        if self.writer:
            self.writer.release()
            
            
    def update(self):
        ret, frame = self.cap.read()
        if ret:
            if self.recording and self.writer:
                self.writer.write(frame)

            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.after(10, self.update) 
        
    def run(self):
        self.mainloop()
        # self.cap.release()
        # if self.writer:
        #     self.writer.release()
        # cv2.destroyAllWindows() 

if __name__ == "__main__":
    app = App()
    app.run()