#/usr/bin/python
#-*- coding:utf-8 -*-

#use string to judge IP
def judge_ip(one_str):
    if '.' not in one_str:
        return False
    elif one_str.count('.') != 3:
        return False
    else:
        flag = True
        one_list = one_str.split('.')
        for one in one_list:
            try:
                one_num = int(one)
                if one_num>=0 and one_num<=255:
                    pass
                else:
                    flag = False
            except:
                flag = False
        return flag

if __name__ == '__main__':
    ip_list = ['','172.31.137.251','100.10.0.1000','1.1.1.1','1.2.3','aa.12.1.2','289jjjjjj']
    for one in ip_list:
        if judge_ip(one):
            print '{0} is a legal ip address!'.format(one)
        else:
            print '{0} is not a legal ip address!'.format(one)
