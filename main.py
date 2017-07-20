#-*- coding=utf-8 -*-
import urllib2	# 取得網頁
import urllib	# 取得網頁
import sys		# 輸入參數
import wget		# url 下載
import os
import getpass	# 取得登入使用者

os.system("cls")

# 如果參數沒有輸入，會讓使用者輸入網址
if len(sys.argv) < 2:
	web_url = raw_input("請輸入網址: ")
else:
	web_url = sys.argv[1]

# 如果網址不含有 http 開頭，則補上
if len(web_url.split("http"))<2:
	web_url = "http://"+web_url

# 讀取網頁
res = urllib2.urlopen(web_url)
html = res.read()

# 取得下載連結
url_list = []
html_arr = html.split("href=\"")

# enumerate 列舉
for index, code in enumerate(html_arr):
	if index==0:
		continue
	tmp = code.split("\"")
	url_list.append(tmp[0])



# 下載 ===================================================================
download_list = []
'''
# 取得 pdf 連結，練習使用含有 index 的寫法
for index, url in enumerate(url_list):
	tmp = url.split(".pdf")
	if len(tmp) > 1:
		download_list.append(tmp[0]+".pdf")
	else:
		continue
'''
# 所有連結都下載
for url in url_list:
	download_list.append(url)

# =======================================================================


'''
# 複製 Google Chrome 捷徑到本地目錄=========================================
cwd = os.getcwd()
user = getpass.getuser()
path = "\"C:\Users\\"+user+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk\" "
os.system("copy "+path+cwd+"\chrome.lnk")
# =======================================================================
'''


# 將要在後方加入子網站網址的 web_url 去除掉含有 ? 的參數
web_url_arr = web_url.split("?")
web_url = web_url_arr[0]

# 針對每一個 download list 下載檔案
for index, url in enumerate(download_list):

	part = "進度：(" + str(index+1) + "/" + str(len(download_list)) + ")"
	print "\n\n\n\n\n"+ part + "\n" + url

	# 如果下載網址是含有 http 開頭的完整網址
	if len(url.split("http"))>1:
		download_url = url
	else:
		download_url = web_url+"/../"+url

	# 如果是 https 跳過
	tmp = download_url.split("https://")
	if len(tmp)>1:
		continue

	# 將 http 如果有兩個 // 要改成一個 /
	tmp = download_url.split("http://")
	tmp[1] = tmp[1].replace("//","/")
	download_url = "http://" + tmp[1]
	print download_url
	filename = wget.download(download_url)
'''
	# 透過 google chrome 下載
	# 如果本地目錄有成功取得 Chrome 連結
	if os.path.isfile("./chrome.lnk"):
		os.system("chrome.lnk "+download_url)
	else:
	# 否則就透過 wget 下載
		filename = wget.download(download_url)

'''

# Reference

# 參考: http://seanlin.logdown.com/posts/210856-python-idioms-6-enumerate
# 一種 for 也可以取得 index 的方法