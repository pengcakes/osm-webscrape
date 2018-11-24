import csv
import numpy as np
import matplotlib.pyplot as plt



with open('csv/irontest.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')



# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)

# plt.scatter(x, y)
# plt.show()


end = time.time()
print(round(end - start, 5))