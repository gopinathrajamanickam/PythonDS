# Tabulate

from tabulate import tabulate

data = [
        ["first","last","ldap"]
       ,["Gopi","Raja","gopiraja"]
       ,["Geerthy","Guna","geerthyguna"] 
       ]

print(tabulate(data, headers = 'firstrow', tablefmt = 'grid'))
print(tabulate(data, headers = 'firstrow', tablefmt = 'fancy_grid'))
