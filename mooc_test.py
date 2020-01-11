import sys
import random
from datetime import datetime


def guide_page(guide_word):
    print("{}{}{}".format("*"*20,guide_word,"*"*20))


def all_num(n):
    """
    判断玩家输入的是否为数字
    :param n: 用于接收用于判定的变量的值
    :return: True/False
    """
    return n.isdigit()


def num_legals(ls):
    """
    数值合法性的判断
    :param ls:玩家输入区间的起始值和终止值
    :return:
    """
    #将列表中的数据转化成int类型
    ls_int=list(map(int,ls))
    #当区间起始值与终止值相同时，退出程序
    if ls_int[0]==ls_int[1]:
        print("您输入的区间数字相同！！请重新启动程序。")
        sys.exit()
    #区间其实位置的值大于终止位置
    elif ls_int[0]>ls_int[1]:
        print("您输入的数字区间大小有误！！请重新启动程序。")
        sys.exit()
    else:
        return 1


def set_final_num(num1,num2):
    """
    产生指定区间的随机数
    :param num1: 起始值
    :param num2: 终止值
    :return:
    """
    final_num=[num1,num2]   #将起始值和终止值保存到列表中
    #判断数据的起始值和终止值是否是数字，并将结果转换成list
    rest = list(filter(all_num,final_num))
    #都为数字时rest长度应该为2
    if len(rest)==2:
        #判断区间的起始值和终止值是否合法
        if num_legals(rest):
            #返回数值区间内的随机整数
            return random.randint(int(num1),int(num2))
    else:
        print("您输入的为非数字字符，请重新启动！")
        sys.exit()


def check_num_legal(num):
    """
    判断数值是否在指定的区间
    :param num: 玩家输入的数
    :return:
    """
    if int(i)<=num<=int(j):
        return True
    else:
        print("对比起您输入的数字未在指定区间！！！")
        return False


def write_record(times,value):
    """
    将玩家每一次猜测数字和本次猜测次数两项信息写入日志文件
    :param times: 玩家猜测的次数
    :param value: 本次猜测的具体数字
    :return:
    """
    now_time=datetime.now() #获取玩家每一次猜测数字的时间
    with open("record.txt","a+",encoding="utf-8") as f:
        f.write("{}: 第{}次猜测的数字为: {}\n".format(now_time,times,value))


def main(rand1):
    temp=0 #接收猜测的次数
    while True:
        guess_number=input("请继续输入您猜测的数字")
        #判断数据是否为数字
        if all_num(guess_number):
            guess_number=int(guess_number)
        else:
            print("您输入的是非数字字符，请重新输入。")
            continue
        temp=temp+1
        write_record(temp,guess_number)
        #判断玩家猜测的数字是否在起始值与终止区间内
        if check_num_legal(guess_number)==False:
            #退出本次循环
            continue
        else:
            print("*"*20)
            #当猜测数字小于随机数时
            if guess_number<rand1:
                print("Lower than the answer")
            elif guess_number>rand1:
                print("Higher than the answer")
            else:
                print("恭喜您！只用了{}次就赢得了游戏".format(temp))
                break


if __name__=="__main__":
    guide_page("欢迎进入数字猜猜猜小游戏")
    i=input("数字区间起始值：")
    j=input("数字区间终止值：")
    rand_num=set_final_num(i,j)
    print("所产生的随机数字区间为：",[i,j])
    main(rand_num)

