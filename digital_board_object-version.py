import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw
import os


class color_box:
    def __init__(self, parent):  # Pass master to initialize widgets in the APP window
        bar_image = os.path.join(os.path.dirname(__file__), 'new_bar.png')
        self.color_box_image = tk.PhotoImage(file=bar_image)  # Store the image as an instance attribute
        tk.Label(parent, image=self.color_box_image, bg="#f2f3f5").place(x=0, y=20)


class canvas_menu_button:
    def __init__(self, parent,canvas_body):
        # Create the canvas button
        self.menu_button = tk.Canvas(parent, width=30, height=30, bg="#f2f3f5", highlightthickness=0)
        self.menu_button.place(x=70, y=5)
        
        self.canvas_body=canvas_body
        # Draw three small horizontal lines to represent the 3-dot menu
        self.line_1 = self.menu_button.create_line(5, 8, 25, 8, width=2)
        self.line_2 = self.menu_button.create_line(5, 15, 25, 15, width=2)
        self.line_3 = self.menu_button.create_line(5, 22, 25, 22, width=2)

        # Create the dropdown menu
        self.main_menu = tk.Menu(parent, tearoff=False)
        self.main_menu.add_command(label=" Save As ", background="light blue", font="arial 10 bold", command=self.save_canvas)
        self.main_menu.add_command(label=" Clear Screen ", background="sky blue", font="arial 10 bold", command=self.new_canvas)

        # Bind the click event to display the menu
        self.menu_button.bind("<Button-1>", self.show_menu)

    def show_menu(self, event):
        # Show the dropdown menu at the location of the mouse click
        self.main_menu.post(event.x_root, event.y_root)
        
    def new_canvas(self):
        self.canvas_body.can_drawing.delete('all')  #it clears the canvas_widget in the canvas_body

    def save_canvas(self):
        file_path= filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png"),("JPEG files","*.jpeg"),("JPG files","*.jpg"),("All Files","*.*")])
        if file_path:
            # Create a new PIL image with the size of the canvas
            canvas_width = self.canvas_body.can_drawing.winfo_width()
            canvas_height = self.canvas_body.can_drawing.winfo_height()
            image = Image.new("RGB", (canvas_width, canvas_height), "white")
            draw = ImageDraw.Draw(image)

            # Draw the content of the canvas onto the image
            for item in self.canvas_body.can_drawing.find_all():
                coords = self.canvas_body.can_drawing.coords(item)
                item_color = self.canvas_body.can_drawing.itemcget(item, "fill")
                item_width = int(float(self.canvas_body.can_drawing.itemcget(item, "width")))  # Convert to float first, then to int
                draw.line(coords, fill=item_color, width=item_width)

            # Save the image
            image.save(file_path)


class color_trey:
    def __init__(self,parent,canvas_body):
            self.colors=tk.Canvas(parent,bg="snow2",width=33,height=300,bd=0)
            self.colors.place(x=36,y=70)

            self.colours_pallate=['black','Red','Blue','Green','Yellow','Purple','Orange','Brown','Light Blue','Grey']
            self.x1_y1_x2_y2=[(8,8,28,28),(8,38,28,58),(8,68,28,88),(8,98,28,118),(8,128,28,148),(8,158,28,178),(8,188,28,208),(8,218,28,238),(8,248,28,268),(8,278,28,298)]
        
            # Using zip to access color and corresponding coordinates
            for colour, coords in zip(self.colours_pallate, self.x1_y1_x2_y2):

                id = self.colors.create_rectangle(coords,fill=colour)
                self.colors.tag_bind(id, '<Button-1>', lambda x, c=colour: canvas_body.show_color(c))           
            

class eraser_photo:
    def __init__(self,parent,canvas_body):
        self.canvas_body = canvas_body  # Store a reference to the canvas_body

        self.eraser_image=os.path.join(os.path.dirname(__file__), 'color_eraser_2.png')
        self.ereser=tk.PhotoImage(file=self.eraser_image)
        tk.Button(parent,image=self.ereser,bg="#f2f3f5",relief="raised", command=self.use_eraser).place(x=36,y=400)

    def use_eraser(self):
        self.eraser_color='white'
        self.canvas_body.show_color(self.eraser_color)
    

class canvas_body:
    def __init__(self,parent) :
        self.can_drawing=tk.Canvas(parent,height=500,width=950,background="white",cursor="hand2")
        self.can_drawing.pack(anchor="se")

        self.can_drawing.bind("<Button-1>",self.locate_xy)
        self.can_drawing.bind("<B1-Motion>",self.add_line)
        self.color="Black"

        self.class_slider_object=slider(parent)
        

    def locate_xy(self,event):

        self.current_y=event.y
        self.current_x=event.x

    def show_color(self,choose_color):
        self.color=choose_color 
        
    def add_line(self,event):
        self.updated_width=float(self.class_slider_object.get_current_value())
        self.can_drawing.create_line((self.current_x,self.current_y,event.x,event.y),width=self.updated_width,fill=self.color)
        # Update the current point to the new point
        self.current_x = event.x
        self.current_y = event.y  



class slider:
    
    def __init__(self,parent) :
        self.current_value= tk.DoubleVar()
        self.slider=ttk.Scale(parent,from_=0,to=20,orient="horizontal",command=self.slider_value,variable=self.current_value,length=200,style='Horizontal.TScale')
        self.slider.place(x=100,y=520)
            #value label
        self.value_label= ttk.Label(parent,text=self.get_current_value())
        self.value_label.place(x=27,y=550)
            #brush_size -image
        self.pen_path = os.path.join(os.path.dirname(__file__), 'brush_size.png')
        self.pen_img=tk.PhotoImage(file=self.pen_path)
        self.img_label=tk.Label(parent,image=self.pen_img)
        self.img_label.place(x=18,y=500)

    def get_current_value(self):
      return '{: .2f}'.format(self.current_value.get())
    
    def slider_value(self,event):
        self.value_label.config(text=self.get_current_value())
    

class APP(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Digital Whiteboard")
        self.geometry("1050x570")
        self.resizable(False, False)
        self.configure(background="#f2f3f5")
            # icon:
        icon_image = os.path.join(os.path.dirname(__file__), 'white_board.ico')
        self.wm_iconbitmap(icon_image)
            # color-box:
        self.color_box = color_box(self)  # Pass 'self' to the color_box instance to link it to the main window 
            # canvas-body:
        self.canvas_body = canvas_body(self)  # Initialize canvas_body first        
            #3_lined-canvas menu button:
        self.menu_btn=canvas_menu_button(self, self.canvas_body)
            #color-trey-canvas in the color_box photo:
        self.color_trey = color_trey(self, self.canvas_body)
            #set the default chosen color is black: 
        self.color="black"
            #eraser-photo:
        self.eraser_photo=eraser_photo(self,self.canvas_body)

        self.mainloop()
# creating an 'a' object of the main(APP) class fopr running the application window:
a = APP()