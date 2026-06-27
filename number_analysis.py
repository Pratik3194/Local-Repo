def find_even_odd(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd


numbers = [12, 7, 5, 20, 33, 18, 41, 50, 29, 14]

even_numbers, odd_numbers = find_even_odd(numbers)

print("Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

print("Total Numbers:", len(numbers))
print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))
print("Average:", sum(numbers) / len(numbers))