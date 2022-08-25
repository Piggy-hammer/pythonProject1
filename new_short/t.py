# num = []
# with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/Ones_with_UsdRaisedError5.txt", 'r') as f:
#     listIn = f.readlines()
#     for e in listIn:
#         num.append(e.split('#')[0])
# print(num)
# with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/test1.txt", 'r') as f1:
#     with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/Ones_with_UsdRaisedError6.txt", 'w') as f2:
#         listIn1 = f1.readlines()
#         for e1 in listIn1:
#             if num.count(e1.split('#')[0]) > 0 :
#                 print(e1.split('#')[0])
#                 if e1.endswith('?'):
#                     e1 = e1[:-1]
#                 if e1.endswith('/'):
#                     e1 = e1[:-1]
#                 f2.write(e1)


# with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/web_error.txt", 'r') as f:
#     with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/web_error1.txt", 'w') as f1:
#         listIn1 = f.readlines()
#         for e1 in listIn1:
#             if e1.strip().replace("\n", "") == '':
#                 continue
#             print(e1)
#             f1.write(e1)

import os

filePath = 'D:/pro/messy2'
name = os.listdir(filePath)
ids = []
for file_name in name:
    file_id = file_name.split('.')[0]
    ids.append(file_id)
    print(file_id)
print(len(ids))
with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/web_error2.txt", 'r') as f:
    with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/ones_with_website3.txt", 'w') as f1:
        original_names = f.readlines()
        for original_name in original_names:
            f1.write(original_name)
        with open("C:/Users/95328/PycharmProjects/pythonProject1/new_short/ones_with_website.txt", 'r') as read:
            with_webs = read.readlines()
            for with_web in with_webs:
                if ids.__contains__(with_web.split('#')[0]):
                    f1.write(with_web)