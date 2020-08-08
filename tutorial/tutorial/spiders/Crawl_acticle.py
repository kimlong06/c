import scrapy
import json
import codecs
class Crawl(scrapy.Spider):
    name = "long"
    sequence_number = 0
    def start_requests(self):
        base_url = ["https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-1-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-2-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-3-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-4-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-5-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-12-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-13-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-14-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-149-0-3-1-0.chn",
        "https://kenh14.vn/timeline/laytinmoitronglist-{}-2-1-1-1-1-152-0-3-1-0.chn",
        ]

        for url in base_url:
            for i in range(2):
                # for j in range(20):
                yield scrapy.Request(url =url.format(i), callback = self.parse_link)


    def parse_link(self, response):
        for i in response.css("h3.knswli-title"):
            link = "https://kenh14.vn"+i.css("a::attr(href)").get()
            yield scrapy.Request(url = link , callback = self.parse)



    def parse(self, response):
        if response.status==200:
            content =""
            for i in response.css("div.knc-content p::text"):
                content += i.get() +"\n"


            List_tags =[]
            for tag in response.css("li.kli"):
                List_tags.append(tag.css("a::text").get())


            article = {
                "STT" : self.sequence_number,
                "Tieude": response.css("h1.kbwc-title::text").get(),
                "Thời gian": response.css("span.kbwcm-time::attr(title)").get(),
                "Tags" :List_tags,
                "Noi dung": content,
                "Tác giả" : response.css("span.kbwcm-author::text").get(),
                "Nguồn": response.css("span.kbwcm-source a::text").get()
            }

            self.sequence_number+=1
            with codecs.open("test8.json" , "a" , encoding= 'utf8') as content_file:
                json.dump(article , content_file ,indent= 4 ,ensure_ascii=False)
# import scrapy
# import json
# import codecs
# class Crawl(scrapy.Spider):
#     name = "long"
#     def start_requests(self):
#         base_url = "https://news.gearvn.com/category/cong-nghe/page/"
#         print("~~~~~~~~START REQUEST IS RUNNING")
#         for i in range(20):
#             yield scrapy.Request(url=base_url+str(i)+"/", callback = self.parse_link)

    
#     def parse_link(self, response):
#         print("~~~~~~~~~~~PARSE LINK IS RUNNING")
#         for i in response.css("h3.entry-title"):
#             link = i.css("a::attr(href)").get()
#             yield scrapy.Request(url = link , callback = self.parse)


#     def parse(self, response):
#         content =""
#         print("~~~~~  PARSE IS RUNNING")
#         for i in response.css("div.td-post-content p::text"):
#             content += i.get() +"\n"

#         article = {
#             "Tieude": response.css("h1.entry-title::text").get(),
#             "Noi dung": content,
#         }
#         with codecs.open("test.json" , "a" , encoding= 'utf8') as content_file:
#             json.dump(article , content_file ,indent= 4 ,ensure_ascii=False)