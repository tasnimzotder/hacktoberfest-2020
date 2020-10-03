from tkinter import *
from convertor import *

root=Tk()


#important function are defined here

def but():

    def checker():
                count = 1


                e = boxe.get()
                f = boxf.get()
                g = boxg.get()

                for i in range(0,3):
                    if (e==0 or e==1) and i==0:
                        if e==0:
                            answer1 = Label(root1, text="                                        ", font="TIMESNEWROMAN 30 bold")
                            answer1.place(x=100, y=90)
                            count += 1


                        elif e==1 or count==1:
                            converting = decimal(searchvalue.get())

                            answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                            answer1.place(x=100, y=90)
                            count += 1



                    elif (f==1 or f==0) and i==1:
                        if f==1:
                            count += 1
                            converting = octal(searchvalue.get())
                            answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                            answer1.place(x=120, y=150)
                        else:
                            answer1 = Label(root1, text="                                                                                                                                                                     ", font="TIMESNEWROMAN 27 bold")
                            answer1.place(x=120, y=150)

                    elif (g==0 or g==1) and i==2:
                        if g==1:
                            converting = hexadecimal(searchvalue.get())
                            answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                            answer1.place(x=120, y=210)
                        else:
                            answer1 = Label(root1, text="                                           ",
                                            font="TIMESNEWROMAN 27 bold")
                            answer1.place(x=120, y=210)


                    #this is when user selects binary at first check box


                    #when user select 2nd option

    def checker2():

        count = 1

        e = boxe.get()
        f = boxf.get()
        g = boxg.get()

        for i in range(0, 3):
            if (e == 0 or e == 1) and i == 0:
                if e == 0:
                    answer1 = Label(root1, text="                                                                                                                                                            ",
                                    font="TIMESNEWROMAN 30 bold")
                    answer1.place(x=100, y=90)
                    count += 1


                elif e == 1 or count == 1:
                    converting =binary(searchvalue.get())

                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=100, y=90)
                    count += 1



            elif (f == 1 or f == 0) and i == 1:
                if f == 1:
                    count += 1
                    converting = octal(binary(searchvalue.get()))
                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=150)
                else:
                    answer1 = Label(root1, text="                                                                                                                        ",
                                                                                                                                                                    font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=150)

            elif (g == 0 or g == 1) and i == 2:
                if g == 1:
                    ga102=searchvalue.get()
                    converting = hexadecimal(binary(ga102))
                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=210)
                else:
                    answer1 = Label(root1, text="                                           ",
                                    font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=210)

    def checker3():
#yaha se karna
        count = 1

        e = boxe.get()
        f = boxf.get()
        g = boxg.get()

        for i in range(0, 3):
            if (e == 0 or e == 1) and i == 0:
                if e == 0:
                    answer1 = Label(root1, text="                                                                                                                    ",font="TIMESNEWROMAN 30 bold")
                    answer1.place(x=100, y=90)
                    count += 1


                elif e == 1 or count == 1:
                    converting =oct2bin(searchvalue.get())

                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=100, y=90)
                    count += 1



            elif (f == 1 or f == 0) and i == 1:
                if f == 1:
                    count += 1
                    converting = decimal(oct2bin(searchvalue.get()))
                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=150)
                else:
                    answer1 = Label(root1, text="                                           ",
                                    font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=150)

            elif (g == 0 or g == 1) and i == 2:
                if g == 1:
                    converting = hexadecimal(oct2bin(searchvalue.get()))
                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=210)
                else:
                    answer1 = Label(root1, text="                                           ",
                                    font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=210)

    def checker4():
        count = 1

        e = boxe.get()
        f = boxf.get()
        g = boxg.get()

        for i in range(0, 3):
            if (e == 0 or e == 1) and i == 0:
                if e == 0:
                    answer1 = Label(root1, text="                                                                                                                    ",font="TIMESNEWROMAN 30 bold")
                    answer1.place(x=100, y=90)
                    count += 1


                elif e == 1 or count == 1:
                    converting =hex2bin(searchvalue.get())

                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=100, y=90)
                    count += 1



            elif (f == 1 or f == 0) and i == 1:
                if f == 1:
                    count += 1
                    converting = decimal(hex2bin(searchvalue.get()))
                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=150)
                else:
                    answer1 = Label(root1, text="                                           ",
                                    font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=150)

            elif (g == 0 or g == 1) and i == 2:
                if g == 1:
                    converting = octal(hex2bin(searchvalue.get()))
                    answer1 = Label(root1, text=converting, font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=210)
                else:
                    answer1 = Label(root1, text="                                           ",
                                    font="TIMESNEWROMAN 27 bold")
                    answer1.place(x=120, y=210)


            # this  are defined functions

    a=boxa.get()
    b=boxb.get()
    c= boxc.get()
    d= boxd.get()
    file=open(r"data.txt","w")
    datafile=file.write(str(a))
    datafile=file.write(str(b))
    datafile=file.write(str(c))
    datafile=file.write(str(d))
    datafile=file.write("\n")
    if (a+b+c+d)==0:

        L1=Label(text="please select an \n option !",font="TIMESNEWROMAN 20 bold",fg="red")
        L1.place(x=200,y=90)
    elif (a+b+c+d)>=2:
        la = Label(text="please select only \n one option !", font="TIMESNEWROMAN 20 bold", fg="red")
        la.place(x=200, y=90)
    else:
        la = Label(text="                                    \n                             ", font="TIMESNEWROMAN 25 bold")
        la.place(x=200, y=90)
        root.destroy()


        if a==1:




            root1=Tk()

            root1.geometry("400x350")
            root1.maxsize(4000, 350)
            root1.minsize(450, 351)
            root1.title("CONVERTOR")

            l2 = Label(root1, text="Enter the sequence :", font="TIMESNEWROMAN 20 bold")
            l2.place(x=10, y=10)

            searchvalue = StringVar()

            input2 = Entry(root1, textvariable=searchvalue)
            input2.place(x=300, y=22)

            l3 =Label(root1, text="CONVERT TO :",font="TIMESNEWROMAN 20 bold")
            l3.place(x=10, y=50)

            boxe=IntVar()
            boxf=IntVar()
            boxg=IntVar()

            box6 =Checkbutton(root1, text="DECIMAL",variable=boxe)
            box7 =Checkbutton(root1, text="OCTAL",variable=boxf)
            box8 =Checkbutton(root1, text="HEXADECIMAL",variable=boxg)


            box6.place(x=10, y=100)
            box7.place(x=10, y=160)
            box8.place(x=10, y=220)

            convertbutton=Button(text="CONVERT",font="TIMESNEWROMAN 20 bold",command=checker).place(x=175,y=275)




            root1.mainloop()
            #2nd input
        elif b==1:
            root1 = Tk()

            root1.geometry("400x350")
            root1.maxsize(4000, 350)
            root1.minsize(450, 351)
            root1.title("CONVERTOR")

            l2 = Label(root1, text="Enter the sequence :", font="TIMESNEWROMAN 20 bold")
            l2.place(x=10, y=10)

            searchvalue = StringVar()

            input2 = Entry(root1, textvariable=searchvalue)
            input2.place(x=300, y=22)

            l3 = Label(root1, text="CONVERT TO :", font="TIMESNEWROMAN 20 bold")
            l3.place(x=10, y=50)

            boxe = IntVar()
            boxf = IntVar()
            boxg = IntVar()

            box6 = Checkbutton(root1, text="BINARY", variable=boxe)
            box7 = Checkbutton(root1, text="OCTAL", variable=boxf)
            box8 = Checkbutton(root1, text="HEXADECIMAL", variable=boxg)

            box6.place(x=10, y=100)
            box7.place(x=10, y=160)
            box8.place(x=10, y=220)

            convertbutton = Button(text="CONVERT", font="TIMESNEWROMAN 20 bold", command=checker2).place(x=175, y=275)

            root1.mainloop()
        elif c==1:
            root1 = Tk()

            root1.geometry("400x350")
            root1.maxsize(4000, 350)
            root1.minsize(450, 351)
            root1.title("CONVERTOR")

            l2 = Label(root1, text="Enter the sequence :", font="TIMESNEWROMAN 20 bold")
            l2.place(x=10, y=10)

            searchvalue = StringVar()

            input2 = Entry(root1, textvariable=searchvalue)
            input2.place(x=300, y=22)

            l3 = Label(root1, text="CONVERT TO :", font="TIMESNEWROMAN 20 bold")
            l3.place(x=10, y=50)

            boxe = IntVar()
            boxf = IntVar()
            boxg = IntVar()

            box6 = Checkbutton(root1, text="BINARY", variable=boxe)
            box7 = Checkbutton(root1, text="DECIMAL", variable=boxf)
            box8 = Checkbutton(root1, text="HEXADECIMAL", variable=boxg)

            box6.place(x=10, y=100)
            box7.place(x=10, y=160)
            box8.place(x=10, y=220)

            convertbutton = Button(text="CONVERT", font="TIMESNEWROMAN 20 bold", command=checker3).place(x=175, y=275)


        elif d==1:
            root1 = Tk()

            root1.geometry("400x350")
            root1.maxsize(4000, 350)
            root1.minsize(450, 351)
            root1.title("CONVERTOR")

            l2 = Label(root1, text="Enter the sequence :", font="TIMESNEWROMAN 20 bold")
            l2.place(x=10, y=10)

            searchvalue = StringVar()

            input2 = Entry(root1, textvariable=searchvalue)
            input2.place(x=300, y=22)

            l3 = Label(root1, text="CONVERT TO :", font="TIMESNEWROMAN 20 bold")
            l3.place(x=10, y=50)

            boxe = IntVar()
            boxf = IntVar()
            boxg = IntVar()

            box6 = Checkbutton(root1, text="BINARY", variable=boxe)
            box7 = Checkbutton(root1, text="DECIMAL", variable=boxf)
            box8 = Checkbutton(root1, text="OCTAL", variable=boxg)

            box6.place(x=10, y=100)
            box7.place(x=10, y=160)
            box8.place(x=10, y=220)

            convertbutton = Button(text="CONVERT", font="TIMESNEWROMAN 20 bold", command=checker4).place(x=175, y=275)





#geometry of the window1
root.geometry("400x350")
root.maxsize(400,350)
root.minsize(450,175)
root.title("This is a GUI")

l1=Label(root,text="Choose your input type :",font="TIMESNEWROMAN 20 bold")
l1.place(x=50,y=30)


boxa=IntVar()
boxb=IntVar()
boxc=IntVar()
boxd=IntVar()


#first 4 checkboxes
box1=Checkbutton(root,text="BINARY",variable=boxa)
box2=Checkbutton(root,text="DECIMAL",variable=boxb)
box3=Checkbutton(root,text="OCTAL",variable=boxc)
box4=Checkbutton(root,text="HEXADECIMAL",variable=boxd)



box1.place(x=50,y=80)
box2.place(x=50,y=110)
box3.place(x=50,y=140)
box4.place(x=50,y=170)

#first button


button1=Button(root,text="SELECT",bg="grey",borderwidth=5,padx=8,command=but)
button1.place(x=50,y=220)









root.mainloop()
