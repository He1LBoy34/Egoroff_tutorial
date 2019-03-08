k = 0

for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
            for b4 in 'tukva':
                for b5 in 'tukva':
                    for b6 in 'tukva':
                        rez = b1 + b2 + b3 + b4 + b5 + b6
                        if rez[0] in 'tkv' and rez[-1] in 'tkv':
                            if rez.count('a') + rez.count('u') == 2:
                                k += 1

print(k)
