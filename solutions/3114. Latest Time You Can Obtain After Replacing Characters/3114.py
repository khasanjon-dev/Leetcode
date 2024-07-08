def find_latest_time(s: str) -> str:
    oclock = ''
    first: str
    last: str
    hour, minute = s.split(':')
    if hour[0] == hour[1] == '?':
        oclock += '11'
    elif hour[0] == '?':
        if hour[1] == '1' or hour[1] == '0':
            oclock += '1' + hour[1]
        else:
            oclock += '0' + hour[1]
    elif hour[1] == '?':
        if hour[0] == '1':
            oclock += '11'
        else:
            oclock += hour[0] + '9'
    else:
        oclock += hour

    oclock += ':'

    if minute[0] == minute[1] == '?':
        oclock += '59'
    elif minute[0] == '?':
        oclock += '5' + minute[1]
    elif minute[1] == '?':
        oclock += minute[0] + '9'
    else:
        oclock += minute
    return oclock


print(find_latest_time("1?:?4"))
