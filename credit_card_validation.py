card_no = "5610591081018350"
odd_sum = 0
even_sum = 0
double_list = []

number = list(card_no)
for(index,value) in enumerate(number):
    if index%2!=0:
        odd_sum += int(value)
    else:
        double_list.append(int(value)*2)
double_string =""
for x in double_list:
    double_string += str(x)
double_list = list(double_string)
for x in double_list:
    even_sum += int(x)
net_sum = odd_sum + even_sum 

if net_sum%10 == 0:
    print("Valid Card")
else:
    print("Invalid Card")