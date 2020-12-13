import matplotlib.pyplot as plt 

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Gold', 'Silver', 'Bronze'
medals = [315, 203, 107]
colors = ['gold', 'silver', 'brown']



fig1, ax1 = plt.subplots()
ax1.pie(medals, labels=labels, autopct='%1.1f%%', colors=colors,
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()