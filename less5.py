#### ##1
# funk = open('less5.txt', 'w')
# line = input('Введите текст\n')
# while line:
#     funk.writelines(line)
#     line = input('Введите текст\n')
#     if not line:
#         break
# 2
# m_file = open('less5.txt', 'r')
# content = m_file.read()
# print(f'text: \n {content}')
# m_file = open('less5.txt', 'r')
# content = m_file.readlines()
# print(f'Кол-во строк - {len(content)}')
# m_file = open('less5.txt', 'r')
# content = m_file.readlines()
# for i in range(len(content)):
#     print(f'Кол-во символов, {len(content[i])}')
# m_file = open('less5.txt', 'r')
# content = m_file.read()
# content = content.split()
# print(f'Кол-во слов - {len(content)}')
# m_file.close()

#3
# with open('zp.txt', 'r') as d_file:
#     salary = []
#     averg = []
#     d_list = d_file.read().split('\n')
#     for i in d_list:
#         i = i.split()
#         if int(i[1]) < 20000:
#             averg.append(i[0])
#         salary.append(i[1])
# print(f'Оклад меньше 20.000 {averg}, средний оклад {sum(map(int, salary)) / len(salary)}')

#4
# numm = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# my_f = []
# with open("zp.txt", "r") as file_obj:
#     # content = "zp.txt"
#     for i in file_obj:
#         i = i.split(' ', 1)
#         my_f.append(numm[i[0]] + '  ' + i[1])
#     print(my_f)
# with open('zp_1.txt', 'w') as file_obj_2:
#     file_obj_2.writelines(my_f)

# 5
def summary():
    try:
        with open('n5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            m_b = line.split()
            print(sum(map(int, m_b)))
    except ValueError:
        print('error')
summary()
