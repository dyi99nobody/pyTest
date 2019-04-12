# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import *
import xlwt
import xlrd
import re




# 银行
class Account(object):
    def __init__(self, name, password):
        workbook = xlrd.open_workbook('names.xls')
        sheet = workbook.sheet_by_index(0)
        self.user_number = sheet.nrows
        self.name = name
        self.password = password
        self.names = sheet.col_values(0)
        self.passwords = sheet.col_values(1)
        self.name_password = {}
        for i in range(self.user_number):
            self.name_password[self.names[i]] = self.passwords[i]

    # 修改密码
    def change_password(self):
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        if self.name not in self.names:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nSorry, but you are not our user yet\nPlease create an account first.')
        elif self.password == self.name_password[self.name]:
            for i in range(len(self.names)):
                sheet.write(i, 0, self.names[i])
                sheet.write(i, 1, self.passwords[i])
            sheet.write(self.names.index(self.name), 1, self.password)
            workbook.save('names.xls')
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nYour password has been changed.')
        else:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nSorry, \nTo change your password you have to login first.')

    # 验证密码
    def authenticate(self):
        if self.name not in self.names:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nSorry but you are not our customer, \nOr you have input wrong password,\nPlease Create  an account')
        elif self.password != self.name_password[self.name]:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nWrong password! Try again.')
        else:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nWelcome back!')

    # 修改用户名
    def change_name(self):
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        if self.password not in self.passwords:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nSorry but you are not our customer, \nOr you have input wrong password,\n Or please Create  an account')
        else:
            for i in range(len(self.names)):
                sheet.write(i, 0, self.names[i])
                sheet.write(i, 1, self.passwords[i])
            sheet.write(self.passwords.index(self.password), 0, self.name)
            workbook.save('names.xls')
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nyour name has been changed')

    # 创建账户
    def create_account(self):
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        if self.name not in self.names:
            for i in range(len(self.names)):
                sheet.write(i, 0, self.names[i])
                sheet.write(i, 1, self.passwords[i])
            sheet.write(self.user_number, 0, self.name)
            sheet.write(self.user_number, 1, self.password)
            workbook.save('names.xls')
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nCongradulations! You are now part of us.\n Please login now.')
        else:
            tkTextInfo.delete(0.0, END)
            tkTextInfo.insert('insert', '\nYou are already our user, please check your password.')


def login():
    name = tkInputBoxName.get()
    password = tkInputBoxPassword.get()
    check = Account(name, password)
    check.authenticate()


def create_account():
    name = tkInputBoxName.get()
    password = tkInputBoxPassword.get()
    check = Account(name, password)
    check.create_account()


def reset_name():
    name = tkInputBoxName.get()
    password = tkInputBoxPassword.get()
    check = Account(name, password)
    check.change_name()
    tkTextInfo.insert('insert', '\nReinput your name and press "Reset my name" again to change your name.')


def reset_password():
    name = tkInputBoxName.get()
    password = tkInputBoxPassword.get()
    check = Account(name, password)
    check.change_password()
    tkTextInfo.insert('insert', '\nReinput your password and press "Reset my password" again to change your password.')


# 设置UI界面
window = tk.Tk()
window.title('Bank Account')
window.geometry('400x300')
tkInputBoxName = tk.Entry(window)
tkInputBoxName.pack()
tkInputBoxPassword = tk.Entry(window, show='*')
tkInputBoxPassword.pack()
tkButtonLogin = tk.Button(window, text='Login', command=login).pack()
tkButtonCreate = tk.Button(window, text='Create  an account', command=create_account).pack()
tkButtonResetName = tk.Button(window, text='Reset my name', command=reset_name).pack()
tkButtonResetPassword = tk.Button(window, text='Reset my password', command=reset_password).pack()
tkTextInfo = tk.Text(window, width=50, height=20)
tkTextInfo.pack()

window.mainloop()
