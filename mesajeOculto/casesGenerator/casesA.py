import random
import string

def create_input(filename):
    with open(filename, 'w') as f:
        N = random.randint(1, 100)
        M = 0
        words = []
        for _ in range(N):
            length = random.randint(1, 9)
            word = ''.join(random.choices('bcdefghijklmnopqrstuvwxyz', k=length))
            word = 'a' + word  # Ensure the first character is 'a'
            words.append(word)
            M = max(M, length + 1) 

        f.write(f"{N} {M}\n")
        for word in words:
            f.write(f"{len(word)} {word}\n")

def create_output(filename):
    with open(filename, 'w') as f:
        f.write("\n")

for i in range(10):
    input_filename = f"../cases/sub1.{str(i)}.in"
    create_input(input_filename)
    create_output(input_filename.replace('.in', '.out'))
