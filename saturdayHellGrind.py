import random

def summarize(*numbers, precision: int = 2):
    if not numbers:
        return {"max": 0.0, "min" : 0.0, "avg" : 0.0}

    resultDict: [dict, str] = { 
                    "max": round(max(numbers), precision),
                    "min": round(min(numbers), precision),
                    "avg": round((sum(numbers) / len(numbers)), precision)
    }
    return resultDict


inputTests = summarize(1, 2, 0)

print(inputTests)

#today we learn something quick


with open("sales.txt", "w") as f:
    for i in range(100_000):
        # Format: TransactionID,Category,Amount
        category = random.choice(["Electronics", "Clothing", "Home", "Books"])
        amount = round(random.uniform(5.0, 500.0), 2)
        f.write(f"{i},{category},{amount}\n")
print("sales.txt created successfully!")


