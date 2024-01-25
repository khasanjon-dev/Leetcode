def reformat_date(date: str) -> str:
    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    result = ''
    d, m, year = date.split()
    result += year
    result += '-' + month[m]
    result += '-'
    if len(d) == 4:
        result += d[:2]
    else:
        result += '0' + d[0]
    return result


print(reformat_date('20th Oct 2052'))
