
def number_of_ways(corridor: str) -> int:
    strings = [corridor]
    count = 0
    left_index = 0
    for i in range(len(corridor)):
        if count == 2:
            if corridor[i:].count('S') >= 2:
                strings.append(corridor[i:])
                count = 0
            else:
                strings.append(corridor[i:])
        if corridor[i] == 'S':
            count += 1
    return strings


print(number_of_ways('SPPSPSSPSSSPSPPSPPS'))
'''
SPPSPSSPSSSPSPPSPPS
    PSSPSSSPSPPSPPS    
       PSSSPSPPSPPS  
          SPSPPSPPS
             PPSPPS
'''
