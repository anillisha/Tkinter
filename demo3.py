import tkinter as tk
import time
root = tk.Tk()
# width=width chars, height=lines text
text = tk.Text(root, width=20, height=1, bg='yellow')
text.pack()
# use a proportional font to handle spaces correctly
text.config(font=('courier', 24, 'bold'))
s1 = "WELCOME TO ALISHA EMBESOFT PVT LTD .THANks"
# pad front and end with 20 spaces
s2 = ' ' * 10
s = s2 + s1 + s2
while True:
    for k in range(len(s)):
      # use string slicing to do the trick
      ticker_text = s[k:k+20]
      text.insert("1.1", ticker_text)
      root.update()
	    # delay by 0.15 seconds
      time.sleep(0.13)
root.mainloop()
