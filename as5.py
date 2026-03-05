def check_course(code):
    if len(code) == 5 or len(code) == 6:
        letters = code[:-3]
        numbers = code[-3:]
        
        if letters.isupper() and letters.isalpha() and numbers.isdigit():
            return True
    return False

def check_hex(color):
    if len(color) != 7:
        return False
    
    if color[0] != "#":
        return False
    
    for c in color[1:]:
        if c not in "0123456789ABCDEFabcdef":
            return False
            
    return True

def sum_numbers(text):
    words = text.split()
    total = 0
    
    for w in words:
        if w.isdigit():
            total += int(w)
    
    return total