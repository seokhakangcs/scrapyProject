import scrapy


class QuotesSpider(scrapy.Spider):
    name = "NewsSpider"

    def start_requests(self):
        urls = ['https://www.usatoday.com/story/news/politics/2021/03/06/covid-stimulus-bill-what-changed-between-senate-and-house-versions/4610104001',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        main_text = response.css('p.gnt_ar_b_p::text').getall()
        print('main text: ', main_text)
        filename = 'result.html'
        print('type: ', type(main_text))
        outfile = open("result.txt", "w")
        
        #result2 = read_result.writelines("result2.txt", "w")

        for main_texts in main_text:
            outfile.write(main_texts + "\n")

        outfile.close()

        print('\n''\n''\n''\n')
        read_result = open("result.txt", "r")
        #print(read_result.readlines())
        words = []
        for line in read_result.readlines():
            #print(line, '\n')
            splitted_line = line.split()
            print('splitted line: ', splitted_line, '\n')
            for i in range(len(splitted_line)):
                words.append(splitted_line[i])
        print(words)
        read_result.close()
        #yield main_text

# import scrapy

# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'

#     def start_request(self):
#         start_urls = ['https://www.usatoday.com/story/news/politics/2021/03/06/covid-stimulus-bill-what-changed-between-senate-and-house-versions/4610104001/']
#         yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         main_text = response.css('p.gnt_ar_b_p')
#         print('main text', main)