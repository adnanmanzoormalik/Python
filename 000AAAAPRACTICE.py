class BalError(Exception):
    def __init__(self, bal, amt):
        self.bal = bal
        self.wd = amt

        super().__init__(
            f"Balance cant be greater than withdrawl. Balance: {bal}, Withdrawl: {amt}"
        )

bal = 1000
wd = 10000

try:
    if bal<wd:
        raise BalError(bal, wd)
    
except BalError as e:
    print(e)
else:
    print(bal-wd)
