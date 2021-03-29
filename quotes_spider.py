import scrapy
import nltk
from nltk.corpus import stopwords

class NewsCrawler(scrapy.Spider):
    name = "news"

    def start_requests(self):
        url = 'https://www.usatoday.com/news/'
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
        
        def getURLs(CSS):
            str = CSS + " ::attr(href)"
            return response.css(str).extract()

        def sortList(dictionary):
            dictionary_list = list(dictionary.items())
            dictionary_list.sort(key=lambda x: x[1], reverse=True)
            return dictionary_list

        words = []
        dictionary = dict()
        text = getText('p.gnt_ar_b_p')
        words = getWords(text)
        dictionary = calculateRepetition(words)
        sorted_dictionary = sortList(dictionary)
        next_page_urls = getURLs(".gnt_m_flm_a")
        
        print(sorted_dictionary)

        for next_page_url in next_page_urls:
            yield scrapy.Request(response.urljoin(next_page_url))