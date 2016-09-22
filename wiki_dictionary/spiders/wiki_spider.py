# -*- coding: utf-8 -*-

import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "wiki"

    start_urls = [

    ]

    """
        'https://en.wikipedia.org/wiki/Glossary_of_botanical_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_tensor_theory',
        'https://en.wikipedia.org/wiki/Glossary_of_plant_morphology',
        'https://en.wikipedia.org/wiki/Glossary_of_biology',
        'https://en.wikipedia.org/wiki/Glossary_of_ichthyology',
        'https://en.wikipedia.org/wiki/Glossary_of_entomology_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_ecology',
        'https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations',
        'https://en.wikipedia.org/wiki/List_of_legal_abbreviations',
        'https://en.wikipedia.org/wiki/Glossary_of_firelighting',
        'https://en.wikipedia.org/wiki/Glossary_of_invasion_biology_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_gene_expression_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_astronomy',
        'https://en.wikipedia.org/wiki/Glossary_of_classical_physics',
        'https://en.wikipedia.org/wiki/Glossary_of_elementary_quantum_mechanics',
        'https://en.wikipedia.org/wiki/Glossary_of_physics',
        'https://en.wikipedia.org/wiki/Glossary_of_climate_change',
        'https://en.wikipedia.org/wiki/Glossary_of_geology',
        'https://en.wikipedia.org/wiki/Outline_of_metalworking',
        'https://en.wikipedia.org/wiki/Heideggerian_terminology',
        'https://en.wikipedia.org/wiki/Severe_weather_terminology_(United_States)',
        'https://en.wikipedia.org/wiki/Glossary_of_wildfire_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_chemistry_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_philosophy',
        'https://en.wikipedia.org/wiki/Glossary_of_education_terms_(A%E2%80%93C)',
        'https://en.wikipedia.org/wiki/Index_of_object-oriented_programming_articles',
        'https://en.wikipedia.org/wiki/Category:Computing_terminology',
        'https://en.wikipedia.org/wiki/Glossary_of_computer_hardware_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_Unified_Modeling_Language_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_machine_vision',
        'https://en.wikipedia.org/wiki/Glossary_of_mill_machinery',
        'https://en.wikipedia.org/wiki/Glossary_of_Buddhism',
        'https://en.wikipedia.org/wiki/Glossary_of_ancient_Roman_religion',
        'https://en.wikipedia.org/wiki/Glossary_of_Christianity',
        'https://en.wikipedia.org/wiki/Glossary_of_HVAC_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_Hinduism_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_Islam',
        'https://en.wikipedia.org/wiki/Glossary_of_spirituality_terms',
        'https://en.wikipedia.org/wiki/List_of_Latin_legal_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_engineering',
        'https://en.wikipedia.org/wiki/Glossary_of_aerospace_engineering',
        'https://en.wiktionary.org/wiki/Appendix:Glossary_of_legal_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_broadcasting_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_fuel_cell_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_firefighting',
        'https://en.wikipedia.org/wiki/Glossary_of_firefighting_equipment',
        'https://en.wikipedia.org/wiki/Glossary_of_Internet-related_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_textile_manufacturing',
        'https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence',
        'https://en.wikipedia.org/wiki/Glossary_of_fishery_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_woodworking',
        'https://en.wikipedia.org/wiki/Glossary_of_blogging',
        'https://en.wikipedia.org/wiki/Glossary_of_automotive_design',
        'https://en.wiktionary.org/wiki/Appendix:Glossary_of_aviation,_aerospace,_and_aeronautics',
        'https://en.wikipedia.org/wiki/Glossary_of_nautical_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_rail_transport_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_United_Kingdom_railway_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_North_American_railway_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_New_Zealand_railway_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_road_transport_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_the_American_trucking_industry',
        'https://en.wikipedia.org/wiki/Architectural_glossary',
        'https://en.wikipedia.org/wiki/Glossary_of_dance_moves',
        'https://en.wikipedia.org/wiki/Glossary_of_glass_art_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_graffiti',
        'https://en.wikipedia.org/wiki/Glossary_of_literary_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_musical_terminology',
        'https://en.wikipedia.org/wiki/Glossary_of_jazz_and_popular_music',
        'https://en.wikipedia.org/wiki/Glossary_of_sculpting',
        'https://en.wikipedia.org/wiki/Glossary_of_chess',
        'https://en.wikipedia.org/wiki/Glossary_of_contract_bridge_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_poker_terms',
        'https://en.wikipedia.org/wiki/Role-playing_game_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_American_football',
        'https://en.wikipedia.org/wiki/Glossary_of_association_football_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_baseball',
        'https://en.wikipedia.org/wiki/Glossary_of_basketball_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_climbing_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_cricket_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_cue_sports_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_curling',
        'https://en.wikipedia.org/wiki/Glossary_of_cycling',
        'https://en.wikipedia.org/wiki/Glossary_of_darts',
        'https://en.wikipedia.org/wiki/Glossary_of_equestrian_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_fencing',
        'https://en.wikipedia.org/wiki/Glossary_of_figure_skating_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_golf',
        'https://en.wikipedia.org/wiki/Glossary_of_ice_hockey_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_rowing_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_rugby_league_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_underwater_diving_terminology',
        'https://en.wikipedia.org/wiki/Glossary_of_table_tennis',
        'https://en.wikipedia.org/wiki/Glossary_of_tennis_terms',
        'https://en.wikipedia.org/wiki/Volleyball_jargon',
        'https://en.wikipedia.org/wiki/Glossary_of_water_polo',
        'https://en.wikipedia.org/wiki/Glossary_of_professional_wrestling_terms',
        'https://en.wikipedia.org/wiki/Glossary_of_magic_(illusion)',
        'https://en.wikipedia.org/wiki/Glossary_of_medical_terms_related_to_communications_disorders',
        'https://en.wikipedia.org/wiki/Glossary_of_diabetes',
        'https://en.wikipedia.org/wiki/List_of_medical_roots,_suffixes_and_prefixes',
        'https://en.wikipedia.org/wiki/List_of_medical_abbreviations',
        'https://en.wikipedia.org/wiki/Glossary_of_psychiatry',
        'https://en.wikipedia.org/wiki/Glossary_of_clinical_research',
        'https://en.wikipedia.org/wiki/Index_of_articles_related_to_motion_pictures',
        'https://en.wikipedia.org/wiki/Glossary_of_military_abbreviations',
        'https://en.wikipedia.org/wiki/Glossary_of_nautical_terms',
        'https://en.wikipedia.org/wiki/List_of_terms_relating_to_algorithms_and_data_structures',
        'https://en.wikipedia.org/wiki/Glossary_of_areas_of_mathematics',
        'https://en.wikipedia.org/wiki/Glossary_of_arithmetic_and_diophantine_geometry',
        'https://en.wikipedia.org/wiki/Glossary_of_category_theory',
        'https://en.wikipedia.org/wiki/Glossary_of_cryptographic_keys',
        'https://en.wikipedia.org/wiki/Glossary_of_differential_geometry_and_topology',
        'https://en.wikipedia.org/wiki/Glossary_of_topology',
        'https://en.wikipedia.org/wiki/Glossary_of_field_theory',
        'https://en.wikipedia.org/wiki/Glossary_of_game_theory',
        'https://en.wikipedia.org/wiki/Glossary_of_graph_theory',
        'https://en.wikipedia.org/wiki/List_of_mathematical_jargon',
        'https://en.wikipedia.org/wiki/List_of_linear_algebra_topics',
        'https://en.wikipedia.org/wiki/Glossary_of_order_theory',
        'https://en.wikipedia.org/wiki/Glossary_of_probability_and_statistics',
        'https://en.wikipedia.org/wiki/Glossary_of_ring_theory',
        'https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry',
        'https://en.wikipedia.org/wiki/Glossary_of_Riemannian_and_metric_geometry',
        'https://en.wikipedia.org/wiki/Glossary_of_semisimple_groups',
        'https://en.wikipedia.org/wiki/Glossary_of_shapes_with_metaphorical_names',
    """

    def is_in(self, url, list_all):
        for i in list_all:
            if i in url:
                return True
        return False

    def parse(self, response):
        result = {}

        rule_name_main = ''
        rule_name_sub = ''

        rule_def_main = ''
        rule_def_sub = ''

        rule_word = ''

        type_of_algo = 0

        c1 = "Culture and the arts"
        c2 = "Arts"

        ff = 0
        ggg = 0

        if self.is_in(response.url, [
            "Architectural_glossary",
            "Glossary_of_chess",
            "Glossary_of_American_football",
            "Glossary_of_cricket_terms",
            "Glossary_of_cue_sports_terms",
            "Glossary_of_fencing",
            "Glossary_of_underwater_diving_terminology",
            "Glossary_of_rugby_league_terms",
            "Glossary_of_medical_terms_related_to_communications_disorders",
            "Glossary_of_nautical_terms",
            "Glossary_of_Internet-related_terms",
            "Glossary_of_firefighting_equipment",
            "Glossary_of_HVAC_terms",
            "Glossary_of_broadcasting_terms",
            "Glossary_of_philosophy",
            "Glossary_of_wildfire_terms",
            "Glossary_of_entomology_terms",
            "Glossary_of_botanical_terms",

        ]):

            rule_name_main = '//dt[@class="glossary"]'
            rule_name_sub = './dfn[@class="glossary"]'

            rule_def_main = 'dd'
            rule_def_sub = '.'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Glossary_of_dance_moves",
            "Heideggerian_terminology",

        ]):
            if "Heideggerian_terminology" in response.url:
                ggg = 1

            rule_name_main = '//h3'
            rule_name_sub = './span[@class="mw-headline"]'

            rule_def_main = 'p'
            rule_def_sub = '.'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Glossary_of_ancient_Roman_religion",

        ]):
            rule_name_main = '//h4'
            rule_name_sub = './span[@class="mw-headline"]'

            rule_def_main = 'p'
            rule_def_sub = '.'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Glossary_of_graffiti",
            "Glossary_of_basketball_terms",
            "Glossary_of_contract_bridge_terms",
            "Glossary_of_cycling",
            "Glossary_of_darts",
            "Glossary_of_equestrian_terms",
            "Glossary_of_figure_skating_terms",
        ]):
            rule_name_main = './dt'
            rule_name_sub = '.'

            rule_def_main = './dd'
            rule_def_sub = '.'

            rule_word = '//dl'
            type_of_algo = 1

        elif self.is_in(response.url, [
            "Glossary_of_glass_art_terms",
            "Role-playing_game_terms",
            "Glossary_of_association_football_terms",
            "Glossary_of_magic_(illusion)",
            "Volleyball_jargon",
            "Glossary_of_tennis_terms",
            "Glossary_of_table_tennis",
            "Glossary_of_machine_vision",
            "Glossary_of_Unified_Modeling_Language_terms",
            "Glossary_of_artificial_intelligence",
            "Glossary_of_woodworking",
            "Glossary_of_fishery_terms",
            "Glossary_of_firefighting",
            "Glossary_of_engineering",
            "Glossary_of_spirituality_terms",
            "Glossary_of_Hinduism_terms",
            "Glossary_of_Christianity",
            "Glossary_of_education_terms_",
            "Glossary_of_chemistry_terms",
            "Severe_weather_terminology_(United_States)",
            "Glossary_of_geology",
            "Glossary_of_climate_change",
            "Glossary_of_physics",
            "Glossary_of_classical_physics",
            "Glossary_of_astronomy",
            "Glossary_of_gene_expression_terms",
            "Glossary_of_ecology",
            "Glossary_of_biology",

        ]):
            rule_name_main = './b[1]'
            rule_name_sub = '.'

            rule_def_main = '.'
            rule_def_sub = '.'

            rule_word = '//li'
            type_of_algo = 1

        elif self.is_in(response.url, [
            "Glossary_of_musical_terminology",
            "Glossary_of_poker_terms",
            "Glossary_of_climbing_terms",
            "Glossary_of_jazz_and_popular_music",
            "Glossary_of_curling",
            "Glossary_of_golf",
            "Glossary_of_water_polo",
            "Glossary_of_rowing_terms",
            "Glossary_of_ice_hockey_terms",
            "Glossary_of_the_American_trucking_industry",
            "Glossary_of_road_transport_terms",
            "Glossary_of_New_Zealand_railway_terms",
            "Glossary_of_North_American_railway_terms",
            "Glossary_of_United_Kingdom_railway_terms",
            "Glossary_of_rail_transport_terms",
            "Glossary_of_automotive_design",
            "Glossary_of_blogging",
            "Glossary_of_computer_hardware_terms",
            "Glossary_of_textile_manufacturing",
            "Appendix:Glossary_of_legal_terms",
            "Glossary_of_Islam",
            "Glossary_of_elementary_quantum_mechanics",
            "Glossary_of_invasion_biology_terms",
        ]):
            rule_name_main = '//dt'
            rule_name_sub = '.'

            rule_def_main = 'dd'
            rule_def_sub = '.'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Glossary_of_sculpting",
            "Glossary_of_baseball",
            "Glossary_of_fuel_cell_terms",
        ]):
            rule_name_main = '//h3'
            rule_name_sub = './span[@class="mw-headline"]'

            rule_def_main = 'dl'
            rule_def_sub = '.'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Glossary_of_literary_terms",
            "Glossary_of_aviation",
        ]):
            rule_name_main = './child::td[1]'
            rule_name_sub = '.'

            rule_def_main = './child::td[2]'
            rule_def_sub = '.'

            rule_word = '//tr'
            type_of_algo = 1

        elif self.is_in(response.url, [
            "List_of_Latin_legal_terms",
        ]):
            rule_name_main = './child::td[1]'
            rule_name_sub = '.'

            rule_def_main = './child::td[3]'
            rule_def_sub = '.'

            rule_word = '//tr'
            type_of_algo = 1

        elif self.is_in(response.url, [
            "Glossary_of_professional_wrestling_terms",
        ]):
            rule_name_main = '//dl'
            rule_name_sub = './dt[@class="glossary"]/dfn[@class="glossary"]'

            rule_def_main = 'dl'
            rule_def_sub = './dd'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Glossary_of_mill_machinery",
            "Glossary_of_tensor_theory",
        ]):
            rule_name_main = '//dl'
            rule_name_sub = './dt'

            rule_def_main = 'p'
            rule_def_sub = '.'

            type_of_algo = 0

        elif self.is_in(response.url, [
            "Outline_of_metalworking",
            "Index_of_object-oriented_programming_articles",
            "Category:Computing_terminology",
        ]):
            ff = 1

            rule_word = '//div[@class="mw-content-ltr"][1]//li'

            rule_name_main = '.'
            rule_name_sub = '.'

            rule_def_main = '.'
            rule_def_sub = '.'

            type_of_algo = 1

        elif self.is_in(response.url, [

            "Glossary_of_firelighting",
            "Glossary_of_aerospace_engineering",
            "List_of_legal_abbreviations",
            "List_of_computing_and_IT_abbreviations",
            "Glossary_of_ichthyology",
            "Glossary_of_plant_morphology",

        ]):

            if "Glossary_of_firelighting" in response.url:
                rule_def_main = u"–"
                rule_def_sub = u"–"
            elif "Glossary_of_aerospace_engineering" in response.url:
                rule_def_main = u" —"
                rule_def_sub = u"—"
            elif "List_of_legal_abbreviations" in response.url:
                rule_def_main = u" — "
                rule_def_sub = u" - "
            elif "List_of_computing_and_IT_abbreviations" in response.url:
                rule_def_main = u"—"
                rule_def_sub = u"—"
            elif "Glossary_of_ichthyology" in response.url:
                rule_def_main = u": "
                rule_def_sub = u": "
            elif "Glossary_of_plant_morphology" in response.url:
                rule_def_main = u"–"
                rule_def_sub = u"–"

            rule_word = '//div[@class="mw-content-ltr"][1]//li'

            rule_name_main = '.'
            rule_name_sub = '.'

            type_of_algo = 2

        elif self.is_in(response.url, [
            "Glossary_of_Buddhism",
        ]):
            rule_name_main = './child::td[1]'
            rule_name_sub = './b'

            rule_def_main = 'child::td[1]'
            rule_def_sub = '.'

            rule_word = '//tr'
            type_of_algo = 1
        else:
            print '\033[91m' + response.url + '\033[0m'
            return

        words = []
        definitions = []

        if type_of_algo == 0:
            ruling = rule_name_main + "[following-sibling::*[1][self::" + rule_def_main + "]]"
            if ggg == 1:
                ruling = rule_name_main + "[following-sibling::" + rule_def_main + "]"

            for item in response.xpath(ruling):
                item2 = item.xpath(rule_name_sub)
                tt = (''.join(item2.xpath(".//text()").extract()), item2.xpath('./a/@href').extract_first())
                words.append(tt)

            for item in response.xpath(ruling + '/following::' + rule_def_main + '[1]'):
                item2 = item.xpath(rule_def_sub)
                definitions.append(''.join(item2.xpath(".//text()").extract()))

        elif type_of_algo == 1:
            for item in response.xpath(rule_word):
                item2 = item.xpath(rule_name_main)
                item2 = item2.xpath(rule_name_sub)
                tt = (''.join(item2.xpath(".//text()").extract()), item2.xpath('./a/@href').extract_first())
                item2 = item.xpath(rule_def_main)
                item2 = item2.xpath(rule_def_sub)
                tt2 = ''.join(item2.xpath(".//text()").extract())
                if (tt[0] != tt2 or (len(tt[0]) > 3 and ff == 1)) and tt[0] != "Creative Commons Attribution-ShareAlike License":
                    if tt not in words:
                        words.append(tt)
                        definitions.append(tt2)

        elif type_of_algo == 2:
            for item in response.xpath(rule_word):
                item2 = item.xpath(rule_name_main)
                item2 = item2.xpath(rule_name_sub)

                tttttt = []
                if len(''.join(item2.xpath("(.//text())").extract()).split(rule_def_main)) != 1:
                    tttttt = ''.join(item2.xpath("(.//text())").extract()).split(rule_def_main)
                elif len(''.join(item2.xpath("(.//text())").extract()).split(rule_def_sub)) != 1:
                    tttttt = ''.join(item2.xpath("(.//text())").extract()).split(rule_def_sub)

                try:
                    tt = (tttttt[0], item2.xpath('./node()[1][name()="a"]/@href').extract_first())
                except:
                    tt = ("" ,"")

                tt2 =''
                if len(tttttt) == 2:
                    tt2 = tttttt[1]
                elif len(tttttt) == 1:
                    tt2 = tttttt[0]
                else:
                    tt = ("","")
                    tt2 = ""

                if (tt[0] != tt2 or (len(tt[0]) > 3 and ff == 1)) and "Williams, Gerald W. (Summer 2000)" not in tt[0]:
                    if tt not in words:
                        words.append(tt)
                        definitions.append(tt2)

        words_json_array = []
        for i in range(0, min(len(words), len(definitions))):
            word = {}
            word['name'] = words[i][0]
            word['def'] = definitions[i]
            word['link'] = words[i][1]
            if word['name'] != "" and ((word['link'] is not None and word['link'] != "") or word['def'] != ""):
                words_json_array.append(word)

        result['words'] = words_json_array
        result['c1'] = c1
        result['c2'] = c2
        result['c3'] = response.url.replace("https://en.wikipedia.org/wiki/", "")

        result_json = json.dumps(result, sort_keys=True, indent=4)

        file_name = result['c3']
        if "Glossary_of_aviation" in file_name:
            file_name = "Glossary_of_aviation"

        if "Glossary_of_legal_terms" in file_name:
            file_name = "Glossary_of_legal_terms"

        if "Computing_terminology" in file_name:
            file_name = "Computing_terminology"

        file = open(file_name + ".json", 'w')
        file.write(result_json)
        file.close()
