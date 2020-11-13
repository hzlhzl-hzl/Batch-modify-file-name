import os
import sys 
import tkinter
import tkinter.simpledialog
from tkinter.filedialog import askdirectory

#下面是GUI界面
class GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文件名批量修改工具v1.0")           #窗口名
        self.init_window_name.geometry('450x120+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.init_window_name.geometry('1068x681+10+10')
        self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.8)                          #虚化，值越小虚化程度越高
        #标签
        self.name_in = tkinter.Label(self.init_window_name, text="文件名",bg="pink")
        self.name_in.grid(row=1, column=0)
        self.name_change = tkinter.Label(self.init_window_name, text="修改后的文件名",bg="pink")
        self.name_change.grid(row=2, column=0)
        self.path = tkinter.Label(self.init_window_name, text="文件夹路径",bg="pink")
        self.path.grid(row=3, column=0)
        #文本框
        self.name_in_text = tkinter.Text(self.init_window_name, width=20, height=1,fg='red')  #原始数据录入框
        self.name_in_text.grid(row=1, column=3, rowspan=1, columnspan=1)
        self.name_change_text = tkinter.Text(self.init_window_name, width=20, height=1,fg='red')  #修改后文件名
        self.name_change_text.grid(row=2, column=3, rowspan=1, columnspan=1)
        self.path_text = tkinter.Text(self.init_window_name, width=40, height=1,fg='red')  #路径
        self.path_text.grid(row=3, column=3, rowspan=1, columnspan=1)
        #按钮
        self.change_filename_button2 = tkinter.Button(self.init_window_name, text="修改", bg="lightblue", width=10, command=self.change_filename)  # 调用内部方法
        self.change_filename_button2.grid(row=10, column=3)
    # def myprint(self):
    #     user=self.path_text.get(1.0,"current")#获取文本框内容 = x
    #     print(user)
    def change_filename(self): 
        file_path = self.path_text.get(1.0,"current")
        file_path = file_path.replace("\\\\","\\")
        now_name  = self.name_in_text.get(1.0,"current")
        now_name  = now_name.rstrip() 
        new_name  = self.name_change_text.get(1.0,"end")
        new_name  = new_name.rstrip() 
        # file_path = r'E:\python\prj\test\ceshi'
        # now_name  = '333.txt'
        # new_name  = 'wdwd3.txt'
        print(file_path,now_name,new_name)
        for filepath, dirnames, filenames in os.walk(file_path):     #用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
            for filename in filenames:     #遍历列表下的文件路径，子文件夹名,子文件名
                if filename == now_name:#如果文件名是 1.xlsx （1.xlsx可以更据你的需要换成要改变的文件名），
                                        #则修改为 K1223+376.xlsx（K1223+376.xlsx可以替换为要变成的文件名）
                                        #注意：子文件夹内不能有名字和改变后一样的文件，此程序可以改变路径文件夹下所有的子文件（包括子文件夹里的）
                    os.rename(os.path.join(filepath,now_name),os.path.join(filepath,new_name))  #子文件重命名
                    print ("change successfully")   #输出提示
def gui_start():
    init_window = tkinter.Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
gui_start()
    # now_name  = '111.txt'                         #文件修改前的名字
    # new_name  = 'ktbyz1.txt'                      #文件修改后的名字
    # file_path = r'E:\python\prj\test\ceshi'    #运行程序前，记得修改主文件夹路径，路径为包含子文件夹的文件夹
  