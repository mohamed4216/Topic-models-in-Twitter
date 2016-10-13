import matplotlib.pyplot as plt

# Vectors
my_listX = []
my_listY = []

# number of docs
number = 700

#Read file
fopen = open("Mallet2Output/perplexity"+str(number)+".txt")

# Draw curve
line = fopen.readline()
count = 2
while line : 
		value = line.split(" ")[2]
		my_listX.append(count)
		my_listY.append(float(value))
		line = fopen.readline()
		count = count + 1	

plt.xlabel('Number of topics')
plt.ylabel('Perplexity')
plt.title('Perplexity = f(#Topics) for #docs='+str(number))
fopen.close()
plt.plot(my_listX, my_listY)
plt.grid(True)
plt.show()
