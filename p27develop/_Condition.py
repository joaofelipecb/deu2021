import p26struct._Condition
import p28except._InvalidConditionOperator

class Condition(p26struct._Condition.Condition):
    def __init__(self, operator, operands):
        import p23control._Condition
        if not p23control._Condition.is_operator_valid(operator):
            raise p28except._InvalidConditionOperator.InvalidConditionOperator(operator)
        super().__init__(operator,operands)
        