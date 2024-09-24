import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many commmand-line arguments')
elif len(sys.argv[1]) < 3:
    sys.exit('Not a CSV file')
elif sys.argv[1][-4:] != '.csv':
    sys.exit('Not a CSV file')

pizzas = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        pizza_type = reader.fieldnames[0]
        for row in reader:
            pizzas.append({
                pizza_type : row[pizza_type],
                'Small' : row['Small'],
                'Large' : row['Large'],
            })

except FileNotFoundError:
    sys.exit('File does not exist')

tabulate_data = tabulate(pizzas, headers="keys", tablefmt="grid")
print(tabulate_data)