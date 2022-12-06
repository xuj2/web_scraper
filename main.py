from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from bbuy import bestbuy_automation
from nike import nike_automation
import time
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

root = Tk()
root.title('Shop Bot')
root.geometry('600x500')

def web_scrape():
    url_input = url.get()
    size_input = size.get()
    delay_input = int(delay.get())
    phone_number = phone.get()
    if "nike.com" in url_input:
        if len(size_input) == 0:
            messagebox.showwarning("Warning", "Size required!")
            return 0
        if len(phone_number) == 0:
            messagebox.showwarning("Warning", "Phone number required!")
            return 0            
        while True:
            status = nike_automation(url_input, size_input)
            if status == 0:
                
                message = client.messages.create(
                    body=("Product is available at %s " % url_input),
                    from_=keys.from_num,
                    to = "+1" + str(phone_number)
                )
                
                messagebox.showinfo("Info", "Product is in stock!")
                break
            time.sleep(delay_input)
    elif "bestbuy.com" in url_input:
        if len(phone_number) == 0:
            messagebox.showwarning("Warning", "Phone number required!")
            return 0 
        while True:
            status = bestbuy_automation(url_input)
            if status == 0:
                
                message = client.messages.create(
                    body=("Product is available at %s " % url_input),
                    from_=keys.from_num,
                    to = "+1" + str(phone_number)
                )
                
                messagebox.showinfo("Info", "Product is in stock!")
                break
            time.sleep(delay_input)
    else:
        messagebox.showwarning("Warning", "Invalid URL!")

#URL widgets
Label(root, text="URL: ").place(x=30, y=50)
url = Entry(root, width=30)
url.pack()
url.place(x=130, y=50)

#size widgets
Label(root, text="Size: ").place(x=30, y=80)
size = Entry(root, width=5)
size.pack()
size.place(x=130, y=80)

#delay widget
Label(root, text="Delay: ").place(x=30, y=110)
delay = Entry(root, width=5)
delay.pack()
delay.place(x=130, y=110)
delay.insert(0, '30')

#phone number widget
Label(root, text="Phone: ").place(x=30, y=140)
phone = Entry(root, width=10)
phone.pack()
phone.place(x=130, y=140)

#buttons
start = Button(text="Start", command=web_scrape)
start.pack()
start.place(x=360, y=400)
stop = Button(text="Stop")
stop.pack()
stop.place(x=450, y=400)

root = mainloop()