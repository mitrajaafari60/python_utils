class Student:
    def __init__(self, count, ages, heights, weights):
        self.count = count
        self.age = [int(age) for age in ages]
        self.height = [int(height) for height in heights]
        self.weight = [int(weight) for weight in weights]

    def age_avg(self):
        total = sum(self.age)
        return total / self.count

    def height_avg(self):
        total = sum(self.height)
        return total / self.count

    def weight_avg(self):
        total = sum(self.weight)
        return total / self.count


A_count = int(input())
A_age = input().split()
A_height = input().split()
A_weight = input().split()

A = Student(A_count, A_age, A_height, A_weight)

B_count = int(input())
B_age = input().split()
B_height = input().split()
B_weight = input().split()

B = Student(B_count, B_age, B_height, B_weight)

A_age_AVG = A.age_avg()
A_height_AVG = A.height_avg()
A_weight_AVG = A.weight_avg()

B_age_AVG = B.age_avg()
B_height_AVG = B.height_avg()
B_weight_AVG = B.weight_avg()

print(A_age_AVG)
print(A_height_AVG)
print(A_weight_AVG)
print(B_age_AVG)
print(B_height_AVG)
print(B_weight_AVG)

if A_height_AVG == B_height_AVG:
    if A_weight_AVG == B_weight_AVG:
        print("Same")
    elif A_weight_AVG > B_weight_AVG:
        print("A")
    else:
        print("B")
elif A_height_AVG > B_height_AVG:
    print("A")
else:
    print("B")
