import matplotlib.pyplot as plt 


data = {'Canada':625, 'Finland':434} 

countries = list(data.keys()) 
medals = list(data.values()) 

plt.bar(countries, medals, color ='maroon',  
        width = 0.4) 

plt.xlabel("Countries") 
plt.ylabel("Total Medals") 
plt.title("Canada vs Finland Olympic Medals")

plt.show()