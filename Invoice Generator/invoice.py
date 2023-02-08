def generate_invoice(client, total, items, date):
    invoice = "Invoice for {}\n".format(client)
    invoice += "Date: {}\n".format(date)
    invoice += "Items:\n"
    for item in items:
        invoice += "- {}: ${}\n".format(item[0], item[1])
    invoice += "Total: ${}\n".format(total)
    return invoice

inv = generate_invoice("Paul George", 1000, [("Item 1", 300), ("Item 2", 200), ("Item 3", 500)], "2023-02-07")
print(inv)
