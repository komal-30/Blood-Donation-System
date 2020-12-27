from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import LibBksDatabase
class Library:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Blood Donation Management System")
        self.root.geometry("1350x750+0+0")

        Mty = StringVar()
        Ref = StringVar()
        Tit = StringVar()
        fna = StringVar()
        sna = StringVar()
        Adr1 = StringVar()
        Adr2 = StringVar()
        pcd = StringVar()
        MNo = StringVar()
        BkID = StringVar()
        Bkt = StringVar()
        BkT = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        sPr = StringVar()
        LrF = StringVar()
        DoD = StringVar()
        DonL = StringVar()

    # =======================Function Declaration===========================#
        def iExit():
            iExit = tkinter.messagebox.askyesno('Blood Donation Management System','Confirm if you want to exit')
            if iExit > 0:
                root.destroy()
                return
        def ClearData():
            self.txtMType.delete(0,END)
            self.txtBkID.delete(0,END)
            self.txtRef.delete(0,END)
            self.txtBkt.delete(0,END)
            self.txtTit.delete(0,END)
            self.txtAtr.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtDdu.delete(0,END)
            self.txtAdr1.delete(0,END)
            self.txtAdr2.delete(0,END)
            self.txtDonL.delete(0,END)
            self.txtLrF.delete(0,END)
            self.txtpcd.delete(0,END)
            self.txtDoD.delete(0,END)
            self.txtMNo.delete(0,END)
            self.txtsPr.delete(0,END)
            self.txtDBo.delete(0,END)

        def addData():
            if(len(Mty.get())!=0):
                LibBksDatabase.addDataRec(Mty.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),
                                          MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get())
                booklist.delete(0, END)
                booklist.insert(END, (
                Mty.get(), Ref.get(), Tit.get(), fna.get(), sna.get(), Adr1.get(), Adr2.get(), pcd.get(),
                MNo.get(), BkID.get(), Bkt.get(), Atr.get(), DBo.get(), Ddu.get(), sPr.get(), LrF.get(), DoD.get(),
                DonL.get()))


        def DisplayData():
            booklist.delete(0,END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END,row)

        def SelectedBook(event):
            global sb
            searchBk = booklist.curselection()[0]
            sb = booklist.get(searchBk)
            self.txtMType.delete(0, END)
            self.txtMType.insert(END,sb[1])
            self.txtBkID.delete(0, END)
            self.txtBkID.insert(END,sb[2])
            self.txtRef.delete(0, END)
            self.txtRef.insert(END,sb[3])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END,sb[4])
            self.txtTit.delete(0, END)
            self.txtTit.insert(END,sb[5])
            self.txtAtr.delete(0, END)
            self.txtAtr.insert(END,sb[6])
            self.txtBkt.delete(0, END)
            self.txtBkt.insert(END,sb[7])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END,sb[8])
            self.txtDdu.delete(0, END)
            self.txtDdu.insert(END,sb[9])
            self.txtAdr1.delete(0, END)
            self.txtAdr1.insert(END,sb[10])
            self.txtAdr2.delete(0, END)
            self.txtAdr2.insert(END,sb[11])
            self.txtDonL.delete(0, END)
            self.txtDonL.insert(END,sb[12])
            self.txtLrF.delete(0, END)
            self.txtLrF.insert(END,sb[13])
            self.txtpcd.delete(0, END)
            self.txtpcd.insert(END,sb[14])
            self.txtDoD.delete(0, END)
            self.txtDoD.insert(END,sb[15])
            self.txtMNo.delete(0, END)
            self.txtMNo.insert(END,sb[16])
            self.txtsPr.delete(0, END)
            self.txtsPr.insert(END,sb[17])
            self.txtDBo.delete(0, END)
            self.txtDBo.insert(END,sb[18])

        def DeleteDate():
            if(len(Mty.get())!=0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()

        def searchDatabase():
            booklist.delete(0,END)
            for row in LibBksDatabase.searchData(Mty.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(),
                                          MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get()):
                booklist.insert(END, row)

        '''def update():
            if(len(Mty.get())!=0):
                LibBksDatabase.dataUpdate(sb[0],Mty.get(), Ref.get(), Tit.get(), fna.get(), sna.get(), Adr1.get(), Adr2.get(),pcd.get(), MNo.get(), BkID.get(), Bkt.get(), Atr.get(), DBo.get(), Ddu.get(), sPr.get(),LrF.get(), DoD.get(), DonL.get())
        '''
        #=======================Frames===========================#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitFrame = Frame(MainFrame,bd=2,padx=40,pady=8,bg='red',relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame,font=('arial',46,'bold'),text='Blood Donation Management System',)
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame,bd=2,width=1350,height=100,bg='red',padx=20,pady=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame,bd=0,width=1300,height=50,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,bd=1,width=1300,height=400,padx=20,bg='red',pady=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame,bd=1,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Patient & Donor Details:",bg='misty rose',)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=20,pady=3,relief=RIDGE,font=('arial',12,'bold'),text="Updated Data:",bg='misty rose',)
        DataFrameRIGHT.pack(side=RIGHT)

    # =======================Lables and Entries===========================#

        self.lblMemberType = Label(DataFrameLEFT,font=('arial',12,'bold'),text='Salutation:',padx=2,pady=2,bg='misty rose',)
        self.lblMemberType.grid(row=0,column=0,sticky=W)

        self.txtMType = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Mty,width=25)
        self.txtMType.grid(row=0,column=1)

        self.lblBkID=Label(DataFrameLEFT,font=('arial',12,'bold'),text='Name Of Donor:',padx=2,pady=2,bg='misty rose',)
        self.lblBkID.grid(row=0, column=2, sticky=W)
        self.txtBkID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=BkID,width=25)
        self.txtBkID.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Reference No:', padx=2, pady=2,
                             bg='misty rose',)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblBkt = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Blood Group Of Donor:', padx=2, pady=2,
                         bg='misty rose',)
        self.lblBkt.grid(row=1, column=2, sticky=W)
        self.txtBkt = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Bkt, width=25)
        self.txtBkt.grid(row=1, column=3)

        self.lblTit = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Name Of Doctor:', padx=2, pady=2,
                        bg='misty rose',)
        self.lblTit.grid(row=2, column=0, sticky=W)
        self.txtTit = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Tit, width=25)
        self.txtTit.grid(row=2, column=1)

        self.lblAtr = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Age Of Donor:', padx=2, pady=2,
                           bg='misty rose',)
        self.lblAtr.grid(row=2, column=2, sticky=W)
        self.txtAtr = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Atr, width=25)
        self.txtAtr.grid(row=2, column=3)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='First Name:', padx=2, pady=2,
                         bg='misty rose',)
        self.lblfna.grid(row=3, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=fna, width=25)
        self.txtfna.grid(row=3, column=1)

        self.lblDBo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Date Of Donation:', padx=2, pady=2,
                            bg='misty rose',)
        self.lblDBo.grid(row=3, column=2, sticky=W)
        self.txtDBo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DBo, width=25)
        self.txtDBo.grid(row=3, column=3)

        self.lblsna = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Surname:', padx=2, pady=2,
                           bg='misty rose',)
        self.lblsna.grid(row=4, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=sna, width=25)
        self.txtsna.grid(row=4, column=1)

        self.lblDdu = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Blood(Litres):', padx=2, pady=2,
                           bg='misty rose',)
        self.lblDdu.grid(row=4, column=2, sticky=W)
        self.txtDdu = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ddu, width=25)
        self.txtDdu.grid(row=4, column=3)

        self.lblAdr1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Address:', padx=2, pady=2,
                          bg='misty rose',)
        self.lblAdr1.grid(row=5, column=0, sticky=W)
        self.txtAdr1 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr1, width=25)
        self.txtAdr1.grid(row=5, column=1)

        self.lblDonL= Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Sex Of Donor:', padx=2, pady=2,
                             bg='misty rose',)
        self.lblDonL.grid(row=5, column=2, sticky=W)
        self.txtDonL = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DonL, width=25)
        self.txtDonL.grid(row=5, column=3)

        self.lblAdr2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Age Of Patient:', padx=2, pady=2,
                   bg='misty rose',)
        self.lblAdr2.grid(row=6, column=0, sticky=W)
        self.txtAdr2 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr2, width=25)
        self.txtAdr2.grid(row=6, column=1)

        self.lblLrF = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Contact Of Donor:', padx=2, pady=2,
                          bg='misty rose',)
        self.lblLrF.grid(row=6, column=2, sticky=W)
        self.txtLrF = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=LrF, width=25)
        self.txtLrF.grid(row=6, column=3)

        self.lblpcd = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Blood Group Of Patient:', padx=2, pady=2,
                       bg='misty rose',)
        self.lblpcd.grid(row=7, column=0, sticky=W)
        self.txtpcd = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=pcd, width=25)
        self.txtpcd.grid(row=7, column=1)

        self.lblDoD = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Address Of Donor:', padx=2, pady=2,
                   bg='misty rose',)
        self.lblDoD.grid(row=7, column=2, sticky=W)
        self.txtDoD = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DoD, width=25)
        self.txtDoD.grid(row=7, column=3)

        self.lblMNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Patient Contact Number:', padx=2, pady=2,
                           bg='misty rose',)
        self.lblMNo.grid(row=8, column=0, sticky=W)
        self.txtMNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=MNo, width=25)
        self.txtMNo.grid(row=8, column=1)

        self.lblsPr = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Medical History :', padx=2, pady=2,
                            bg='misty rose',)
        self.lblsPr.grid(row=8, column=2, sticky=W)
        self.txtsPr = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=sPr, width=25)
        self.txtsPr.grid(row=8, column=3)

        #====================ListBox and ScrollBar========================#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        booklist = Listbox(DataFrameRIGHT,width=45,height=12,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        #===================Buttons Widget==================#

        self.btnAddData = Button(ButtonFrame,text='Add Data',font=('arial',14,'bold'),height=2,width=13,bd=4,command = addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame, text='Display Data', font=('arial', 14, 'bold'
                                                                                          ''), height=2, width=13, bd=4,command = DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text='Clear Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,command = ClearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text='Delete Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,command = DeleteDate)
        self.btnDeleteData.grid(row=0, column=3)

        '''self.btnUpdateData= Button(ButtonFrame, text='Update Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=4) '''

        self.btnSearchData = Button(ButtonFrame, text='Search Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 14, 'bold'), height=2, width=13, bd=4,command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__=='__main__' :
    root = Tk()
    application = Library(root)
    root.mainloop()






