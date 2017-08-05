# -*- coding: utf-8 -*-

import urllib.request

#urlと保存パスを指定
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#ダウンロード
mem = urllib.request.urlopen(url).read()
#バイナリの文字コードで確認できる
print(mem)
with open(savename,mode='wb') as f:
  f.write(mem)
  print("保存しました") 