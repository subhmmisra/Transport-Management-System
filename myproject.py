


from Tkinter import *
import ttk
from random import *
import time
import sqlite3
from tkMessageBox import *

root=Tk()
#def login1():
conn=sqlite3.connect('myproject.db')
c=conn.cursor()
    


root.geometry('1366x768')
def home():
    #------------------how to get back to the home window ,using the home button--------------------------------------------------------------
    while True:
        try:
            b.title("Welcome Operator")
            button_1=Button(booking_frame4,text=" Booking ",font=('arial',15),bd=10,relief='raise',command=booking)
            button_2=Button(booking_frame4,text=" Enquiry ",font=('arial',15),bd=10,relief='raise',command=enquiry)
            button_3=Button(booking_frame4,text=" Delivery",font=('arial',15),bd=10,relief='raise',command=delivery)

            button_4=Button(booking_frame4,text="  Exit  ",font=('arial',15),bd=10,relief='raise')
            button_1.grid(row=5,column=1)
            button_2.grid(row=5,column=4)
            button_3.grid(row=5,column=5)
            button_4.grid(row=5,column=7,sticky=S)
            b.mainloop()
        except(SyntaxError,NameError):
            b.title("Welcome Operator")
            button_1=Button(booking_frame4,text=" Booking ",font=('arial',15),bd=10,relief='raise',command=booking)
            button_2=Button(booking_frame4,text=" Enquiry ",font=('arial',15),bd=10,relief='raise',command=enquiry)
            button_3=Button(booking_frame4,text=" Delivery",font=('arial',15),bd=10,relief='raise',command=dlivery)

            button_4=Button(booking_frame4,text="  Exit  ",font=('arial',15),bd=10,relief='raise')
            button_1.grid(row=5,column=1)
            button_2.grid(row=5,column=4)
            button_3.grid(row=5,column=5)
            button_4.grid(row=5,column=7,sticky=S)
            b.mainloop()
            
#---------------------------------------------------------delivery window-----------------------------------------------------------------------
def delivery():
    import dlivery


    
#-------------------------------------------------------booking window-----------------------------------------------------------------------------    
def booking():
    #c.execute("create table if not exists booking(cngr text ,origin text ,destination text,tin_no number ,gr_no number,permit_no number,issue_date varchar2,vehcile_no varchar2,driver_name text,driver_ph number,item_name text,item_weight number,fare_ number,advance_ number, labour_charge number, insurance_charge number)")
    book=Tk()
    book.geometry('1366x768')
    book.title('Booking')
    clock_frame=Frame(book)
    clock_frame.grid(row=0,column=0,sticky=W)#clock_frame ,row=0
    
    #book.focus()
    def rand1():
            a=randrange(1,190000);
            party_entry.insert(16,a)
            party_entry.configure(state='readonly')
        
    label_frame=Frame(book,relief='raise')
    label_frame.grid(row=1,column=0,sticky=W)
    label_party=Button(label_frame,text='Gr No.:*',font=('arial 15 bold'),command=rand1)
    label_party.grid(row=0,column=0,sticky=W)
    party_entry=Entry(label_frame,font=('arial 15'),bg='yellow')
    party_entry.grid(row=0,column=1,sticky=W)


    name_frame=Frame(book)
    name_frame.grid(row=2,column=0,sticky=W)#name_frame, row=2
    name_party=Label(name_frame,text='Cngr*            ',font=('arial 15 bold'))
    name_party.grid(row=0,column=0,sticky=W)
    name_entry=Entry(name_frame,font=('arial 15'),width=45)
    name_entry.grid(row=0,column=1,sticky=W)


    firm_party=Label(name_frame,text='     Firm*            ',font=('arial 15 bold'))
    firm_party.grid(row=0,column=2,sticky=E)
    firms_entry=Entry(name_frame,font=('arial 15'),width=45)
    firms_entry.grid(row=0,column=3,sticky=W)


    origin_frame=Frame(book)
    origin_frame.grid(row=3,column=0,sticky=W)#origin_frame, row=3
    origin_party=Label(origin_frame,text='Origin*          ',font=('arial 15 bold'))
    origin_party.grid(row=0,column=0,sticky=W)
    origin_entry=Entry(origin_frame,font=('arial 15'),width=45)
    origin_entry.grid(row=0,column=1,sticky=W)


    destination_party=Label(origin_frame,text='     Destination* ',font=('arial 15 bold'))
    destination_party.grid(row=0,column=2,sticky=W)
    destination_entry=Entry(origin_frame,font=('arial 15'),width=45)
    destination_entry.grid(row=0,column=3,sticky=W)


    firm_frame=Frame(book)
    firm_frame.grid(row=4,column=0,sticky=W)#firm_frame, row=4
    fir_party=Label(firm_frame,text='Item Name    ',font=('arial 15 bold'))
    fir_party.grid(row=0,column=0,sticky=W)
    frm_entry=Entry(firm_frame,font=('arial 15'),width=45)
    frm_entry.grid(row=0,column=1,sticky=W)
    firm_party=Label(firm_frame,text='     Tin No.         ',font=('arial 15 bold'))
    firm_party.grid(row=0,column=2,sticky=W)
    firm_entry=Entry(firm_frame,font=('arial 15'),width=45)
    firm_entry.grid(row=0,column=3,sticky=W)


    item_frame=Frame(book)
    item_frame.grid(row=5,column=0,sticky=W)#item_frame, row=5
    item_party=Label(item_frame,text='Item Weight* ',font=('arial 15 bold'))
    item_party.grid(row=0,column=0,sticky=W)
    item_entry=Entry(item_frame,font=('arial 15'),width=45)
    item_entry.grid(row=0,column=1,sticky=W)
    type_party=Label(item_frame,text='     Item type*    ',font=('arial 15 bold'))
    type_party.grid(row=0,column=2,sticky=W)
    type_entry=ttk.Combobox(item_frame,font=('arial 15'),width=43,state='readonly')
    type_entry['values']=['SELECT','Clothing','Spices','Iron Ore','Machine']
    type_entry.current(0)
    type_entry.grid(row=0,column=3,sticky=W)


    p=IntVar()
    p.set(0)
    permit_frame=Frame(book)
    permit_frame.grid(row=6,column=0,sticky=W)#permit_frame, row=6
    permit_label=Label(permit_frame,text='Permit',font=('arial 15 bold'))
    permit_label.grid(row=0,column=0,sticky=W)
    rd_button=Radiobutton(permit_frame,text='Yes',variable=p,value=0,font=('arial 15 bold'))
    rd_button.grid(row=0,column=1,sticky=W)
    rd2_button=Radiobutton(permit_frame,text='No',variable=p,value=1,font=('arial 15 bold'))
    rd2_button.grid(row=0,column=2,sticky=W)
    permit_party=Label(permit_frame,text='Permit No.    ',font=('arial 15 bold'))
    permit_party.grid(row=1,column=0,sticky=W)
    permit_entry=Entry(permit_frame,font=('arial 15'),width=45)
    permit_entry.grid(row=1,column=1,sticky=W)
    date_party=Label(permit_frame,text='     Issue Date   ',font=('arial 15 bold'))
    date_party.grid(row=1,column=2,sticky=W)
    date_entry=Entry(permit_frame,font=('arial 15'),width=45)
    date_entry.grid(row=1,column=3,sticky=W)


    vehicle_frame=Frame(book)
    vehicle_frame.grid(row=7,column=0,sticky=W)#vehcile_frame,row=7
    vehcile_detail=Label(vehicle_frame,text='Vehcile Details',font=('arial 15 bold'),relief='sunken',width=112)
    vehcile_detail.grid(row=0,column=0)
    veh_frame=Frame(book)
    veh_frame.grid(row=8,column=0,sticky=W)#vehcile_frame,row=8
    veh_no=Label(veh_frame,text='Vehcile No.* ',font=('arial 15 bold'))
    veh_no.grid(row=0,column=0,sticky=W)
    veh_entry=Entry(veh_frame,font=('arial 15'),width=45)
    veh_entry.grid(row=0,column=1,sticky=W)
    dr_name=Label(veh_frame,text='     Driver Name* ',font=('arial 15 bold'))
    dr_name.grid(row=0,column=2,sticky=W)
    dr_entry=Entry(veh_frame,font=('arial 15'),width=45)
    dr_entry.grid(row=0,column=3,sticky=W)
    dr_ph_label=Label(veh_frame,text='Driver Ph.*',font=('arial 15 bold'))
    dr_ph_label.grid(row=2,column=0,sticky=W)
    dr_ph_entry=Entry(veh_frame,font=('arial 15 '),width=45)
    dr_ph_entry.grid(row=2,column=1)


    payment_frame=Frame(book)
    payment_frame.grid(row=9,column=0,sticky=W)#payment_frame,row=9
    payment_label=Label(payment_frame,text='Payment details',font=('arial 15 bold'),relief='sunken',width=112)
    payment_label.grid(row=0,column=0)

    fare_frame=Frame(book)
    fare_frame.grid(row=10,column=0,sticky=W)#payment_frame, row=10
    fare_label=Label(fare_frame,text='Fare*          ',font=('arial',15,'bold'))
    #v=StringVar()
    #v.set('0')
    #a=IntVar()
    #a.set('0')



    fare_label.grid(row=0,column=0,sticky=W)
    advance_label=Label(fare_frame,text='       Advance   ',font=('arial',15,'bold'))
    advance_label.grid(row=0,column=2,sticky=W)
    advance_entry=Entry(fare_frame,font=('arial',15),justify='right',width=41)
    advance_entry.grid(row=0,column=5,sticky=W)
    fare_entry=Entry(fare_frame,font=('arial',15),justify='right',width=50)
    fare_entry.grid(row=0,column=1,sticky=W)


    sales_frame=Frame(book,bd=5)
    sales_frame.grid(row=13,column=0,sticky=W)#sales_frame row=13 delivery
    sales_button=Label(sales_frame,text='Sales Tax   ',font=('arial',15,'bold'),justify='right')
    sales_button.grid(row=0,column=0,sticky=W)
    sales_entry=Entry(sales_frame,font=('arial',15),justify='right',width=50)
    sales_entry.grid(row=0,column=1,sticky=W)


    vat_frame=Frame(book,bd=5)
    vat_frame.grid(row=12,column=0,sticky=W)#vat_frame row=12,delivery
    vat_label=Label(vat_frame,text='VAT            ',font=('arial',15,'bold'))
    vat_label.grid(row=0,column=0,sticky=W)
    v8=StringVar()

    #v8.set('my name')

    vat_entry=Entry(vat_frame,font=('arial',15),justify='right',width=50)

    #vat_entry.bind('<Button-1>',fun)


    vat_entry.grid(row=0,column=1,sticky=W)


    total_frame=Frame(book,bd=5)
    total_frame.grid(row=14,column=0,sticky=W)#total frame row=14,delivery
    total_label=Label(total_frame,text='Grand Total',font=('arial',15,'bold'))
    total_label.grid(row=0,column=0,sticky=W)
    total_entry=Entry(total_frame,font=('arial',15),width=50,justify='right')
    total_entry.grid(row=0,column=1,sticky=W)
    due_label=Label(total_frame,text='      Due ',font=('arial',15,'bold'))
    due_label.grid(row=0,column=2,sticky=E)
    due_entry=Entry(total_frame,width=50,font=('arial',15),justify='right')
    due_entry.grid(row=0,column=3,sticky=W)


    #due_frame=Frame(delivery,bd=5)
    #due_frame.grid(row=12,column=0,sticky=W)
    #labr=IntVar()
    #gate=IntVar()
    #insurance=IntVar()
    #labr.set('0')
    #gate.set('0')
    #insurance.set('0')
             
    other_charges_frame=Frame(book)
    other_charges_frame.grid(row=11,sticky=N+W+E+S) # other_charges_frame row=14,delivery
    other_Labour_charge=Label(other_charges_frame,text='Other Charges',width=15,font=('arial 15 bold underline'),relief='sunken' ,bd=5)
    other_Labour_charge.grid(row=0,column=0,sticky=N+W+E+S)
    other_Labour_charge1=Label(other_charges_frame,text='Amount',width=10,font=('arial 15 bold underline'),relief='sunken' ,bd=5)
    other_Labour_charge1.grid(row=0,column=1,sticky=N+W+E+S)
    other_Labour_charge=Label(other_charges_frame,text='Labour Charges',width=15,font=('arial 15 bold'),relief='sunken' ,bd=5)
    other_Labour_charge.grid(row=1,column=0,sticky=N+W+E+S)
    labour_entry=Entry(other_charges_frame,width=15,font=('arial 15'),relief='sunken' ,bd=5,justify='right')
    labour_entry.grid(row=1,column=1)
    gatepass_charge=Label(other_charges_frame,text='Gatepass Charges',width=15,font=('arial 15 bold'),relief='sunken' ,bd=5)
    gatepass_charge.grid(row=2,column=0,sticky=N+W+E+S)
    gatepass_entry=Entry(other_charges_frame,width=15,font=('arial 15 '),relief='sunken' ,bd=5,justify='right')
    gatepass_entry.grid(row=2,column=1)
    insurance_charge=Label(other_charges_frame,text='Insurance Charge',width=15,font=('arial 15 bold'),relief='sunken' ,bd=5)
    insurance_charge.grid(row=3,column=0,sticky=N+W+E+S)
    insurance_entry=Entry(other_charges_frame,width=15,font=('arial 15'),relief='sunken' ,bd=5,justify='right')
    insurance_entry.grid(row=3,column=1)

    #------------------------------------------------------------DATABASE-----------------------------------------------------------------

    #c.execute("create table if not exists booking(cngr text ,origin text ,destination text,tin_no number ,gr_no number,permit_no number,issue_date varchar2,vehcile_no varchar2,driver_name text,driver_ph number,item_name text,item_weight number,fare_ number,advance_ number, labour_charge number, insurance_charge number)")

    #c.execute('insert into booking values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[(name_entry.get()),(origin_entry.get()),(destination_entry.get()),(firm_entry.get()),(party_entry.get()),(permit_entry.get()),(date_entry.get()),(veh_entry.get()),(dr_entry.get()),(dr_ph.get()),])
    def book1():
        c.execute("create table if not exists booking(cngr text ,origin text ,destination text,tin_no number ,gr_no number,permit_no number,issue_date varchar2,vehcile_no varchar2,driver_name text,driver_ph number,item_name text,item_weight number,fare_ number,advance_ number, labour_charge number, insurance_charge number)")
        c.execute('insert into booking values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[(name_entry.get()),(origin_entry.get()),(destination_entry.get()),(firm_entry.get()),(party_entry.get()),(permit_entry.get()),(date_entry.get()),(veh_entry.get()),(dr_entry.get()),(dr_ph_entry.get()),(frm_entry.get()),(item_entry.get()),(fare_entry.get()),(advance_entry.get()),(labour_entry.get()),(insurance_entry.get())])
        conn.commit()
        if name_entry.get()==''or origin_entry.get()=='' or destination_entry.get()=='' or party_entry.get()=='' or veh_entry.get()=='' or dr_entry.get()=='' or dr_ph_entry.get()==''or item_entry.get()=='' or fare_entry.get()=='' :
            showinfo('Warning','* marked entries are mandatory to fill')
        
            
        else:
            bill()
        
        
    #b.focus_set(b)
#(name_entry.get()),(origin_entry.get()),(destination_entry.get()),(firm_entry.get()),(party_entry.get()),(permit_entry.get()),(date_entry.get()),(veh_entry.get()),(dr_entry.get()),(dr_ph_entry.get()),(frm_entry.get()),(item_entry.get()),(fare_entry.get()),(advance_entry.get()),(labour_entry.get()),(insurance_entry.get())

    def bill():
        
        bill=Tk()
        bill.geometry('500x300')
        t=Text(bill,font=('arial 15 bold'),width=300,height=300,bg='light yellow')
        t.insert(END,"\t\t  The Mishra's Enterprise\n")
        t.insert(END,'__________________________________________________')
        t.insert(END,'\n|Gr_No|     :\t'+party_entry.get(),'\n')
        t.insert(END,'\n|Consigner Name|:'+name_entry.get())
        t.insert(END,'\n|Firm Name|         :'+firms_entry.get(),'\n')
        t.insert(END,'\n|Origin|                :'+origin_entry.get()+'\t\t\t')
        t.insert(END,'|Destination|   :'+destination_entry.get())
        t.insert(END,'\n|Item Name|         :'+frm_entry.get()+'\t\t\t'+"|Item Weight|  :\t"+item_entry.get())
        t.insert(END,'\n|Permit No|          :'+permit_entry.get()+'\t\t\t'+'|Permit Date|  :\t'+date_entry.get())
        t.insert(END,'\n|Vehcile No|         :'+veh_entry.get()+'\t\t\t'+"|Driver's Ph.|  :\t"+dr_ph_entry.get())
        t.insert(END,'\n|fare|                    :'+fare_entry.get()+'\t\t\t'+"|Advance Amt|:\t"+advance_entry.get())
        t.insert(END,'\n|Labour Charge|   :'+labour_entry.get()+'\t\t\t'+"|Insurance|     :\t"+insurance_entry.get())
        t.insert(END,'\n_____________________________________________________')
        t.insert(END,'\n|GRAND TOTAL|  :'+total_entry.get()+'\t\t\t'+"|DUE Amount|.:\t"+due_entry.get())
        t.grid(row=0,column=0)
        bill.mainloop()    
    button_frame=Frame(book)
    button_frame.grid(row=15,sticky=W)#button_frame row=15
    print_reciept=Label(button_frame,width=85,font=('arial 15 bold underline'),relief='raise')
    print_reciept.grid(row=0,column=0,sticky=W)
    #bill_button=Button(button_frame,text='Print',command=bill)
    #bill_button.grid(row=0,column=1)
    total_button=Button(button_frame,text='Total',font=('arial 15 bold underline'),relief='raise',bd=5)
    total_button.grid(row=0,column=2,sticky=W)
    book_button=Button(button_frame,text='Book',bg='powder blue',font=('arial 15 bold underline'),relief='raise',bd=5,command=book1)
    book_button.grid(row=0,column=3,sticky=W)
    def canclebook():
        book.withdraw()
    cancle_button=Button(button_frame,text='Cancel',bg='red',font=('arial 15 bold underline'),relief='raise',bd=5,command=canclebook)
    cancle_button.grid(row=0,column=4,sticky=W)


    mainloop()
#####*************************************************************************************************************************************************#########


    
#--------------------------------------------------------------enquiry window setup------------------------------------------------
def enquiry():
    import enquiry
    
    
#---------------------------------------------step2 login------------------------------------------------------
def login():#function to close the login windwo and to open the new window simultaneously
    u=StringVar()
    p=StringVar()

    e1=StringVar()
    e2=StringVar()
    e1=entry1.get()
    e2=entry2.get()
    conn=sqlite3.connect('myproject.db')
    c=conn.cursor()
    #c.execute("CREATE TABLE IF NOT EXISTS project(username text CONSTRAINT name_ NOT NULL,password text CONSTRAINT pass_ NOT NULL)")#(u'mishra',)

    
    #c.executemany('insert into project values(?,?)',[(entry1.get(),entry2.get())])
    #conn.commit()
    c.execute('select username from project')
    u=c.fetchone()
    c.execute('select password from project')
    p=c.fetchone()
    #print p
    #print u
    
    if e1=='':
        showerror('Error ID','username cannot be empty')
    elif e2=='':
        showerror('Error Paassword','password cannot be empty')
    
    elif e2==p[0]and e1==u[0]:#and v.get()==1:
        root.destroy()
        b=Tk()
        b.geometry('1368x794')
        localtime=time.asctime(time.localtime(time.time()))
        l2=Label(b,text=localtime,font=('Arial','15','bold'),fg='Steel Blue')
        l2.place(relx=0,rely=0)
        booking_frame4=Frame(b,width=1600,height=800,bg='floral white')
        booking_frame4.pack()
    
        
        #fname=Canvas(bg='black',height=600,width=900)
        #fname.grid(row=2,column=0)
#------------------------------------------------------------------image------------------------------------------------------------------------------------
        a=PhotoImage(file='Air-Road-Silver.gif')
        l=Label(booking_frame4,image=a)
        l.grid(row=0)
        #image='12A1421'.create_image(image=a)
#------------------------------------------------------------------image--------------------------------------------------------------------------------------        
        bt_frame=Frame(booking_frame4)
        bt_frame.grid(row=0,column=1)
        b.title("Welcome Operator")
        button_1=Button(b,text=" Booking    ",font=('arial',15),bd=10,relief='raise',command=booking,bg='blue')
        button_2=Button(b,text=" Enquiry    ",font=('arial',15),bd=10,relief='raise',command=enquiry)
        button_3=Button(b,text=" Delivery   ",font=('arial',15),bd=10,relief='raise',command=delivery)
        def exit1():
            b.withdraw()
        button_4=Button(b,text="     Exit     ",font=('arial',15),bd=10,relief='raise',command=exit1)
        button_1.place(relx=0,rely=0.75)
        button_2.place(relx=0.45,rely=0.75)
        button_3.place(relx=0.9,rely=0.75)
        button_4.place(relx=0.45,rely=0.83)
        b.mainloop()
    #elif e2==p[0]and e1==u[0]:#and v.get()==2:
#-----------------------------------------------------------------manager login window-------------------------------------------------------------------------------------
        #v.get()==2#if manager will login
        #root.destroy()
        #m=Tk()
        #m.title("Welcome Manager")
##        m.geometry('1368x794')
##        booking_frame5=Frame(m,width=1600,height=800,bd=10,relief='raise',bg='powder blue')
##        booking_frame5.grid(row=2,column=1,sticky=N)
##    
##        localtime=time.asctime(time.localtime(time.time()))
##        l2=Label(m,text=localtime,font=('Arial','15','bold'),fg='Steel Blue')
##        l2.grid(row=1,column=0,sticky=W)
##        #fname=Canvas(bg='black',height=600,width=900)
##        #fname.grid(row=2,column=0)
##
##        #a=PhotoImage(file='12A1421.gif')
##        #image=fname.create_image(image=a)
##        #Label(m,image=a).grid(row=4,column=0)
##        
##        m.title("Welcome Manager")
##        button_1=Button(booking_frame5,text=" Booking ",font=('arial',15),bd=10,relief='raise',command=booking)
##        button_2=Button(booking_frame5,text=" Enquiry ",font=('arial',15),bd=10,relief='raise',command=enquiry)
##        button_3=Button(booking_frame5,text=" Delivery",font=('arial',15),bd=10,relief='raise')
##
##        button_4=Button(booking_frame5,text="  Exit  ",font=('arial',15),bd=10,relief='raise')
##        button_1.grid(row=5,column=1)
##        button_2.grid(row=5,column=4)
##        button_3.grid(row=5,column=5)
##        button_4.grid(row=5,column=7,sticky=S)
##        
##        c1=Button(booking_frame5,text="Salary details",font=('arial',15),bd=10,relief='raise')
##        c2=Button(booking_frame5,text="Market Dues",font=('arial',15),bd=10,relief='raise')
##        c1.grid(row=1,column=5)
##        c2.grid(row=1,column=6)
    else:showerror('Error','Incorrect username/password')
    
#------------------------------------------------------------------quite function---------------------------------------------------------------------------------------

def quite():#function for the quite button
    abx=askyesno('Quit','Are you sure you want to quit')
    if abx>0:
        root.destroy()
        return
#---------------------------------------------------------------------root window  setup-----------------------------------------------------------------------------

localtime=time.asctime(time.localtime(time.time()))
l2=Label(root,text=localtime,font=('Arial','15','bold'),fg='Steel Blue')
l2.place(relx=0,rely=0)

f1=Frame(root)
f1.place(relx=0.02,rely=0.038)
l1=Label(f1,text="Welcome to The Mishra Enterprise ",font=('arial','40','bold'),fg='cornflower blue',bd=5,width=40,relief='raise')
l1.grid(row=0,column=0)
f3=Frame(root,width=1600,height=400,bd=10,relief='raise',)
f3.place(relx=0.32,rely=0.32)
username=Label(f3,text="Username",font=('arial','20','bold'))#username entered by the user
username.grid(row=4,column=0,sticky=E)
password=Label(f3,text="Password",font=('arial','20','bold'))#password entered by the user
password.grid(row=5,column=0,sticky=E)
entry1=Entry(f3,font=('arial','20','bold'),insertwidth=4,bg='light blue',bd=8)
entry2=Entry(f3,font=('arial','20','bold'),insertwidth=4,bg='powder blue',bd=8,show='*')
entry1.grid(row=4,column=1,sticky=E)
entry2.grid(row=5,column=1,sticky=E)
button1=Button(f3,text="login",font=('arial',18),bd=5,command=login,cursor='hand2')#login button
button2=Button(f3,text="Quit",font=('arial',18),bd=5,command=quite)#quite button
button1.grid(row=8,column=0,sticky=W)
button2.grid(row=8,column=1,sticky=E)
v=IntVar()

#v.set(1)
#operator=[("Office",1),("Manager",2)]
#l3=Label(f3,text="operator:",font=('arial',15))
#l3.grid(row=7,column=0)
#def show(): checking the radiobutton
 #   print v.get()
#rb1=Radiobutton(f3,text="Office",variable=v,value=1,font=('arial',15))
#rb2=Radiobutton(f3,text="Manager",variable=v,value=2,font=('arial',15))
#rb1.grid(row=7,column=1,sticky=W)
#rb2.grid(row=7,column=1,sticky=E)
def devlop():
        devlop1=Tk()
        devlop1.geometry('500x200')
        t=Text(devlop1,font=('arial 15 bold'),width=45,height=7,bg='orchid')
        t.insert(END,"\t     Devloper's Information\t")
        t.insert(END,'\nName::Mangalam Mishra')
        t.insert(END,'\nEnroll::151403'+'\t\t\t\tBatch::B6')
        t.insert(END,'\nBranch::CSE')
        t.insert(END,'\nEmail::subhmmisra0309@gmail.com')
        t.insert(END,'\nContact No::786919331')
        t.insert(END,'\ncopyright@2016')
       
        t.place(relx=0,rely=0.07)
        #t.configure(state='readonly')
        devlop1.after(3000,lambda:devlop1.destroy())
        devlop1.mainloop()
        
devloper_frame=Frame(root)
devloper_frame.place(relx=0.88,rely=0)
d_Button=Button(devloper_frame,text='@devloper',font=('arial 12 italic underline'),fg='red',command=devlop,bd=0)
d_Button.pack()
#============================================login function========================================================


root.mainloop()
