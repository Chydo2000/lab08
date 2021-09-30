def check_int(num):
    retval = str(num)
    if num == 10 or num == 20:
        retval = "Luku on 10 tai 20"
    if num == 100 or num == 200:
        retval = "Luku on 100 tai 200"
    return retval