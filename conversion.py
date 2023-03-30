import glob
import pandas as pd

path = r"C:\Users\Bindu\Desktop\datamyne"
file_list = glob.glob(path + "/*.xlsx")
excl_list = []
for file in file_list:
    excl_list.append(pd.read_excel(file, dtype='unicode', engine='openpyxl'))
excl_merged = pd.DataFrame()
for excl_file in excl_list:
    excl_merged = excl_merged.append(excl_file, ignore_index=True)
excl_merged.to_excel(r"C:\Users\Bindu\Desktop\datamyne\hongkong-us.xlsx", index=False)
