from tkinter import *            #this is import to use the widgets of tkinter
import csv                       # this is import to use the csv file
def main_scree():                #defination of function
    
    global screen9               #global is used so that we can call this screen from other screens 
    screen9=Tk()
    screen9.title("menu")        #title
    screen9.configure(background="grey")          #this is used to set the background color
    Label(screen9,text="Welcome To Parking Management System",font=("bold",30),bg="pink").pack()
    #this Label is used to write label on screen 
    #syntax of label is Label(root name,text="what u want to write",font=("font style",size),bg="bg color")
    Label(screen9,text="",bg="grey").pack()       #we used this to give space b|w to widgets
    Button(screen9,text="Login",command=logi,bd=30,bg="cyan",font=("bold",15)).pack() #this is used for button
    Label(screen9,text="",bg="grey").pack()
    Button(screen9,text="Register",command=reg,bd=30,bg="cyan",font=("bold",15)).pack()
    Label(screen9,text="",bg="grey").pack()
    Button(screen9,text="Availability",command=avai,bd=30,bg="cyan",font=("bold",15)).pack()
    Label(screen9,text="",bg="grey").pack()
def bo():
    
    global screen7
    screen7=Toplevel(screen)    # this is used to show which is root window
    screen7.title("booking")
    screen7.configure(background="grey")
    global vnum            # this is used to global the variable
    vnum=StringVar()        # declare the string variable
    Label(screen7,text="Booking",font=("bold",30),bg="pink").pack()
    Label(screen7,text="Vehicle Type",font=("bold",20),bg="grey").pack()
    OPTIONS = ["car","truck","tractor","bus","Two-wheeler"]    
    # here we have to write the options,we want in option menu
    global vehicle
    vehicle= StringVar()              #variable for option menu
    vehicle.set(OPTIONS[0])           # this is used to set options in variable
    OptionMenu(screen7, vehicle, *OPTIONS).pack() 
    # this is used to display option menu on screen
    Label(screen7,text="Vehicle Number",font=("bold",20),bg="grey").pack()
    Entry(screen7,bd=10,bg="pink",width=30,textvariable=vnum).pack()
    Button(screen7,text="Check Availability",bd=15,bg="cyan",command=parkin).pack()
    Button(screen7,text="Continue booking",bd=15,bg="cyan",command=bookin).pack()
def che2():

    Label(screen3,text="2 VIP and 10 normal Parking are available",font=("bold",20),bg="grey").pack()
    Label(screen3,text="",bg="grey").pack()
    Label(screen3,text="press 'BOOK' for booking or 'Menu' for Menu",font=("bold",20),bg="grey").pack()
    Button(screen3,text="BOOK",command=bo,bd=30,bg="cyan",font=("bold",15)).pack()
    Button(screen3,text="Menu",command=main_scree,bd=30,bg="cyan",font=("bold",15)).pack()
    

def che():
    f=open("svd.csv") # this is used to open the file and we have save it on f variable
    data=csv.reader(f) #we are reading our f file in data variable
    cp=1               
    #this is used for password it is 1 its means we have not check it yet
    cu=1
    #this is used for ussername it is 1 its means we have not check it yet
    
    for r in data:
        if(r[0]==t1.get()):
#r[0] is used for ussername in our csv file , here we are checking that is there is any user regitered with the name 
#which we have enter in login
            
            cu=0
#if yes then our cu will become 0 ,its means user is registed        
            if(r[1]==t2.get()):
# this is used to check the password
                
                cp=0
                
                break
    f.close()
    if(cu==1):  # cu will remain 1 ,it will show the following label
        Label(screen3,text="wrong ussername",font=("bold",20),bg="grey").pack()
    elif(cp==1):  # cp will remain 1 ,it will show the following label
        Label(screen3,text="incorrect password",font=("bold",20),bg="grey").pack()
    else:
        
        che2()  #if both pasword and ussername are correct ,this will work
def log():
    
    
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Login")
    screen3.configure(background="grey")
    global t1
    global t2
    t1=StringVar()
    t2=StringVar()
    Label(screen3,text="Login",font=("bold",40),bg="pink").pack()
    Label(screen3,text="",bg="grey").pack()
    Label(screen3,text="Ussername",font=("bold",25),bg="grey").pack()
    Entry(screen3,bd=5,textvariable=t1,bg="pink",width=30).pack()
    Label(screen3,text="",bg="grey").pack()
    Label(screen3,text="Password",font=("bold",25),bg="grey").pack()
    Entry(screen3,bd=5,textvariable=t2,show="*",bg="pink",width=30).pack()
    Label(screen3,text="",bg="grey").pack()
    Button(screen3,text="check availability",command=che,bg="cyan",font=("bold",15),bd=10).pack()
def bookin():
    if(vnum.get()==""):    # if usser will not enter the vehicle number then following label will work
        Label(screen7,text="Please fill vehicle number",font=("italic",20)).pack()
    else:
        global screen5
        screen5=Toplevel(screen)
        screen5.resizable(width=False, height=False)
        screen5.title("Booking")
        screen5.configure(background="grey")
        Label(screen5,text="Booking",font=("bold",30),bg="red").pack()
        
        if(vehicle.get()=="car"):  #this is used to check which vehicle we have choose
            
            Label(screen5,text="Select the type of parking for your car ",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="truck"): #this is used to check which vehicle we have choose
            
            Label(screen5,text="Select the type of parking for your truck",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="Two-wheeler"): #this is used to check which vehicle we have choose
            
            Label(screen5,text="Select the type of parking for your Two-wheeler",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="tractor"): #this is used to check which vehicle we have choose
            
            Label(screen5,text="Select the type of parking for your tractor",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="bus"): #this is used to check which vehicle we have choose
            
            Label(screen5,text="Select the type of parking for your bus",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        parking = ["VIP","Normal"] 
        global type
        type= StringVar()
        type.set(parking[0]) 
        OptionMenu(screen5, type, *parking).pack()
        global days
        days=StringVar()
        Label(screen5,text="Number of days you want to park your "+vehicle.get(),font=("italic",20),bg="grey").pack()
        Entry(screen5,bg="pink",bd=5,textvariable=days).pack()
        Label(screen5,text="",bg="grey").pack()
        Button(screen5,text="Price",bd=15,bg="cyan",command=price).pack()
        Label(screen5,text="",bg="grey").pack()
        Button(screen5,text="BOOK",bd=15,bg="cyan",command=final).pack()

def parkin():
    
    Label(screen7,text="2 VIP and 10 normal Parking are available",font=("italic",20),bg="grey").pack()
def boo():
        if(captcha.get()=="!@#$%"):  #this is used to check the captcha
            
            global screen7
            screen7=Toplevel(screen)
            screen7.title("booking")
            screen7.configure(background="grey")
            
            global vnum
            vnum=StringVar()
            Label(screen7,text="Booking",font=("bold",30),bg="pink").pack()
            Label(screen7,text="Vehicle Type",font=("bold",20),bg="grey").pack()
            OPTIONS = ["car","truck","tractor","bus","Two-wheeler"] 
            global vehicle
            vehicle= StringVar()
            vehicle.set(OPTIONS[0]) 
            OptionMenu(screen7, vehicle, *OPTIONS).pack()
            Label(screen7,text="Vehicle Number",font=("bold",20),bg="grey").pack()
            Entry(screen7,bd=10,bg="pink",width=30,textvariable=vnum).pack()
            Button(screen7,text="Check Availability",bd=15,bg="cyan",command=parkin).pack()
            Button(screen7,text="Continue booking",bd=15,bg="cyan",command=bookin).pack()
        else:
            Label(screen3,text="WRONG CAPTCHA",font=("bold",20),bg="grey").pack()
def chec2():
    global captcha
    captcha=StringVar()
    Label(screen3,text="CAPTCHA",font=("bold",20),bg="grey").pack()
    Label(screen3,text="!@#$%",font=("bold",20),bg="grey").pack()
    Entry(screen3,bg="pink",textvariable=captcha).pack()
    Button(screen3,text="SUBMIT",bd=15,bg="cyan",command=boo).pack()
def chec():
    f=open("svd.csv")
    data=csv.reader(f)
    cp=1
    cu=1
    
    for r in data:
        if(r[0]==t1.get()):
            
            cu=0
            
            if(r[1]==t2.get()):
                
                cp=0
                
                break
    f.close()
    if(cu==1):
        Label(screen3,text="wrong ussername",font=("bold",20),bg="grey").pack()
    elif(cp==1):
        Label(screen3,text="incorrect password",font=("bold",20),bg="grey").pack()
    else:
        
        chec2()
def final():
    screen6=Toplevel(screen)
    screen6.title("receipt")
    screen6.configure(background="grey")
    Label(screen6,text="THANK YOU FOR VISITING",font=("bold",30),bg="pink").pack()
    Label(screen6,text="You booked parking for "+ days.get()+ "day(s)",font=("bold",20),bg="grey").pack()
    Label(screen6,text="VEHICLE TYPE :- "+ vehicle.get(),font=("bold",20),bg="grey").pack()
    Label(screen6,text="PARKING TYPE :- "+ type.get() ,font=("bold",20),bg="grey").pack()
    Label(screen6,text="PRICE",font=("bold",20),bg="grey").pack()
    if(vehicle.get()=="car" and type.get()=="Normal"): # to check vehicle and parking type
        
        Label(screen6,text="Rs."+str(100*int(days.get())),font=("bold",20),bg="grey").pack()
    if((vehicle.get()=="bus" or vehicle.get()=="truck" or vehicle.get()=="tractor") and type.get()=="Normal"):
        # to check vehicle and parking type
        
        Label(screen6,text="Rs."+str(150*int(days.get())),font=("bold",20),bg="grey").pack()
    if(vehicle.get()=="Two-wheeler" and type.get()=="Normal"):
        # to check vehicle and parking type
        
        Label(screen6,text="Rs."+str(50*int(days.get())),font=("bold",20),bg="grey").pack()
    if(vehicle.get()=="car" and type.get()=="VIP"):
        # to check vehicle and parking type
        
        Label(screen6,text="Rs."+str(120*int(days.get())),font=("bold",20),bg="grey").pack()
    if((vehicle.get()=="bus" or vehicle.get()=="truck" or vehicle.get()=="tractor") and type.get()=="VIP"):
        # to check vehicle and parking type
        
        Label(screen6,text="Rs."+str(170*int(days.get())),font=("bold",20),bg="grey").pack()
    if(vehicle.get()=="Two-wheeler" and type.get()=="VIP"):
        # to check vehicle and parking type
        
        Label(screen6,text="Rs."+str(70*int(days.get())),font=("bold",20),bg="grey").pack()
    
    
    
    
    
    
def price():
    if(vehicle.get()=="car" and type.get()=="Normal"):
        # to check vehicle and parking type
        
        Label(screen5,text="              ",font=("bold",20),bg="red").place(x=360,y=250)
        
        # place is used to give the value of x and y axis where we want to place our widget
        
        Label(screen5,text="Rs."+str(100*int(days.get())),font=("bold",20),bg="red").place(x=360,y=250)
    if((vehicle.get()=="bus" or vehicle.get()=="truck" or vehicle.get()=="tractor") and type.get()=="Normal"):
        Label(screen5,text="              ",font=("bold",20),bg="red").place(x=360,y=250)
        Label(screen5,text="Rs."+str(150*int(days.get())),font=("bold",20),bg="red").place(x=360,y=250)
    if(vehicle.get()=="Two-wheeler" and type.get()=="Normal"):
        Label(screen5,text="              ",font=("bold",20),bg="red").place(x=360,y=250)
        Label(screen5,text="Rs."+str(50*int(days.get())),font=("bold",20),bg="red").place(x=360,y=250)
    if(vehicle.get()=="car" and type.get()=="VIP"):
        Label(screen5,text="              ",font=("bold",20),bg="red").place(x=360,y=250)
        Label(screen5,text="Rs."+str(120*int(days.get())),font=("bold",20),bg="red").place(x=360,y=250)
    if((vehicle.get()=="bus" or vehicle.get()=="truck" or vehicle.get()=="tractor") and type.get()=="VIP"):
        Label(screen5,text="              ",font=("bold",20),bg="red").place(x=360,y=250)
        Label(screen5,text="Rs."+str(170*int(days.get())),font=("bold",20),bg="red").place(x=360,y=250)
    if(vehicle.get()=="Two-wheeler" and type.get()=="VIP"):
        Label(screen5,text="              ",font=("bold",20),bg="red").place(x=360,y=250)
        Label(screen5,text="Rs."+str(70*int(days.get())),font=("bold",20),bg="red").place(x=360,y=250)
    
        
def book():
        if(captcha.get()=="!@#$%"):
            
            global screen4
            screen4=Toplevel(screen)
            screen4.title("booking")
            screen4.configure(background="grey")
            #screen4.geomatry('3000x400')
            global vnum
            vnum=StringVar()
            Label(screen4,text="Booking",font=("bold",30),bg="pink").pack()
            Label(screen4,text="Vehicle Type",font=("bold",20),bg="grey").pack()
            OPTIONS = ["car","truck","tractor","bus","Two-wheeler"] 
            global vehicle
            vehicle= StringVar()
            vehicle.set(OPTIONS[0]) 
            OptionMenu(screen4, vehicle, *OPTIONS).pack()
            Label(screen4,text="Vehicle Number",font=("bold",20),bg="grey").pack()
            Entry(screen4,bd=10,bg="pink",width=30,textvariable=vnum).pack()
            Button(screen4,text="Check Availability",bd=15,bg="cyan",command=parking).pack()
            Button(screen4,text="Continue booking",bd=15,bg="cyan",command=booking).pack()
        else:
            Label(screen2,text="WRONG CAPTCHA",font=("bold",20),bg="grey").pack()

def parking():
    
    Label(screen4,text="2 VIP and 10 normal Parking are available",font=("italic",20),bg="grey").pack()
def booking():
    if(vnum.get()==""):
        Label(screen4,text="Please fill vehicle number",font=("italic",20),bg="grey").pack()
    else:
        global screen5
        screen5=Toplevel(screen)
        screen5.resizable(width=False, height=False)
        screen5.title("Booking")
        screen5.configure(background="grey")
        Label(screen5,text="Booking",font=("bold",30),bg="pink").pack()
        
        if(vehicle.get()=="car"):
            
            Label(screen5,text="Select the type of parking for your car ",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="truck"):
            
            Label(screen5,text="Select the type of parking for your truck",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="Two-wheeler"):
            
            Label(screen5,text="Select the type of parking for your Two-wheeler",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="tractor"):
            
            Label(screen5,text="Select the type of parking for your tractor",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        if(vehicle.get()=="bus"):
            
            Label(screen5,text="Select the type of parking for your bus",font=("italic",20),bg="grey").pack()
            Label(screen5,text="Vehicle number :- " +vnum.get(),font=("italic",20),bg="grey").pack()
        parking = ["VIP","Normal"] 
        global type
        type= StringVar()
        type.set(parking[0]) 
        OptionMenu(screen5, type, *parking).pack()
        global days
        days=StringVar()
        Label(screen5,text="Number of days you want to park your "+vehicle.get(),font=("italic",20),bg="grey").pack()
        Entry(screen5,bg="pink",bd=5,textvariable=days).pack()
        Label(screen5,text="",bg="grey").pack()
        Button(screen5,text="Price",bd=15,bg="cyan",command=price).pack()
        Label(screen5,text="",bg="grey").pack()
        Button(screen5,text="BOOK",bd=15,bg="cyan",command=final).pack()
        
       

    
    
def check2():
    global captcha
    captcha=StringVar()
    Label(screen2,text="CAPTCHA",font=("bold",20),bg="grey").pack()
    Label(screen2,text="!@#$%",font=("bold",20),bg="grey").pack()
    Entry(screen2,bg="pink",textvariable=captcha).pack()
    Button(screen2,text="SUBMIT",bd=15,bg="cyan",command=book).pack()
    

        
    

def check():
    f=open("svd.csv")
    data=csv.reader(f)
    cp=1
    cu=1
    
    for r in data:
        if(r[0]==r1.get()):
            
            cu=0
            
            if(r[1]==r2.get()):
                
                cp=0
                
                break
    f.close()
    if(cu==1):
        Label(screen2,text="wrong ussername",font=("bold",20),bg="grey").pack()
    elif(cp==1):
        Label(screen2,text="wrong password",font=("bold",20),bg="grey").pack()
    else:
        
        check2()
    
 
    

def login():
        if(len(e2.get())<6):   #if password will be less then 6 charcterthen it will not work further 
            
            Label(screen1,text="Your password should have atleast 6 characters",font=("bold",20),fg="red",bg="grey").pack()
        else:           # else data will be saved in our file named svd(shubhi,vaibhav,devansh :\ )
            f=open("svd.csv","a+")    #open file in append mode
            f.write(e1.get()+","+e2.get())  #ussername , password will be saved 
            f.write("\n")     # for new line
            f.close()          # close file
           
   
            
           
            global screen2
            screen2=Toplevel(screen)
            screen2.title("Login")
            screen2.configure(background="grey")
            global r1
            global r2
            r1=StringVar()
            r2=StringVar()
            Label(screen2,text="Login",font=("bold",40),bg="pink").pack()
            Label(screen2,text="",bg="grey").pack()
            Label(screen2,text="Ussername",font=("bold",25),bg="grey").pack()
            Entry(screen2,bd=5,textvariable=r1,bg="pink",width=30).pack()
            Label(screen2,text="",bg="grey").pack()
            Label(screen2,text="Password",font=("bold",25),bg="grey").pack()
            Entry(screen2,bd=5,textvariable=r2,show="*",bg="pink",width=30).pack()
            Label(screen2,text="",bg="grey").pack()
            Button(screen2,text="login",command=check,bg="cyan",font=("bold",15),bd=10).pack()
    

    
    
    

def reg():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("registration ")
    screen1.configure(background="grey")
    global e1
    global e2
    global gender
    e1=StringVar()   #useername
    e2=StringVar()   #password
    
    Label(screen1,text="Registration Form",font=("bold",30),bg="pink").pack()
    Label(screen1,text="Name(ussername)*",font=("bold",20),bg="grey").pack()
    usser_entry=Entry(screen1,bd=5,textvariable=e1,bg="pink",width=30).pack()
    Label(screen1,text="Password*",font=("bold",20),bg="grey").pack()
    password_entry=Entry(screen1,bd=5,textvariable=e2,bg="pink",width=30).pack()
    Label(screen1,text="Phone Number",font=("bold",20),bg="grey").pack()
    Entry(screen1,bd=5,bg="pink",width=30).pack()
    Label(screen1,text="Email ID",font=("bold",20),bg="grey").pack()
    Entry(screen1,bd=5,bg="pink",width=30).pack()
    Label(screen1,text="Gender",font=("bold",20),bg="grey").pack()
    genders = ["male","female","others"] 
    global gender
    gender=StringVar()
    gender.set(genders[0]) 
    OptionMenu(screen1, gender, *genders).pack()
    Label(screen1,text="",bg="grey").pack()
    
    Button(screen1,text="register",command=login,bg="cyan",font=("bold",15),bd=10).pack()
    
def logi():   #login window
    
    
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Login")
    screen3.configure(background="grey")
    global t1
    global t2
    t1=StringVar()  #ussername
    t2=StringVar()  #password
    Label(screen3,text="Login",font=("bold",40),bg="pink").pack()
    Label(screen3,text="",bg="grey").pack()
    Label(screen3,text="Ussername",font=("bold",25),bg="grey").pack()
    Entry(screen3,bd=5,textvariable=t1,bg="pink",width=30).pack()
    Label(screen3,text="",bg="grey").pack()
    Label(screen3,text="Password",font=("bold",25),bg="grey").pack()
    Entry(screen3,bd=5,textvariable=t2,show="*",bg="pink",width=30).pack()
    Label(screen3,text="",bg="grey").pack()
    Button(screen3,text="login",command=chec,bg="cyan",font=("bold",15),bd=10).pack()
    
def avai():   #availability
    
    global screen8
    screen8=Tk()
    screen8.title("menu")
    screen8.configure(background="grey")
    Label(screen8,text="To Check availablity of parking",font=("bold",25),bg="pink").pack()
    Label(screen8,text="",bg="grey").pack()
    Button(screen8,text="Register",command=reg,bd=30,bg="cyan",font=("bold",15)).pack()
    Label(screen8,text="",bg="grey").pack()
    Label(screen8,text="already Member",font=("bold",25),bg="pink").pack()
    Label(screen8,text="",bg="grey").pack()
    Button(screen8,text="Login",command=log,bd=30,bg="cyan",font=("bold",15)).pack()
    
def main_screen():    # main window 
    
    global screen
    screen=Tk()
    screen.title("menu")
    screen.configure(background="grey")
    Label(screen,text="Welcome To Parking Management System",font=("bold",30),bg="pink").pack()
    Label(screen,text="",bg="grey").pack()
    Button(screen,text="Login",command=logi,bd=30,bg="cyan",font=("bold",15)).pack()
    Label(screen,text="",bg="grey").pack()
    Button(screen,text="Register",command=reg,bd=30,bg="cyan",font=("bold",15)).pack()
    Label(screen,text="",bg="grey").pack()
    Button(screen,text="Availability",command=avai,bd=30,bg="cyan",font=("bold",15)).pack()
    Label(screen,text="",bg="grey").pack()
   
main_screen()  # all the code is written b|w tkinter import* and main_screen()
