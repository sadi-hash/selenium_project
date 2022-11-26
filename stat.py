import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_excel("stat.xls",sheet_name="5010003")
print(data)

data.plot(x="Наиминования,показателей",y=2021, kind="bar")
plt.show()