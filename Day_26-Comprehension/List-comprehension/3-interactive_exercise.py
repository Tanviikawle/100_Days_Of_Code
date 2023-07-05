with open("C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_26-Comprehension/file1.txt") as file1:
    file1_data=file1.readlines()

with open("C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_26-Comprehension/file2.txt") as file2:
    file2_data=file2.readlines()

result=[int(num) for num in file1_data if num in file2_data]
print(result)
