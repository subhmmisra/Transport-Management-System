from Tkinter import *
import time
import sqlite3
conn=sqlite3.connect('myproject.db')
c=conn.cursor()
enquiry=Tk()
enquiry.geometry('1368x794')
localtime=time.asctime(time.localtime(time.time()))
l2=Label(enquiry,text=localtime,font=('Arial','15','bold'),fg='Steel Blue')
l2.place(relx=0,rely=0)
A2=StringVar()
B2=StringVar()
C2=StringVar()
D2=StringVar()
E2=StringVar()
F2=IntVar()

x2=IntVar()
y2=StringVar()
z2=StringVar()
w2=StringVar()
o2=StringVar()
p2=StringVar()
q2=StringVar()
G2=StringVar()
H2=StringVar()
def gm(m):
    try:
        #A=IntVar()
        c.execute('select gr_no from booking where gr_no=?',[(gr_entryE.get())])
        x2=c.fetchone()
        if m==str(x2[0]):
            c.execute('select cngr from booking where gr_no=?',[(gr_entryE.get())])
            y2=c.fetchone()
            c.execute('select origin from booking where gr_no=?',[(gr_entryE.get())])
            z2=c.fetchone()
            c.execute('select destination from booking where gr_no=?',[(gr_entryE.get())])
            w2=c.fetchone()
            c.execute('select item_weight from booking where gr_no=?',[(gr_entryE.get())])
            o2=c.fetchone()
            c.execute('select item_name from booking where gr_no=?',[(gr_entryE.get())])
            p2=c.fetchone()
            c.execute('select fare_ from booking where gr_no=?',[(gr_entryE.get())])
            q2=c.fetchone()
            #A.set('hi')
            print y2[0],z2[0],w2[0],o2[0],p2[0]
            #else:print 'no'
            #print m
            A2.set(y2)
            B2.set(z2)
            C2.set(w2)
            D2.set(o2)
            E2.set(p2)
            F2.set(q2[0])
            G2.set('Available in godown no. 5                                                   ' )
            H2.set('######              ')
            #print q[0]
            
        #elif m=='':
            #G2.set('#############')  
        else:
            G2.set('******************************')
            A2.set('******************************')
            B2.set('******************************')
            C2.set('******************************')
            D2.set('******************************')
            E2.set('******************************')
            F2.set('******************************')
    
    except(TypeError):
            G2.set('Not yet arrived                                                        ')
            A2.set('******************************')
            B2.set('******************************')
            C2.set('******************************')
            D2.set('******************************')
            E2.set('******************************')
            F2.set('******************************')

            #return None
                
            
        #else:
            #return None

gr_frameE=Frame(enquiry,relief='raise',bd=5)
gr_frameE.grid(row=1,column=0,sticky=W)## grframe ,row=1 delivery
gr_entryE=Entry(gr_frameE,font=('arial',15,'bold'),width=30,bg='yellow')
gr_entryE.grid(row=0,column=1,sticky=W)
gr_labelE=Button(gr_frameE,text='GR No.',font=('arial',15,'bold'),height=0,command=lambda:gm(gr_entryE.get()))
gr_labelE.grid(row=0,column=0,sticky=W)
m=gr_entryE.get()

status_frameE=Frame(enquiry,bd=5)
status_frameE.grid(row=2,column=0,sticky=W)## status frame row=2 delivery
status_labelE=Label(status_frameE,text='Status        ',font=('arial',15,'bold'))
status_labelE.grid(row=0,column=0,sticky=W)
status_entryE=Entry(status_frameE,font=('arial',15,'bold'),width=104,textvariable=G2,justify='right')
status_entryE.grid(row=0,column=1,sticky=W)


booking_frameE=Frame(enquiry,bd=5)
booking_frameE.grid(row=3,column=0,sticky=W)##booking_frame row=3 delivery
booking_labelE=Label(booking_frameE,text='Booking_Dt',font=('arial',15,'bold'))
booking_labelE.grid(row=0,column=0,sticky=W)
booking_entryE=Entry(booking_frameE,font=('arial',15,'bold'),width=32)
booking_entryE.grid(row=0,column=1,sticky=W)
shipper_labelE=Label(booking_frameE,text='Shipper',font=('arial',15,'bold'))
shipper_labelE.grid(row=0,column=2,sticky=W)
shipper_entryE=Entry(booking_frameE,font=('arial',15),width=30,textvariable=H2,justify='right')
shipper_entryE.grid(row=0,column=3,sticky=W)
cngr_labelE=Label(booking_frameE,text='Cngr',font=('arial',15,'bold'),textvariable=A2)
cngr_labelE.grid(row=0,column=4,sticky=W)
cngr_entryE=Entry(booking_frameE,font=('arial',15,'bold'),width=29,justify='right')
cngr_entryE.grid(row=0,column=5,sticky=W)


good_frameE=Frame(enquiry,bd=5)
good_frameE.grid(row=4,column=0,sticky=W)## good_frame row=4 delivery
good_labelE=Label(good_frameE,text='Good          ',font=('arial',15,'bold'))
good_labelE.grid(row=0,column=0,sticky=W)
good_entryE=Entry(good_frameE,font=('arial',15,'bold'),width=65,textvariable=E2,justify='right')
good_entryE.grid(row=0,column=1,sticky=W)
value_labelE=Label(good_frameE,text='value',font=('arial',15,'bold'))
value_labelE.grid(row=0,column=2,sticky=W)
value_entryE=Entry(good_frameE,font=('arial',15),width=33,textvariable=D2,justify='right')
value_entryE.grid(row=0,column=3,sticky=W)


from_frameE=Frame(enquiry,bd=5)
from_frameE.grid(row=5,column=0,sticky=W)## from_frame row=5 delivery
from_labelE=Label(from_frameE,text='From          ',font=('arial',15,'bold'))
from_labelE.grid(row=0,column=0,sticky=W)
from_entryE=Entry(from_frameE,font=('arial',15),width=51,textvariable=B2,justify='right')
from_entryE.grid(row=0,column=1,sticky=W)
to_labelE=Label(from_frameE,text='To',font=('arial',15,'bold'))
to_labelE.grid(row=0,column=2,sticky=W)
to_entryE=Entry(from_frameE,font=('arial',15),width=50,textvariable=C2,justify='right')
to_entryE.grid(row=0,column=3,sticky=W)


##    type_frameE=Frame(enquiry,bd=5)
##    type_frameE.grid(row=6,sticky=W)## type_frame row=6 delivery
##    type_labelE=Label(type_frameE,text='Delivery Type',font=('arial',15,'bold'))
##    type_labelE.grid(row=0,column=0,sticky=W)
f_enq=Label(enquiry,width=170,bd=10,relief='raise')
f_enq.grid(row=6
           )


enquiry.mainloop()

