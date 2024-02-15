def equipment_info():
    equip_id=input('enter the id of equipment:')
    equip_name=input('enter the name of equipment:')
    equip_status=input('enter the status of equipment:')
    borrower=input('enter your name:')

def locate_equipment(equip_id, equip_name, equip_status, borrower):
    #将用户输入的信息作为函数的参数
    with open("./equipmentInfo","r") as file:
        for line in file:
            fields=line.split(',')
        #检查是否与用户输入的信息匹配
        if fields[0]==equip_id and fields[1]==equip_name and fields[2]==equip_status and fields[3]==borrower:
            #如果匹配，打印找到的信息
            print('Found the equipment:',line)
            break
    else:
        #如果没有匹配，打印没有找到信息
        print('No equipment found.')
