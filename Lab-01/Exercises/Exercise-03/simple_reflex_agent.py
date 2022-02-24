A = 'A'
B = 'B'

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4,
}

environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': 'A'
}


def interpret_input(input):
    return input


def rule_match(state, rules):
    rule = rules.get(tuple(state))
    return rule


def simple_reflex_agent(percept):
    state = interpret_input(percept)
    rule = rule_match(state, rules)
    action = RULE_ACTION[rule]
    return action


def sensors():
    location = environment['Current']
    return (location, environment[location])


def actuators(action):
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        environment['Current'] = B
    elif action == 'Left' and location == B:
        environment['Current'] = A


def run(n):
    print('      Current                       New')
    print('location\tstatus\taction\tlocation\tstatus')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:12s}{:8s}".format(location, status), end='')
        action = simple_reflex_agent(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == "__main__":
    run(10)
