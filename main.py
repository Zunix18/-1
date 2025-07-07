t1, t2, t3 = map(int, input("Введіть три значення: ").split())

speed = 1/t1 + 1/t2 + 1/t3
time = 1 / speed

print(f"Час, необхідний для з'їдання пирога: {time:.2f} годин")
