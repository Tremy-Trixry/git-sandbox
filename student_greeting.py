# student_greeting.py
name = input("Enter your name: ")
programme = input("What programme are you doing? ")
interesting_course = input(f"Which filled under {programme} are you interested in? ")
interesting_course = interesting_course.title()
year = input("What year are you in? ")

print("\n")
print(f"Hello {name}!")
print(f"Welcome to {programme}, year {year}.")
print(f"\n{interesting_course} is full of fun. You're even gonna love it more as you process in the lessons")
print(f"Good luck {name}. And don't forget to have fun...!!!!")
print("Have a great day")
