# coding=utf-8

import gc
import sys

# 系统包

sys.path.append('../Program_Files/System')

import __bios__
import __thanks__
import __calc__
import __user__


# 自建包

# import some modules

def __n_start__():
    def __first_choose__():
        with open('first.txt', 'r') as First:
            first = First.readline()
        # 检查是否为初始
        if first == 'True':
            # 如果是
            __user__.u_first()
            # 创建用户
            first = 'False'
            with open('first.txt', "w", encoding="utf-8") as First:
                First.write(first)
            # 然后清除初始状态
            del first
            gc.collect()
        # 如果不是，就啥事也不做

    def __language__(model, us_en, zn_cn, zn_tw):
        if users_language == 'US_en':
            if model == 'print':
                print(us_en)
            elif model == 'input':
                print(us_en, end='')
                variable = input("")
                return variable
            elif model == '()':
                print(us_en)
                print()
            else:
                print('error: input an undefined thing')

        elif users_language == 'ZN_cn':
            if model == 'print':
                print(zn_cn)
            elif model == 'input':
                print(zn_cn, end='')
                variable = input("")
                return variable
            elif model == '()':
                print(zn_cn)
                print()
            else:
                print('error: input an undefined thing')

        elif users_language == 'Zn_tw':
            if model == 'print':
                print(zn_tw)
            elif model == 'input':
                print(zn_tw, end='')
                variable = input("")
                return variable
            elif model == '()':
                print(zn_tw)
                print()
            else:
                print('error: input an undefined thing')
        else:
            print('error: your language is wrong ')

    __first_choose__()
    __bios__.bios()
    __user__.user()

    with open('.//now//language.txt', 'r') as lan:
        users_language = lan.readline()
    with open('.//now//power.txt', 'r') as power:
        users_power = power.readline()

    del power, lan
    gc.collect()
    while 1:
        __language__('()', '-Desktop-', '-桌面-', '-桌面-')
        __language__('()', '0: Start', '0: 开始菜单', '0: 開始菜單')
        __language__('()', '1: Explorer', '1: 此电脑', '1: 我的電腦')
        __language__('()', '2: Log out', '2: 退出账号', '2: 退出賬號')
        if users_power != 'visitor':
            __language__('()', '3: user software', '3: 用户软件', '3: 用戶軟件')
        if users_power == 'admin':
            __language__('()', '98: thanks', '98: 致谢名单', '98: 致謝名單')
        __language__('()', '99: Exit', '99：关机', '99：關機')
        choose = __language__('input', 'want?', '你干嘛', '你幹嘛')
        if choose == '0':
            while 1:  # Start menu 需要 while 1!
                __language__('()', '-start-', '-开始菜单-', '-開始菜單-')
                __language__('()', '0: back', '0: 退出', '0: 退出')
                __language__('()', '1: sys software', '1: 汐筒软件', '1: 系統軟件')
                choose = __language__('input', 'want?', '你干嘛', '你幹嘛')
                if choose == '0':
                    print("Good bye!")
                    break
                elif choose == '1':
                    while 1:
                        choose = __language__('input', '1:back,2:continue', '1:返回,2:继续', '1:返回,2:繼續')
                        if choose == '1':
                            print("Good bye!")
                            break
                        elif choose == '2':
                            while 1:
                                __language__('()', '-sys software-', '-汐筒软件-', '-系統軟件-')
                                __language__('()', '0: back', '0: 退出', '0: 退出')
                                __language__('()', '1: calc', '1: 计算器', '1: 計算器')
                                __language__('()', '2: Time', '2: 时间', '2: 時間')
                                if users_power == 'admin':
                                    __language__('()', '3: user', '3: 用户', '3: 用戶')
                                choose = __language__('input', 'want?', '你干嘛', '你幹嘛')
                                if choose == '0':
                                    print("Good bye!")
                                    break
                                elif choose == '1':
                                    __calc__.calc()
                                elif choose == '2':
                                    choose = __language__('input',
                                                          '1:back,2:continue',
                                                          '1:返回,2:继续',
                                                          '1:返回,2:繼續')
                                    if choose == '1':
                                        print("Good bye!")
                                    elif choose == '2':
                                        def time(model):
                                            def g_days(year, month):
                                                if month > 12 or month <= 0:
                                                    return '-1'
                                                if month == 2:
                                                    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                                                        return '29'
                                                    else:
                                                        return '28'
                                                if month in (4, 6, 9, 11):
                                                    return '30'
                                                else:
                                                    return '31'

                                            if model == 1:
                                                import calendar as cal
                                                import time as t
                                                print(t.strftime("%Y-%m-%d %H:%M:%S",
                                                                 t.localtime(t.time())))
                                                year = t.strftime("%Y")
                                                month = t.strftime('%m')
                                                print(
                                                    'This month has {0} days!'.format((g_days(year,
                                                                                              month))))
                                                ca = cal.month(int(year), int(month))
                                                print(year + 'year' + month + "mouth's calendar:")
                                                print(ca)
                                                day = int(t.strftime('%d'))
                                                t = (0, 31, 59, 90, 120,
                                                     151, 181, 212, 243,
                                                     273, 304, 334)[int(month) - 1]
                                                t += day
                                                leap = 0
                                                if year % 4 == 0 or year % 400 == 0:
                                                    leap = 1
                                                if leap == 1 and int(month) > 2:
                                                    t += 1
                                                if t % 10 == 1:
                                                    print('the %d st day' % t)
                                                elif t % 10 == 2:
                                                    print('the %d nd day' % t)
                                                elif t % 10 == 3:
                                                    print('the %d rd day' % t)
                                                else:
                                                    print('the %d th day' % t)
                                                print()
                                                del g_days, year, month, ca, day, t, leap
                                                gc.collect()
                                            elif model == 2:
                                                while 1:
                                                    try:
                                                        year = int(float(input('year:')))
                                                        month = int(float(input('month:')))
                                                        day = int(float(input('day:')))
                                                        if 1 <= month <= 12 and 1 <= day <= 31:
                                                            t = (0, 31, 59, 90, 120, 151,
                                                                 181, 212, 243, 273, 304, 334)[
                                                                month - 1]
                                                        break
                                                    except ValueError:
                                                        print("error: input an undefined thing")
                                                print('This month has ' + str(g_days(year, month)) + ' days')
                                                t += day
                                                leap = 0
                                                if year % 4 == 0 or year % 400 == 0:
                                                    leap = 1
                                                if leap == 1 and month > 2:
                                                    t += 1
                                                if t % 10 == 1:
                                                    print('the %d st day' % t)
                                                elif t % 10 == 2:
                                                    print('the %d nd day' % t)
                                                elif t % 10 == 3:
                                                    print('the %d rd day' % t)
                                                else:
                                                    print('the %d th day' % t)
                                                print()
                                                del g_days, year, month, day, t, leap
                                                gc.collect()
                                            else:
                                                print('error')

                                        time(1)
                                    else:
                                        print('error: input an undefined thing')
                                elif choose == '3':
                                    if users_power != 'admin':
                                        print('error: input an undefined thing')
                                    choose = __language__('input',
                                                          '1:back,2:continue',
                                                          '1:返回,2:继续',
                                                          '1:返回,2:繼續')
                                    if choose == '1':
                                        print("Good bye!")
                                    elif choose == '2':
                                        __language__('print',
                                                     '1.change the current user',
                                                     '1.更改当前用户',
                                                     '1.更改當前用戶')
                                        __language__('print',
                                                     '2.create a new user',
                                                     '2.创建新用户',
                                                     '2.創建新用戶')
                                        choose = __language__('input', 'want?', '你干嘛', '你幹嘛')
                                        if choose == '1':
                                            with open('.//now//password.txt', 'r') as password:
                                                users_password = password.readline()
                                            # read the Password
                                            while 1:
                                                input_password = __language__('input',
                                                                              'administrator,input your password:',
                                                                              '管理员,请输入密码:',
                                                                              '管理员,請輸入密碼:')
                                                if input_password != users_password:
                                                    __language__('print',
                                                                 'the password you input is wrong',
                                                                 '密码错误',
                                                                 '密碼錯誤')
                                                __user__.change()
                                        if choose == '2':
                                            with open('.//now//password.txt', 'r') as password:
                                                users_password = password.readline()
                                            # read the Password
                                            while 1:
                                                input_password = __language__('input',
                                                                              'administrator,password:',
                                                                              '管理员,请输入密码:',
                                                                              '管理员,請輸入密碼:')
                                                if input_password != users_password:
                                                    __language__('print',
                                                                 'Error : password wrong',
                                                                 '密码错误',
                                                                 '密碼錯誤')
                                                __user__.u_new()
                                    else:
                                        print('error')

                        else:
                            print('error: input an undefined thing')
                else:
                    print('error: input an undefined thing')
        elif choose == '1':  # Explorer 需要 while 1!# 施工
            while 1:
                choose = __language__('input', '1:back,2:continue',
                                      '1:返回,2:继续',
                                      '1:返回,2:繼續')
                if choose == '1':
                    print("Good bye!")
                    break
                elif choose == '2':
                    print('正在制作')
                else:
                    print('error: input an undefined thing')
        elif choose == '2':
            choose = __language__('input', '1:back,2:continue',
                                  '1:返回,2:继续',
                                  '1:返回,2:繼續')
            if choose == '1':
                print("Good bye!")
            elif choose == '2':
                __user__.user()
            else:
                print('error: input an undefined thing')
        elif choose == '3':
            choose = __language__('input', '1:back,2:continue',
                                  '1:返回,2:继续',
                                  '1:返回,2:繼續')
            if choose == '1':
                print("Good bye!")
            elif choose == '2':
                __language__('print', '1:make user software',
                             '1:创建用户软件',
                             '1:創建用戶軟件')
                __language__('print', '2:user software',
                             '2:用户软件',
                             '2:用戶軟件')
                if choose == '1':
                    print('正在制作')
                elif choose == '2':
                    print('正在制作')
                else:
                    print('error: input an undefined thing')
            else:
                print('error: input an undefined thing')
        elif choose == '98':
            if users_power != 'admin':
                print('error: input an undefined thing')
            choose = __language__('input', '1:back,2:continue',
                                  '1:返回,2:继续',
                                  '1:返回,2:繼續')
            if choose == '1':
                print("Good bye!")
            elif choose == '2':
                __thanks__.thanks()
        elif choose == '99':
            exit(0)
        else:
            print('error: input an undefined thing')


__n_start__()
