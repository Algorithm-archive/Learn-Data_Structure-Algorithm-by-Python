from search import linearSearch

hayStack = ['book','pencil','pen','note book','sharpener','rubber']
needle = input('What do you want to find: ')

if linearSearch(needle, hayStack):
    print('Found')
else:
    print('Not Found')
