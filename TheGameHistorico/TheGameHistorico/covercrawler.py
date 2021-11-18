# from requests.compat import urljoin
import urllib.request
import re

def get_cover(strIn):
    query1 = strIn
    query2 = query1.replace(" ", "%20")
    out = []
    with urllib.request.urlopen("https://vgcollect.com/search/" + query2) as response:
        html = response.read()
        seq = re.findall('\[NA\]</a>', str(html))
        # print(seq)
        #    for i in range(len(str(html))):
        f = open(query1 + ".txt", "w")
        f.write(str(seq))
        
        for i in range(0, len(str(html))):
            if("[NA]</a> - Official Release" == str(html)[i : i + len("[NA]</a> - Official Release")]):
                input = str(html)[i : i + 1200]
                # url1 = "https://vgcollect.com/item/"
                url1 = 'https://vgcollect.com/images/front-box-art/'
                url2 = '.jpg'
                
                try:
                    index1 = input.index(url1)
                    index2 = input.index(url2)
                    # f.write(str(input)[index : len(url1)])
                    # f.write("\n\n\n\n")
                    # print(str(input)[index1 : index2 + 4])
                    f.write("\n" + str(input)[index1 : index2 + 4] + "\n\n")
                    out.append(str(input)[index1 : index2 + 4])
                except:
                    continue
        f.close()
    return out
