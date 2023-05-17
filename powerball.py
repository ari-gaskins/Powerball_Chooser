from random import choice, sample

num_options = [i for i in range(1, 70)]
powerball = [i for i in range(1, 27)]

my_nums = sample(num_options, 5)
my_powerball = choice(powerball)

for num in my_nums:
    print(num, end=' ')

print(my_powerball)
