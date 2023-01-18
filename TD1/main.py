import pandas
import os
def get_sf(str):
    str=str.split("-")
    sf = str[2]
    return sf

def get_bw(str):
    str=str.split("-")
    bw = str[1]
    return bw

def get_cr(stri):
    stri=stri.replace(".csv","")
    stri=stri.split("-")
    cr = stri[3]
    cr = cr.replace("_"," ")
    return cr

def load_data(str):
    cr = get_cr(str)
    if not str.endswith('.csv'):
        str = str + '.csv'
    path = os.path.join(__file__.replace("main.py",""),'raw',str)
    df = pandas.read_csv(path)
    df['File UART (TXT)']=df['File UART (TXT)'].astype("string")
    df. rename(columns = {'Timestamp (S)':'Time(S)', 'File Main Current (A)':'Current(A)', 'File Main Voltage (V)':'Voltage(V)', 'File Main Energy (J)':" Energy(J)", "File UART (TXT)":"UART" }, inplace = True)
    df2= df.assign(CR=cr)
    return df2

def save_data(string):
    df = load_data(string)
    name= "dataset-"+get_bw(string)+"-"+get_sf(string)+".csv"
    print(name)
    path = os.path.join(__file__.replace("main.py",""),'raw',name)
    print(path)
    df.to_csv(path)

"""def fusion_data(directory):
    df12 = pandas.DataFrame(columns=["Time(s)","Current(A)","Voltage(V)","Energy(J)","UART"])
    path = os.path.join(__file__.replace("main.py", ""), directory)
    listFile = os.listdir(path)
    for i in listFile:
        listTemp=load_data(i)
        for j in range(len(listFile)):
            if int(get_sf(listFile[j])) == 12:
                for k in range(len[listTemp]):
                    df12.index[len(df12)+1].append(listTemp[k])
    return df12

print(fusion_data("raw"))"""