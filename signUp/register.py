import getpass
import hashlib


def check_username(newUsername):
    try:
        with open("../UserInfo", "r") as file:
            for line in file:
                oldUsername = line.split(" ")
                if oldUsername == newUsername:
                    return False
    except FileNotFoundError:
        try:
            with open("./UserINfo", "r") as file:
                for line in file:
                    oldUsername, _ = line.split(" ")
                    if oldUsername == newUsername:
                        return False
            # 避免在不同路径执行文件的问题
        except FileNotFoundError:
            print("File not found.")
        except IOError as e:
            print(f"Error writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return True


def calc_pass(password, name):
    result = hashlib.md5()
    result.update(f"{password}{name}".encode("utf-8"))
    return result.hexdigest()


def append_line_to_file(line_to_add):
    try:
        with open("../UserInfo", "a") as file:
            file.write(line_to_add+"\n")

    except FileNotFoundError:
        try:
            with open("../UserInfo", "a") as file:
                print(line_to_add, file=file)
        except FileNotFoundError:
            print("File not found.")
        except IOError as e:
            print(f"Error writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    except IOError as e:
        print(f"Error writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def create_username():
    user_name = input("Please create a username: ")
    while not check_username(user_name):
        user_name = input(
            "the username is used, please create a new one (or type [quit] to quit sign up process): \n"
        )
        if user_name == "quit":
            return -1
    return user_name


def create_password():
    user_password = getpass.getpass("Please create a password: ")
    user_password_confirm = getpass.getpass("Please type your password again: ")
    while user_password != user_password_confirm:
        print("check fail, please retry \n")
        user_password = getpass.getpass("please type your password \n")
        user_password_confirm = getpass.getpass("please type your password again \n")
    return user_password


def sign_up():
    username = create_username()
    if username == -1:
        print("quit sign up")
        return False
    password = create_password()
    encode_pass = calc_pass(password, username)
    append_line_to_file(f"{username} {encode_pass}")
    print("Successfully sign up!")
