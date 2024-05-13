import logging
import time
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import*

class MyTestCase(unittest.TestCase):
    def test_all(self):
        logging.info("=============运行所有的case==========")
        suit=unittest.defaultTestLoader.discover(test_path,'test*.py')
        # t = time.strftime('%Y_%m_%d_%H_%M_%S')
        with  open(report_file, 'wb')as f:
            HTMLTestRunner(
                stream=f,
                title='xzs测试用例',
                description='xzs登录和注册用例集',
                verbosity=2
            ).run(suit)
        # 发送邮件
        send_email(report_file)
        logging.info("===================测试结束===================")
if __name__ == '__main__':
    unittest.main()



def discover():#载入指定目录下的测试用例
    return unittest.defaultTestLoader.discover(test_case_path)
def run(suit):#执行测试用例，生成测试报告
    logging.info("====测试开始====")
    with open(report_file,"wb") as f:
        HTMLTestRunner(
            stream=f,
            title="接口测试",
            description="测试描述",
            verbosity=2
        ).run(suit)
    # send_emoil(report_file)
    logging.info("====测试结束====")
def run_all():#运行所有用例
    run(discover())
def run_suite(suite_name):#运行自定义的test
    suite = get_suit(suite_name)
    print(suite)
    if isinstance(suite,unittest.TestSuite):
       run(suite) #运行条件
    else:
        print("TestSuite不存在")


def collect():
    suite = unittest.TestSuite()
    def _collect(test):
        if isinstance(test,unittest.TestSuite):
            if test.countTestCases()!=0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return  suite
def collect_only():
    to = time.time()
    i = 0
    for case in collect():
        i+=1
        print("{}.{}".format(str(i),case.id()))
    print("----------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time() - tO))

def makesuit_by_testlist(testlist_file):
    with open(testlist_file,encoding='utf-8') as f:
        testlist=f.readines()
        testlist=[i.strip() for i in testlist if not i.starswith("#")]
        suit=unittest.TestSuite()
        all_cases=collect()
        for case in all_cases:
            if case.testNethodName in testlist:
                suit.addTest(case)
        return suit

def makesuit_by_tag(tag):
    suit = unittest.TestSuite()
    for i in collect():
        print(i._testMethodDoc)

    if __name__=='__main__':
        #testlist_suit = makesuit_by_testlist(config.config.test_file);
        #run(testlist_suit)
        makesuit_by_tag("level1")