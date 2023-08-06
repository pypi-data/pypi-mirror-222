#! /usr/bin/env python
'''
@Author: xiaobaiTser
@Email : 807447312@qq.com
@Time  : 2023/6/16 0:04
@File  : Demo.py
'''

import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import itertools
import string
import time
import threading
import hashlib

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_label = tk.Label(self, text="选择需要解密的文件：")
        self.file_label.pack(side="top")

        self.file_button = tk.Button(self, text="选择文件", command=self.select_file)
        self.file_button.pack(side="top")

        self.len_label = tk.Label(self, text="密码长度（6-12位）：")
        self.len_label.pack(side="top")

        self.len_var = tk.StringVar()
        self.len_var.set("6")
        self.len_entry = tk.Entry(self, textvariable=self.len_var)
        self.len_entry.pack(side="top")

        self.crack_button = tk.Button(self, text="开始解密", command=self.start_cracking)
        self.crack_button.pack(side="top")

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(side="top")

    def calculate_sha1(self, file_path):
        sha1_hash = hashlib.sha1()
        with open(file_path, 'rb') as file:
            # 以二进制模式打开文件，并逐块更新哈希值
            for chunk in iter(lambda: file.read(4096), b''):
                sha1_hash.update(chunk)
        return sha1_hash.hexdigest()

    def select_file(self):
            self.file_path = filedialog.askopenfilename()

    def generate_passwords(self, length):
        chars = string.digits #string.ascii_letters + string.digits
        for password in itertools.product(chars, repeat=length):
            yield "".join(password)

    def crack_password(self):
        length = int(self.len_var.get())
        if not 6 <= length <= 12:
            self.result_label.config(text="密码长度必须在6-12位之间")
            return

        self.result_label.config(text="正在解密，请稍候...")
        start_time = time.time()

        hashcat_path = r"E:\Program Files\hashcat-6.2.6\hashcat.exe" # hashcat可执行文件的路径，根据实际情况修改
        hash_type = "100" # 哈希类型，根据实际情况修改,100为SHA1
        wordlist_file = "wordlist.txt" # 字典文件的路径，根据实际情况修改
        output_file = os.path.join(os.getcwd(), "output.txt") # 密码破解结果输出文件的路径

        with open(wordlist_file, "w") as f:
            for password in self.generate_passwords(length):
                f.write(password + "\n")

        command = f"{hashcat_path} -D 1 -m {hash_type} {self.calculate_sha1(self.file_path)} {wordlist_file} -o {output_file}"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = result.stdout.decode("utf-8")
        error = result.stderr.decode("utf-8")
        print(f'output==>{output}')
        print(f'error==>{error}')
        if "Session........." in output:
            with open(output_file, "r") as f:
                password = f.read().strip()
                self.result_label.config(text=f"解密成功，密码是：{password}")

        else:
            self.result_label.config(text="解密失败")

        if os.path.isfile(wordlist_file): os.remove(wordlist_file)
        if os.path.isfile(output_file): os.remove(output_file)

        end_time = time.time()
        self.result_label.config(text=f"用时：{end_time - start_time:.2f}秒")

    def start_cracking(self):
        if not hasattr(self, "file_path"):
            self.result_label.config(text="请选择需要解密的文件")
            return

        self.crack_thread = threading.Thread(target=self.crack_password)
        self.crack_thread.start()

root = tk.Tk()
app = Application(master=root)
app.mainloop()