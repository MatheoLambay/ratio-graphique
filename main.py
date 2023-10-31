from tkinter import *
from tkinter import ttk
from createGraph import *

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('GraphCreator')
        self.geometry("500x500")
        self.config(background='#2a313c')
        self.listData = ["Ratio","UP/DOWN"]

        self.mainFrame()

    def mainFrame(self):
        self.main_win = Frame(self,bg='#2a313c')

        self.label_title = Label(self.main_win,text='Chart Maker',font=("arial",30), bg='#2a313c', fg='#98e3da').pack()
        self.btn_add_data = Button(self.main_win, text = 'Add', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command = self.addFrame).pack()
        self.btn_del_data = Button(self.main_win, text = 'Delete', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command=self.delFrame).pack()
        self.btn_show_chart_ratio = Button(self.main_win, text = 'Show Chart Ratio', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command=showChartratio).pack()
        self.btn_show_chart_UpDown = Button(self.main_win, text = 'Show Chart U/D', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command=showChartUpDown).pack()
        self.btn_leave_main = Button(self.main_win, text = 'Quit', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command=self.leave).pack()

        self.main_win.pack()

    def addFrame(self):
        self.main_win.forget()
        date = todayDate()
        self.add_win = Frame(self,bg='#2a313c')

        self.label_title = Label(self.add_win,text='Add',font=("arial",30), bg='#2a313c', fg='#98e3da').pack()

        self.entry_frame = Frame(self.add_win,bg='#2a313c')

        self.label_entry_int = Label(self.entry_frame,text='Data Ratio',font=("arial",10),bg='#2a313c', fg='#98e3da')
        self.label_entry_int.pack(anchor=W)

        self.entry_int = Entry(self.entry_frame,font=("arial",14),bg='white', fg='black')
        self.entry_int.pack()

        self.label_entry_int_inv = Label(self.entry_frame,text='',font=("arial",10),bg='#2a313c', fg='#98e3da')
        

        self.entry_int_inv = Entry(self.entry_frame,font=("arial",14),bg='white', fg='black')
        
        self.entry_frame.pack()

        self.label_error = Label(self.add_win,text='',font=("arial",10),bg='#2a313c', fg='red')
        self.label_error.pack()

        self.label_choice = Label(self.add_win,text='Choix du graphique',font=("arial",10),bg='#2a313c', fg='#98e3da').pack()

        self.List_Combo = ttk.Combobox(self.add_win,values=self.listData) 
        self.List_Combo.current(0)
        
        self.List_Combo.pack()
       

        self.label_date = Label(self.add_win,text=date,font=("arial",10),bg='#2a313c', fg='white').pack()
        self.btn_save_data = Button(self.add_win, text = 'Save', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command=self.ConfirmCombo).pack()
        self.btn_back = Button(self.add_win, text = 'Back', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command= lambda: self.back(self.add_win)).pack()
        
        self.add_win.pack()
        self.List_Combo.bind("<<ComboboxSelected>>", self.selectedCombo)

    def delFrame(self):
        self.main_win.forget()
        self.del_win = Frame(self,bg='#2a313c')

        self.label_title = Label(self.del_win,text='Delete',font=("arial",30), bg='#2a313c', fg='#98e3da').pack()

        self.table = ttk.Treeview(self.del_win,columns=('date','int'),show='headings', selectmode="browse")
        
        self.table.heading('date', text='date')
        self.table.heading('int', text='int')

        data = openData("dataRatio.json")
        for i in data.items():
            self.table.insert('', 'end', values=i)

        self.table.pack()

        self.btn_del = Button(self.del_win, text = 'Delete', width = 15, height = 1, font = ('Arial', 14), bg='#FF0040', fg = 'white',command= self.delData).pack()
        self.btn_back = Button(self.del_win, text = 'Back', width = 15, height = 1, font = ('Arial', 14), fg = 'black',command= lambda: self.back(self.del_win)).pack()

        self.del_win.pack()

    def delData(self):
        data = openData("dataRatio.json")
        try:
            del data[self.table.item(self.table.focus())['values'][0]]
            for i in self.table.selection():
                self.table.delete(i)
            newData(data,"dataRatio.json")
        except:
            pass
           
    def ConfirmCombo(self):
        select = self.List_Combo.get()
        if select == 'Ratio':
            addDateJson(self.getEntry(self.entry_int),self.label_error,dataName="dataRatio.json",dataType="Ratio")
        elif select == 'UP/DOWN':
            addDateJson(self.getEntry(self.entry_int),self.label_error,dataName="dataUD.json",dataType="UP/DOWN",ratio2=self.getEntry(self.entry_int_inv))
        else:
            self.label_error['text'] = 'nonexistent data'

    def selectedCombo(self,event):
        select = self.List_Combo.get()
        if select == 'UP/DOWN':
            self.label_entry_int['text']= 'Data Upload'
            self.label_entry_int_inv.pack(anchor=W)
            self.label_entry_int_inv['text']= 'Data Download'
            self.entry_int_inv.pack()
        else:
            self.entry_int_inv.forget()
            self.label_entry_int_inv.forget()
            self.label_entry_int['text']= 'Data Ratio'
        


    def getEntry(self,entry): 
        return entry.get()
    
    def leave(self):
        self.destroy()

    def back(self,frame):
        frame.forget()
        self.mainFrame()

if __name__ == '__main__':
    app = Application()
    app.mainloop()