import json
import csv
import sys


OVERDRAFT_LIMIT = 70/100


class Client:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.accounts = []

    def __repr__(self):
        return f"Client(name={repr(self.name)})"
    
class Account:
    def __init__(self, id, owner, overdraft=0):
        self.id = id
        self.owner = owner
        self.overdraft = overdraft
        self.balance = 0

    def __repr__(self):
        return f"Account(id={repr(self.id)})"
    
    def is_overdraft(self):
        return (
            self.balance < 0 and
            -self.balance >= OVERDRAFT_LIMIT * self.overdraft
        )

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        # nu îl lăsăm să treacă de overdraft!
        if self.balance - amount < -self.overdraft:
            raise ValueError("Insufficient funds!")
        self.balance -= amount

    def notify(self):
        print("aici îi trimit un mesaj")


def log(level, *messages):
    print(f"[{level}]", *messages, file=sys.stderr)

def process_clients(jsonfile):
    # 0. ne inițializăm lista
    clients = []

    # 1. deschidem jsonul
    with open(jsonfile) as fp:
        cdata = json.load(fp)

        # 2. iterăm prin lista de clienți (care sunt dicționare)
        for cdict in cdata:
            # 3. creăm clientul
            client = Client(cdict['name'], cdict['email_address'])
            
            try:
                # some clients may not have accounts
                acc_list = cdict['bank_accounts']
            except KeyError:
                # acest client nu are conturi.
                # ce facem?
                log("error", f"{client} nu are conturi!")
            else:
                # we do have an account list
                # 4. creăm conturile
                for acc in acc_list:
                    account = Account(acc['id'],
                                    owner=client,
                                    overdraft=acc['overdraft'])
                    client.accounts.append(account)

            clients.append(client)

    return clients


clients = process_clients("data/clients.json")
#         ^^ this already generates the accounts

acc_dict = {}
for c in clients:
    for acc in c.accounts:
        acc_dict[acc.id] = acc

def process_transactions(csvfile):
    with open(csvfile) as f:
        dreader = csv.DictReader(f)
        
        for row in dreader:
            acc_id = int(row['account_id'])
            ttype = row['transaction_type']
            amount = int(row['amount'])

            try:
                account = acc_dict[acc_id]
            except KeyError:
                log("almost fatal error",
                    "transactions for a non-existant account!",
                    acc_id
                    )
            else:
                if ttype == 'credit':
                    account.credit(amount)
                elif ttype == 'debit':
                    account.debit(amount)
                else:
                    # panic!
                    print("big error")


# this only has side-effects (it populates the balances)
process_transactions("data/transactions.csv")

# now we have the current state
for acc in acc_dict.values():
    if acc.is_overdraft():
        # we must notify these people
        print(acc, acc.overdraft, acc.balance, acc.owner)
