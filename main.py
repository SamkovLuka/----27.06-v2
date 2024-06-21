# # #завдання 1
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum_1 = 0
# sum_2 = 0
# for i in range(a, b, 1):
#     if i%2 != 0:
#       print("сума непарних чисел = ") 
# print(sum_1 + i)
#     elif i%2 == 0:
#       print("сума парних чисел = ") 
# print(sum_2 + i)





#завдання 2

lg = int(input("Введіть довжину лінії: "))
sm = str(input("Введіть символ для заповнення лінії: "))
for i in range(0, lg, 1):
    print(sm)


# завдання 3

nm = int(input("Enter number: "))
for i in range(0, 7, 1):
    if nm == 7:
       print("Good bye!")
       break
    if nm > 0:
       print("Number is positive")
    if nm == 0:
       print("Number is equal to zero")
    if nm < 0:
       print("Number is negative")


#завдання 4

fir = int(input("Enter first number: "))
sec = int(input("Enter second number: "))
sum = fir + sec
for i in range(fir, sec, 1):
   if fir == 7:
      print("Goodbye")
      break
   if sec == 7:
      print("Goodbye")
      break
   if fir > sec:
      print(f"{fir} - максимум, {sec} - мінімум")
      print(f"сума чисел - {sum}")
   if fir < sec:
      print(f"{sec} - максимум, {fir} - мінімум")
      print(f"сума чисел - {sum}")


