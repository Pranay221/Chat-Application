import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost',9999))

print('Server Up')

s.listen(3)

import tkinter as tk

root=tk.Tk()

root.geometry("400x200")

root.title("Chat App Server Side")

root.configure(bg="blue")

c, addr= s.accept()

print("Connected with ",addr)

def send():
	global msg
	msg= x.get()

	c.send(bytes(msg,'utf-8'))

def income():
	m=c.recv(1024).decode()
	y.set(m)


x=tk.StringVar()
y=tk.StringVar()
l= tk.Label(root,textvariable=y,text='')

l.place(x=40, y=55)

e= tk.Entry(root, textvariable=x)

e.place(x=40, y=105, height=30,width=320)

b=tk.Button(root, text="send",command=send, bg="red", fg="white")

b.place(x=160,y=140,height=40,width=80)

b2=tk.Button(root, text="Refresh",command=income, bg="red", fg="white")

b2.place(x=260,y=140,height=20,width=40)

root.mainloop()
