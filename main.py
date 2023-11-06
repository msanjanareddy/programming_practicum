
from childclass2 import Major

def main():
    self_intro = Major("Alpha", "Computer Science", "Fall 2023")
    self_intro1 = Major("Beta", "Health Data Science", "Fall 2023")
    self_intro2 = Major("Gamma", "Computer Science", "Fall 2023")
    print(self_intro.intro())
    print(self_intro1.intro())
    print(self_intro2.intro())
if __name__ == "__main__":
    main()

