from collections import deque

def currencyformat(number):
    st = str(number)
    number_list = st.split('.')
    floating =''
    if number_list[1]:
        floating = list(number_list)[1]
    integer = list(number_list)[0]
    if number < 0:
        integer = integer[1:]
    result = deque(integer[0])
    for i in range(1, len(integer)):
        if (len(integer) - i) % 3 == 0:
            result.append(',') 
        result.append(st[i])
    if floating:
        result.append('.')
        result.extend(floating)
    if number < 0:
        result.appendleft('-')
    return ''.join(result)



print(currencyformat(-6252411313.233))