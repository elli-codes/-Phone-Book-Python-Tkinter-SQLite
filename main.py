from tkinter import*
import sqlite3
from tkinter import ttk
from tkinter import messagebox

class my_class():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("550x350+400+200")
        self.root.title("Phone Book")
        
        self.root.resizable(False, False)
        flag=0
        #Connecting to database
        self.con=sqlite3.connect("phoneBook.db")
        self.cur=self.con.cursor()

        #table on database
        self.cur.execute('''CREATE TABLE IF NOT EXISTS phoneBook
        (name TEXT , phone TEXT) ''')
        self.con.commit()

        #table on tkinter
        columns=("name","phone")
        self.table=ttk.Treeview(self.root,columns=columns,show="headings")
        self.table.heading("name",text="Name")
        self.table.heading("phone",text="Phone")
        self.table.place(x=22,y=100)

        # entry & png

        self.txt1 = Label(self.root, text="Name")
        self.txt1.place(x=80, y=20)

        self.e1 = Entry(self.root, width=25)
        self.e1.place(x=180, y=20)


        self.txt2 = Label(self.root, text="Phone")
        self.txt2.place(x=80, y=60)

        self.e2 = Entry(self.root, width=25)
        self.e2.place(x=180, y=60)

        self.img=PhotoImage(file="1100.png")
        self.txt3=Label(self.root,image=self.img,borderwidth=0)
        self.txt3.place(x=430, y=200)
        #button
        self.b1 = Button(
            self.root,
             text="Add",
            width=10,
            command=self.add
        )
        self.b1.place(x=450, y=40)
        
        self.b2 = Button(
            self.root,
            text="Show All",
            width=10,
            command=self.showall
        )
        self.b2.place(x=450, y=70)

        self.b3 = Button(
            self.root,
            text="Delete",
            width=10,
            command=self.delete
        )
        self.b3.place(x=450, y=100)
        
        self.b4 = Button(
            self.root,
            text="Search",
            width=10,
            command=self.search
        )
        self.b4.place(x=450, y=130)

        self.b5 = Button(
            self.root,
            text="Close",
            width=10,
            command=self.close
        )
        self.b5.place(x=450, y=160)
        
    def add(self):
        self.name=self.e1.get()
        self.phone=self.e2.get()
        
        self.cur.execute( """INSERT INTO phoneBook VALUES(?,?)""" ,
                          (self.name,self.phone))
        self.con.commit()
                          

        self.table.insert("","end",values=(self.name,self.phone))
        
        self.e1.delete(0, END)
        self.e2.delete(0, END)
#######################
                          
    def showall(self):
        self.cur.execute("SELECT * FROM phoneBook")

        result=self.cur.fetchall()

        for row in self.table.get_children() :
            self.table.delete(row)

        for row in result:
            self.table.insert("","end",values=(row[0],row[1]) )

   
#########################        
    def delete(self):
        
        self.name=self.e1.get()
        if  not self.e1.get():
            answer1=messagebox.showinfo("information","Please write the name")
        else:    
            self.cur.execute("DELETE FROM phoneBook WHERE name=?" ,(self.name,))
            self.con.commit()
            answer=messagebox.showwarning("Warning","Are you sure you want to delete this contact?")
            print(answer)
            flag=1
            if (flag==1):
                answer1=messagebox.showinfo("information","The contact was deleted.")
            for row in self.table.get_children():
                self.table.delete(row)

            self.cur.execute("SELECT * FROM phoneBook")
            result=self.cur.fetchall()
            for row in result:
                self.table.insert("","end",values=(row[0],row[1]))
                                          
#########################                                      
    def search(self):
           self.name=self.e1.get()

           self.cur.execute("SELECT * FROM  phoneBook WHERE name=?" ,(self.name,))
           result=self.cur.fetchall()
           if not result:
               answer=messagebox.showwarning("Error!","No contact was found with this name.")
           else:
               for row in self.table.get_children():
                   self.table.delete(row)

               for row in result:
                   self.table.insert("","end",values=(row[0],row[1])) 
                                     
###########################
    def close(self):

        self.con.close()
        self.root.destroy()                   
                   
def main():
    x=my_class()
    x.root.mainloop()
    
if __name__=="__main__":main()    
        
