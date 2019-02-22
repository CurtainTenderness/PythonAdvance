import re
import requests

# 从网页上下载
# def getinfo():
#     response=requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
#     content=response.text
#     result=re.findall(
#         '<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td><td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a>',
#         content)
#     return result


# 从文本中读出
def getinfo():
    with open("content.html","r",encoding="utf-8") as f:
        conser=f.read()
        # print(conser)
    result=re.findall(
        '<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td>'
        '<td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a>',
        conser)
    return result
# print(getinfo())
def writefile():
    with open("result.txt","w",encoding="utf-8") as f:
        for r in getinfo():
            f.write(r[0]+"\t"+r[1])
            f.write("\n")


if __name__=="__main__":
    writefile()

