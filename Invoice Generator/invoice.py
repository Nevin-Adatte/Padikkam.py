def generate_invoice(client, total, items, date):
    invoice = "Invoice for {}\n".format(client)
    invoice += "Date: {}\n".format(date)
    invoice += "Items:\n"
    for item in items:
        invoice += "- {}: ${}\n".format(item[0], item[1])
    invoice += "Total: ${}\n".format(total)
    return invoice

inv = generate_invoice("John Doe", 1000, [("Item 1", 100), ("Item 2", 200)], "2022-12-31")
print(inv)
