print("Q1")
list = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
        953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
        687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958, 743, 527]
for i in list:
    if i == 237:
        break
    elif i % 2 == 0:
        print(i)

print("Q2")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3 = color_list_1-color_list_2
print(color_list_3)


print("Q3")
s = input().lower()
i = 0
al = "abcdefghijklmnopqrstuvwxyz"
for j in al:
    if j not in s:
        print(" not a pangram")
        break
    else:
        i = i + 1
if i == 26:
    print("a pangram")

print("Q4")
i = int(input())
n = i
nn = int(str(i) * 2)
nnn = int(str(i) * 3)
print(n+nn+nnn)

print("Q5")
s = input().split('#')
s1 = s[0].split()
s2 = s[1].split()
s1 = [int(i) for i in s1]
s2 = [int(i) for i in s2]
print(s1)
print(s2)

print("Q6")
string = input()
grp = string.split(',')
grp.sort()
print((', '.join(grp)))

print("Q7")
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
     'Marks': [57, 87, 67, 79]}
max = d['Marks'].index(max(d['Marks']))
print(d['Student'][max])

print("Q8")
string = input()
d = 0
l = 0
for i in string:

    if i.isalpha():
        l += 1

    elif i.isnumeric():
        d += 1

print('LETTERS ' + str(l))
print('DIGITS ' + str(d))


print("Q9")
d = {'Name': ['Akash', 'Soniya', 'Vishakha', 'Akshay', 'Rahul', 'Vikas'],
     'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
     'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
sub = input()
newsub = []
newd = {}
for i in range(len(d['Subject'])):
    if(d['Subject'][i] != sub):
        continue
    else:
        newsub.append(i)
newd['Name'] = []
newd['Subject'] = []
newd['Ratings'] = []
for i in newsub:
    newd['Name'].append(d['Name'][i])
    newd['Subject'].append(d['Subject'][i])
    newd['Ratings'].append(d['Ratings'][i])
print(newd)

print("Q10")
n = int(input())


class Generator:
    def generator(self, n):
        for i in range(0, n):
            if not i % 7:
                yield i


gen = Generator()
for i in gen.generator(n):
    print(i)


print("Q11")
up = eval(input('UP : '))
down = eval(input('DOWN : '))
left = eval(input('LEFT : '))
right = eval(input('RIGHT : '))

vertical = (up - down)
horizontal = (right - left)

dist = (vertical**2 + horizontal**2)**0.5

print(round(dist))
