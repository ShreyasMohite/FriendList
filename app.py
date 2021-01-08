from tkinter import *
from tkinter import ttk
from db import *
import tkinter.messagebox



class Friend:
    def __init__(self,root):
        self.root=root
        self.root.title("Friend list")
        self.root.geometry("400x450")
        self.root.iconbitmap(r"C:\Users\SHREYAS\Desktop\shreyas python\FriendList\app\logo788.ico")
        self.root.resizable(0,0)

        sid=StringVar()
        name=StringVar()
        facebook=IntVar()
        instagram=IntVar()
        whatsapp=IntVar()




        def add():
            try:
                if facebook.get()==1:
                    face="present"            
                else:
                    face="not present"
                    
                if instagram.get()==1:
                    insta="present"
                else:
                    insta="not present"
                            
                if whatsapp.get()==1:
                    whats="present"  
                else:
                    whats="not present"

                if name.get()!="":                    
                    add_friendlist(name.get(),face,insta,whats)
                    show()
                else:
                    tkinter.messagebox.showerror('Error',"Please Add Your Friend Name")
            except Exception as e:
                print(e)

        

        def show():
            contact_trees.delete(*contact_trees.get_children())
            for row in view_friendlist():
                contact_trees.insert('',END,values=row)
        
        


        def delete():
            delete_friendlist(sid.get())
            sid.set("")
            show()

        
        def update():
            try:
                if sid.get()!="":
                    delete_friendlist(sid.get())
                    if name.get()!="":
                        if facebook.get()==1:
                            face="present"            
                        else:
                            face="not present"
                            
                        if instagram.get()==1:
                            insta="present"
                        else:
                            insta="not present"
                                    
                        if whatsapp.get()==1:
                            whats="present"  
                        else:
                            whats="not present"                    
                        add_friendlist(name.get(),face,insta,whats)

                        show()
                else:
                    tkinter.messagebox.showerror("Error","Please Select what you have to update")
            except:
                pass

            
        
        
        




#====================frame==============================#
        
        mainframe=Frame(self.root,width=400,height=450,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=394,height=230,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=394,height=214,relief="ridge",bd=3)
        secondframe.place(x=0,y=230)


#======================firstframe========================#
        
        identry=Entry(firstframe,width=3,font=('times new roman',14),relief="ridge",bd=3,textvariable=sid)
        identry.place(x=0,y=0)

        lab_name=Label(firstframe,text="Enter Name",font=('times new roman',15))
        lab_name.place(x=150,y=10)

        ent_name=Entry(firstframe,width=25,font=('times new roman',15),relief='ridge',bd=3,justify="center",textvariable=name)
        ent_name.place(x=65,y=50)

        facebook_cbutton=Checkbutton(firstframe,text="facebook",variable=facebook,font=('times new roman',15),onvalue=1,offvalue=0)
        facebook_cbutton.place(x=15,y=110)

        instagram_cbutton=Checkbutton(firstframe,text="Instagram",variable=instagram,font=('times new roman',15),onvalue=1,offvalue=0)
        instagram_cbutton.place(x=135,y=110)

        whatsapp_cbutton=Checkbutton(firstframe,text="Whatsapp",variable=whatsapp,font=('times new roman',15),onvalue=1,offvalue=0)
        whatsapp_cbutton.place(x=255,y=110)

        but_add=Button(firstframe,text="Add",width=10,font=('times new roman',14),cursor="hand2",command=add)
        but_add.place(x=10,y=170)

        but_update=Button(firstframe,text="Update",width=10,font=('times new roman',14),cursor="hand2",command=update)
        but_update.place(x=135,y=170)

        but_delete=Button(firstframe,text="Delete",width=10,font=('times new roman',14),cursor="hand2",command=delete)
        but_delete.place(x=260,y=170)



#===================================secondframe==================================================#

        def  game(event):
            crow=contact_trees.focus()
            contents=contact_trees.item(crow)
            row=contents['values']
            sid.set(row[0])
            name.set(row[1])
        
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')

        contact_trees=ttk.Treeview(secondframe,columns=("ID","Name","Facebook","Instagram","Whatsapp"),height=9,yscrollcommand=scol.set)
        contact_trees.heading("ID",text="ID")
        contact_trees.heading("Name",text="Name")
        contact_trees.heading("Facebook",text="Facebook")
        contact_trees.heading("Instagram",text="Instagram")
        contact_trees.heading("Whatsapp",text="Whatsapp")
        contact_trees['show']="headings"
        contact_trees.column("ID",width=30,minwidth=10)
        contact_trees.column("Name",width=110,minwidth=40)
        contact_trees.column("Facebook",width=76,minwidth=40)
        contact_trees.column("Instagram",width=76,minwidth=40)
        contact_trees.column("Whatsapp",width=76,minwidth=40)
        contact_trees.place(x=0,y=0)
        contact_trees.bind('<ButtonRelease-1>',game)



if __name__=="__main__":
    root=Tk()
    Friend(root)
    root.mainloop()