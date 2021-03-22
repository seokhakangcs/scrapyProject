import scrapy


class QuotesSpider(scrapy.Spider):
    name = "NewsSpider"

    def start_requests(self):
        urls = ['https://www.usatoday.com/story/news/politics/2021/03/06/covid-stimulus-bill-what-changed-between-senate-and-house-versions/4610104001',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        def getAllClassText(classTag):
            classTags = classTag + "::text"
            main_text = response.css(classTags).getall()
            # print(main_text)
            return main_text

        def changeTextToList(main_text):
            sentence = []
            words = []
            for i in range(len(main_text)):
                sentence = main_text[i].split()
                for j in range(len(sentence)):
                    sentence[j] = sentence[j].strip(" ,.\'\"")
                    if(sentence[j].isalpha()):
                        words.append(sentence[j])
            # for index in range(len(words)):
            #     words[index] = words[index].strip(" ,.\'\"")
            return words

        words = []
        # main_text = getAllClassText('p.gnt_ar_b_p')
        # main_text = response.css('p.gnt_ar_b_p::text').getall()
        main_text = getAllClassText('p.gnt_ar_b_p')
        words = changeTextToList(main_text)

        print("\n\n\n")
        print(words)
        print("\n\n\n")
