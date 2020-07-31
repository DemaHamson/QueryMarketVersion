import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import threading

def getHuawei():
	# phantomjs 完整路径
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	# 你的app应用市场链接
	driver.get("https://appgallery.cloud.huawei.com/uowap/index.html#/detailApp/xxxx")
	time.sleep(5)
	element = driver.find_elements_by_class_name("info_val")[2]
	print('华为{0}'.format(element.text))
	driver.quit()

def getXiaomi():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')	
	driver.get("http://app.mi.com/details?id=xxxx")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	version=soup.select('.preventDefault ul li') [3].text
	print('小米{0}'.format(version))
	driver.quit()

def getVivo():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get("http://info.appstore.vivo.com.cn/detail/xxxx")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	version=soup.small.text
	print('vivo{0}'.format(version))
	driver.quit()

def getMeizu():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get("http://app.meizu.com/apps/public/detail?package_name=xxxx")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	version=soup.select('div.app_content.ellipsis.noPointer')[0].text
	print('魅族{0}'.format(version))
	driver.quit()

def getYingyongbao():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get("https://sj.qq.com/myapp/detail.htm?apkName=xxxx")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	version=soup.select('.det-othinfo-data')[0].text
	print('应用宝{0}'.format(version))
	driver.quit()

def getBaidu():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get("http://shouji.baidu.com/software/xxxx.html")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	element = driver.find_elements_by_class_name("version")[0]
	print('百度{0}'.format(element.text))
	driver.quit()

def get360():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get("http://zhushou.360.cn/detail/index/soft_id/xxxx")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	version=soup.select('.base-info table tr:nth-of-type(2) td')[0].text
	print('360{0}'.format(version))
	driver.quit()

def getIOS():
	driver=webdriver.PhantomJS(executable_path='xxxx/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get("https://apps.apple.com/cn/app/xxxx")
	time.sleep(5)
	soup = bs(driver.page_source,'lxml')
	version=soup.select('p.l-column.small-6.medium-12.whats-new__latest__version')[0].text
	print('iOS{0}'.format(version))
	driver.quit()

if __name__ == '__main__':
	threads=[
		threading.Thread(target=getHuawei),
		threading.Thread(target=getXiaomi),
		threading.Thread(target=getVivo),
		threading.Thread(target=getMeizu),
		threading.Thread(target=getYingyongbao),
		threading.Thread(target=getBaidu),
		threading.Thread(target=get360),
		threading.Thread(target=getIOS)
	]
	for t in threads:
		t.start()
