def read_single_digit(digit):
    if digit == 0:
        return "영"
    elif digit == 1:
        return "일"
    elif digit == 2:
        return "이"
    elif digit == 3:
        return "삼"
    elif digit == 4:
        return "사"
    elif digit == 5:
        return "오"
    elif digit == 6:
        return "육"
    elif digit == 7:
        return "칠"
    elif digit == 8:
        return "팔"
    elif digit == 9:
        return "구"
    else:
        return "" 
    
def read_number(num):
    
    if num < 0 or num > 999:
        return ""  
    
    hundreds = num // 100  
    tens = (num % 100) // 10  
    units = num % 10  
    
    result = ""
    
    if hundreds > 0:
        result += read_single_digit(hundreds) + "백"
    
    if tens > 0:
        result += read_single_digit(tens) + "십"
    
    if units > 0 or (hundreds == 0 and tens == 0):  
        result += read_single_digit(units)
    
    return result

