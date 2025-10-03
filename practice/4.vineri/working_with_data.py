# cerință 1:
# =========
# dat fiind transactions.csv
# calculați balanța curentă a tuturor conturilor
#
# credit = account receives money
# debit  = account spends money


# strategie:
#
# un dicționar cu cheia fiecărui `account_id`
# rezultat:
# balance = {
#    562: 635,
#    628: ...,
#    ...
# }
#
# 1. parcurgem fișierul.
#     a) prima coloană se duce în cheia dicționarului
#     b) a doua coloană ne spune dacă este plus sau minus
#     c) a 3a se duce în valoare

import csv

def process_transactions(csvfile):
    balance = {}

    with open(csvfile) as f:
        dreader = csv.DictReader(f)
        
        
        for row in dreader:
            acc_id = int(row['account_id'])
            ttype = row['transaction_type']
            amount = int(row['amount'])

            if acc_id not in balance:
                balance[acc_id] = 0
            
            if ttype == 'credit':
                balance[acc_id] = balance[acc_id] + amount
            elif ttype == 'debit':
                balance[acc_id] = balance[acc_id] - amount
            else:
                # panic!
                print("big error")
    
    return balance

import json
def pretty_print(obj):
    print(json.dumps(obj, indent=2))

# pretty_print(process_transactions("data/transactions.csv"))

# cerință 2:
# =========
# a) dat fiind clients.json
#    aflați care sunt clienții cu balanță negativă
#    și care au depășit pentru respectivul cont 70% din limita de overdraft
#
# b) notificați-i
#    (ne prefacem că le trimitem un mail pre-formatat după un template)

# clients.json este o listă de dicționare de forma
#   {
#     "name": "...",
#     "email_address": "...",
#     "bank_accounts": [
#       {
#         "id": ...,
#         "overdraft": ...
#       },
#       ...
#     ]
#   }

OVERDRAFT_LIMIT = 70/100

balances = process_transactions("data/transactions.csv")

def warn(customer, account):
    print("warning", customer)
    print(account)

with open("data/clients.json") as fp:
    clients = json.load(fp)

    for client in clients:
        # client is a dict
        accounts = client["bank_accounts"]
        for account in accounts:
            acc_id = account['id']
            overdraft = account['overdraft']

            current_value = balances[acc_id]
            if (
                current_value < 0 and
                -current_value >= OVERDRAFT_LIMIT * overdraft
            ):
                warn(client, account)