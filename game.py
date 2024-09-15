import random

BO_CAU_HOI_FILE_NAME ='bo_cau_hoi.txt'
CAU_TRA_LOI_FILE_NAME ='cau_tra_loi.txt'
PHAN_THUONG_FILE_NAME ='giai_thuong.txt'
FIFTY_FIFTY_FILE_NAME ='fifty_fifty.txt'
KHAO_SAT_FILE_NAME ='khao_sat.txt'

BO_CAU_HOI = BO_CAU_HOI_FILE_NAME
CAU_TRA_LOI = CAU_TRA_LOI_FILE_NAME
PHAN_THUONG = PHAN_THUONG_FILE_NAME
FIFTY_FIFTY = FIFTY_FIFTY_FILE_NAME
KHAO_SAT = KHAO_SAT_FILE_NAME

with open(BO_CAU_HOI,'r',encoding='utf-8') as f:
    BO_CAU_HOI_LIST =f.readlines()

with open(CAU_TRA_LOI,'r',encoding='utf-8') as f:
    CAU_TRA_LOI_LIST =f.readlines()

with open(PHAN_THUONG,'r',encoding='utf-8') as f:
    PHAN_THUONG_LIST =f.readlines()

with open(FIFTY_FIFTY,'r',encoding='utf-8') as f:
    FIFTY_FIFTY_LIST =f.readlines()

with open(KHAO_SAT,'r',encoding='utf-8') as f:
    KHAO_SAT_LIST =f.readlines()

def ViTri():
    while True:
        x = random.randint(0, 18)
        if x not in ViTriCu:
            ViTriCu.append(x)
            break
    return x

def fifty_fifty(a):
    dap_an_1 = CAU_TRA_LOI_LIST[a]
    dap_an_2 = chr(random.randint(65, 68))
    while dap_an_2.lower() == dap_an_1.lower():
        dap_an_2 = chr(random.randint(65, 68))

    dap_an_list = [dap_an_1, dap_an_2]
    dap_an_1_display = random.randint(0, 1)
    dap_an_2_display = 1 - dap_an_1_display
    print(f"Hai lựa chọn còn lại: {dap_an_list[dap_an_1_display]} --- {dap_an_list[dap_an_2_display]}")
    return

ViTriCu = []
Help = [1]

while True:
    for i in range(0,15):
        a = ViTri()
        print(BO_CAU_HOI_LIST[a])      
        if len(Help)>0:
            z = input("Bạn có muốn sử dụng trợ giúp 50/50?(Y/N):")
            if z.strip().upper() == "Y":
                fifty_fifty(a)
                Help.remove(1)
        Answer = input("Nhập câu trả lời:")
        if Answer.strip().upper() == CAU_TRA_LOI_LIST[a].strip().upper():
            if i == 14:
                print(f"Chúc mừng bạn đã hoàn thành tất cả câu hỏi! Giải thưởng của bạn là {PHAN_THUONG_LIST[i]}")
            print("Chúc mừng bạn đã trả lời đúng!")        
            print("Giải thưởng hiện tại của bạn là:", PHAN_THUONG_LIST[i])
            Continue = input("Bạn có muốn đi tiếp không? (Y/N):")
            if Continue.strip().upper() == "Y":
                continue
            if Continue.strip().upper() == "N":
                print(f'Cảm ơn bạn đã tham gia trò chơi! Giải thưởng của bạn là {PHAN_THUONG_LIST[i]}')
                break
        else:
            print("Bạn đã trả lời sai!")
            if i == 0:
                print("Bạn đã sai câu hỏi đầu tiên nên không có phần thưởng!")
            else:
                print("Cảm ơn bạn đã tham gia trò chơi! Phần thưởng của bạn là 100.000đ")
            break
    break