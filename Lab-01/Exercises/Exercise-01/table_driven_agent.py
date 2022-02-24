A = 'A'
B = 'B'

percepts = []
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((A, 'Clean'),): 'Suck',
    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean')): 'Suck',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (A, 'Clean')): 'Left'
}


def LOOKUP(percepts, table):
    action = table.get(tuple(percepts))
    return action


def TABLE_DRIVEN_AGENT(percept):
    percepts.append(percept)
    action = LOOKUP(percepts, table)
    return action


def run():
    print('Action   Percepts')
    print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)


if __name__ == '__main__':
    run()
