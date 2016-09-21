import scrapy
import json


class QuotesSpider(scrapy.Spider):

    name = "wiki"

    start_urls = [
        'https://en.wikipedia.org/wiki/Glossary_of_architecture',
        'https://en.wikipedia.org/wiki/Glossary_of_dance_moves',
        'https://en.wikipedia.org/wiki/Glossary_of_graffiti',
        'https://en.wikipedia.org/wiki/Glossary_of_glass_art_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_musical_terminology',
        'https://en.wikipedia.org/wiki/Glossary_of_jazz_and_popular_music',
        'https://en.wikipedia.org/wiki/Glossary_of_sculpting',
        'https://en.wikipedia.org/wiki/Glossary_of_basketball_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_poker_terms',
        'https://en.wikipedia.org/wiki/Role-playing_game_terms',
        """

        'https://en.wikipedia.org/wiki/Glossary_of_climbing_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_baseball',
        'https://en.wikipedia.org/wiki/Glossary_of_literary_terms',

        """
    ]

    def parse(self, response):
        result = {}

        rule1 = ''
        rule2 = ''
        rule = ''
        type_of_algo = 0

        c1 = "Culture and the arts"
        c2 = "Arts"

        if "Glossary_of_architecture" in response.url:
            rule1 = '//dfn[@class="glossary"]'
            rule2 = 'dd[@class="glossary"]'
            type_of_algo = 0

        elif "Glossary_of_dance_moves" in response.url:
            rule1 = '//h3/span[@class="mw-headline"]'
            rule2 = 'p'
            type_of_algo = 0

        elif "Glossary_of_graffiti" in response.url or "Glossary_of_basketball_terms" in response.url :
            rule1 = './dt'
            rule2 = './dd'
            rule = '//dl'
            type_of_algo = 1

        elif "Glossary_of_glass_art_terms" in response.url or "Role-playing_game_terms" in response.url:
            rule1 = './b'
            rule2 = '.'
            rule = '//li'
            type_of_algo = 1

        #elif "Glossary_of_musical_terminology" in response.url or "Glossary_of_climbing_terms" in response.url:
        elif "Glossary_of_musical_terminology" in response.url or "Glossary_of_poker_terms" in response.url:
            rule1 = '//dt'
            rule2 = 'dd'
            type_of_algo = 0

        elif "Glossary_of_jazz_and_popular_music" in response.url:
            rule1 = '//dt'
            rule2 = 'dd'
            type_of_algo = 0

        elif "Glossary_of_sculpting" in response.url:
            rule1 = '//h3/span[@class="mw-headline"]'
            rule2 = 'dl'
            type_of_algo = 0

        #elif "Glossary_of_baseball" in response.url:
         #   rule1 = '//h3/span[@class="mw-headline"]'
          #  rule2 = 'dl'
           # type_of_algo = 0

        words = []
        definitions = []

        if type_of_algo == 0:
            for item in response.xpath(rule1 + "[following-sibling::*[1][self::" + rule2 + "]]"):
                tt = (''.join(item.xpath(".//text()").extract()), item.xpath('./a/@href').extract_first())
                #if "Fermata" not in tt[0] and "Hold" not in tt[0] and tt[0] != "Telemark" and tt[0] != "Time Step" and tt[0] != "bozzetto" and tt[0] != "Taille directe":
                words.append(tt)

            for item in response.xpath(rule1 + '/following::' + rule2 + '[1]'):
                definitions.append(''.join(item.xpath(".//text()").extract()))

        elif type_of_algo == 1:
            for item in response.xpath(rule):
                item2 = item.xpath(rule1)
                tt =(''.join(item2.xpath(".//text()").extract()), item2.xpath('./a/@href').extract_first())
                words.append(tt)
                item3 = item.xpath(rule2)
                definitions.append(''.join(item3.xpath(".//text()").extract()))

        words_json_array = []
        for i in range(0, min(len(words), len(definitions))):
            word = {}
            word['name'] = words[i][0]
            word['def'] = definitions[i]
            word['link'] = words[i][1]

            if word['def'] != "" and word['name'] != "":
                words_json_array.append(word)

        result['words'] = words_json_array;
        result['c1'] = c1
        result['c2'] = c2
        result['c3'] = response.url.replace("https://en.wikipedia.org/wiki/","")

        result_json = json.dumps(result, sort_keys=True, indent=4)

        file = open(result['c3'], 'w')
        file.write(result_json)
        file.close()