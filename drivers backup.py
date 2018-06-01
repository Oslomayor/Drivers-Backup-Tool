# 14:51, June 1st, 2018 @ Dorm 602
# GUI 小程序, 驱动备份小工具

# To do:
# 1.运行dism需要 CMD 管理员权限

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


# 安全文件夹路径
backup_dir = ''
# Windows cmd 驱动备份命令
drivers_backup_cmd = 'dism /online /export-driver /destination:'
# Windows cmd 驱动安装命令，没成功，提示“错误 50”
drivers_install_cmd = 'dism /online /Add-Driver /Driver:' + ' /Recurse'

def select_dir():
    global backup_dir
    # 选择安全文件夹
    if messagebox.askokcancel('镇长出品', '选择一个安全文件夹存放驱动') == False:
        os._exit(0)
    backup_dir = filedialog.askdirectory()

def start_backup():
    global backup_dir
    if backup_dir == '':
        messagebox.askquestion('Error!','请选择一个安全文件夹')
    else:
        print(backup_dir)
        os.system(drivers_backup_cmd + backup_dir)

def main():
    top = tk.Tk(className='驱动备份小工具V1-镇长出品')
    top.minsize(400, 200)

    # 按钮配置
    start_button = tk.Button(top, text="点击制作驱动备份", command=start_backup)
    select_button = tk.Button(top, text="选择安全文件夹", command=select_dir)

    # 上件
    start_button.pack()
    select_button.pack()

    # 窗体循环
    top.mainloop()

if __name__ == '__main__':
    main()

