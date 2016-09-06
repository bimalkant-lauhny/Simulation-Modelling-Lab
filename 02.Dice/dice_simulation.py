###		#   #	 #
#  #	# #		 #
###		##		 #
#  #	# #		 #
###		#   #	 #####

import random
import numpy as np
import matplotlib.pyplot as plt


simulations = int(raw_input("Enter the number of simulation you want to perform: "))

print "Performing simulations..."

occurences = [0]*7

for _ in range(0, simulations):
	number = random.randint(1,6)
	occurences[number] += 1

print "\nSimulation Results : \n"
print "Number\tOccurences"

for i in range(1, 7):
	print i,"\t\t",occurences[i]

n_groups = 6
occurences.pop(0)
objects = ('1', '2', '3', '4', '5','6')
y_pos = np.arange(n_groups)
 
plt.bar(y_pos, occurences, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Number on Dice')
plt.ylabel('Number of Occurences')
plt.title('6-Faced Dice Simulation')
plt.legend()
plt.tight_layout()
plt.show()