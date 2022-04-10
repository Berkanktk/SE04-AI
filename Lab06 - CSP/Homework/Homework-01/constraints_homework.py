class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_south_america_csp():
    a, bo, br, ch, co, e, fg, g, pa, pe, s, u, v = 'A', 'BO', 'BR', 'CH', 'CO', 'E', 'FG', 'G', 'PA', 'PE', 'S', 'U', 'V'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [a, bo, br, ch, co, e, fg, g, pa, pe, s, u, v]
    domains = {
        a: values[:],
        bo: values[:],
        br: values[:],
        ch: values[:],
        co: values[:],
        e: values[:],
        fg: values[:],
        g: values[:],
        pa: values[:],
        pe: values[:],
        s: values[:],
        u: values[:],
        v: values[:]
    }
    neighbours = {
        a: [ch, u, br, pa, bo],
        bo: [a, pa, br, pe, ch],
        br: [u, a, pa, bo, pe, co, v, g, s, fg],
        ch: [a, bo, pe],
        co: [e, pe, br, v],
        e: [pe, co],
        fg: [s, br],
        g: [v, br, s],
        pa: [a, br, bo],
        pe: [ch, bo, br, co, e],
        s: [g, br, fg],
        u: [a, br],
        v: [co, br, g]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        a: constraint_function,
        bo: constraint_function,
        br: constraint_function,
        ch: constraint_function,
        co: constraint_function,
        e: constraint_function,
        fg: constraint_function,
        g: constraint_function,
        pa: constraint_function,
        pe: constraint_function,
        s: constraint_function,
        u: constraint_function,
        v: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
