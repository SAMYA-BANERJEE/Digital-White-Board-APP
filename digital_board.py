from tkinter import *
from tkinter import ttk,filedialog
from PIL import Image, ImageDraw
import os

###### Globaly decleared variables:
current_x=0
current_y=0
color = 'black'

####### Functions definition:
def save_canvas():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png"),("JPEG files", "*.jpg"),("All Files", "*.*")])
    if file_path:
        # Create a new PIL image with the size of the canvas
        canvas_width = can_drawing.winfo_width()
        canvas_height = can_drawing.winfo_height()
        image = Image.new("RGB", (canvas_width, canvas_height), "white")
        draw = ImageDraw.Draw(image)

        # Draw the content of the canvas onto the image
        for item in can_drawing.find_all():
            coords = can_drawing.coords(item)
            item_color = can_drawing.itemcget(item, "fill")
            item_width = int(float(can_drawing.itemcget(item, "width")))  # Convert to float first, then to int
            draw.line(coords, fill=item_color, width=item_width)

        # Save the image
        image.save(file_path)

def locate_xy(event):
    global current_x,current_y

    current_x = event.x
    current_y = event.y

def get_current_value():
    return '{: .2f}'.format(current_value.get())
    
def slider_value(event):
    value_label.configure(text=get_current_value())

def add_line(event):
    global current_x,current_y
    can_drawing.create_line((current_x,current_y,event.x,event.y),width=get_current_value(),fill=color)
    current_x = event.x
    current_y = event.y

def menu_click(event):
    # Popup the menu at the position of the event (mouse click)
    main_menu.post(event.x_root, event.y_root)

def show_color(choose_color):
    global color
    color=choose_color

def new_canvas():
    can_drawing.delete('all')
    color_pallete()
  
def use_eraser():
    global color
    color = 'white'  # Sets the color to white for erasing


def color_pallete():

        id = colors.create_rectangle((8,8,28,28),fill="black")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('black'))

        id = colors.create_rectangle((8,38,28,58),fill="Red")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Red'))

        id = colors.create_rectangle((8,68,28,88),fill="Blue")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Blue'))

        id = colors.create_rectangle((8,98,28,118),fill="Green")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Green'))

        id = colors.create_rectangle((8,128,28,148),fill="Yellow")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Yellow'))

        id = colors.create_rectangle((8,158,28,178),fill="Purple")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Purple'))

        id = colors.create_rectangle((8,188,28,208),fill="Orange")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Orange'))

        id = colors.create_rectangle((8,218,28,238),fill="Brown")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Brown'))

        id = colors.create_rectangle((8,248,28,268),fill="Light Blue")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Light Blue'))

        id = colors.create_rectangle((8,278,28,298),fill="Gray")
        colors.tag_bind(id, '<Button-1>',lambda x : show_color('Gray'))

###### The main GUI window:
if __name__ == '__main__':
    root=Tk()
    root.title("White Board")
    root.geometry("1050x570")
    root.config(bg="#f2f3f5")
    root.resizable(False,False)


    # icon:
    icon_image=os.path.join(os.path.dirname(__file__), 'white_board.ico')
    root.wm_iconbitmap(icon_image)
    

    #left- frame:------
    f1=Frame(root,width=100)
    f1.pack(side=LEFT,fill=Y)


    # color box:
    bar_image=os.path.join(os.path.dirname(__file__), 'new_bar.png')
    color_box=PhotoImage(file=bar_image)
    Label(f1,image=color_box,bg="#f2f3f5").place(x=0,y=20)
    
    #canvas-menu_button:
    menu_button = Canvas(f1, width=30, height=30, bg="#f2f3f5", highlightthickness=0)
    menu_button.place(x=70, y=5)
    
    # Draw three small horizontal lines to represent the 3-dot menu
    line_1 = menu_button.create_line(5, 8, 25, 8, width=2)
    line_2 = menu_button.create_line(5, 15, 25, 15, width=2)
    line_3 = menu_button.create_line(5, 22, 25, 22, width=2)

    # Bind the click event to the Canvas
    menu_button.bind("<Button-1>", menu_click)

    main_menu= Menu(f1,tearoff=False)
    main_menu.add_command(label=" Save As ",background="light blue",font="arial 10 bold",command=save_canvas)
    main_menu.add_command(label=" Clear Screen ",background="sky blue",font="arial 10 bold",command=new_canvas)
    
    #color trey:
    colors=Canvas(f1,bg="snow2",width=33,height=300,bd=0)
    colors.place(x=36,y=70)

    #eraser photo:
    eraser_image=os.path.join(os.path.dirname(__file__), 'color_eraser_2.png')
    ereser=PhotoImage(file=eraser_image)
    Button(f1,image=ereser,bg="#f2f3f5",relief=RAISED, command=use_eraser).place(x=36,y=400)

    #canvas - body:
    can_drawing=Canvas(root,height=500,width=950,background="white",cursor="hand2")
    can_drawing.pack(side=TOP)

    can_drawing.bind("<Button-1>",locate_xy)
    can_drawing.bind("<B1-Motion>",add_line)

    ############ slider #############
    
    #pen_size image:
    pen_image=os.path.join(os.path.dirname(__file__), 'brush_size.png')
    pen=PhotoImage(file=pen_image)
    Label(root,image=pen,bg="#f2f3f5").place(x=17,y=504)
    
    current_value = DoubleVar()

    slider=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=slider_value,variable=current_value,activebackground='Light Blue',background='Light Blue',relief=GROOVE,state=ACTIVE,length=350)
    slider.place(x=100,y=520)
    
    #value label
    value_label= ttk.Label(root,text=get_current_value())
    value_label.place(x=27,y=550)

    color_pallete()
    root.mainloop()