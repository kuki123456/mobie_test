import yaml
def build_data(data_key,filename):
    # ls_data=[]
    with open("data/"+filename,"r",encoding="utf-8") as f:
        data=yaml.load(f)
        # for i in data[data_key].values():
        #     ls_data.append(i)
        return data[data_key].values()
