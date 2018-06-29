
# coding: utf-8

# In[2]:


import requests  
import json
import urllib.request

def tk(a):
    TKK = (lambda a=561666268, b=1526272306:str(406398) + '.' + str(a + b))()
    
    def b(a, b):
        for d in range(0, len(b)-2, 3):
            c = b[d + 2]
            c = ord(c[0]) - 87 if 'a' <= c else int(c)
            c = a >> c if '+' == b[d + 1] else a << c
            a = a + c & 4294967295 if '+' == b[d] else a ^ c
        return a
    
    e = TKK.split('.')
    h = int(e[0]) or 0
    g = []
    d = 0
    f = 0
    while f < len(a):
        c = ord(a[f])
        if 128 > c:        
            g.insert(d,c)
            d += 1
        else:
            if 2048 > c:
                g[d] = c >> 6 | 192
                d += 1
            else:
                if (55296 == (c & 64512)) and (f + 1 < len(a)) and (56320 == (ord(a[f+1]) & 64512)):
                    f += 1
                    c = 65536 + ((c & 1023) << 10) + (ord(a[f]) & 1023)
                    g[d] = c >> 18 | 240
                    d += 1
                    g[d] = c >> 12 & 63 | 128
                    d += 1
                else:
                    g[d] = c >> 12 | 224
                    d += 1
                    g[d] = c >> 6 & 63 | 128
                    d += 1
                g[d] = c & 63 | 128
                d += 1
        f += 1
    a = h
    for d in range(len(g)):
        a += g[d]
        a = b(a, '+-a^+6')
    a = b(a, '+-3^+b+-f')
    a ^= int(e[1]) or 0
    if 0 > a:a = (a & 2147483647) + 2147483648
    a %= 1E6
    return str(int(a)) + '.' + str(int(a) ^ h)

def main():
    content = input('your word：')
    if content == '':
        return
    else:
        content_tk = tk(content+' ')  
        content_url_template ='https://translate.google.com.tw/translate_tts?ie=UTF-8&q={q}&tl=en&total=1&idx=0&textlen={tlen}&tk={tk}&client=t&prev=input'
        content_url = content_url_template.format(tk='{}'.format(content_tk),q='{}'.format(content+' '),tlen='{}'.format(len(content)))  # 根据待翻译content和tk值拼凑URL
        doc = requests.get(content_url)
        with open(content+'.mp3', 'wb') as f:
            f.write(doc.content)

if __name__ == '__main__':
    print(main())

