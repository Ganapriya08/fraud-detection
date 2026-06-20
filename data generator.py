import random
import time
import pandas as pd
from datetime import datetime

locations = ["Delhi", "Mumbai", "Hyderabad", "Bangalore"]

def generate_transaction():
    return {
        "user_id": f"user_{random.randint(1,5)}",
        "amount": random.randint(100, 50000),
        "location": random.choice(locations),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

print("Generating transactions...")

while True:
    tx = generate_transaction()
    df = pd.DataFrame([tx])
    df.to_csv("transactions.csv", mode="a", header=False, index=False)
    print(tx)
    time.sleep(2)