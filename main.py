from login.login import login
from signUp.register import sign_up
from find.find import list_status, find_status
import sys
import blockchain
import json

blockchainUse=blockchain.Blockchain()
initial_func_list = [{"quit", 0}, {"login", 1}, {"sign_up", 2}]  # 记录初始功能
main_func_list = [
    {"quit", 0},
    {"logout", 1},
    {"list_status", 2},
    {"find", 3},
    {"borrow", 4},
    {"return",5},
]  # 记录正式系统功能

is_login = False
current_environment = "pre_login"  # 初始环境为登陆前


def wellcome():
    print("Welcome to the borrowing system. What do you want to do?")


def list_function():
    print("{0:^10}\t{1:^10}".format("function", "key"))
    
    if current_environment == "pre_login":
        for func, key in initial_func_list:
            print("{0:^9}\t{1:^9}".format(key, func))
    elif current_environment == "post_login":
        for func, key in main_func_list:
            print("{0:^9}\t{1:^9}".format(key, func))


def Initial_step():
    global current_environment
    global usernameId
    reslt=""
    while True:
        cmd = input()
        match cmd:
            case "q":
                print("bye~")
                return -1
            case "1":
                reslt = login()
                if reslt!="false":  # 登录成功
                    current_environment = "post_login"
                    usernameId=reslt
            case "2":
                sign_up()
            case "h":
                list_function()
            case _:
                print("wrong command, you can type [q] or [0] to quit or [h] for help")
                
        if reslt:
            return 1

def borrow():
    borrowId = input("Please input the id of the equipment that you want to borrow, input 0 to quit")
    
    while (borrowId != "0"):
        temp = [usernameId,borrowId,"borrow"]
        blockchainUse.add_new_transaction(json.dumps(temp))
        borrowId = input("Any more to borrow? Input 0 to quit")
        
    blockchainUse.mine()
                     

    
def main_step():
    global current_environment
    print("Input h to be helped")
    while True:
        cmd = input()
        reslt = 0
        match cmd:
            case "q":
                print("bye~")
                return -1
            case "1":
                is_login = False
                current_environment = "pre_login"
            case "2":
                list_status()
            case "3":
                s = input("\U0001F50D: ")
                find_status(s)
            case "4":
                borrow()
            case "h":
                list_function()
            case _:
                print("wrong command, you can type [q] or [0] to quit or [h] for help")
        if reslt:
            return 1


def main():
    wellcome()
    list_function()
    
    while True:
        if current_environment == "pre_login":
            if Initial_step() == -1:
                break
        elif current_environment == "post_login":
            if main_step() == -1:
                break


if __name__ == "__main__":
    main()
