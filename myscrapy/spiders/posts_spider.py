import scrapy
class PostsSpider(scrapy.Spider):
    name = 'posts'
    start_url = [
        'https://www.bhhsamb.com/agents/1',
        'https://www.bhhsamb.com/agents/2'
    ]

def parse(self.response):
    page = response.url.split('/')[-1]
    filename = 'posts-%s.html' % page
    with open (filename,'wb') as f:
        f.write(response.body)
        