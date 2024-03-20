# def show_message() :
#     print('hello world!')
#     print('good job!')

# print('시작')
# show_message()
# print('끝')

# num = 1004
# print(num)
# num = '천사'
# print(num)

# def show_message(msg='안녕하세요', name='여러분') :
#     print(msg, name, "님")
# print('시작')
# show_message()
# show_message(name='김근식')
# show_message(msg='반갑습니다')
# show_message('안녕')
# print('끝')

# def show_message():
#     print('hello')
#     return 'good bye!'

# print('시작')
# result = show_message()
# print(result)
# print('끝')

# print('당신의 이름은? ', end='')
# name = input()
# print('반가워요', name)

# name = input('당신의 이름은?')
# print('반가워요', name)

# def make_message():
#     name = input('당신의 이름은?')
#     msg = '반가워요 ' + name
#     print(msg)

# print('시작')
# make_message()
# print('마침')

def make_message(name) :
    msg = '반가워요 ' + name
    return msg

print('시작')
input_name = input('당신의 이름은?')
result = make_message(input_name)
print(result)
print('끝')