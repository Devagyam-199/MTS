from tkinter import *
from tkinter import messagebox, ttk
import qrcode
from PIL import ImageTk, Image

#Name: Devagya Mistry
#Roll.no: E035
#Sap ID: 60002220263
#Branch: EXTC E1(2)

#root
root=Tk()
root.geometry("600x400+300+300")
root.title("Login.MTS")
root.configure(bg="white")
root.resizable(False,False) 

#commands

def tktshow():
    ticket_window=Toplevel(root)
    ticket_window.geometry("400x280+300+300")
    ticket_window.title("Ticket")
    ticket_window.configure(bg="white")
    ticket_window.resizable(False,False) 

    qr_img = qrcode.make("Ticket")   
    qr_img.save("Ticket.png")
                            
    frame4=Frame(ticket_window, width=425, height= 375, bg="white")
    frame4.place(x=48,y=2)

    Label(frame4,text="Your Booked Ticket",font=("Montserrat",16,"bold"), fg="#fc6203", bg="White").place(x=48,y=3)

    img1 = ImageTk.PhotoImage(Image.open("Ticket.png"))
    label4 = Label(frame4, image = img1, height=210, width=210)
    label4.place(x=50,y=35)

    ticket_window.mainloop()


def signin():
    Username=user.get()
    Password=pswrd.get()
    usr=open("Usernames.txt","r")
    s=" "
    while(s):
        s=usr.read()
        L=s.split()
        if Username in L:
            psw=open("Passwords.txt","r")
            s1=" "
            while(s1):
                s1=psw.read()
                L1=s1.split()
                if Password in L1:
                    screen=Toplevel(root)
                    screen.geometry("400x250+300+300")
                    screen.title("Welcome to MTS")
                    screen.configure(bg="white")
                    screen.resizable(False,False) 

                    def book():
                        book_window=Toplevel(root)
                        book_window.geometry("600x450+300+300")
                        book_window.title("Booking Counter!")
                        book_window.configure(bg="white")
                        book_window.resizable(False,False)

                        def line_picker(e):
                            if line_combobox.get() == "Yellow-Line":
                                depart_combobox.config(values=ylline)
                                depart_combobox.current(0)
                                arrive_combobox.config(values=ylline)
                                arrive_combobox.current(0)
                            if line_combobox.get() == "Red-Line":
                                depart_combobox.config(values=rdline)
                                depart_combobox.current(0)
                                arrive_combobox.config(values=rdline)
                                arrive_combobox.current(0)
                            if line_combobox.get() == "Ghatkopar-Versova":
                                depart_combobox.config(values=gp_vs)
                                depart_combobox.current(0)
                                arrive_combobox.config(values=gp_vs)
                                arrive_combobox.current(0)

                        frame3=Frame(book_window, width=540, height= 400, bg="white")
                        frame3.place(x=33,y=24)
                        Label(frame3,text="Booking counter!",font=("Montserrat",20,"bold"), fg="#fc6203", bg="White").place(x=175,y=5)

                        lines=["Yellow-Line","Red-Line","Ghatkopar-Versova"]
                        ylline=['Dahisar East',
                                'Upper Dahisar', 
                                'Kandarpada', 
                                'Mandapeshwar', 
                                'Eksar',
                                'Borivali (West)',
                                'Pahadi Eksar',
                                'Kandivali (West)',
                                'Dahanukarwadi',
                                'Valnai',
                                'Malad (West)', 
                                'Lower Malad', 
                                'Pahadi Goregaon', 
                                'Goregaon (West)',
                                'Oshiwara', 
                                'Lower Oshiwara', 
                                'Andheri (West)']
                        
                        rdline=['Dahisar East', 
                                'Ovaripada', 
                                'Rashtriya Udyan', 
                                'Devipada', 
                                'Magathane', 
                                'Poisar', 
                                'Akurli', 
                                'Kurar', 
                                'Dindoshi', 
                                'Aarey', 
                                'Goregaon East', 
                                'Jogeshwari East', 
                                'Mogra', 
                                'Gundavali']
                        
                        gp_vs=['Versova', 
                                'D.N. Nagar', 
                                'Azad Nagar', 
                                'Andheri', 
                                'WEH', 
                                'Chakala', 
                                'Airport Road', 
                                'Marol Naka', 
                                'Saki Naka', 
                                'Asalpha', 
                                'Jagruti Nagar',
                                'Ghatkopar']
                        
                        Label(frame3,text="Select Line:",font=("Montserrat",12), fg="black", bg="white").place(x=23,y=103)
                        line_combobox= ttk.Combobox(frame3, values=lines)
                        line_combobox.current(0)
                        line_combobox.place(x=110,y=106)

                        line_combobox.bind("<<ComboboxSelected>>",line_picker)

                        Label(frame3,text="Depart from:",font=("Montserrat",12), fg="black", bg="white").place(x=23,y=203)
                        depart_combobox= ttk.Combobox(frame3, values=[" "])
                        depart_combobox.place(x=115,y=206)

                        Label(frame3,text="Destination:",font=("Montserrat",12), fg="black", bg="white").place(x=303,y=203)
                        arrive_combobox= ttk.Combobox(frame3, values=[" "])
                        arrive_combobox.place(x=393,y=206)
                        
                        book=Button(frame3, text="Book Now!", fg="white", bg="#fc6203" , font=("Montserrat",13,"bold"), pady=7 , padx=9, command=tktshow)
                        book.place(x=212,y=290)

                        screen.destroy()
                        book_window.mainloop()
                    
                    frame2=Frame(screen, width=300, height= 250, bg="white")
                    frame2.place(x=48,y=26)
                    Label(frame2,text="Welcome to MTS!",font=("Montserrat",16,"bold"), fg="#fc6203", bg="White").place(x=70,y=5)

                    book=Button(frame2, text="Book Ticket!", fg="white", bg="#fc6203" , font=("Montserrat",13,"bold"), pady=7 , padx=9, command=book)
                    book.place(x=90,y=55)

                    show=Button(frame2, text="Show Ticket!", fg="white", bg="#fc6203" , font=("Montserrat",13,"bold"), pady=7 , padx=9, command=tktshow)
                    show.place(x=88,y=125)

                    screen.mainloop()
                elif Password not in L1:
                        messagebox.showerror("Invalid","Invalid Password")
                else:
                    messagebox.showerror("Invalid","Enter a valid password")
                psw.close()
        elif Username not in L:
            messagebox.showerror("Invalid","Invalid Username")
        else:
            messagebox.showerror("Invalid","Enter a valid Username")
        usr.close()
     
      


def signup():
    def saveinfo():
        Username=(" "+user1.get())
        Password=(" "+pswrd1.get())
        Mail=(" "+mail.get())
        usr = open("Usernames.txt", "a")
        usr.write(Username)
        usr = open("Usernames.txt", "r")
        usr.close()        
        psw=open("Passwords.txt", "a")
        psw.write(Password)
        psw = open("Passwords.txt", "r")
        psw.close()
        ml=open("Emails.txt", "a")
        ml.write(Mail)
        ml = open("Emails.txt", "r")
        ml.close()
        messagebox.showinfo("Saved!","Your Details have been saved!")
        sup.destroy()

    sup=Toplevel(root)
    sup.geometry("400x300+300+300")
    sup.title("Sign Up!")
    sup.configure(bg="white")
    sup.resizable(False,False)

    frame1=Frame(sup, width=300, height= 250, bg="white")
    frame1.place(x=48,y=26)
    Label(frame1, text="Enter Details", fg="#fc6203", bg="white" , font=("Montserrat",12,"bold")).place(x=97,y=5)

    us=Label(frame1,text="UserName",bg="white",font=("Montserrat",10))
    us.place(x=55,y=55)
    user1=Entry(frame1,fg="black", width=25, border=0, bg="#eaeaea",font=("Montserrat",10), cursor="ibeam")
    user1.place(x=55,y=80)

    us=Label(frame1,text="Password",bg="white",font=("Montserrat",10))
    us.place(x=55,y=105)
    pswrd1=Entry(frame1,fg="black" , width=25, border=0, bg="#eaeaea",font=("Montserrat",10), show="*")
    pswrd1.place(x=55,y=130)

    us=Label(frame1,text="Email-Id",bg="white",font=("Montserrat",10))
    us.place(x=55,y=155)
    mail=Entry(frame1,fg="black" , width=25, border=0, bg="#eaeaea",font=("Montserrat",10))
    mail.place(x=55,y=180)

    save=Button(frame1, text="Save", bg="#fc6203", fg="white", width=20,font=("Montserrat",10, "bold"), border=0, pady= 4,cursor="hand2", command=saveinfo)
    save.place(x=59,y=212)
   
    sup.mainloop()

#image
bgimg=PhotoImage(file="login.png")
Label(root,image=bgimg,bg="white",height=250,width=250).place(x=33,y=65)

#frame
frame=Frame(root, width=300, height= 500, bg="white")
frame.place(x=315,y=25)
head=Label(frame, text="Sign In", fg="#fc6203", bg="white" , font=("Montserrat",18,"bold"))
head.place(x=62,y=35)

#username
us=Label(frame,text="UserName",bg="white",font=("Montserrat",13))
us.place(x=18,y=100)
user=Entry(frame,fg="black", width=25, border=0, bg="#eaeaea",font=("Montserrat",11), cursor="ibeam")
user.place(x=18,y=125)


#password
us=Label(frame,text="Password",bg="white",font=("Montserrat",13))
us.place(x=18,y=150)
pswrd=Entry(frame,fg="black" , width=25, border=0, bg="#eaeaea",font=("Montserrat",11), show="*")
pswrd.place(x=18,y=175)

#SignButton
sgin=Button(frame, text="Sign In", bg="#fc6203", fg="white", width=22,font=("Montserrat",11, "bold"), border=0, pady= 6,cursor="hand2", command=signin)
sgin.place(x=18,y=212)
lb=Label(frame, text="Don't have an account?", fg="black", bg="white" , font=("Montserrat",9))
lb.place(x=17,y=255)

#SignupButton
sgup=Button(frame, text="Sign Up!", fg="#fc6203", bg="white" , font=("Montserrat",9), border=0,cursor="hand2", command=signup)
sgup.place(x=152,y=255)

#main
root.mainloop()