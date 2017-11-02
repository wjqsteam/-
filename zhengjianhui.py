# coding = utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


Urllist = []
Pagelist = []
neimu = 0
xinxi = 0
weigui = 0
zhengquan = 0
caozong = 0
jijin = 0
touzi = 0
duanxian = 0
def gettags(Url):
    global neimu
    global xinxi
    global weigui
    global zhengquan
    global caozong
    global jijin
    global touzi
    global duanxian
    html = urlopen("http://www.csrc.gov.cn/pub/zjhpublic/"+Url)
    bsObj = BeautifulSoup(html, 'html.parser')
    text = bsObj.find("div",{"class":"contentss"},{"id":"ContentRegion"})
    texted = text.get_text()
    if re.search("内幕交易",texted) != None :
        neimu = neimu + 1
    if re.search("信息披露违法",texted) != None :
        xinxi = xinxi + 1
    if re.search("违规买卖股票",texted) != None :
        weigui = weigui + 1
    if re.search("挪用资金",texted) != None :
        zhengquan = zhengquan + 1
    if re.search("操纵市场",texted) != None :
        caozong = caozong + 1
    if re.search("\"老鼠仓\"",texted) != None :
        jijin = jijin + 1
    if re.search("欺诈客户",texted) != None :
        touzi = touzi + 1
    if re.search("短线交易",texted) != None :
        duanxian = duanxian + 1

def getUrls(StartingSite):
    global Urllist
    html = urlopen(StartingSite)
    bsObj = BeautifulSoup(html,'html.parser')
    urls = bsObj.findAll("a", href = re.compile("(\.\.\/\.\.\/)+"))
    for i in urls:
        Urllist.append(i['href'].strip('../../'))


#getpages("http://www.csrc.gov.cn/pub/zjhpublic/G00306212/201710/t20171010_325107.htm")
#getUrls("http://www.csrc.gov.cn/pub/zjhpublic/3300/3313/index_7401.htm")
count = 0
Pagelist.append("http://www.csrc.gov.cn/pub/zjhpublic/3300/3313/index_7401.htm")
try:
    for s in range(1,52):
        page = "http://www.csrc.gov.cn/pub/zjhpublic/3300/3313/index_7401_%s.htm" %s
        Pagelist.append(page)
    for i in Pagelist:
        getUrls(i)
    for url in Urllist:
        count = count + 1
        gettags(url)
        print(count)
except:
    print("error")
print(neimu)
print(xinxi)
print(weigui)
print(zhengquan)
print(caozong)
print(jijin)
print(touzi)
print(duanxian)