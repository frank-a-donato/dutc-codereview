guests = ['Alice', 'Bob', 'Charlie']
amount = 235_05 # $235.01 in cents

# get the amount that everyone has to pay
equal = amount // len(guests)

# get the additional amount the last guest must pay if the bill doesn't split evenly
addl = amount % len(guests)

# hold everyone's payment in a dictionary
bill = {}
extra = ""

for g in range(len(guests)):
    if addl > 0 and g == len(guests)-1:
        bill[guests[g]] = (equal/100) + (addl/100) # convert to dollars and cents
        extra = " extra"
    else:
        bill[guests[g]] = (equal/100)
    print(f"{guests[g]} pays{extra}: ${bill[guests[g]]:.2f}")