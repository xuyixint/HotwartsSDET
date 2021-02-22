from pythoncode.Calculate import Calculate
import pytest
import sys
import yaml

sys.path.append('..')
print(sys.path)


def get_dates():
    with open("./data/cala.yml") as f:
        datas = yaml.safe_load(f)
        return (datas['add']['datas'],datas['add']['ids'],datas['idv']['datas'])



#yaml json excel csv xml
#测试类
class TestCalc:


    #datas类型提示
    datas:list=get_dates()
    #前置条件
    def setup_class(self):
        print("开始计算")
        self.calc=Calculate()
    #后置条件
    def teardown_class(self):
        print("结束计算")

##todo 补全加法
##todo 补全除法
##第一个是datas[0]，第二个是datas[1]是类型，ids一定要加=
    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_add(self,a,b,result):
       print(f"a={a},b={b},result={result}")
       assert result==round(self.calc.add(a,b),2)

    @pytest.mark.parametrize("a,b,result",datas[2])
    def test_div(self,a,b,result):
        if b!=0:
            assert result==self.calc.div(a,b)
        else:
            try:
                self.calc.div(a,b)
            except Exception as e:
                print(e)

