def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    bmi = weight / (height*height)
    print("BMI="+ str(bmi))
    
    if bmi<18.5:
        print("User is underweight")
        return -1
    elif 18.5<=bmi<=25.0:
        print("User is normal weight")
        return 0
    else :
        print("User is overweight")
        return 1


calculate_bmi(weight=67, height=1.73)