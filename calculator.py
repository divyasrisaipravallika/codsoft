from tkinter import *
first_num=0
ma=''
def calc(math_type):
    global first_num,ma
    ma=math_type
    first_num=op.get()
    ge()
def equal():
    result=''
    global first_num
    second_num=op.get()
    ge()
    if ma=='add':result=int(first_num)+int(second_num)
    elif ma=='sub':result=int(first_num)-int(second_num)
    elif ma=='mul':result=int(first_num)*int(second_num)
    elif ma=='div':result=int(first_num)/int(second_num)
    op.insert(0,result)
def ge():
    op.delete(0,len(op.get()))
def btn_clk(num):
    cur_num=op.get()
    ge()
    f_num=cur_num+num
    op.insert(0,f_num)
window=Tk()
window.title("Simple-Calculator")
op=Entry(window,font=("Arial", 20), justify=RIGHT,fg="black")
op.grid(row=0,columnspan=3)
bt1=Button(window,width=5,text="7",font="Calibral 30",command=lambda:btn_clk('7'))
bt1.grid(row=1,column=0)
bt2=Button(window,width=5,text="8",font="Calibral 30",command=lambda:btn_clk('8'))
bt2.grid(row=1,column=1)
bt3=Button(window,width=5,text="9",font="Calibral 30",command=lambda:btn_clk('9'))
bt3.grid(row=1,column=2)
bt21=Button(window,width=5,text="4",font="Calibral 30",command=lambda:btn_clk('4'))
bt21.grid(row=2,column=0)
bt22=Button(window,width=5,text="5",font="Calibral 30",command=lambda:btn_clk('5'))
bt22.grid(row=2,column=1)
bt23=Button(window,width=5,text="6",font="Calibral 30",command=lambda:btn_clk('6'))
bt23.grid(row=2,column=2)
bt31=Button(window,width=5,text="1",font="Calibral 30",command=lambda:btn_clk('1'))
bt31.grid(row=3,column=0)
bt32=Button(window,width=5,text="2",font="Calibral 30",command=lambda:btn_clk('2'))
bt32.grid(row=3,column=1)
bt33=Button(window,width=5,text="3",font="Calibral 30",command=lambda:btn_clk('3'))
bt33.grid(row=3,column=2)
bt41=Button(window,width=5,text="0",font="Calibral 30",command=lambda:btn_clk('0'))
bt41.grid(row=4,column=0)
bt42=Button(window,width=10,text="Clear",font="Calibral 30",command=ge)
bt42.grid(row=4,column=1,columnspan=2)
bt51=Button(window,width=5,text="+",font="Calibral 30",command=lambda:calc('add'))
bt51.grid(row=5,column=0)
bt52=Button(window,width=10,text="=",font="Calibral 30",command=equal)
bt52.grid(row=5,column=1,columnspan=2)
bt61=Button(window,width=5,text="-",font="Calibral 30",command=lambda:calc('sub'))
bt61.grid(row=6,column=0)
bt62=Button(window,width=5,text="*",font="Calibral 30",command=lambda:calc('mul'))
bt62.grid(row=6,column=1)
bt63=Button(window,width=5,text="/",font="Calibral 30",command=lambda:calc('div'))
bt63.grid(row=6,column=2)
window.mainloop()
