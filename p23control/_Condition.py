import p17data._Condition
import p23control._String
import p23control._Symbol
import p27develop._Condition

def is_operator_valid(operatorName):
    return operatorName in p17data._Condition.operators

def parse(string):
    operator = ''
    operands = []
    mode = 'first'
    buffer = ''
    for i in string:
        if mode == 'first':
            if i == ' ':
                mode = 'operator'
                operands.append(buffer)
                buffer = ''
            else:
                buffer = buffer + i
        elif mode == 'operator':
            buffer = buffer + i
            if buffer == 'IS NOT NULL':
                operator = buffer
    return p27develop._Condition.Condition(operator,operands)
    
def verify(condition,namespace):
    operands = condition.operands
    resolvedOperands = list(map(lambda x: p23control._Symbol.resolve(x,namespace),operands))
    snakedOperator = p23control._String.to_snake_case(condition.operator)
    return globals()['verify_'+snakedOperator](resolvedOperands)

def verify_is_not_null(operands):
    operand = operands[0]
    return operand is not None
