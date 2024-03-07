import operator
import pydash


class Constraint:
    def __init__(self, constraint_field_path:str, constraint_condition:operator, constraint_target):
        self.constraint_field_path = constraint_field_path
        self.constraint_condition = constraint_condition
        self.constraint_target = constraint_target
        
    def check(self, application):
        field = pydash.get(application, self.constraint_field_path)
        if field is None:
            return False
        result = self.constraint_condition(field, self.constraint_target)
        return result


class Bank:
    def __init__(self, name, constraints=[]):
        self.name = name
        self.constraints = constraints
        self.constraints_length = len(self.constraints)
        
    def check_constraints(self, application):
        result = all([c.check(application) for c in self.constraints])
        return result        
    