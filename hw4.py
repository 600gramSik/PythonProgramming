name = input("Input his/her name: ")
def rep_char(c, n):
    print(c * n)

def draw_line_string(string_literal):
    rep_char('-', (len(string_literal)*2))
    print(f'Helo {string_literal},\nWelcome to Seoul')
    rep_char('-', (len(string_literal)*2))

draw_line_string(name)