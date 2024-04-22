def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    bmi = weight / (height*height)
    print("BMI="+ str(bmi))
    
    if bmi<18.5:
        print("User is underweight")
    elif 18.5<=bmi<=25.0:
        print("User is normal weight")
    else :
        print("User is overweight")


calculate_bmi(weight=67, height=1.73)