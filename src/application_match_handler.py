import operator
from src.bank import Bank, Constraint
    
    
def get_banks():
    banks = []
    
    consumer_loans = Constraint("borrowerType", operator.eq, "consumer")
    risk = Constraint("riskLevel", operator.lt, 80)
    banks.append(Bank("First Lama Bank", [consumer_loans, risk]))
    
    amount = Constraint("requestedAmount", operator.lt, 200000)
    banks.append(Bank("Lama International Bank", [amount]))
    
    student = Constraint("loanType", operator.eq, "Student Loan")
    state = Constraint("state", operator.eq, "CA")
    risk = Constraint("riskLevel", operator.lt, 60)
    banks.append(Bank("Bank HaPoalama", [student, state, risk]))
    
    bussiness = Constraint("borrowerType", operator.eq, "business")
    amount = Constraint("requestedAmount", operator.gt, 500000)
    risk = Constraint("riskLevel", operator.lt, 80)
    banks.append(Bank("Salt and Pepper", [bussiness, amount, risk]))
    
    industry = Constraint("industry" ,operator.eq, "Restaurant")
    student = Constraint("loanType", operator.eq, "Line of Credit")
    banks.append(Bank("Bank Otzar Halama", [industry, student]))
    
    banks.sort(reverse=True, key=lambda bank:bank.constraints_length)
    return banks
  
    
def application_match_handler(application_request):
    banks = get_banks()
    result = []
    for bank in banks:
        if bank.check_constraints(application_request):
            result.append(bank.name)
        if len(result) == 2:
            break
    return result
