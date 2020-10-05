def configureEquation(expression):
    lhs, rhs = list(map(str.strip, expression.split("=")))
    new_expression = f"{lhs} - ({rhs})"
    return new_expression