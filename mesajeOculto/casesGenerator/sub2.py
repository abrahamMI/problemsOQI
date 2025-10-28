import random
import string

def create_input(filename):
    with open(filename, 'w') as f:
        N = random.randint(1, 100)
        M = 0
        words = []
        for _ in range(N):
            length = random.randint(1, 10)
            word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))
            word = word  # Ensure the first character is 'a'
            words.append(word)
            M = max(M, length) 

        f.write(f"{N} {M}\n")
        for word in words:
            f.write(f"{len(word)} {word}\n")

def create_output(filename):
    with open(filename, 'w') as f:
        f.write("\n")


for i in range(10):
    input_filename = f"../cases/sub2.{str(i)}.in"
    create_input(input_filename)
    create_output(input_filename.replace('.in', '.out'))
    input_filename = f"../cases/sub3.{str(i)}.in"
    create_input(input_filename)
    create_output(input_filename.replace('.in', '.out'))
    input_filename = f"../cases/sub4.{str(i)}.in"
    create_input(input_filename)
    create_output(input_filename.replace('.in', '.out'))
    input_filename = f"../cases/sub5.{str(i)}.in"
    create_input(input_filename)
    create_output(input_filename.replace('.in', '.out'))
