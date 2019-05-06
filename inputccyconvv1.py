def conv_CHF_in_EUR(CHF):
        EUR = CHF * 0.88
        return "As per today " + str(CHF) + " chf equal " + str(EUR) +  " eur"

user_input = input("Please enter amount of CHF you want to convert in EUR: ")
result = (conv_CHF_in_EUR (float(user_input) * 0.88))

print(result)

if float(user_input) <= 100000:
    print("you are not rich!")
if float(user_input) > 100000:
    print("you are rich!")

    












