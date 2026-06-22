import pandas as pd
import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 25, 15, 30]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.bar(df['Category'], df['Values'], color='skyblue')

plt.title('Data Visualization Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()