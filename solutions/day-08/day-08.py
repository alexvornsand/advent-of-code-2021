# advent of code
# day 8

# part 1
"""
displays = open('day-08.txt', 'r').read().split('\n')[:-1]

print(displays)

def decodeDisplays(displays, partTwo=False):
    displayValue = 0
    if partTwo is False:
        for display in displays:
            digits = display.split(' | ')[1].split(' ')
            displayValue += len([digit for digit in digits if len(digit) in [2, 3, 4, 7]])
    else:

    print(displayValue)


decodeDisplays(displays)

"""

display = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'


def parseDisplay(display):
    keys = [[seg for seg in key] for key in display.split(' | ')[0].split(' ')]
    assignments = {}
    segments = {}
    for i in range(len(keys)):
        if len(keys[i]) == 2:
            assignments['1'] = keys[i]
        if len(keys[i]) == 4:
            assignments['4'] = keys[i]
        if len(keys[i]) == 3:
            assignments['7'] = keys[i]
    if '1' in assignments and '7' in assignments:
        segments['A'] = list(
            set(assignments['7']).difference(set(assignments['1'])))[0]
    if '1' not in assignments and '4' in assignments and '7' in assignments:
        assignments['1'] = list(
            set(assignments['4']).intersection(set(assignments['7'])))
    while len(assignments) < 10 and len(segments) < 7:
        for key in keys:
            if len(key) == 5:
                if all([seg in key for seg in assignments['1']]):
                    assignments['3'] = key
            if len(key) == 6:
                if not all([seg in key for seg in assignments['1']]):
                    assignments['6'] = key
                    segments['C'] = list(
                        set(assignments['1']).difference(set(assignments['6'])))[0]


parseDisplay(display)
