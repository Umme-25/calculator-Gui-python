import tkinter as tk

# Global variable to store the display content, managed by StringVar
display_var = None
first_num = None
operator = None

def button_click(number):#Appends the clicked number/operator to the display."""
     current = display_var.get()
     if number == '.' and '.' in current:
         return
     display_var.set(current + str(number))



def button_clear():#Clears the calculator display."""
    display_var.set("")
    global first_num, operator
    first_num = None
    operator = None

def button_operation(op):
    global first_num, operator
    try:
        first_num = float(display_var.get())
        operator = op
        display_var.set("")
    except ValueError:
        display_var.set("Error")
        first_num = None
        operator = None

def button_equals():
    global first_num, operator
    try:
        second_num = float(display_var.get())
        display_var.set("")
        if first_num is not None and operator is not None:
            result = 0
            if operator == '+':
                result = first_num + second_num
            elif operator == '-':
                result = first_num-second_num
            elif operator == '*':
                result = first_num * second_num
            elif operator == '/':
                result = first_num/ second_num

            if result == int(result):
                display_var.set(str(int(result)))
            else:
                display_var.set(result)
            

    except ValueError:
        display_var.set("Error")
    except Exception as e:
        display_var.set(f"Error: {e}")
    finally:
        first_num = None
        operator = None


#application window
root = tk.Tk()
root.title("Calculator") #window tittle

#sizing of window
root.geometry("300x400")  #width x height

#window resizing on expansion
for i in range(4):#4 column
    root.grid_columnconfigure(i,weight=1)
for i in range(1,6): #5 row for buttons
    root.grid_rowconfigure(i,weight=1)
#root.grid_rowconfigure(0,weight=1)

# Create the StringVar and link it to the Entry widget
display_var = tk.StringVar()
e = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 16),
justify='right', textvariable=display_var)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#Entry display
#e = tk.Entry(root,width=35,borderwidth=5, font=('Arial',16),justify='right')
#placing row 0  and spanning all columns and sticking side by side
#e.grid(row=0, column=0, columnspan=4, padx=10 ,pady=10, sticky="nsew")

"""
Define buttons -->
Buttons with their cooresponding grid positions
(row, column)
"""
buttons_data = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), # + will span 2 columns
    ('C',5,0), ('=',5,1)   #  = will span 3 columns

]
#Dynamic buttons creation and placing
button_font =('Arial',14) 
for item_data in buttons_data:
    button_text = item_data[0]
    r= item_data[1]
    c = item_data[2]
    button_type = item_data[3] if len(item_data)>3 else 'number' # Default to 'nuber
    btn = None
    command_func =None
    column_span = 1
    if button_type == 'clear':
        command_func = button_clear
    elif button_type == 'equals':
        command_func = button_equals
        column_span = 3
    elif button_type == 'operator':
        command_func = lambda op=button_text:button_operation(op)
    elif button_type == 'operator':
        command_func = lambda op=button_text:button_operation(op)
    else:
        command_func = lambda num= button_text: button_click(num)


for (button_text, r, c) in buttons_data:

    if button_text == 'C':
        cmd = button_clear
        col_span = 1

    elif button_text == '=':
        cmd = button_equals
        col_span = 3

    elif button_text in ['+', '-', '*', '/']:
        cmd = lambda op=button_text: button_operation(op)
        col_span = 1

    elif button_text == '+':   # special layout
        cmd = lambda op=button_text: button_operation(op)
        col_span = 2

    else:
        cmd = lambda num=button_text: button_click(num)
        col_span = 1

    btn = tk.Button(root, text=button_text, font=button_font,
                    padx=20, pady=20, command=cmd)

    btn.grid(row=r, column=c, columnspan=col_span,
             padx=5, pady=5, sticky="nsew")


#slight row expansion also
#root.grid_rowconfigure(0,weight=1)
#btn = tk.Button(root, text=button_text, font = button_font, padx=20, pady=20, command = command_func)
#btn.grid(row=r, column=c, columnspan=column_span, padx=5, pady=5, sticky="nsew")

#starting Tkinter event loops 
root.mainloop()
