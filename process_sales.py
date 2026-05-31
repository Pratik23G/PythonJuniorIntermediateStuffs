def sales_generator(file_name):
    for rows in open(file_name, "r"):
            parts = rows.strip().split(",")

            category = parts[1]
            price = float(parts[2])

            if category == "Electronics":
                yield price

total_updated_rev = sum(sales_generator("sales.txt"))

print(f"The total rev in $: {total_updated_rev}")