import os
import pandas as pd

# 获取当前目录下的所有Excel文件
excel_files = [f for f in os.listdir('.') if f.endswith('.xlsx')]

# 遍历每个Excel文件
for file in excel_files:
    # 读取Excel文件
    df = pd.read_excel(file)

    # 按题型和问题排序
    sorted_df = df.sort_values(by=['题型', '问题'], ascending=[True, True])

    # 保存排序后的数据到新的Excel文件
    sorted_df.to_excel(f'sorted_{file}', index=False)

