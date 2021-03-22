import scrapy


class QuotesSpider(scrapy.Spider):
    name = "NewsSpider"

    def start_requests(self):
        urls = ['https://www.usatoday.com/story/news/politics/2021/03/06/covid-stimulus-bill-what-changed-between-senate-and-house-versions/4610104001',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        def getCSSText(classTag):
            classTags = classTag + "::text"
            main_text = response.css(classTags).getall()
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
            return words

        def calculateRepetition(words):
            repetition = dict()
            for word in words:
                if(word not in repetition):
                    repetition[word] = 1
                else:
                    repetition[word] += 1
            return repetition

        words = []
        dictionary = dict()
        main_text = getCSSText('p.gnt_ar_b_p')
        words = changeTextToList(main_text)
        dictionary = calculateRepetition(words)
        dictionary_list = list(dictionary.items())
        dictionary_list.sort(key=lambda x: x[1], reverse=True)

        print("\n\n\n")
        print(dictionary_list)
        print("\n\n\n")
