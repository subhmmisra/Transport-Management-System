

from Tkinter import *
import time
import sqlite3
conn=sqlite3.connect('myproject.db')
c=conn.cursor()

delivery=Tk()
delivery.title('Delivery')
delivery.geometry('1600x800+0+0')
localtime=time.asctime(time.localtime(time.time()))############# time modeule

time_display=Label(delivery,text=localtime,font=('Arial','15','bold'),fg='Steel Blue')

time_display.grid(row=0,column=0,sticky=W)###### time display
A1=StringVar()
B1=StringVar()
C1=StringVar()
D1=StringVar()
E1=StringVar()
F1=IntVar()

x=IntVar()
y=StringVar()
z=StringVar()
w=StringVar()
o=StringVar()
p=StringVar()
q=StringVar()
G1=StringVar()
H1=StringVar()
def gr(s):
    try:   
        c.execute('select gr_no from booking where gr_no=?',[(gr_entry.get())])
        x=c.fetchone()
        if s==str(x[0]):
            c.execute('select cngr from booking where gr_no=?',[(gr_entry.get())])
            y=c.fetchone()
            c.execute('select origin from booking where gr_no=?',[(gr_entry.get())])
            z=c.fetchone()
            c.execute('select destination from booking where gr_no=?',[(gr_entry.get())])
            w=c.fetchone()
            c.execute('select item_weight from booking where gr_no=?',[(gr_entry.get())])
            o=c.fetchone()
            c.execute('select item_name from booking where gr_no=?',[(gr_entry.get())])
            p=c.fetchone()
            c.execute('select fare_ from booking where gr_no=?',[(gr_entry.get())])
            q=c.fetchone()
            #A.set('hi')
            A1.set(y)
            B1.set(z)
            C1.set(w)
            D1.set(o)
            E1.set(p)
            F1.set(q[0])
            G1.set('Available in godown no. 5                                                   ' )
            H1.set('######              ')
            print q[0]
            
        elif s=='':
            G1.set('#############')  
        else:
            G1.set('Not yet arrived')
            A1.set('******************************')
            B1.set('******************************')
            C1.set('******************************')
            D1.set('******************************')
            E1.set('******************************')
            F1.set('******************************')
    
    except(TypeError):
        G1.set('Not yet arrived                                                        ')
        A1.set('******************************')
        B1.set('******************************')
        C1.set('******************************')
        D1.set('******************************')
        E1.set('******************************')
        F1.set('******************************')

        #return None
     
gr_frame=Frame(delivery,relief='raise',bd=5)
gr_frame.grid(row=1,column=0,sticky=W)## grframe ,row=1 delivery
gr_entry=Entry(gr_frame,font=('arial',15,'bold'),width=30,bg='yellow')
gr_entry.grid(row=0,column=1,sticky=W)
s=gr_entry.get()

gr_label=Button(gr_frame,text='GR No.     ',font=('arial',15,'bold'),height=0,command=lambda:gr(gr_entry.get()))
gr_label.grid(row=0,column=0,sticky=W)

status_frame=Frame(delivery,bd=5)
status_frame.grid(row=2,column=0,sticky=W)## status frame row=2 delivery
status_label=Label(status_frame,text='Status        ',font=('arial',15,'bold'))
status_label.grid(row=0,column=0,sticky=W)
status_entry=Entry(status_frame,font=('arial',15),justify='right',width=104,textvariable=G1)
status_entry.grid(row=0,column=1,sticky=W)


booking_frame=Frame(delivery,bd=5)
booking_frame.grid(row=3,column=0,sticky=W)##booking_frame row=3 delivery
booking_label=Label(booking_frame,text='Booking_Dt',font=('arial',15,'bold'))
booking_label.grid(row=0,column=0,sticky=W)
booking_entry=Entry(booking_frame,font=('arial',15,'bold'),width=32)
booking_entry.grid(row=0,column=1,sticky=W)
shipper_label=Label(booking_frame,text='Shipper',font=('arial',15,'bold'))
shipper_label.grid(row=0,column=2,sticky=W)
shipper_entry=Entry(booking_frame,font=('arial',15),width=30,textvariable=H1,justify='right')
shipper_entry.grid(row=0,column=3,sticky=W)
cngr_label=Label(booking_frame,text='Cngr',font=('arial',15,'bold'))
cngr_label.grid(row=0,column=4,sticky=W)
cngr_entry=Entry(booking_frame,font=('arial',15),justify='right',width=29,textvariable=A1)
cngr_entry.grid(row=0,column=5,sticky=W)


good_frame=Frame(delivery,bd=5)
good_frame.grid(row=4,column=0,sticky=W)## good_frame row=4 delivery
good_label=Label(good_frame,text='Good          ',font=('arial',15,'bold'))
good_label.grid(row=0,column=0,sticky=W)
good_entry=Entry(good_frame,font=('arial',15),justify='right',width=65,textvariable=E1)
good_entry.grid(row=0,column=1,sticky=W)
value_label=Label(good_frame,text='value',font=('arial',15,'bold'))
value_label.grid(row=0,column=2,sticky=W)
value_entry=Entry(good_frame,font=('arial',15),justify='right',width=33,textvariable=D1)
value_entry.grid(row=0,column=3,sticky=W)


from_frame=Frame(delivery,bd=5)
from_frame.grid(row=5,column=0,sticky=W)## from_frame row=5 delivery
from_label=Label(from_frame,text='From          ',font=('arial',15,'bold'))
from_label.grid(row=0,column=0,sticky=W)
from_entry=Entry(from_frame,font=('arial',15),width=51,textvariable=B1)
from_entry.grid(row=0,column=1,sticky=W)
to_label=Label(from_frame,text='To',font=('arial',15,'bold'))
to_label.grid(row=0,column=2,sticky=W)
to_entry=Entry(from_frame,font=('arial',15),justify='right',width=50,textvariable=C1)
to_entry.grid(row=0,column=3,sticky=W)


type_frame=Frame(delivery,bd=5)
type_frame.grid(row=6,sticky=W)## type_frame row=6 delivery
type_label=Label(type_frame,text='Delivery Type',font=('arial',15,'bold'))
type_label.grid(row=0,column=0,sticky=W)
s=IntVar()
s.set(1)

type_radiobutton=Radiobutton(type_frame,text='Godown Delivery',value=1,variable=s,font=('arial',15,'bold'))
type_radiobutton.grid(row=0,column=1,sticky=W)
type_radiobutton2=Radiobutton(type_frame,text='Home Delivery',value=2,variable=s,font=('arial',15,'bold'))
type_radiobutton2.grid(row=0,column=2,sticky=W)

#############################################################    payment functions   #############################################################################################
#def fun(event):
 #   vat_entry.configure(fg='black')
  #  vat_entry.delete(0,END)

f=IntVar()
f1=IntVar()
sales=IntVar()
g_t=StringVar
t=StringVar()
w=StringVar()
p=StringVar()
g=IntVar()
def f():
    try:
        
        f=int(fare_entry.get())
        g=int(((f)*5)/100)
        f1.set(str(g))
        h=int((int(f)*10)/100)
        sales.set(h)
        g_t=int(int(fare_entry.get())+int(h)+int(g)+int(labour_entry.get())+int(gatepass_entry.get())+int(insurance_entry.get()))
        t.set(g_t)
        p=int(int(g_t))-(int(advance_entry.get()))
        w.set(p)
    except(ValueError):
        return None
    


#----------------------------------------------------------payment--------------------------------------------------------------------
payment_frame=Frame(delivery,bd=5)
payment_frame.grid(row=7,column=0,sticky=W)## payment_frame row=7,column=0
payment_label=Label(payment_frame,text='Payment',font=('arial',15,'bold'),width=112,relief='sunken')
payment_label.grid(row=0,column=0,sticky=W)


fare_frame=Frame(delivery,bd=5)
fare_frame.grid(row=8,column=0,
                sticky=W)
fare_label=Label(fare_frame,text='Fare           ',font=('arial',15,'bold'))
v=StringVar()
v.set('0')
a=IntVar()
a.set('0')



fare_label.grid(row=0,column=0,sticky=W)
advance_label=Label(fare_frame,text='       Advance   ',font=('arial',15,'bold'))
advance_label.grid(row=0,column=2,sticky=W)
advance_entry=Entry(fare_frame,font=('arial',15),textvariable=a,justify='right',width=41)
advance_entry.grid(row=0,column=5,sticky=W)
fare_entry=Entry(fare_frame,font=('arial',15),textvariable=F1,justify='right',width=50)
fare_entry.grid(row=0,column=1,sticky=W)


sales_frame=Frame(delivery,bd=5)
sales_frame.grid(row=11,column=0,sticky=W)#sales_frame row=9 delivery
sales_button=Label(sales_frame,text='Sales Tax   ',font=('arial',15,'bold'),justify='right')
sales_button.grid(row=0,column=0,sticky=W)
sales_entry=Entry(sales_frame,font=('arial',15),textvariable=sales,justify='right',width=50)
sales_entry.grid(row=0,column=1,sticky=W)


vat_frame=Frame(delivery,bd=5)
vat_frame.grid(row=10,column=0,sticky=W)#vat_frame row=10,delivery
vat_label=Label(vat_frame,text='VAT            ',font=('arial',15,'bold'))
vat_label.grid(row=0,column=0,sticky=W)
v8=StringVar()

#v8.set('my name')

vat_entry=Entry(vat_frame,font=('arial',15),justify='right',width=50,textvariable=f1)

#vat_entry.bind('<Button-1>',fun)


vat_entry.grid(row=0,column=1,sticky=W)


total_frame=Frame(delivery,bd=5)
total_frame.grid(row=12,column=0,sticky=W)#total frame row=11,delivery
total_label=Label(total_frame,text='Grand Total',font=('arial',15,'bold'))
total_label.grid(row=0,column=0,sticky=W)
total_entry=Entry(total_frame,font=('arial',15),width=50,textvariable=t,justify='right')
total_entry.grid(row=0,column=1,sticky=W)
due_label=Label(total_frame,text='      Due ',font=('arial',15,'bold'))
due_label.grid(row=0,column=2,)
due_entry=Entry(total_frame,width=50,font=('arial',15),textvariable=w,justify='right')
due_entry.grid(row=0,column=3,sticky=W)


#due_frame=Frame(delivery,bd=5)
#due_frame.grid(row=12,column=0,sticky=W)
labr=IntVar()
gate=IntVar()
insurance=IntVar()
labr.set('0')
gate.set('0')
insurance.set('0')
         
other_charges_frame=Frame(delivery)
other_charges_frame.grid(row=9,sticky=N+E+W+S) # other_charges_frame row=12,delivery
other_Labour_charge=Label(other_charges_frame,text='Other Charges',width=15,font=('arial 15 bold underline'),relief='sunken' ,bd=5)
other_Labour_charge.grid(row=0,column=0,sticky=N+W+E+S)
other_Labour_charge1=Label(other_charges_frame,text='Amount',width=10,font=('arial 15 bold underline'),relief='sunken' ,bd=5)
other_Labour_charge1.grid(row=0,column=1,sticky=N+W+E+S)
other_Labour_charge=Label(other_charges_frame,text='Labour Charges',width=15,font=('arial 15 bold'),relief='sunken' ,bd=5)
other_Labour_charge.grid(row=1,column=0,sticky=N+W+E+S)
labour_entry=Entry(other_charges_frame,width=15,font=('arial 15'),relief='sunken' ,bd=5,justify='right',textvariable=labr)
labour_entry.grid(row=1,column=1)
gatepass_charge=Label(other_charges_frame,text='Gatepass Charges',width=15,font=('arial 15 bold'),relief='sunken' ,bd=5)
gatepass_charge.grid(row=2,column=0,sticky=N+W+E+S)
gatepass_entry=Entry(other_charges_frame,width=15,font=('arial 15 '),relief='sunken' ,bd=5,justify='right',textvariable=gate)
gatepass_entry.grid(row=2,column=1)
insurance_charge=Label(other_charges_frame,text='Insurance Charge',width=15,font=('arial 15 bold'),relief='sunken' ,bd=5)
insurance_charge.grid(row=3,column=0,sticky=N+W+E+S)
insurance_entry=Entry(other_charges_frame,width=15,font=('arial 15'),relief='sunken' ,bd=5,justify='right',textvariable=insurance)
insurance_entry.grid(row=3,column=1)


button_frame=Frame(delivery)
button_frame.grid(row=13,sticky=W)
print_reciept=Label(button_frame,text='',width=85,font=('arial 15 bold underline'),relief='raise')
print_reciept.grid(row=0,column=0,sticky=W)
total_button=Button(button_frame,text='Total',font=('arial 15 bold underline'),relief='raise',command=f,bd=5)
total_button.grid(row=0,column=1,sticky=W)
#print_reciept=Button(button_frame,text='Print',font=('arial 15 bold underline'),relief='raise',bd=5)
#print_reciept.grid(row=0,column=2,sticky=W)
#home=Button(button_frame,text='Home',font=('arial 15 bold underline'),relief='raise',bd=5)
#home.grid(row=0,column=3,sticky=W)
def cancle():
    delivery.withdraw()

cancle_=Button(button_frame,text='Cancle',font=('arial 15 bold underline'),relief='raise',bd=5,bg='red',command=cancle)
cancle_.grid(row=0,column=4,sticky=W)

x=StringVar()
y=StringVar()
z=StringVar()
w=StringVar()
o=StringVar()
p=StringVar()
q=StringVar()
l=StringVar()

delivery.mainloop()
