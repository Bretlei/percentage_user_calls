# Importing my modules!
import os

# Defining some variables!
search_path = 'C:/Users/bretlei/Documents/Notes/'
file_type = '.txt'
search_str = ['client name goes here']
results = []
not_results = []
counter = 0
not_counter = 0

# Open file for reading
# If anything from the open files is anything from search_str...
# Do some hardcore shit.
# If not, let me know because I don't trust you.

for fname in os.listdir(path=search_path):
    file_open_and_read = open(search_path + fname).read()

    if any(x in file_open_and_read.lower() for x in search_str):
        if fname not in results:
            counter += 1
            results.append(fname)
    else:
        not_counter += 1
        not_results.append(fname)

print(str(counter) + ' matches!')
print(str(not_counter) + " didn't match.")

percent = float(counter / not_counter * 100)

print('Percentage chance of CLIENT calling is ~%s percent' % percent)
