from tkinter import *
import compute
def com1():
    global lavel
    
    charge1val=Charge1.get()
    #print(charge1val)
    charge2val=Charge2.get()
    #print(charge2val)
    root.destroy()
    root1=Tk()
    global flag

    root1.title("OUTPUT")
    root1.geometry("7000x6000")
    root1.minsize(500,600)
    canvas=Canvas(root1,width=2000,height=2200,bg="sky blue")
    canvas.place(x=0,y=0)
    M=StringVar()

    x_1,y_1,x_2,y_2=550,200,650,300  #coordinates for the big circle
    a_1,b_1,a_2,b_2=730,220,790,280  #coordinates for the small circle
    global countsmallclick,countbigclick
    #global bigclick,smallclick
    bigclick=0
    smallclick=0
    if charge1val>charge2val:      
        oval1=canvas.create_oval(x_1,y_1,x_2,y_2,fill="orange")        
        oval2=canvas.create_oval(a_1,b_1,a_2,b_2,fill="grey")
        text1=canvas.create_text(600,250,text=f"{charge1val}",fill="white")
        text2=canvas.create_text(760,250,text=f"{charge2val}",fill="white")
        line1=canvas.create_line(650,250,730,250,fill="black",width="3")
        f,g=compute.mp(650,250,730,250)
        dist=int((compute.liner(650,250,730,250)//80))
        distance=canvas.create_text(f,g,text=f"{dist}")
        flag=1
        countbigclick=0
        countsmallclick=0

      
    elif charge2val>charge1val:
        charge1val,charge2val=charge2val,charge1val
        oval1=canvas.create_oval(x_1,y_1,x_2,y_2,fill="orange")        
        oval2=canvas.create_oval(a_1,b_1,a_2,b_2,fill="grey")
        text1=canvas.create_text(600,250,text=f"{charge1val}",fill="white")
        text2=canvas.create_text(760,250,text=f"{charge2val}",fill="white")
        line1=canvas.create_line(650,250,730,250,fill="black",width="3")
        countbigclick=0
        countsmallclick=0
        f,g=compute.mp(650,250,730,250)
        dist=int((compute.liner(650,250,730,250)//80))
        distance=canvas.create_text(f,g,text=f"{dist}")
        
        flag=1
        
    else:
        oval1=canvas.create_oval(610,220,670,280,fill="grey")
        text1=canvas.create_text(640,250,text=f"{charge1val}",fill="white")        
        oval2=canvas.create_oval(730,220,790,280,fill="grey")
        text2=canvas.create_text(760,250,text=f"{charge2val}",fill="white")
        line2=canvas.create_line(670,250,730,250,fill="black",width="3")
        countbigclick=0
        countsmallclick=0
        f,g=compute.mp(670,250,730,250)
        dist=int((compute.liner(670,250,730,250))//60) 
        distance=canvas.create_text(f,g,text=f"{dist}")
        flag=2
        
    bumbam=i.get()
    bambum=mango.get()
    q=compute.getter(bambum)
    force=compute.forcecalc(charge1val,charge2val,q,dist,bumbam)
    M.set(str(force))
    lavel=Label(root1,textvariable=M,font="TIMESNEWROMAN 12 bold",bd=3,height=1,fg="green") 
    lavel.place(x=865,y=600)
    lav=Label(root1,text="The Electrostatic Force Of Attraction is :",font="TIMESNEWROMAN 12 bold",bg="white",fg="red")
    lav.place(x=550,y=600)
    def dad(event):#radius of bigcircle=50, radius of smaller circle=30
        global x11,x_11
        global y11,y_11
        global lavel1,heaven
        global oval3,oval4
        global text3,text4
        global line3,line4
        global distancenew
        heaven=0
        m=event.x
        n=event.y
        
        if flag==1:  #for un even circles
            if countsmallclick>=0:
                try:
                    xaxis=x11-30     #coordinates for bigger circle
                    yaxis=y11
                    flagbig=1
                    
                except:
                    xaxis=730   #coordinates for bigger circle
                    yaxis=250
                    flagbig=0
                    
            if countbigclick>=0:
                try :
                    x_axis=x_11+50 #coordinates for smaller circle
                    y_axis=y_11
                    
                    flagsmall=1
                except:
                    x_axis=650     #coordinates for smaller circle
                    y_axis=250
                    flagsmall=0
                    
            if m<650:    
                x1=m-50
                y1=n-50
                x2=m+50
                y2=n+50
                try:
                    canvas.delete(text3)
                    canvas.delete(oval3)
                    canvas.delete(line3)
                    canvas.delete(distancenew)
                    oval3=canvas.create_oval(x1,y1,x2,y2,fill="orange")
                    text3=canvas.create_text(m,n,text=f"{charge1val}")
                    line3=canvas.create_line(x2,n,xaxis,yaxis,fill="black",width="2")
                    f,g=compute.mp(x2,n,xaxis,yaxis)
                    distnew=int((compute.liner(x2,n,xaxis,yaxis))//80)
                    distancenew=canvas.create_text(f,g,text=f"{distnew}")
                    
                    x_11=m
                    y_11=n
                    
                except NameError or UnboundLocalError:
                    if flagbig==0: #chota circle nahi hila hai
                        canvas.delete(line1)
                        canvas.delete(oval1)
                        canvas.delete(text1)
                        canvas.delete(distance)
                        oval3=canvas.create_oval(x1,y1,x2,y2,fill="orange")
                        text3=canvas.create_text(m,n,text=f"{charge1val}")
                        line3=canvas.create_line(x2,n,xaxis,yaxis,fill="black",width="2")
                        f,g=compute.mp(x2,n,xaxis,yaxis)
                        distnew=int((compute.liner(x2,n,xaxis,yaxis))//80)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
                        x_11=m
                        y_11=n
                    elif flagbig==1:  #chota circle hila hai 
                        canvas.delete(line3)
                        canvas.delete(oval1)
                        canvas.delete(text1)
                        canvas.delete(distancenew)
                        oval3=canvas.create_oval(x1,y1,x2,y2,fill="orange")
                        text3=canvas.create_text(m,n,text=f"{charge1val}")
                        line3=canvas.create_line(x2,n,xaxis,yaxis,fill="black",width="2")
                        
                        f,g=compute.mp(x2,n,xaxis,yaxis)
                        distnew=int((compute.liner(x2,n,xaxis,yaxis))//80)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
                        x_11=m
                        y_11=n
            elif m>730:#right side of the blank bar
                a1=m-30
                b1=n-30
                a2=m+30
                b2=n+30
                try:  
                    canvas.delete(text4)
                    canvas.delete(oval4)
                    canvas.delete(line3)
                    canvas.delete(distancenew)
                    oval4=canvas.create_oval(a1,b1,a2,b2,fill="orange")
                    text4=canvas.create_text(m,n,text=f"{charge2val}")
                    line3=canvas.create_line(x_axis,y_axis,a1,n,fill="black",width="2")
                    x11=m
                    y11=n
                    f,g=compute.mp(x_axis,y_axis,a1,n)
                    distnew=int((compute.liner(x_axis,y_axis,a1,n))//80)
                    distancenew=canvas.create_text(f,g,text=f"{distnew}")
                    
                    

                except NameError or UnboundLocalError:
                    if flagsmall==0:
                        canvas.delete(line1)
                        canvas.delete(oval2)
                        canvas.delete(text2)
                        canvas.delete(distance)
                        oval4=canvas.create_oval(a1,b1,a2,b2,fill="orange")
                        text4=canvas.create_text(m,n,text=f"{charge2val}")
                        line3=canvas.create_line(x_axis,y_axis,a1,n,fill="black",width="2")
                        x11=m
                        y11=n
                        f,g=compute.mp(x_axis,y_axis,a1,n)
                        distnew=int((compute.liner(x_axis,y_axis,a1,n))//80)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
                        
                    elif flagsmall==1:
                        canvas.delete(line3)
                        canvas.delete(oval2)
                        canvas.delete(text2)
                        canvas.delete(distancenew)
                        oval4=canvas.create_oval(a1,b1,a2,b2,fill="orange")
                        text4=canvas.create_text(m,n,text=f"{charge2val}")
                        line3=canvas.create_line(x_axis,y_axis,a1,n,fill="black",width="2")
                        x11=m
                        y11=n
                        f,g=compute.mp(x_axis,y_axis,a1,n)
                        distnew=int((compute.liner(x_axis,y_axis,a1,n))//80)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")

            ######################################################################################################################
                        #for same sized circles
        elif flag==2:
            if countsmallclick>=0:
                try:
                    xaxis=x11-30     #coordinates for bigger circle
                    yaxis=y11
                    flagbig=1
                    
                except:
                    xaxis=730   #coordinates for bigger circle
                    yaxis=250
                    flagbig=0
                    
            if countbigclick>=0:
                try :
                    x_axis=x_11+30 #coordinates for smaller circle
                    y_axis=y_11
                    
                    flagsmall=1
                except:
                    x_axis=650     #coordinates for smaller circle
                    y_axis=250
                    flagsmall=0
                    
            if m<650:    
                x1=m-30
                y1=n-30
                x2=m+30
                y2=n+30
                try:
                    canvas.delete(oval3)
                    canvas.delete(text3)
                    canvas.delete(line3)
                    canvas.delete(distancenew)
                    oval3=canvas.create_oval(x1,y1,x2,y2,fill="orange")
                    text3=canvas.create_text(m,n,text=f"{charge1val}")
                    line3=canvas.create_line(x2,n,xaxis,yaxis,fill="black",width="2")
                    x_11=m
                    y_11=n
                    f,g=compute.mp(x2,n,xaxis,yaxis)
                    distnew=int((compute.liner(x2,n,xaxis,yaxis))//60)
                    distancenew=canvas.create_text(f,g,text=f"{distnew}")
                    
                    
                except NameError or UnboundLocalError:
                    if flagbig==0: #chota circle nahi hila hai
                        canvas.delete(line2)
                        canvas.delete(oval1)
                        canvas.delete(text1)
                        canvas.delete(distance)
                        oval3=canvas.create_oval(x1,y1,x2,y2,fill="orange")
                        text3=canvas.create_text(m,n,text=f"{charge1val}")
                        line3=canvas.create_line(x2,n,xaxis,yaxis,fill="black",width="2")
                        f,g=compute.mp(x2,n,xaxis,yaxis)
                        distnew=int((compute.liner(x2,n,xaxis,yaxis))//60)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
                        x_11=m
                        y_11=n
                        
                    elif flagbig==1:  #chota circle hila hai 
                        canvas.delete(line3)
                        canvas.delete(oval1)
                        canvas.delete(text1)
                        canvas.delete(distancenew)
                        oval3=canvas.create_oval(x1,y1,x2,y2,fill="orange")
                        text3=canvas.create_text(m,n,text=f"{charge1val}")
                        line3=canvas.create_line(x2,n,xaxis,yaxis,fill="black",width="2")
                        f,g=compute.mp(x2,n,xaxis,yaxis)
                        distnew=int((compute.liner(x2,n,xaxis,yaxis))//60)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
                        x_11=m
                        y_11=n
                        
            elif m>730:#right side of the blank bar
                a1=m-30
                b1=n-30
                a2=m+30
                b2=n+30
                try:
                    canvas.delete(distancenew)
                    canvas.delete(text4)
                    canvas.delete(oval4)
                    canvas.delete(line3)
                    oval4=canvas.create_oval(a1,b1,a2,b2,fill="orange")
                    text4=canvas.create_text(m,n,text=f"{charge2val}")
                    line3=canvas.create_line(x_axis,y_axis,a1,n,fill="black",width="2")
                    f,g=compute.mp(x_axis,y_axis,a1,n)
                    distnew=int((compute.liner(x_axis,y_axis,a1,n))//60)
                    distancenew=canvas.create_text(f,g,text=f"{distnew}")
                    x11=m
                    y11=n

                except NameError or UnboundLocalError:
                    
                    if flagsmall==0:
                       
                        canvas.delete(distance)
                        canvas.delete(line2)
                        canvas.delete(oval2)
                        canvas.delete(text2)
                        oval4=canvas.create_oval(a1,b1,a2,b2,fill="orange")
                        text4=canvas.create_text(m,n,text=f"{charge2val}")
                        line3=canvas.create_line(x_axis,y_axis,a1,n,fill="black",width="2")
                        x11=m
                        y11=n
                        
                        f,g=compute.mp(x_axis,y_axis,a1,n)
                        distnew=int((compute.liner(x_axis,y_axis,a1,n))//60)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
                    elif flagsmall==1:
                        canvas.delete(line3)
                        canvas.delete(oval2)
                        canvas.delete(text2)
                        canvas.delete(distancenew)
                        oval4=canvas.create_oval(a1,b1,a2,b2,fill="orange")
                        text4=canvas.create_text(m,n,text=f"{charge2val}")
                        line3=canvas.create_line(x_axis,y_axis,a1,n,fill="black",width="2")
                        x11=m
                        y11=n
                        f,g=compute.mp(x_axis,y_axis,a1,n)
                        distnew=int((compute.liner(x_axis,y_axis,a1,n))//60)
                        distancenew=canvas.create_text(f,g,text=f"{distnew}")
        bamchik=i.get()
        bumchik=mango.get()
        z=compute.getter(bamchik)        
        force=compute.forcecalc(charge1val,charge2val,z,distnew,bamchik)
        M.set(str(force))       
    canvas.bind("<Button-1>",dad)                        
    root1.mainloop()
#second window ka mainloop hai confuse mat hona  
############################################################################################################################################################
#FIRST WINDOW BY AWASTHIJI 
root=Tk()
root.title("COULOMB'S LAW")
root.minsize(550,350)
root.maxsize(550,350)
label1=Label(root,text="Charge1",font="TIMESNEWROMAN 15 bold",bg="grey",fg="black",bd=2,relief="solid")
label1.place(x=100,y=20)
label2=Label(root,text="Charge2",font="TIMESNEWROMAN 15 bold",bg="grey",fg="black",bd=2,relief="solid")
label2.place(x=100,y=60)
Charge1=IntVar()
Charge1.set(1)
entry1=Entry(root,textvariable=Charge1,bd=3,relief="sunken")
entry1.place(x=190,y=26)
Charge2=IntVar()
Charge2.set(1)
entry2=Entry(root,textvariable=Charge2,bd=3,relief="sunken")
entry2.place(x=190,y=66)
box=IntVar()
label3=Label(root,text="MEDIUM :",font="TIMESNEWROMAN 15 bold",bg="grey",fg="black",bd=2,relief="solid")
label3.place(x=100,y=100)
box1=Radiobutton(root,text="Air",value=1,variable=box,bd=2,relief="sunken")
box1.place(x=210,y=100)
box4=Radiobutton(root,text="Vaccum",value=2,variable=box,bd=2,relief="sunken")
box4.place(x=280,y=100)
box5=Radiobutton(root,text="Free Space",value=3,variable=box,bd=2,relief="sunken")
box5.place(x=380,y=100)
label4=Label(root,text="UNIT :",font="TIMESNEWROMAN 16 bold",bg="grey",fg="black",bd=2,relief="solid")
label4.place(x=100,y=150)

i=IntVar()
r1=Radiobutton(root,text="pm",value=123,variable=i,bd=2,relief="sunken")
r2=Radiobutton(root,text="cm",value=234,variable=i,bd=2,relief="sunken")
r3=Radiobutton(root,text="mm",value=345,variable=i,bd=2,relief="sunken")
r4=Radiobutton(root,text="nm",value=456,variable=i,bd=2,relief="sunken")
r1.place(x=200,y=150)
r2.place(x=260,y=150)
r3.place(x=320,y=150)
r4.place(x=380,y=150)

mango=IntVar()
label5=Label(root,text="CHARGE'S UNIT:",font="TIMESNEWROMAN 12 bold",bg="grey",fg="black",bd=2,relief="solid").place(x=50,y=200)
rad1=Radiobutton(root,text="c",value=123,variable=mango,bd=2,relief="sunken")
rad2=Radiobutton(root,text="pc",value=234,variable=mango,bd=2,relief="sunken")
rad3=Radiobutton(root,text="mc",value=345,variable=mango,bd=2,relief="sunken")
rad4=Radiobutton(root,text="nc",value=456,variable=mango,bd=2,relief="sunken")
rad1.place(x=200,y=200)
rad2.place(x=260,y=200)
rad3.place(x=320,y=200)
rad4.place(x=380,y=200)
button=Button(root,text="ENTER",command=com1,bg="grey",fg="black",font="TIMESNEWROMAN 15 bold",bd=4,relief="sunken")
button.place(x=250,y=290)
root.mainloop()
