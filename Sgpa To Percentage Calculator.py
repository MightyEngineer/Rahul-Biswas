#SGPA TO PERCENTAGE CALCULATOR

#Input
sgpa=float(input("SGPA : "))

#Formulas
percentage=(sgpa-.75)*10
print(percentage,"%")

#Arguments 
if percentage <40:
    print("Faild")
elif percentage >40 and percentage <50:
    print("Below Average")
elif percentage >50 and percentage <60:
    print("Fair")
elif percentage >60 and percentage <70:
    print("Good")
elif percentage >70 and percentage <80:
    print("Very Good")
elif percentage >80 and percentage <90:
    print("Excellent")
else :
    print("Outstanding")





