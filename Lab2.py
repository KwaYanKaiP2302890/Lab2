
def display_main_menu():
    print("Enter some numbers seperated by commas(e.g. 5,67,32)")

def get_user_input():
    user_input=input()
    mylist= user_input.split(",")

    for i in range(len(mylist)):
        mylist.append(float(mylist[0]))
        #Append function add the new float no. to the back of the array
        mylist.pop(0)
        #pop function would remove the index 0 of the array
        #hence elements in the array is being changed from str to float one by one like a shift register
    return mylist


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

def calc_median_temp(value_list):
    asc_list = sorted(value_list)
    check=len(asc_list)%2
    if check==0:
        index=len(asc_list)/2
        index=int(index)
        median=(asc_list[index]+asc_list[index-1])/2
        return median
    else:
        index=len(asc_list)/2
        index = int(index)
        return asc_list[index]

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list= get_user_input()
    print ("Average: "+ str(calc_avg_temp(num_list)))
    print ("[Min,Max]: " + str(calc_min_max_temp(num_list)))
    print("Median: "+ str(calc_median_temp(num_list)))

if __name__=="__main__":
    main()
