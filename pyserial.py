# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from pathlib import Path
import tkinter.messagebox as tkm
import tkinter.font as tkFont
import hashlib
import ctypes 

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  

tool_gui = Tk()  

class OPEN:
    def __init__(self,root):
        self.root = root
        run_but = Button(self.root,text = "打开串口",bg = 'Aqua',bd = 2,width =16,command = self.close_serial)
        run_but.place(x=60,y=235)
    def close_serial(self):
        run_but = Button(self.root,text = "关闭串口",bg = 'Tomato',bd = 2,width =16,command = self.open_serial)
        run_but.place(x=60,y=235)
    def open_serial(self):
        run_but = Button(self.root,text = "打开串口",bg = 'Aqua',bd = 2,width =16,command = self.close_serial)
        run_but.place(x=60,y=235)

def rx_comb(root):
    port_var = StringVar()
    port_comb = ttk.Combobox(root,textvariable = port_var,width = 15)
    frez_var = StringVar()
    frez_comb = ttk.Combobox(root,textvariable = frez_var,width = 15)
    check_var = StringVar()
    check_comb = ttk.Combobox(root,textvariable = check_var,width = 15)
    stop_var = StringVar()
    stop_comb = ttk.Combobox(root,textvariable = stop_var,width = 15)
    data_var = StringVar()
    data_comb = ttk.Combobox(root,textvariable = data_var,width = 15)

    port_comb['values'] = ('COM3','COM4','COM5','COM6')
    port_comb.current(1)
    frez_comb['values'] = ('115200','9600','4800','1200')
    frez_comb.current(0)
    check_comb['values'] = ('NONE','ODD','EVEN','MASK')
    check_comb.current(0)
    data_comb['values'] = ('8','7','6','5')
    data_comb.current(0)
    stop_comb['values'] = ('1','1.5','2')
    stop_comb.current(1)

    port_comb.place(x=100,y=10)
    frez_comb.place(x=100,y=60)
    check_comb.place(x=100,y=105)
    data_comb.place(x=100,y =150)
    stop_comb.place(x=100,y=195)


def rx_button(root):
    clear_but = Button(root,text = "清空接受区域",bg = "DarkOrange",bd = 2,width =10)
    stop_but = Button(root,text = "停止显示",bg = "DarkOrange",bd = 2,width =10)
    clear_but.place(x=20,y=280)
    stop_but.place(x=120,y=280)


def rx_label_gen(root):
    dx= 0
    dy = 0
    port_label = Label(root,text = "端口选择",bg = "lightblue",bd = 5,width = 10)
    frez_label = Label(root,text = "波特率",bg = "lightblue",bd = 5,width = 10)
    check_label = Label(root,text = "校验位",bg = "lightblue",bd = 5,width = 10)
    data_label = Label(root,text = "数据位",bg = "lightblue",bd = 5,width = 10)
    stop_label = Label(root,text = "停止位",bg = "lightblue",bd = 5,width = 10)
    port_label.place(x=5,y=10)
    frez_label.place(x=5,y=55)
    check_label.place(x=5,y=100)
    data_label.place(x=5,y=145)
    stop_label.place(x=5,y=190)

def rx_text(root):
    rx_data_label = Label(root,text = "接收数据窗口",bg = "lightblue")
    rx_data_text =  Text(root,width=68,height=20)
    rx_data_label.place(x=450,y=10)
    rx_data_text.place(x=250,y=40)

def tx_button(root):
    tool_str = IntVar()
    #tool_str.set(1)
    method_label =  Label(root,text = "方式",bg = "lightblue",height = 3)
    aut_send_but = Radiobutton(root, text='自动发送数据',variable=tool_str,value=0, indicatoron=True)
    noaut_send_but = Radiobutton(root, text='手动发送数据',variable=tool_str,value=1, indicatoron=True)

    method_label.place(x=5,y=35)
    aut_send_but.place(x=40,y=30)
    noaut_send_but.place(x=40,y=70)

    data_str = IntVar()
    #data_str.set(1)
    data_label =  Label(root,text = "数据",bg = "lightblue",height =3)
    bin_send_but = Radiobutton(root, text='二进制数据',variable=data_str,value=0, indicatoron=True)
    hex_send_but = Radiobutton(root, text='十六进制数据',variable=data_str,value=1, indicatoron=True)
    data_label.place(x=5,y=145)
    bin_send_but.place(x=40,y=140)
    hex_send_but.place(x=40,y=180)

    clear_but =  Button(root,text = "清空发送区域",bg = "DarkOrange",bd = 2,width =10)
    clear_but.place(x=60,y=250)


def tx_label(root):
    file_label =  Label(root,text = "文件名",bg = "lightblue")
    file_var = StringVar()
    file_entry = Entry(root,textvariable =file_var,width = 25,)
    file_entry.place(x=50,y=220)
    file_label.place(x=5,y=220)

def rsv_button(root):
    global tool_gui
    quit_but = Button(root,text = "退出",bg = "DarkOrange",bd = 2,width =10,command = tool_gui.quit)
    quit_but.place(x=200,y=600)



def tx_text(root):
    tx_data_label = Label(root,text = "发送数据窗口",bg = "lightblue")
    tx_data_text =  Text(root,width=68,height=21)
    tx_data_label.place(x=450,y=2)
    tx_data_text.place(x=250,y=30)

def place_gui(root):
    rsv_lab =  ttk.LabelFrame(root,text = "等待开发区域")
    rsv_lab.pack(fill=BOTH, expand=FALSE, padx=5, pady=5,side = RIGHT,ipadx= 148)

    rx_ctrl_lab = ttk.LabelFrame(root,text = "接收区域")
    rx_ctrl_lab.pack(fill=BOTH, expand=YES, padx=10, pady=2)

    
    tx_ctrl_lab = ttk.LabelFrame(root,text = "发送区域")
    tx_ctrl_lab.pack(fill=BOTH, expand=YES, padx=10, pady=2)

    rx_label_gen(rx_ctrl_lab)
    rx_comb(rx_ctrl_lab)
    rx_button(rx_ctrl_lab)
    test = OPEN(rx_ctrl_lab)
    #serial_choose(rx_ctrl_lab)
    rx_text(rx_ctrl_lab)

    tx_button(tx_ctrl_lab)
    tx_text(tx_ctrl_lab)
    tx_label(tx_ctrl_lab)

    rsv_button(rsv_lab)


def define_gui(root):
    place_gui(root)
    helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
    root.title("八戒V1.0")
    root.geometry('1068x680+10+10')
    root.resizable(0, 0)
    root.attributes("-alpha",1.0)
    root.iconbitmap('bajie.ico')
    root.mainloop()
    

if __name__ == "__main__":
     
    define_gui(tool_gui)
    
