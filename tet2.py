s ="i am a student."
b = s.split(' ')
b.reverse()
c = ' '.join(b)

if __name__ == '__main__':
    print(b)
    print(c)
    print(type(c))