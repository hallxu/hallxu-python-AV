#病毒库2022.9.3 16:00
#本软件的开发者并非安全专家，处理流程来自微步云沙箱的处置建议！！！



import hashlib
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator
from tkinter import ttk
import tkinter.filedialog
import threading
def ts(bt,text):
    messagebox.showinfo(bt, text)
def xz(bt,text):

    # 弹出对话框
    result = tkinter.messagebox.askokcancel(title=bt, message=text)


    return result
def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()
def gxgg(text):#更新公告
    messagebox.showinfo("公告", text)

def xzwj():#选择文件
    fn = tkinter.filedialog.askopenfilename(title='请选择需要查杀的文件', filetypes=[('所有文件', '.*')])
    return fn
def cs():
    lujing = xzwj()
    FileMD5 = GetMD5FromLocalFile(lujing)
    bingdu = ('eda588c0ee78b585f645aa42eff1e57a')
    bingdu2 = ('19dbec50735b5f2a72d4199c4e184960')
    bingdu3 = ('815b63b8bc28ae052029f8cbdd7098ce')
    bingdu4 = ('c71091507f731c203b6c93bc91adedb6')
    bingdu5 = ('0a456ffff1d3fd522457c187ebcf41e4')
    bingdu6 = ('1aa4c64363b68622c9426ce96c4186f2')
    bingdu7 = ('d214c717a357fe3a455610b197c390aa')
    bingdu8 = ('b14299fd4d1cbfb4cc7486d978398214')
    bingdu9 = ('dffe6e34209cb19ebe720c457a06edd6')
    bingdu10 = ('512301c535c88255c9a252fdf70b7a03')
    bingdu11 = ('d4a05ada747a970bff6e8c2c59c9b5cd')
    bingdu12 = ('ad41ec81ab55c17397d3d6039752b0fd')
    bingdu13 = ('a57db79f11a8c58d27f706bc1fe94e25')
    bingdu14 = ('fc14eaf932b76c51ebf490105ba843eb')
    bingdu15 = ('2a92da4b5a353ca41de980a49b329e7d')
    bingdu16 = ('68abd642c33f3d62b7f0f92e20b266aa')
    bingdu17 = ('ff5e1f27193ce51eec318714ef038bef')
    bingdu18 = ('4c36884f0644946344fa847756f4a04e')
    bingdu19 = ('2391109c40ccb0f982b86af86cfbc900')
    bingdu20 = ('915178156c8caa25b548484c97dd19c1')
    bingdu21 = ('dac5f1e894b500e6e467ae5d43b7ae3e')
    bingdu22 = ('84c82835a5d21bbcf75a61706d8ab549')
    bingdu23 = ('db349b97c37d22f5ea1d1841e3c89eb4')
    bingdu24 = ('1de73f49db23cf5cc6e06f47767f7fda')
    bingdu25 = ('71b6a493388e7d0b40c83ce903bc6b04')
    bingdu26 = ('b1a85fdd944c21070a0551e8c59a6158')
    bingdu27 = ('e60e767e33acf49c02568a79d9cbdadd')
    bingdu28 = ('f5ecda7dd8bb1c514f93c09cea8ae00d')
    bingdu29 = ('6cdcb9f86972efc4cfce4b06b6be053a')
    bingdu30 = ('f785b1a9a657aca7e70d16ac5effaabd')
    bingdu31 = ('ebcdda10fdfaa38e417d25977546df4f')
    bingdu32 = ('e22638ce44a5f9faf9dd450438c1d492')
    bingdu33 = ('de35f0262c089cc880fe8cee5d6b0156')
    bingdu34 = ('a635d6a35c2fc054042b6868ef52a0c3')
    bingdu35 = ('c4391b3b073bb1354afef0f1260b8fb8')
    bingdu36 = ('cd8c86863628f4d0c7f54fc3350fb1d9')
    bingdu37 = ('e60e767e33acf49c02568a79d9cbdadd')
    bingdu38 = ('af6d91121887f5bb0a85a06b1ded0db7')
    ###后门
    bingdu39 = ('29b1550a1de57efda52b039aedeb4710')
    bingdu40 = ('203c4f24052a8df191e7c9fdc74a3b38')
    bingdu41 = ('7d8dcebef26d40a717a1dbdf895c8676')
    bingdu42 = ('')
    ###以上是病毒库
    ###下面是发现病毒的处理步骤

    if FileMD5 == bingdu:

        ts('查杀结果', '发现恶搞程序！！！类型：Trojan.Win32.FormatAll.V')
        xuan = xz('处理方式', "是否直接处理")

        if xuan == True:

            os.remove(lujing)
            os.system('taskkill /f /im %s' % 'ZhuYao.bat')
            os.remove(r'C:\GYF\*')
            os.system('reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system" /f')
        else:
            print(2)
            os.remove(lujing)

    elif FileMD5 == bingdu2:
        print('发现病毒！！病毒类型：Trojan.Win32.MEMZ.A')
        os.remove(lujing)
    elif FileMD5 == bingdu3:
        print('发现恶搞程序，类型：Virus.Win32.Blamon')
        os.remove(lujing)
    elif FileMD5 == bingdu4:
        print('发现危险恶搞程序，类型：Trojan.Win32.Disabler')
        xuab = input('1 = 运行前 0 = 运行后清理')
        if xuab == 1:
            os.remove(lujing)
            os.remove(r'c:\1.bat')
            os.remove(r'c:\drawerror.exe')
            os.remove(r'c:\Ghost.exe')
            os.remove(r'c:\羽翼.bat')
            os.system(
                r'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskMgr" /f')
            os.system(
                r'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoLogOff" /f')
            os.system(
                r'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoRecentDocsMenu" /f')
        else:
            os.remove(lujing)
    elif FileMD5 == bingdu5:
        print('发现蠕虫病毒，类型：Worm.VBS.yuyun.A / Cantix.A')
        os.remove(lujing)
    elif FileMD5 == bingdu6:
        print('发现病毒！！此病毒会感染主板BIOS，引导扇区，类型:TrojanDownloader:Win32.Jadtre.B')
        os.remove(lujing)
    elif FileMD5 == bingdu7:
        print('发现病毒！！病毒类型：Virus.Win32.disttrackA')
        os.remove(lujing)
    elif FileMD5 == bingdu8:
        print('发现病毒！！病毒类型：Virus.Win32.disttrackA')
        os.remove(lujing)
    elif FileMD5 == bingdu9:
        print('发现病毒！！类型：Trojan:Win32/Dynamer!rfn')
        os.remove(lujing)
    elif FileMD5 == bingdu10:
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        os.remove(lujing)
    elif FileMD5 == bingdu11:
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        os.remove(lujing)
    elif FileMD5 == bingdu12:
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        os.remove(lujing)
    elif FileMD5 == bingdu13:
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        os.remove(lujing)
    elif FileMD5 == bingdu14:
        print('发现蠕虫病毒！！病毒类型：Net-Worm.Win32.Blaster.A')
        os.remove(lujing)
    elif FileMD5 == bingdu15:
        print('发现蠕虫病毒！！病毒类型：Net-Worm.Win32.Sasser.A')
        os.remove(lujing)
    elif FileMD5 == bingdu16:
        print('发现病毒！！病毒类型：Virus.Win32.Ramnit/Nimnul.A')
        os.remove(lujing)
    elif FileMD5 == bingdu17:
        print('发现病毒！！病毒类型：Virus.Win32.Ramnit/Nimnul.A')
        os.remove(lujing)
    elif FileMD5 == bingdu18:
        print('发现病毒！！病毒类型：Virus.Win32.Xorer.A')
        num = input('运行后杀毒输入1深度清理病毒 运行前杀毒输入0:')
        if num == 1:
            os.remove(lujing)
            os.system('taskkill /f /im %s' % 'regsvr32.exe')
            os.system('taskkill /f /im %s' % 'cacls.exe')
            os.remove(r'C:\NetApi00.sys')
            os.remove(r'C:\Windows\System32\com\smss.exe')
            os.remove(r'C:\Windows\System32\com\lsass.exe')
            os.remove(r'C:\Windows\System32\dnsq.dll')
            os.system(
                'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Folder\SuperHidden" /f')
        elif num == 0:
            os.remove(lujing)
        else:
            os.remove(lujing)
    elif FileMD5 == bingdu19:
        print('发现AV终结者！！病毒类型：Worm.Win32.Pabug')
        os.remove(lujing)
    elif FileMD5 == bingdu20:
        print('发现病毒！！此病毒会删除文件！！！病毒类型：Worm.Win32.AutoRun.xxx')
        os.remove(lujing)
    elif FileMD5 == bingdu21:
        print('发现病毒！！此病毒会删除文件！！！病毒类型：Worm.Win32.AutoRun.xxx')
        os.remove(lujing)
    elif FileMD5 == bingdu22:
        os.remove(lujing)
        print('发现勒索病毒！！病毒类型：Ransom.Win32.WannaCryptor')
        os.remove(lujing)
    elif FileMD5 == bingdu23:
        print('发现勒索病毒！！病毒类型：Ransom.Win32.WannaCryptor')
        os.remove(lujing)
    elif FileMD5 == bingdu24:
        print('发现勒索病毒！！病毒类型：Ransom.Win32.WannaRen')
        os.remove(lujing)
        print('火绒已经发布解密工具')
        print('链接：https://www.huorong.cn/download/tools/wannaren_decryptor/HRDecryptor.exe')
    elif FileMD5 == bingdu25:
        print('发现勒索病毒！！病毒类型：Ransom.Win32.Petya')
        os.remove(lujing)
    elif FileMD5 == bingdu26:
        print('发现后门病毒！！类型：Backdoor.Win32.Poison.A')
        os.remove(lujing)
    elif FileMD5 == bingdu27:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu28:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu29:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu30:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu31:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu32:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu33:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu34:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu35:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu36:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu37:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu38:
        print('发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu39:
        print('发现后门木马！！')
        os.remove(lujing)
    elif FileMD5 == bingdu40:
        print('发现后门木马！！')
        os.remove(lujing)
    elif FileMD5 == bingdu41:
        print('发现后门木马！！')
        os.remove(lujing)
    else:
        ts('查杀结果','并未发现病毒')

def GetMD5FromLocalFile(filename):
    """
    Get local file's MD5 Info.
    @param filename:file path & file name
    @return:MD5 Info
    """
    file_object = open(filename, 'rb')
    file_content = file_object.read()
    file_object.close()
    file_md5 = hashlib.md5(file_content)
    return file_md5.hexdigest()




if __name__ == '__main__':

    window = Tk()  # 创建TK窗口

    window.title("杀毒软件")  # 窗口标题
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 700
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    window.resizable(width=False, height=False)
    huanying = Label(window, text="欢迎来到杀毒软件！", font=("微软雅黑", 14))
    huanying.pack()
    csan = Button(window, text="单文件查杀", command=lambda: thread_it(cs))
    csan.place(x=300, y=100)
    gxgg('新增2款支持清理的病毒：中华黑豹病毒,卢本伟病毒\n病毒库：2022.9.3 08:00\n此为开源版本')
    window.mainloop()


###删除注册表为测试功能
