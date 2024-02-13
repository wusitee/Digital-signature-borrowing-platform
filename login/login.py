import hashlib
import getpass

# 问题部分
# 检查文件内是否存储密钥


def check_username(typedUsername, typedpassword):
    try:
        with open("../UserInfo", "r") as file:
            for line in file:
                # print(f"{typedUsername} {typedpassword}\n")
                if line == f"{typedUsername} {typedpassword}\n":
                    # print(line)
                    # 注意line的末尾有一个换行符
                    # print("login successfully")
                    return True
            # print("login failed")
            return False
    except FileNotFoundError:
        try:
            with open("./UserInfo", "r") as file:
                for line in file:
                    if line == f"{typedUsername} {typedpassword}\n":
                        # 注意line的末尾有一个换行符
                        # print("login successfully")
                        return True
                # print("login failed")
                return False
        except FileNotFoundError:
            print("File not found.")


def calc_md5(strings):
    result = hashlib.md5()
    result.update(strings.encode("utf-8"))
    encoded = str(result.hexdigest())
    return encoded


def login():
    # 输入名称与密码
    username = input("Username: ")
    userpassword = getpass.getpass("Password: ")
    # 加密
    encodepassword = calc_md5(userpassword + username)
    # 对比
    if check_username(username, encodepassword):
        print("login successfully")
        return username
    else:
        print("login failed")
        return "false"
