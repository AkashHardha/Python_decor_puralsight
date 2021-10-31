def deco_upper(functions):
    def ret_upper():
        func = functions()
        upper_text = func.upper()
        return upper_text
    
    return ret_upper

def say_HI():
    return "hi"

output = deco_upper(say_HI)
print(output)