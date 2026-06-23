# TITLE: Blind Secret Auction Platform
# DESCRIPTION: A blind auction console system utilizing dynamic nested dictionary data configurations to programmatically isolate independent bid records.
# LIMITATIONS: Volatile Local Retention: Record arrays are stored temporarily inside volatile cache registers; restarting or experiencing a script drop wipes out all database records. | Overwritten Tie Conflict: If multiple bidders independently submit identical maximum cash values, the extraction mechanism defaults to returning whichever user entered their information first.
# CHALLENGE: Upgrade the collection query logic to isolate tie-states, producing a detailed winner breakout message if more than one user possesses matching highest values.

print('''                                         
                 | |                                        
 _ __ ___   __ _| | _____ _ __ ___   ___  _ __   ___ _   _ 
| '_ ` _ \ / _` | |/ / _ \ '_ ` _ \ / _ \| '_ \ / _ \ | | |
| | | | | | (_| |  <  __/ | | | | | (_) | | | |  __/ |_| |
|_| |_| |_|\__,_|_|\_\___|_| |_| |_|\___/|_| |_|\___|\__, |
                                                      __/ |
                                                     |___/ ''')

bid_records = {} 

while True:
    name = input("Enter your name: ").strip().lower()

    if name == 'exit':
        break

    bid = int(input("Enter bid price: $"))

    bid_records[name] = bid


winner_name = max(bid_records, key=bid_records.get)

highest_bid = bid_records[winner_name]

print(bid_records)

print(f"\nThe highest bid is ${highest_bid} by {winner_name.capitalize()}!")