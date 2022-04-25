import scrapy
import html as h
import re 
import pandas as pd
num=0

def remove_tag(content):
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)

    return cleantext

invalid_page_url=False
class WelloSpider(scrapy.Spider):
    playlist_url_list = open("url_list.txt", 'w', encoding="utf-8")
    music_list=open("music_list.txt", 'w', encoding="utf-8")
    name = "crawler"
    
    def start_requests(self): 
        allowed_domains = ['https://music.bugs.co.kr']
        theme_ids=[429, 5615, 8010 ,4184 ,5499, 4172, 9895, 4182, 15239, 18797, 2049 ,6128 ,5432 ,1036, 1377, 223 ,5561 ,8015 ,14275 ,5707 ,1505 ,5788, 492, 781, 930, 386, 5494 ,2188, 5895 ,33123, 21648, 254, 1648 ,1825, 5727, 5735, 6606,29921, 11026, 20593, 296 ,28176, 540, 4178, 5786, 8919, 13384 ,9694, 2796 ,21754 ,22677, 615 ,28177 ,13723, 632, 978, 3090 ,9523, 783, 12686, 31150 ,5729, 5963, 6142 ,240 ,10849, 10504 ,13617, 4093, 5712 ,6161 ,6174, 6889, 1440, 14684, 19752 ,4796]
        theme_names=['신나는','발라드한','그루브한','감성적인','어쿠스틱한','일렉트로닉','달달한','몽환적인','강한','잔잔한','올디스','애절한','감각적인','섹시한','쓸쓸한','소울풀한','청량한','듀엣/피처링','목소리/음색','걸그룹','아이돌','공연/라이브','봄','여름','가을','겨울','아침','오후','저녁','밤/새벽','화창한 날','비/흐림','크리스마스','환절기','눈오는 날','비온후/맑게갠','미세먼지/황사','선선한','쌀쌀한 날','폭염/더위','드라이브','운동/헬스','등교/출근길','하교/퇴근길','휴식/명상','클럽/파티','카페','노래방','산책/여행','독서','방안에서','사무실','편집숍/매장','호텔/바','잠들기 전','결혼','페스티벌','패션쇼','혼술혼밥','에스테틱','공부할 때','사랑/기쁨','이별/슬픔','스트레스/짜증','우울할때','지치고 힘들때','멘붕/불안','그리움','외로울때','썸 탈때','고백','울고 싶을때','새벽감성','싱숭생숭','설렘/심쿵','기분전환','힐링']

        for i in range(len(theme_ids)):
            for page_id in range(1):
                url=f"https://music.bugs.co.kr/musicpd?order=list&tag_id={theme_ids[i]}&page={page_id+1}"
                yield scrapy.Request(url=url, callback=self.get_playlist, meta={'theme':theme_names[i]})

        
        
    def get_playlist(self, response):
        theme = response.meta['theme']
        for i in range(len(response.css("figcaption.info > a"))):
            if i>10:
                break
            if i%2==0:
                url=response.css("figcaption.info > a")[i].get().split('"')[1]
                self.playlist_url_list.write(url + '\n')
                yield scrapy.Request(url=url, callback=self.get_music,meta={'theme':theme, 'url':url})

    def get_music(self, response):
        theme = response.meta['theme']
        url=response.meta['url']
        for i in range(len(response.css('table.list  > tbody > tr'))):
            playlist_id=url.split('/')[5].split('?')[0]
            title=response.css(f'#ESALBUM{playlist_id} > table > tbody > tr:nth-child({i+1}) > th > p > a').get().split(">")[1].split("<")[0].replace(",", " ")
            artist=response.css(f'#ESALBUM{playlist_id} > table > tbody > tr:nth-child({i+1}) > td:nth-child(7) > p > a').get().split(">")[1].split("<")[0].replace(",", " ")
            album=response.css(f'#ESALBUM{playlist_id} > table > tbody > tr:nth-child({i+1}) > td:nth-child(8) > a').get().split(">")[1].split("<")[0].replace(",", " ")
            
            lyric_url=response.css(f'#ESALBUM{playlist_id} > table > tbody > tr:nth-child({i+1}) > td:nth-child(5) > a').get().split('"')[1]
            yield scrapy.Request(url=lyric_url, callback=self.get_lyric, meta={'theme':theme, 'title':title, 'artist':artist, 'album':album})

    def get_lyric(self, response):
        global num
        theme = response.meta['theme']
        title = response.meta['title']
        artist = response.meta['artist']
        album = response.meta['album']

        lyric=remove_tag(response.css("#container > section.sectionPadding.contents.lyrics > div > div > xmp").get()).replace(",", " ").replace(chr(13), "").replace("\n", ".")
        

        
        with open("music_list.csv", 'a' ,encoding="cp949") as f:
            f.write((str(theme)+","+title+","+artist+","+album+","+lyric+"\n"))
            print(num)
            num+=1
        
            
        