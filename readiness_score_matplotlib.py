import pandas as pd
import matplotlib.pyplot as plt

readiness_data = pd.read_csv('oura_readiness.csv')

# Picking out values for the axes
readiness_scores_y = readiness_data.loc[:, 'score']
readiness_scores_x = readiness_data.loc[:, 'day']
readiness_scores_x_numbers = list(range(0, 344))

# 7 day rolling average
readiness_average = readiness_scores_y.rolling(window=7).mean()

# Headings an labels for the diagram 
plt.title('Oura readiness scores (344 days)', fontsize=15)
plt.xlabel('Day', fontsize=10)
plt.ylabel('Readiness Score', fontsize=10)
plt.tick_params(axis='x', which='both', labelsize=10)

 # Styling and naming lines
plt.plot(readiness_scores_y, 'b-', label='Readiness Score', linewidth=1)
plt.plot(readiness_average, 'g-', label='Rolling average', linewidth = 0.7)

plt.legend(loc='lower left')

# Rendering the graph
plt.show()
