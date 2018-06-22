
# list1 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
#
# print(list1)
#
# for i in range(25,51):
#     print(i)
#
# for show in list1:
#     print(show)
#
# numbers = [1, 3, 5, 6, 7, 9]
#
#
# while True:
#     guess  = input("Please guess a number. Press 'q' to quit.")
#     if "q" in guess:
#         break
#     guess = int(guess)
#     if guess in numbers:
#         print("You guessed correctly")
#     else:
#         print("Please guess again")

numbers1 = [8, 19, 148, 4]
numbers2 = [9, 1, 33, 83]
numbers3 = []

for x in numbers1:
    for y in numbers2:
        numbers3.append(x * y)

print(numbers3)
