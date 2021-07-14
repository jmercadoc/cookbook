"""
Problem
    You program has become an unreadable mess of hardcoded slice indices and you want to clean it up

"""
record = '....................100     .......513.25      ..........'

SHARES = slice(20,24)
PRICE = slice(35,41)

print("SHARES",record[SHARES])
print("PRICE", record[PRICE])