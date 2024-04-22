
def display_main_menu():
    print("Enter some numbers seperated by commas(e.g. 5,67,32)")

def get_user_input():
    user_input=input()
    mylist= user_input.split(",")

    for i in range(len(mylist)):
        mylist.append(float(mylist[0]))
        mylist.pop(0)
    return mylist

['0','1','2']
def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def calc_avg_temp(value_list):
    avgtemp=sum(value_list)/len(value_list)
    return avgtemp

def calc_min_max_temp(value_list):
    min_value=min(value_list)
    max_value=max(value_list)
    return [min_value,max_value]


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list= get_user_input()
    print (calc_avg_temp(num_list))
    print (calc_min_max_temp(num_list))

if __name__=="__main__":
    main()
