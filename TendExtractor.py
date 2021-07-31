#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request   #urlopen
from lxml import etree  #xpath
from apscheduler.schedulers.background import BackgroundScheduler

def get_trends():
    yuanma=urllib.request.urlopen("https://trends24.in/japan/")
    html=yuanma.read()
    selector = etree.HTML(html)
     
    #Extract the application information of the four apps
    content = selector.xpath('//*[@id="trend-list"]/div/ol/li/a/text()')
    content.extend(["フォロー",
                    "行く",
                    "秋葉原",
                    "あきば",
                    "あ",
                    "い",
                    "え",
                    "う",
                    "お",
                    "ゲーム",
                    "#アメブロ",
                    "#Tokyo2020",
                    "コロナウイルス",
                    "サッカー",
                    "竹中平蔵会長", 
                    "ビキニ"])
    
    file = open("words_list.txt", "w")
    file.write('\n'.join(content))
    file.close()
    print("Function called!")
    
    
sched = BackgroundScheduler()
sched.add_job(get_trends,'interval',hours=8)
sched.start()
