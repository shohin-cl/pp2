numbers = []

while True:
    number = int(input("Enter a number (0 to end): "))
    if number == 0:
        break
    numbers.append(number)

# Find min, max, sum, and average
min_num = min(numbers)
max_num = max(numbers)
sum_num = sum(numbers)
average_num = sum_num / len(numbers)

# Print the results
print("Min:", min_num)
print("Max:", max_num)
print("Sum:", sum_num)
print("Average:", average_num)

# Count unique values
unique_nums = set(numbers)
print("Unique values:", len(unique_nums))

# Count how many times each value repeats
for num in unique_nums:
    count = numbers.count(num)
    print(f"{num} occurs {count} times")