# Digital-White-Board-APP

Let's dive deeper into the explanation of each part of the code, focusing on how it captures the content from the `Canvas` widget in Tkinter and saves it as an image file using the `Pillow` library.

### **Modules and Functions:**

#### **Pillow (PIL) Library:**
- **Pillow** is a powerful library in Python for image processing. It is the fork of the original Python Imaging Library (PIL) and provides tools to create, modify, and save images in various formats.

- **`Image`**:
  - **Role**: Represents an image in memory. It can be a blank image or one loaded from an existing file. You can manipulate this image (e.g., draw shapes, change colors) and save it in formats like PNG, JPEG, etc.
  - **Common Methods**: 
    - `Image.new()`: Creates a new blank image.
    - `Image.save()`: Saves the image to a file.

- **`ImageDraw`**:
  - **Role**: Provides tools to draw on an image object, including lines, shapes, and text.
  - **Common Methods**:
    - `ImageDraw.Draw(image)`: Creates a drawing context on the image, allowing you to add drawings to it.
    - `draw.line(coords, fill=color, width=width)`: Draws a line on the image using the specified coordinates, color, and width.

### **Function Explanation:**

#### **`save_canvas()` Function:**
This function captures whatever is drawn on the `Canvas` widget (`can_drawing`) in your Tkinter application and saves it as an image file.

1. **Opening the Save File Dialog:**
   ```python
   file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All Files", "*.*")])
   ```
   - **Purpose**: This line of code opens a file dialog that allows the user to specify where they want to save the image and in which format.
   - **`asksaveasfilename()`**: This function brings up a dialog that prompts the user to select a file path for saving the image.
     - `defaultextension=".png"`: Ensures that if the user doesn't specify an extension, the file will be saved as a PNG by default.
     - `filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")]`: Lists the file types the user can choose from (PNG, JPEG, or any file type).

2. **Checking if a File Path is Provided:**
   ```python
   if file_path:
   ```
   - **Purpose**: Ensures that the function proceeds only if the user has provided a valid file path. If the user cancels the dialog, `file_path` will be empty, and the function will exit without saving anything.

3. **Creating the Image:**
   ```python
   image = Image.new("RGB", (canvas_width, canvas_height), "white")
   draw = ImageDraw.Draw(image)
   ```
   - **Purpose**: This section creates a new blank image that matches the size of the `Canvas` in your application. 
   - **`Image.new("RGB", (canvas_width, canvas_height), "white")`**:
     - **`RGB`**: This mode represents the color space (Red, Green, Blue). It's a common choice for color images.
     - **`(canvas_width, canvas_height)`**: These are the dimensions of the canvas, which will also be the dimensions of the image.
     - **`"white"`**: This is the background color of the image.
   - **`ImageDraw.Draw(image)`**:
     - Creates a drawing context on the `image`. This allows the function to draw lines and shapes on this blank image, effectively replicating what was drawn on the Tkinter `Canvas`.

4. **Drawing on the Image:**
   ```python
   for item in can_drawing.find_all():
       coords = can_drawing.coords(item)
       item_color = can_drawing.itemcget(item, "fill")
       item_width = int(float(can_drawing.itemcget(item, "width")))
       draw.line(coords, fill=item_color, width=item_width)
   ```
   - **Purpose**: This block of code loops over all the drawable items on the canvas and redraws them on the `PIL` image.
   - **`can_drawing.find_all()`**:
     - Finds all the drawable items (lines, shapes) on the canvas.
   - **`can_drawing.coords(item)`**:
     - Retrieves the coordinates of each item. For a line, this would include the starting and ending points.
   - **`can_drawing.itemcget(item, "fill")`**:
     - Retrieves the color (`fill`) of the item on the canvas.
   - **`can_drawing.itemcget(item, "width")`**:
     - Retrieves the width of the item as a string (e.g., `'17.0'`). Since the width needs to be an integer for drawing, it's converted to a float and then to an integer using `int(float(...))`.
   - **`draw.line(coords, fill=item_color, width=item_width)`**:
     - Draws a line on the image at the specified coordinates, using the color and width retrieved from the canvas.

5. **Saving the Image:**
   ```python
   image.save(file_path)
   ```
   - **Purpose**: This line saves the image that has been created and drawn on to the file path provided by the user.
   - **`image.save(file_path)`**:
     - Saves the `PIL` image to the location specified by `file_path`, using the file format indicated by the file extension (e.g., `.png`, `.jpg`).

### **Overall Workflow:**
1. **User Draws on Canvas**: The user draws on the Tkinter `Canvas` widget.
2. **User Chooses Save Location**: The user clicks a button to save the drawing. A dialog appears where they select the file path and format.
3. **Image Creation**: The function creates a blank `PIL` image with the same dimensions as the `Canvas`.
4. **Recreate Drawing**: The function loops over all the drawable elements on the canvas, retrieves their properties (coordinates, color, width), and redraws them onto the `PIL` image.
5. **Save the Image**: The `PIL` image, now a copy of the canvas content, is saved to the user’s chosen location and format.

This approach ensures that the canvas content is accurately captured and saved as an image file, making it accessible outside of the Tkinter application.


### **Function: `color_pallete()`**

1. **Create Color Rectangles:**
   - The function uses the `create_rectangle()` method from the `Canvas` widget (`colors`) to draw small colored rectangles on the screen. Each rectangle represents a different color option that the user can choose.
   - The positions and sizes of the rectangles are defined by the coordinates passed to `create_rectangle((x1, y1, x2, y2), fill=color)`. For example, `(8, 8, 28, 28)` creates a rectangle that starts at the point `(8, 8)` and ends at `(28, 28)`.

2. **Assign Colors to Rectangles:**
   - Each rectangle is filled with a specific color using the `fill` attribute. For instance, `fill="black"` fills the first rectangle with black color.

3. **Bind Click Events to Rectangles:**
   - The function uses `tag_bind()` to attach an event to each rectangle. This event listens for a left mouse button click (`'<Button-1>'`) on the rectangle.
   - When a rectangle is clicked, a lambda function is triggered, which calls the `show_color()` function with the specific color of the rectangle as its argument. This changes the current drawing color to the selected color.

### **Example of a Color Selection:**

- The first rectangle is black:
  ```python
  id = colors.create_rectangle((8, 8, 28, 28), fill="black")
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
  ```
  - This code creates a black rectangle. When the user clicks on this rectangle, the `show_color('black')` function is called, which sets the current drawing color to black.

- The second rectangle is red:
  ```python
  id = colors.create_rectangle((8, 38, 28, 58), fill="Red")
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('Red'))
  ```
  - Similarly, this creates a red rectangle, and clicking on it changes the drawing color to red.

### **Summary:**
The `color_pallete()` function creates a vertical row of colored rectangles (representing different colors) on the left side of the application. Each rectangle is clickable, and clicking on one changes the current drawing color to that rectangle's color, allowing users to easily switch colors while drawing on the canvas.