from logo import logo

def get_min_max(x:int):
    num_str = str(x)
    if len(num_str)> 4: #check if the input has more than 4 digits
        print("Invalid Input")
        return
    elif len(num_str)<=4:
        match len(num_str):
            case 1:
                digits = ['0','0','0',num_str[0]]
            case 2:
                digits = ['0','0',num_str[0],num_str[1]]
            case 3:
                digits = ['0',num_str[0],num_str[1],num_str[2]]
            case 4:
                digits = [num_str[0],num_str[1],num_str[2],num_str[3]]
        digits.sort()
        min_num = "".join(digits)
        digits.sort(reverse=True)
        max_num = "".join(digits)
        print(min_num,max_num)
        return int(min_num),int(max_num)


i = 0

def check_karpekar(y:int):
    global i
    min_num,max_num=get_min_max(y)
    new_num = max_num-min_num
    print(f'new_num = {new_num}')
    if new_num == 6174:
        print(f"Reached Karpekar's Constant in {i} iterations! Exiting..")
        return(f"-> 6174 in {i} iterations")
    elif new_num == 0:
        print(f"Reached 0 in {i} iterations! Exiting..")
        return(f"-> 0 in {i} iterations")
    else:
        i += 1
        return check_karpekar(new_num)

def verify_all_digits():
    with open('karpekar.txt','w') as file:
        file.write("Karpekar's Constant\n")
        file.write("Dattatreya Ramachandra Kaprekar\n")
        file.write(f"{logo}\n")
        for n in range(1001,10000):
            print(n)
            output = check_karpekar(n)
            file.write(f"{n}: {output}\n")
            global i
            i = 0
        file.write("Created in Python by: Narendra. Visit me at narendravk.github.io")
if __name__ == '__main__':
    verify_all_digits()   

