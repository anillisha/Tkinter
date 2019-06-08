#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time
import sys
import os
#import PIL
import tkinter
#import PIL.Image
#import PIL.ImageTk
import time

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.top_msg()
        self.middle_msg()
        self.bottom_msg()
        
  

        
    def initialize(self):
        self.grid()
        #Top MESSAGE
        time.time()
        Top=tkinter.Frame(self,height=50,width=1200, bg='Orange',relief='raise')
        #image = PIL.Image.open("abc.jpg")
        #photoimg =PIL.ImageTk.PhotoImage(image)
        label2=tkinter.Message(Top,anchor='center',bg="Orange",bd=1,padx=0,pady=20,width=200,justify='left',text="LOGO TO HERE")
        #label = Tkinter.Label( label2, image= photoimg,height=80,text="NO PIC", relief='raise',width=100 )
        #label.pack()

        label2.pack(side='left')
        
        label1=tkinter.Message(Top,anchor='center',bg="Orange",bd=1,width=200,text="TIME")
        label1.pack(side='right')
        
        label3=tkinter.Message(Top,anchor='center',bg="Orange",font=("arial", 22, "bold"),bd=1,padx=181,pady=20,width=800,justify='left',text="DEZIRE EMBEDDED")
        label3.pack(side='top')
        
        
        Top.pack(side='top')

        #middle MESSAGE
        middle=tkinter.Frame(self,height=200,width=800, bg='white',relief='raise')
        m_right=tkinter.Frame(middle,height=200,width=400,bg='Blue',relief='flat')
        m_right.pack(side='right')
        m_left=tkinter.Frame(middle,height=200,width=400,bg='Red',relief='flat')
        m_left.pack(side='left')
        
        

        middle.pack()
        
        #Bottom MESSAGE
        Bottom = tkinter.Frame(self,height=50,width=200,bg='Green',relief='flat')
        text_width = 20
        text = tkinter.Text(Bottom, width=text_width, height=1, bg='Green')
        text.pack()
        Bottom.pack(side='bottom')
        text.config(font=('courier', 48, 'bold'))
        s1 = "WELCOME TO DEZIRE EMBEDDED  "
        s2 = "Powered By: DETPL "
        s3 = "LED SHOW TIME  "
        s4 = "LET's PARTY"
        # pad front and end of text with spaces
        s5 = ' ' * text_width
        s =s5 + s1 + s2 + s3 + s4 + s5
        for k in range(len(s)):
           # use string slicing to do the trick
            ticker_text = s[k:k+text_width]
            text.insert("1.1", ticker_text)
            self.update()
              # delay by 0.22 seconds
            time.sleep(0.11)
                
            
       

    def top_msg(self):
        pass
    def middle_msg(self):
        pass
    def bottom_msg(self):
        pass

if __name__ == "__main__":
    while True:
          app = simpleapp_tk(None)
          app.title('my application')
          app.mainloop()
          app.quit()
          print ("finished")
