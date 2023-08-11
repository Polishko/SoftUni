nums_file = open("numbers.txt", "r")

sum_nums = 0
for num in nums_file:
    sum_nums += int(num)

print(sum_nums)
nums_file.close()

# hoca napti acti contenti read.split("\n) dedi ama sonda bosluk kaldi sonra comprehension ve ele varsa int(el) (olmayan bosluk
# sonra sum aldi)