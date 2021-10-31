class AccountingSystem():
    def __init__(self):
        self.all_account = set()
    
    def register(self, acc):
        self.all_account.add(acc)

    def ungister(self, acc):
        self.all_account.remove(acc)
    
    def notify(self):
        for account in self.all_account:
            account.update()

class BusinessCustomer():
    def __init__(self, acc_num, money_own):
        self.account_num = acc_num
        self.money_due = money_own
    
    def update(self):
        if self.money_due > 0:
            print(f'{self.account_num} please contact to finance team')
        else:
            print(f'{self.account_num} amount fully paid')


class ConsumerCustomer():
    def __init__(self, acc_num, money_own):
        self.account_num = acc_num
        self.money_due = money_own
    
    def update(self):
        if self.money_due > 0:
            print(f'{self.account_num} Amount need to Pay')
        else:
            print(f'{self.account_num} amount fully paid by customer')

if __name__ == '__main__' :
    cust1 = BusinessCustomer("AC101",10)
    cust2 = BusinessCustomer("AC102", -10)
    cust3 = ConsumerCustomer("AC103", 0)
    cust4 = ConsumerCustomer("AC104", -10)

    acc_sys = AccountingSystem()
    acc_sys.register(cust1)
    acc_sys.register(cust2)
    acc_sys.register(cust3)
    acc_sys.register(cust4)

    acc_sys.notify()

    acc_sys.ungister(cust1)

    print("")

    acc_sys.notify()
