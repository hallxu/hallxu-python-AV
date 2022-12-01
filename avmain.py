#病毒库2022.11.3 19:00




import hashlib
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator
from tkinter import ttk
import tkinter.filedialog
import threading



def qp():
    main = "project1.exe"
    r_v = os.system(main)
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
    bingdu42 = ('76529dc875b43a64a978047b9e138741')
    bingdu43 = ('99724fc3358d168c6f3f375ef1b15cbe')
    bingdu44 = ('73f5e352172e416f6a3970132b551dc3')
    bingdu45 = ('002c4c4ab64bc1fec1a19f9c697e71d3')
    bingdu46 = ('927d0d390ef6ed41c08422710c7946c6')
    bingdu47 = ('feb746f569528c37b59c2e2cee3bcd91')
    bingdu48 = ('23530938e6e8dad252f6330fa1aea637')
    bingdu49 = ('f5dceb6097a46b01202fececfd494de6')
    bingdu50 = ('0c22acdd83ec8154ee2ecb6d4cc0f4dc')
    bingdu51 = ('194862990b45aa89214befc4da19fead')
    bingdu52 = ('af1801ebb4098624686a4bfdba897028')
    bingdu53 = ('205a98bf5d112c59e3aa670dec6cd401')
    bingdu54 = ('ff202fe32785e6419374e13b67f89723')
    bingdu55 = ('a57e6f40fba6dc770bc08b9988ee56e6')
    bingdu56 = ('08f315a6b258691d85bf8c7801808f99')
    bingdu57 = ('651a1fd3bda2573208a818b469a55d3d')
    bingdu58 = ('205a98bf5d112c59e3aa670dec6cd401')
    bingdu59 = ('09407b2f152c82b5211ae0911e5f7fc0')
    bingdu60 = ('1b369fa36a56d47a035cfd2346a1860c')
    bingdu61 = ('00a9249e28abe8150d0ed01977561f5a')
    bingdu62 = ('7febf6c335ec835ad9e57763ce9d3316')
    bingdu63 = ('8e863727e5758b28c62b2b9acfd4b41a')
    bingdu64 = ('a1e5f812cb6400e2da4012c6ccc6235b')
    bingdu65 = ('f3f46f6a1cc57112cb6873654bc801b9')
    bingdu66 = ('dc1002ef3e3578da806703552c68501b')
    bingdu67 = ('6e9fdb1ac3859e908475bc69b239435a')
    bingdu68 = ('9a1c784b6b8cab8f3d5f859404f0500d')
    bingdu69 = ('c1d6fcea01ed82777e63ebc9e6f085ce')
    bingdu70 = ('0b3375428388481d8887cf39e97a5bad')
    bingdu71 = ('3859d6711896623258a227a1acc2a1a8')
    bingdu72 = ('86dcd00ca608d4024ff1731d0429d1d6')
    bingdu73 = ('e05e3a37aa2054cd9db926c38c62b656')
    bingdu74 = ('3cdd22e312cb1d1baa01440736660ac1')
    bingdu75 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu76 = ('96d097045736a2a1526d63c2d83a6b22')
    bingdu77 = ('4520eee1da294b6c8428cea200b81d18')
    bingdu78 = ('53a7ed066adc57f945d18d6eeb60eccd')
    bingdu79 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu80 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu81 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu82 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu83 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu84 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu85 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu86 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu87 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu88 = ('144461034c1c5cf0eac3b47b0eb5f014')
    bingdu89 = ('144461034c1c5cf0eac3b47b0eb5f014')
    caidan1 = ('4e17f0afea0e93a666123a458c7fdeee')
    


    
     ###以上是病毒库
    ###下面是发现病毒的处理步骤

    if FileMD5 == bingdu:
        window.configure(bg='red')         
        ts('查杀结果', '发现恶搞程序！！！类型：Trojan.Win32.FormatAll.V')
        xuan = xz('处理方式', "是否直接处理")

        if xuan == True:

            os.remove(lujing)
            os.system('taskkill /f /im %s' % 'ZhuYao.bat')
            os.remove(r'C:\GYF\*')
            os.system('reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system" /f')
            tkinter.messagebox.showinfo('病毒处理完成！')   
        else:
            print(2)
            os.remove(lujing)

    elif FileMD5 == bingdu2:
        print('发现病毒！！病毒类型：Trojan.Win32.MEMZ.A')
        window.configure(bg='red') 
        tkinter.messagebox.showinfo('警告',"发现病毒！！病毒类型：Trojan.Win32.MEMZ.A'")
        os.remove(lujing)
    elif FileMD5 == bingdu3:
        print('发现恶搞程序，类型：Virus.Win32.Blamon')
        window.configure(bg='red') 
        tkinter.messagebox.showinfo('警告',"发现恶搞程序，类型：Virus.Win32.Blamonr")
        os.remove(lujing)
    elif FileMD5 == bingdu4:

        print('发现危险恶搞程序，类型：Trojan.Win32.Disabler')
        window.configure(bg='red') 
        tkinter.messagebox.showinfo('警告',"发现危险恶搞程序，类型：Trojan.Win32.Disabler")
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
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
        window.configure(bg='red') 
        print('发现蠕虫病毒，类型：Worm.VBS.yuyun.A / Cantix.A')
        tkinter.messagebox.showerror('警告！！','发现蠕虫病毒，类型：Worm.VBS.yuyun.A / Cantix.A')
        os.remove(lujing)
    elif FileMD5 == bingdu6:
        
        window.configure(bg='red')
        print('发现病毒！！此病毒会感染主板BIOS，引导扇区，类型:TrojanDownloader:Win32.Jadtre.B')
        tkinter.messagebox.showerror('警告','发现病毒！！此病毒会感染主板BIOS，引导扇区，类型:TrojanDownloader:Win32.Jadtre.B')
        os.remove(lujing)
    elif FileMD5 == bingdu7:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.disttrackA')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.disttrackA')
        os.remove(lujing)
    elif FileMD5 == bingdu8:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.disttrackA')
        tkinter.messagebox.showerror('警告','发现病毒！！病毒类型：Virus.Win32.disttrackA')
        os.remove(lujing)
    elif FileMD5 == bingdu9:
        window.configure(bg='red')
        print('发现病毒！！类型：Trojan:Win32/Dynamer!rfn')
        tkinter.messagebox.showerror('警告','发现病毒！！类型：Trojan:Win32/Dynamer!rfn')
        os.remove(lujing)
    elif FileMD5 == bingdu10:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.Viking.A')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.remove(lujing)

            os.remove(r'C:\Windows\System32\drivers\spo0lsv.exe')
            os.remove(r'C:\Program Files\Google\Chrome\Application\67.0.3396.99\Installer\chrmstp.exe')
            os.remove(r'C:\MSOCache\All Users\{90120000-0115-0409-0000-0000000FF1CE}-C\DW20.EXE')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\AcroTextExtractor.exe')
            os.remove(r'C:\MSOCache\All Users\{90120000-0011-0000-0000-0000000FF1CE}-C\ose.exe')
            os.remove(r'C:\Program Files\Acrylic DNS Proxy\Uninstall.exe')
            os.remove(r'C:\Program Files\Acrylic DNS Proxy\AcrylicRegExTester.exe')
            os.remove(r'C:\Program Files\Google\Chrome\Application\67.0.3396.99\nacl64.exe')
            os.remove(r'C:\Program Files\Acrylic DNS Proxy\AcrylicController.exe')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\AcroRd32.exe')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\AcroBroker.exe')
            os.remove(r'C:\MSOCache\All Users\{90120000-0115-0409-0000-0000000FF1CE}-C\dwtrig20.exe')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\AdobeCollabSync.exe')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\Eula.exe')
            os.remove(r'C:\Program Files\Acrylic DNS Proxy\AcrylicConsole.exe')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\LogTransport2.exe')
            os.remove(r'C:\Program Files\Google\Chrome\Application\67.0.3396.99\Installer\chrmstp.exe')
            os.remove(r'C:\install.exe')
            os.remove(r'C:\Program Files\Adobe\Reader 10.0\Reader\reader_sl.exe')
            os.remove(r'C:\autorun.inf')
            os.system(
                'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\svcshare" /f') 
            tkinter.messagebox.showinfo('病毒处理完成！')                  
        os.remove(lujing)
    elif FileMD5 == bingdu11:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.Viking.A')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.remove(lujing)

            os.remove(r'C:\tmpom056k\b9f9edb1f334d4cdb8728836887b6b405d7a0261efb7288d95c65e2a2198b2d2.exe')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\$$aAE12.bat')
            os.remove(r'C:\tmpom056k\b9f9edb1f334d4cdb8728836887b6b405d7a0261efb7288d95c65e2a2198b2d2.exe.exe')
            os.remove(r'C:\Windows\virDll.dll')
            os.remove(r'C:\Windows\Logo1_.exe')
            os.system(
                'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\svcshare" /f')   
            tkinter.messagebox.showinfo('病毒处理完成！')                
        else:
            os.remove(lujing)
    elif FileMD5 == bingdu12:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.Viking.A')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.remove(lujing)

            os.remove(r'C:\Windows\System32\drivers\spoclsv.exe')
            os.remove(r'C:\autorun.inf')
            os.system(
                'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\svcshare" /f')   
            tkinter.messagebox.showinfo('病毒处理完成！')            
        os.remove(lujing)
    elif FileMD5 == bingdu13:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Viking.A')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.Viking.A')
        os.remove(lujing)
    elif FileMD5 == bingdu14:
        window.configure(bg='red')
        print('发现蠕虫病毒！！病毒类型：Net-Worm.Win32.Blaster.A')
        tkinter.messagebox.showerror('警告！！','发现蠕虫病毒！！病毒类型：Net-Worm.Win32.Blaster.A')
        os.remove(lujing)
    elif FileMD5 == bingdu15:
        window.configure(bg='red')
        print('发现蠕虫病毒！！病毒类型：Net-Worm.Win32.Sasser.A')
        tkinter.messagebox.showerror('警告！！','发现蠕虫病毒！！病毒类型：Net-Worm.Win32.Sasser.A')
        os.remove(lujing)
    elif FileMD5 == bingdu16:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Ramnit/Nimnul.A')
        tkinter.messagebox.showerror('发现病毒！！病毒类型：Virus.Win32.Ramnit/Nimnul.A')
        os.remove(lujing)
    elif FileMD5 == bingdu17:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Ramnit/Nimnul.A')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.Ramnit/Nimnul.A')
        os.remove(lujing)
    elif FileMD5 == bingdu18:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Xorer.A')
        tkinter.messagebox.showerror('警告！！','发现病毒！！病毒类型：Virus.Win32.Xorer.A')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.remove(lujing)
            os.system('taskkill /f /im %s' % 'regsvr32.exe')
            os.system('taskkill /f /im %s' % 'cacls.exe')
            os.remove(r'C:\NetApi00.sys')
            os.remove(r'C:\Windows\System32\com\smss.exe')
            os.remove(r'C:\Windows\System32\com\lsass.exe')
            os.remove(r'C:\Windows\System32\dnsq.dll')
            os.system(
                'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Folder\SuperHidden" /f')
            tkinter.messagebox.showinfo('病毒处理完成！')                  
        else:
            os.remove(lujing)
    elif FileMD5 == bingdu19:
        window.configure(bg='red')
        print('发现AV终结者！！病毒类型：Worm.Win32.Pabug')
        tkinter.messagebox.showerror('警告！！','发现AV终结者病毒！！病毒类型：Worm.Win32.Pabug')
        os.remove(lujing)
    elif FileMD5 == bingdu20:
        window.configure(bg='red')
        print('发现病毒！！此病毒会删除文件！！！病毒类型：Worm.Win32.AutoRun.xxx')
        tkinter.messagebox.showerror('警告！！','发现病毒！！此病毒会删除文件！！！病毒类型：Worm.Win32.AutoRun.xxx')
        os.remove(lujing)
    elif FileMD5 == bingdu21:
        window.configure(bg='red')
        print('发现病毒！！此病毒会删除文件！！！病毒类型：Worm.Win32.AutoRun.xxx')
        tkinter.messagebox.showerror('警告！！','发现病毒！！此病毒会删除文件！！！病毒类型：Worm.Win32.AutoRun.xxx')
        os.remove(lujing)
    elif FileMD5 == bingdu22:
        window.configure(bg='red')
        os.remove(lujing)
        print('发现勒索病毒！！病毒类型：Ransom.Win32.WannaCryptor')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！病毒类型：Ransom.Win32.WannaCryptor')
        os.remove(lujing)
    elif FileMD5 == bingdu23:
        window.configure(bg='red')
        print('发现勒索病毒！！病毒类型：Ransom.Win32.WannaCryptor')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！病毒类型：Ransom.Win32.WannaCryptor')
        os.remove(lujing)
    elif FileMD5 == bingdu24:
        window.configure(bg='red')
        print('发现勒索病毒！！病毒类型：Ransom.Win32.WannaRen')
        tkinter.messagebox.showinfo("警告！！！","发现勒索病毒！！病毒类型：Ransom.Win32.WannaRenr")
        os.remove(lujing)
        print('火绒已经发布解密工具')
        tkinter.messagebox.showinfo("提示","火绒已经发布解密工具")
        tkinter.messagebox.showinfo("提示","链接：https://www.huorong.cn/download/tools/wannaren_decryptor/HRDecryptor.exe")
        print('链接：https://www.huorong.cn/download/tools/wannaren_decryptor/HRDecryptor.exe')
    elif FileMD5 == bingdu25:
        window.configure(bg='red')
        print('发现勒索病毒！！病毒类型：Ransom.Win32.Petya')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！病毒类型：Ransom.Win32.Petya')
        os.remove(lujing)
    elif FileMD5 == bingdu26:
        window.configure(bg='red')
        print('发现后门病毒！！类型：Backdoor.Win32.Poison.A')
        tkinter.messagebox.showerror('警告！！','发现后门病毒！！类型：Backdoor.Win32.Poison.A')
        os.remove(lujing)
    elif FileMD5 == bingdu27:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu28:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu29:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu30:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu31:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu32:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu33:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu34:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu35:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu36:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu37:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu38:
        window.configure(bg='red')
        print('发现勒索病毒！！')
        tkinter.messagebox.showerror('警告！！','发现勒索病毒！！')
        os.remove(lujing)
    elif FileMD5 == bingdu39:
        window.configure(bg='red')
        print('发现后门木马！！')
        tkinter.messagebox.showerror('警告！！','发现后门木马！！')
        os.remove(lujing)
    elif FileMD5 == bingdu40:
        window.configure(bg='red')
        print('发现后门木马！！')
        tkinter.messagebox.showerror('警告！！','发现后门木马！！')
        os.remove(lujing)
    elif FileMD5 == bingdu41:
        window.configure(bg='red')
        print('发现后门木马！！')
        tkinter.messagebox.showerror('警告！！','发现后门木马！！')
        os.remove(lujing)
    elif FileMD5 == bingdu42:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','硬盘逻辑锁病毒（江民炸弹）类型：Trojan:DOS/Jiang')
        os.remove(lujing) 
    elif FileMD5 == bingdu43:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现后门木马！！')  
        os.remove(lujing)
    elif FileMD5 == bingdu44:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现宏病毒 类型：Virus.Word.Twno.A！！')  
        os.remove(lujing) 
    elif FileMD5 == bingdu45:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现宏病毒 类型：Virus.Word.Chaos.A！！') 
    elif FileMD5 == bingdu46:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：PUA:Win32/Vigua.A !')  
        os.remove(lujing) 
    elif FileMD5 == bingdu47:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Virus:Win32/Virut.BR !')
        os.remove(lujing)
    elif FileMD5 == bingdu48:        
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现恶意广告程序 类型：Trojan:Win32/ToobPug 木马家族：Neoreklami !')
        os.remove(lujing)
    elif FileMD5 == bingdu49:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：JS/Spy.Banker.LJ trojan 木马家族：Banker !')
        os.remove(lujing)
    elif FileMD5 == bingdu50:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：GrayWare/Win32.Pearfoos 木马家族：Agent !')
        os.remove(lujing)
    elif FileMD5 == bingdu51:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现漏洞利用工具 类型：Exploit:O97M/CVE-2017-11882.SUTR!MTB 利用的漏洞：CVE-2017-11882 !')
        os.remove(lujing)        
    elif FileMD5 == bingdu52:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：TrojanDropper:Win32/Tnega!MSR 木马家族：无 !')
        os.remove(lujing)
    elif FileMD5 == bingdu53:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：HEUR:Trojan.Script.Generic（Kaspersky） 木马家族：Generic !')
        os.remove(lujing)                        
    elif FileMD5 == bingdu54:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan:Win32/Leonem 木马家族：Leonem !')
        os.remove(lujing)
    elif FileMD5 == bingdu55:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan:Win32/Leonem 木马家族：Leonem !')
        os.remove(lujing)        
    elif FileMD5 == bingdu56:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan:Win32/Wovdnut!BV 木马家族：Wovdnut!')
        os.remove(lujing)
    elif FileMD5 == bingdu57:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan/MSIL.Agentb 木马家族：Agentb !')
        os.remove(lujing)
    elif FileMD5 == bingdu58:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan/JS.SnakeKeylogger 木马家族：Generic !')
        os.remove(lujing)
    elif FileMD5 == bingdu59:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现挖矿木马 类型：Trojan[Downloader]/MSIL.PsDownload 木马家族：PsDownload !')
        os.remove(lujing)
    elif FileMD5 == bingdu60:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：TrojanDropper:Win32/Tnega!MSR 木马家族：Tnega !')
        os.remove(lujing)   
    elif FileMD5 == bingdu61:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：HEUR:Trojan.PowerShell.Obfuscation.gen（Kaspersky） 木马家族：Obfuscation !')
        os.remove(lujing)  
    elif FileMD5 == bingdu62:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：PWS:MSIL/DarkStealer!MTBTnega 木马家族：DarkStealer !')
        os.remove(lujing)  
    elif FileMD5 == bingdu63:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：HEUR:Trojan.Script.Generic（Kaspersky） 木马家族：Generic!')
        os.remove(lujing)  
    elif FileMD5 == bingdu64:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Generic/Trojan..HscASykA（Qihoo 360） 木马家族：Generic!')
        os.remove(lujing)                                                      
    elif FileMD5 == bingdu65:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan.Generic（Qihoo 360） 木马家族：Generic !')
        os.remove(lujing)

    elif FileMD5 == bingdu66:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan.Generic（Qihoo 360） 木马家族：Generic !')
        os.remove(lujing)  
    elif FileMD5 == bingdu67:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan/Win64.GenKryptik(Antiy) 木马家族：GenKryptik !')
        os.remove(lujing)  
    elif FileMD5 == bingdu68:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：TrojanDownloader:PowerShell/Powdow!MSR 木马家族：Powdow !')
        os.remove(lujing)  
    elif FileMD5 == bingdu69:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：GrayWare/Generic.Generic(Antiy) 木马家族：Generic !')
        os.remove(lujing)  
    elif FileMD5 == bingdu70:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan.Generic 木马家族：Generic !')
        os.remove(lujing)  
    elif FileMD5 == bingdu71:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan/Win32.Injuke(Antiy) 木马家族：Injuke !')
        os.remove(lujing)  
    elif FileMD5 == bingdu72:  
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Trojan/Win32.TSGeneric(Antiy) 木马家族：FlyStudio !')
        os.remove(lujing) 
    elif FileMD5 == bingdu73:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Xorer.A')
        tkinter.messagebox.showerror('警告！！','发现蠕虫病毒 特洛伊木马！！病毒类型：Worm:Win32/AutoRun!atmn家族：AutoRun')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.remove(lujing)
            os.system('taskkill /f /im %s' % 'regsvr32.exe')
            os.system('taskkill /f /im %s' % 'cacls.exe')
            os.remove(r'C:\NetApi00.sys')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\igJNZZGC.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\shG5ahIi.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\qLahmUp4.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\WrrsPQEC.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\rthmEzsT.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\eVDfP7bD.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\Rmwz5vvj.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\oI9FTGDa.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\2u5Rdsez.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\oJuLCOZk.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\4iyM8fNu.ico')
            os.remove(r'%HOMEPATH%\AppData\Local\Temp\c9AIuiUN.ico')
            os.remove(r'C:\ProgramData\Synaptics\Synaptics.exe')

            os.system(
                'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Synaptics Pointing Device Driver" /f')
            tkinter.messagebox.showinfo('病毒处理完成！')   
        else:
            os.remove(lujing)   
    elif FileMD5 == bingdu74:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Xorer.A')
        tkinter.messagebox.showerror('警告！！','发现潜在有害程序！！病毒类型：Win32.Trojan.FlyStudio.A（GDATA）家族：FlyStudio')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.system('taskkill /f /im %s' % 'bilibili.exe')
            os.system('taskkill /f /im %s' % '恭喜你中毒了！此处应是好运来——捆绑大礼包')
            os.remove(r'C:\Users\Administrator\AppData\Local\Temp\E_N60005\krnln.fnr')
            os.system(
                'reg delete "HKEY_CURRENT_USERS\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisadleTaskmgr" /f')
            os.remove(lujing) 
            tkinter.messagebox.showinfo('病毒处理完成！')   
        else:
            os.remove(lujing)   
    elif FileMD5 == bingdu75:
        window.configure(bg='red')
        print('发现病毒！！病毒类型：Virus.Win32.Xorer.A')
        tkinter.messagebox.showerror('警告！！','发现潜在有害程序！！病毒类型：Win32.Trojan.FlyStudio.A（GDATA）家族：FlyStudio')
        xuan = xz('处理方式', "是否处理并进行深度删除（运行后选择此项）")

        if xuan == True:
            os.system('taskkill /f /im %s' % 'bilibili.exe')
            os.system('taskkill /f /im %s' % '恭喜你中毒了！此处应是好运来——捆绑大礼包')
            os.remove(r'C:\Users\Administrator\AppData\Local\Temp\E_N60005\krnln.fnr')
            os.system(
                'reg delete "HKEY_CURRENT_USERS\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisadleTaskmgr" /f')
            os.remove(lujing) 
            tkinter.messagebox.showinfo('病毒处理完成！')
        else:
            os.remove(lujing) 
    elif FileMD5 == bingdu77:  
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：TrojanDropper:Win32/Killav.A 木马家族：Agent !')
        os.remove(lujing)            

 
    elif FileMD5 == bingdu76:
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Win32/ShellcodeRunner.AW trojan(ESET) 木马家族：ShellcodeRunner !')
        os.remove(lujing)         
    elif FileMD5 == caidan1:
        gxgg('作者 哔哩哔哩：hallxu 哔哩哔哩，西瓜视频：体贴的小子')   
    elif FileMD5 == bingdu77:  
        window.configure(bg='red')
        tkinter.messagebox.showerror('警告！！','发现病毒 类型：Worm:VBS/Safrabla.A 木马家族：Agent !')
        os.remove(lujing)                                                              
    else:
        window.configure(bg='green')
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
    

    window.title("python杀毒软件")  # 窗口标题
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
    csan = Button(window, text="指定文件夹扫描", command=lambda: thread_it(qp))
    csan.place(x=300, y=500)


    
    
    


    




    

    window.mainloop()
  
    




