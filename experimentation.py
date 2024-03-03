import pandas as pd

df = pd.read_excel(r"C:\Users\Bailey\Desktop\L6SD_Python\W3\rugby_players_data_extra.xlsx")
data = df["Empty"]
lis = data.tolist()




def BubbleSort(arr):
        
        leng = len(arr)
        for i in range(leng - 1):
            for j in range(leng - i - 1):
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])                  
                j += 1    
            i += 1
        return arr


l1 = []