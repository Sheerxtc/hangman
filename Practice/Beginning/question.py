print("Which one you will choose? A or B?\nJust explain please.")
answer = input()
print("Your answer is ",answer)
with open("answer.txt","w") as f:
    f.write(answer)
with open("answer.txt","r") as f:
    print(f.read())
