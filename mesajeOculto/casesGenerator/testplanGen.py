filename = '../testplan'

with open(filename, 'w') as f:
    f.write('sub1.0 20\n')
    for i in range(1,10):
        f.write(f'sub1.{str(i)} 0\n')
        
    f.write('sub2.0 20\n')
    for i in range(1,10):
        f.write(f'sub2.{str(i)} 0\n')

    f.write('sub3.0 20\n')
    for i in range(1,10):
        f.write(f'sub3.{str(i)} 0\n')   

    f.write('sub4.0 20\n')
    for i in range(1,10):
        f.write(f'sub4.{str(i)} 0\n')

    f.write('sub5.0 20\n')
    for i in range(1,10):
        f.write(f'sub5.{str(i)} 0\n')