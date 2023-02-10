def number_to_words(num):
    words = []
    if num >= 1000:
        words.append(str(num // 1000) + " thousand")
        num %= 1000
    if num >= 100:
        words.append(str(num // 100) + " hundred")
        num %= 100
    if num >= 20:
        words.append(["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][(num // 10) - 2])
        num %= 10
    if num > 0:
        words.append(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][num - 1])
    return " ".join(words)

n = int(input("Enter the maximum number: "))
numbers = list(range(n, 0, -1))
print("The maximum number is", number_to_words(numbers[0]))