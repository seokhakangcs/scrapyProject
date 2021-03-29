import scrapy
import nltk
from nltk.corpus import stopwords

class NewsCrawler(scrapy.Spider):
    name = "news"

    def start_requests(self):

        # urls = response.css("div.recipe-description a::attr(href)").getall()
        # print(stopwords.words('english'))
        urls = ['https://www.usatoday.com/news/',]
        # 'https://www.usatoday.com/story/news/politics/2021/03/06/covid-stimulus-bill-what-changed-between-senate-and-house-versions/4610104001',
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        def getText(classTag):
            classTags = classTag + "::text"
            text = response.css(classTags).getall()
            return text

        def getWords(text):
            splitted_sentence = []
            words = []

            for sentence in text:
                splitted_sentence = sentence.split()
                for word in splitted_sentence:
                    word = word.strip(" ,.\'\"")
                    if(word.isalpha()):
                        words.append(word)
            return words
        def calculateRepetition(words):
            repetition = dict()
            for word in words:
                if(word not in repetition):
                    repetition[word] = 1
                else:
                    repetition[word] += 1
            return repetition

        # urls = response.css(".gnt_m_flm_a ::attr(href)").extract()
        # print("///////////////////////")
        # print(urls, end='\n')

        words = []
        dictionary = dict()
        text = getText('p.gnt_ar_b_p')
        words = getWords(text)
        dictionary = calculateRepetition(words)
        dictionary_list = list(dictionary.items())
        dictionary_list.sort(key=lambda x: x[1], reverse=True)

        # print("\n\n\n")
        # print(dictionary_list)
        # print("\n\n\n")
        # wordCounter = WordCounter()
        next_page_urls = response.css(".gnt_m_flm_a ::attr(href)").extract()
        # print("\n\n\nabcd\n\n\n")
        
        print("///////////////////////")
        print(next_page_urls)
        print("///////////////////////")

        for next_page_url in next_page_urls:
            yield scrapy.Request(response.urljoin(next_page_url))
        print("\n\n\n")
        print(len(next_page_urls))
        print("\n\n\n")


class UrlFetcher():
    def fetch_sub_urls(self, USA_TODAY):
        print()


# class WordCounter(scrapy.Spider):
#     def __init(self, classTag):
#         self.classTag = classTag

#     def getText(self, classTag):
#         classTags = classTag + "::text"
#         text = response.css(classTags).getall()
#         return text