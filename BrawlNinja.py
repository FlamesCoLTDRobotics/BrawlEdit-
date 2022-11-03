import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os
import sys
import struct

class SmashBrosBrawlHexEditor:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text='Edit', width=25, command=self.open_file)
        self.button2 = tk.Button(self.frame, text='Close', width=25, command=self.close_windows)
        self.button1.pack()
        self.button2.pack()
        self.frame.pack()

    def open_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Wii ISO", "*.iso"), ("Wii U ISO", "*.wud")])
        if file_path:
            self.edit(file_path)

    def edit(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
                if len(data) > 0:
                    self.edit_file(data)

    def edit_file(self, data):
        # get the offset of the file
        offset = self.get_offset(data)
        if offset > 0:
            # get the data from the file
            file_data = self.get_file_data(data, offset)
            if len(file_data) > 0:
                # write the data to the file
                # get the code to modify the game with a gpt2 autocorrect
                self.get_code(file_data, offset)
                self.write_file(file_data)

    def get_offset(self, data):
        offset = 0
        if len(data) > 0:
            # get the offset of the file
            offset = struct.unpack('<I', data[0x424:0x428])[0] + 0x1c
        return offset

    def get_file_data(self, data, offset):
        file_data = b''
        if len(data) > 0 and offset > 0:
            # get the file data
            file_data = data[offset:]
        return file_data

    def write_file(self, file_data):
        if len(file_data) > 0:
            # get the file name
            file_name = tk.filedialog.asksaveasfilename(filetypes=[("Wii ISO", "*.iso"), ("Wii U ISO", "*.wud")])
            if file_name:
                # write the file
                with open(file_name, 'wb') as f:
                    f.write(file_data)
                    tk.messagebox.showinfo("Success", "File saved successfully")

    def get_code(self, file_data, offset):
        if len(file_data) > 0:
            # get the code
            code = tk.simpledialog.askstring("Code", "Enter the code to modify the game")
            if code:
                # convert the code to hex
                code_hex = self.code_to_hex(code)
                if len(code_hex) > 0:
                    # write the code to the file
                    self.write_code(file_data, code_hex, offset)

    def code_to_hex(self, code):
        code_hex = b''
        if code:
            # convert the code to hex
            code_hex = code.encode('utf-8')
            code_hex = code_hex.hex()
            code_hex = bytes.fromhex(code_hex)
        return code_hex
        # disable the maximize button

    def write_code(self, file_data, code_hex, offset):
        if len(file_data) > 0 and len(code_hex) > 0:
            # write the code to the file
            file_data = file_data[:offset] + code_hex + file_data[offset + len(code_hex):]
            tk.messagebox.showinfo("Success", "File saved successfully")

    def close_windows(self):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Smash Bros Brawl Hex Editor')
    root.geometry("400x300")
    app = SmashBrosBrawlHexEditor(root)
    root.mainloop()
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os
import sys
import struct
import pyautogui
import time

class SmashBrosBrawlHexEditor:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text='Edit', width=25, command=self.open_file)
        self.button2 = tk.Button(self.frame, text='Close', width=25, command=self.close_windows)
        self.button1.pack()
        self.button2.pack()
        self.frame.pack()

    def open_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Wii ISO", "*.iso"), ("Wii U ISO", "*.wud")])
        if file_path:
            self.edit(file_path)

    def edit(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
                if len(data) > 0:
                    self.edit_file(data)

    def edit_file(self, data):
        # get the offset of the file
        offset = self.get_offset(data)
        if offset > 0:
            # get the data from the file
            file_data = self.get_file_data(data, offset)
            if len(file_data) > 0:
                # write the data to the file
                # get the code to modify the game with a gpt2 autocorrect
                self.get_code(file_data, offset)
                self.write_file(file_data)


### disable the maximize button
class SmashBrosBrawlHexEditorWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

    def get_offset(self, data):
        offset = 0
        if len(data) > 0:
            # get the offset of the file
            offset = struct.unpack('<I', data[0x424:0x428])[0] + 0x1c
        return offset

    def get_file_data(self, data, offset):
        file_data = b''
        if len(data) > 0 and offset > 0:
            # get the file data
            file_data = data[offset:]
        return file_data

    def write_file(self, file_data):
        if len(file_data) > 0:
            # get the file name
            file_name = tk.filedialog.asksaveasfilename(filetypes=[("Wii ISO", "*.iso"), ("Wii U ISO", "*.wud")])
            if file_name:
                # write the file
                with open(file_name, 'wb') as f:
                    f.write(file_data)
                    tk.messagebox.showinfo("Success", "File saved successfully")

    def get_code(self, file_data, offset):
        if len(file_data) > 0:
            # get the code
            code = tk.simpledialog.askstring("Code", "Enter the code to modify the game")
            if code:
                # convert the code to hex
                code_hex = self.code_to_hex(code)
                if len(code_hex) > 0:
                    # write the code to the file
                    self.write_code(file_data, code_hex, offset)

    def code_to_hex(self, code):
        code_hex = b''
        if code:
            # convert the code to hex
            code_hex = code.encode('utf-8')
            code_hex = code_hex.hex()
            code_hex = bytes.fromhex(code_hex)
        return code_hex
        # disable the maximize button

    def write_code(self, file_data, code_hex, offset):
        if len(file_data) > 0 and len(code_hex) > 0:
            # write the code to the file
            file_data = file_data[:offset] + code_hex + file_data[offset + len(code_hex):]
            tk.messagebox.showinfo("Success", "File saved successfully")

def open_iso():
    # open the iso in dolphin
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('dolphin')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(1)
    pyautogui.typewrite('C:\\Users\\joshu\\Desktop\\Super Smash Bros. Brawl.iso')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    def close_windows(self):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Smash Bros Brawl Hex Editor')
    root.geometry("400x300")
    app = SmashBrosBrawlHexEditor(root)
    root.mainloop()
