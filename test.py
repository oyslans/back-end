# list = [234, 456, 567, 2344, 12, 3123, 1]
#
# for i in range(len(list)):
#     for j in range(len(list)-i-1):
#         if list[j] > list[j + 1]:
#             list[j + 1], list[j] = list[j], list[j + 1]
#
#
# text = "This is a sample text"
# print(text[-1:-2:-2])
# print(text[9:-3])
# print(text[-2:-1:2])
# print()
# print()
# print()
# print()
#
# for i in range(0,30,3):
#     print(i)
#
#
# for i in range(5):
#     for j in range(1,i):
#         print(j,end='')
#     print()

# while True:
#     name = input("Enter name : ")
#     print("Type 'q' if want to quit")
#     if name == 'q':
#         break


# l = [16, 25, 8, 6, 3, 81]
# for i in range(len(l)):
#     for j in range(max(l)):
# #         if j*j==l[i]:
# #             print('Match Found :',l[i])
#
# l = [2,3,4,5,6,6]
# new=[4,3,6,7,3]
# for i in range(len(l)):
#     for j in range(len(new)):
#         if new[j]==l[i]:
#             print('Match Found:',new[j])
#
#
# set={3,4,5,6,6,7,8,9}
# print(set)
# set.pop()
# set.pop()
# print(set)

my_dict = {'UK':'London','SL':'Colombo'}
keys_list = list(my_dict.keys())[0]
print(keys_list)

