#-*- coding=utf-8 -*-
import urllib2	# ���o����
import urllib	# ���o����
import sys		# ��J�Ѽ�
import wget		# url �U��
import os
import getpass	# ���o�n�J�ϥΪ�

os.system("cls")

# �p�G�ѼƨS����J�A�|���ϥΪ̿�J���}
if len(sys.argv) < 2:
	web_url = raw_input("�п�J���}: ")
else:
	web_url = sys.argv[1]

# �p�G���}���t�� http �}�Y�A�h�ɤW
if len(web_url.split("http"))<2:
	web_url = "http://"+web_url

# Ū������
res = urllib2.urlopen(web_url)
html = res.read()

# ���o�U���s��
url_list = []
html_arr = html.split("href=\"")

# enumerate �C�|
for index, code in enumerate(html_arr):
	if index==0:
		continue
	tmp = code.split("\"")
	url_list.append(tmp[0])



# �U�� ===================================================================
download_list = []
'''
# ���o pdf �s���A�m�ߨϥΧt�� index ���g�k
for index, url in enumerate(url_list):
	tmp = url.split(".pdf")
	if len(tmp) > 1:
		download_list.append(tmp[0]+".pdf")
	else:
		continue
'''
# �Ҧ��s�����U��
for url in url_list:
	download_list.append(url)

# =======================================================================


'''
# �ƻs Google Chrome ���|�쥻�a�ؿ�=========================================
cwd = os.getcwd()
user = getpass.getuser()
path = "\"C:\Users\\"+user+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk\" "
os.system("copy "+path+cwd+"\chrome.lnk")
# =======================================================================
'''


# �N�n�b���[�J�l�������}�� web_url �h�����t�� ? ���Ѽ�
web_url_arr = web_url.split("?")
web_url = web_url_arr[0]

# �w��C�@�� download list �U���ɮ�
for index, url in enumerate(download_list):

	part = "�i�סG(" + str(index+1) + "/" + str(len(download_list)) + ")"
	print "\n\n\n\n\n"+ part + "\n" + url

	# �p�G�U�����}�O�t�� http �}�Y��������}
	if len(url.split("http"))>1:
		download_url = url
	else:
		download_url = web_url+"/../"+url

	# �p�G�O https ���L
	tmp = download_url.split("https://")
	if len(tmp)>1:
		continue

	# �N http �p�G����� // �n�令�@�� /
	tmp = download_url.split("http://")
	tmp[1] = tmp[1].replace("//","/")
	download_url = "http://" + tmp[1]
	print download_url
	filename = wget.download(download_url)
'''
	# �z�L google chrome �U��
	# �p�G���a�ؿ������\���o Chrome �s��
	if os.path.isfile("./chrome.lnk"):
		os.system("chrome.lnk "+download_url)
	else:
	# �_�h�N�z�L wget �U��
		filename = wget.download(download_url)

'''

# Reference

# �Ѧ�: http://seanlin.logdown.com/posts/210856-python-idioms-6-enumerate
# �@�� for �]�i�H���o index ����k