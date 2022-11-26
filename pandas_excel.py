# import pandas as pd
# import matplotlib.pyplot as plt

# excel_data = pd.read_excel(
#         "sales.xlsx", 
#         sheet_name="Лист1", 
#         usecols=["ID", "Название", "количество продаж"]
#         )

# excel_data.plot(x="Название", y="количество продаж", kind="bar")
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
 
# excel_data = pd.read_excel(
#         "sum.xlsx",
#         sheet_name="Лист1",
#         usecols=["month","total_sum"]
#         )

# excel_data.plot(x="month",y="total_sum", kind="line")
# plt.show()





# students_data = {
#     "Student":["Nuraiym","Nestan","Nazar","Syimyk"],
#     "GPA":[4.8, 4.5, 3.2, 3.9]
# }

# df = pd.DataFrame(students_data,columns=["Student","GPA"])
# df.plot(x="Student",y="GPA", kind="scatter")
# plt.show()