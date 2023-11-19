
import scrapy
import re

from crawler_lyrics.items import CrawlerLyricsItem


class CifrasClubSpider(scrapy.Spider):
    name = 'cifras_club'
    allowed_domains = ['cifraclub.com.br']
    start_urls = ['https://www.cifraclub.com.br/catolicas/']

    def parse(self, response):
        song_list  = response.css('ul#js-a-songs li')

        for song in song_list :
            song_link = song.css('a.art_music-link::attr(href)').get()
            yield response.follow(song_link, self.parse_lyrics)

    def parse_lyrics(self, response):
        titulo = response.css('h1.t1::text').get()
        compositor = response.css('div.cifra-footer a::text').get().replace('Composição de ', '')
        link = response.url
        cifras = self.trataCifras(response.css('pre').get())
        lyrics = self.trataLyrics(response.css('pre').get())

        item = CrawlerLyricsItem(title=titulo, lyric=lyrics, author=compositor, cifra=cifras, link_ref=link)
        yield item
    
    def trataCifras(self, rawHtml):
        return self.remove_specific_tag(rawHtml, '<pre>')
    
    def trataLyrics(self, rawHtml):
        leters = self.remove_all_between_tag(rawHtml, 'b')
        leters = self.remove_all_tags(leters)
        return leters

    def remove_all_between_tag(self, raw_html, tag):
        regex = re.compile(rf'<{tag}[^>]*>(.+?)</{tag}>', re.DOTALL)
        if raw_html is not None:
            return re.sub(regex, '', raw_html)
        else:
            return raw_html
    
    def remove_specific_tag(self, rawHtml, tag):
        if rawHtml is not None and tag is not None:
            regex = re.compile(rf'<{tag}[^>]*>|<\/{tag}>', re.DOTALL)
            rawHtml = re.sub(regex, '', rawHtml)
        return rawHtml

    
    def remove_all_tags(self, raw_html):
        if raw_html is not None:
            without_tags = re.sub(r'<.*?>', '', raw_html)
            without_newlines = self.remove_empty_lines(without_tags)
            return without_newlines
        else:
            return raw_html
        
    def remove_empty_lines(self, text):
        lines = text.split('\n')
        non_empty_lines = [line for line in lines if line.strip() != '']
        result = '\n'.join(non_empty_lines)
        return result

        
        
