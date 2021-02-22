import yaml
##safe_load将yaml数据流转换成Python对象
def test_yaml():
    with open("./data/cala.yml") as f:
        datas=yaml.safe_load(f)
        print(datas['add']['datas'][0])
        return (datas['add']['datas'], datas['add']['ids'])
