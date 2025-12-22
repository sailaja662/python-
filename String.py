text = input("Enter a string: ")

print("\nOriginal String:", text)

# 1. Convert to Uppercase
print("Uppercase:", text.upper())

# 2. Convert to Lowercase
print("Lowercase:", text.lower())

# 3. Replace spaces with underscore
print("Spaces replaced with _ :", text.replace(" ", "_"))

# 4. Reverse the string
print("Reversed String:", text[::-1])

# 5. Replace vowels with *
result = ""
for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print("Vowels replaced with *:", result)
