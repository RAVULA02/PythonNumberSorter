nums = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = float(input("Please enter the Value of %d Element : " %i))
    nums.append(value)

nums.sort()
print('List in Ascending Order: ', nums)

nums.sort(reverse=True)
print('List in Descending Order: ', nums)