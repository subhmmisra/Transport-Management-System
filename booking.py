from tkMessageBox import *
from Tkinter import *
import ttk
import sqlite3
from random import *
conn=sqlite3.connect('myproject.db')
c=conn.cursor()
#c.execute("create table if not exists booking(cngr text ,origin text ,destination text,tin_no number ,gr_no number,permit_no number,issue_date varchar2,vehcile_no varchar2,driver_name text,driver_ph number,item_name text,item_weight number,fare_ number,advance_ number, labour_charge number, insurance_charge number)")
book=Tk()
book.geometry('1366x768')
book.title('Booking')
clock_frame=Frame(book)
clock_frame.grid(row=0,column=0,sticky=W)#clock_frame ,row=0

def rand1():
        a=randrange(1,190000);
        party_entry.insert(16,a)
        party_entry.configure(state='readonly')
    
label_frame=Frame(book,relief='raise')
label_frame.grid(row=1,column=0,sticky=W)
label_party=Button(label_frame,text='Gr No.:',font=('arial 15 bold'),command=rand1)
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
firm_entry=Entry(name_frame,font=('arial 15'),width=45)
firm_entry.grid(row=0,column=3,sticky=W)


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
type_entry['values']=['SELECT','sdchegf','ewjdhwd']
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
dr_ph_label=Label(veh_frame,text='Driver Ph.',font=('arial 15 bold'))
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
v=StringVar()
v.set('0')
a=IntVar()
a.set('0')



fare_label.grid(row=0,column=0,sticky=W)
advance_label=Label(fare_frame,text='       Advance   ',font=('arial',15,'bold'))
advance_label.grid(row=0,column=2,sticky=W)
advance_entry=Entry(fare_frame,font=('arial',15),textvariable=a,justify='right',width=41)
advance_entry.grid(row=0,column=5,sticky=W)
fare_entry=Entry(fare_frame,font=('arial',15),textvariable=v,justify='right',width=50)
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
labr=IntVar()
gate=IntVar()
insurance=IntVar()
labr.set('0')
gate.set('0')
insurance.set('0')
         
other_charges_frame=Frame(book)
other_charges_frame.grid(row=11,sticky=N+W+E+S) # other_charges_frame row=14,delivery
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

#------------------------------------------------------------DATABASE-----------------------------------------------------------------

#c.execute("create table if not exists booking(cngr text ,origin text ,destination text,tin_no number ,gr_no number,permit_no number,issue_date varchar2,vehcile_no varchar2,driver_name text,driver_ph number,item_name text,item_weight number,fare_ number,advance_ number, labour_charge number, insurance_charge number)")

#c.execute('insert into booking values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[(name_entry.get()),(origin_entry.get()),(destination_entry.get()),(firm_entry.get()),(party_entry.get()),(permit_entry.get()),(date_entry.get()),(veh_entry.get()),(dr_entry.get()),(dr_ph.get()),])
def book1():
        c.execute("create table if not exists booking(cngr text ,origin text ,destination text,tin_no number ,gr_no number,permit_no number,issue_date varchar2,vehcile_no varchar2,driver_name text,driver_ph number,item_name text,item_weight number,fare_ number,advance_ number, labour_charge number, insurance_charge number)")

        c.execute('insert into booking values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[(name_entry.get()),(origin_entry.get()),(destination_entry.get()),(firm_entry.get()),(party_entry.get()),(permit_entry.get()),(date_entry.get()),(veh_entry.get()),(dr_entry.get()),(dr_ph_entry.get()),(frm_entry.get()),(item_entry.get()),(fare_entry.get()),(advance_entry.get()),(labour_entry.get()),(insurance_entry.get())])
        conn.commit()
        if name_entry.get()==''or origin_entry.get()=='' or destination_entry.get()=='' or firm_entry.get()=='' or party_entry.get()=='' or veh_entry.get()=='' or dr_entry.get()=='' or dr_ph_entry.get()==''or item_entry.get()=='' or fare_entry.get()=='' :
                showerror('Error','* marked entries are mandatory to fill')

        print name_entry.get()
button_frame=Frame(book)
button_frame.grid(row=15,sticky=W)#button_frame row=15
print_reciept=Label(button_frame,width=85,font=('arial 15 bold underline'),relief='raise')
print_reciept.grid(row=0,column=0,sticky=W)
total_button=Button(button_frame,text='Total',font=('arial 15 bold underline'),relief='raise',bd=5)
total_button.grid(row=0,column=1,sticky=W)
book_button=Button(button_frame,text='Book',bg='powder blue',font=('arial 15 bold underline'),relief='raise',bd=5,command=book1)
book_button.grid(row=0,column=2,sticky=W)
cancle_button=Button(button_frame,text='Cancle',bg='red',font=('arial 15 bold underline'),relief='raise',bd=5)
cancle_button.grid(row=0,column=3,sticky=W)


mainloop()


