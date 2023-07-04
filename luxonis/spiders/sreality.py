import scrapy
from luxonis.items import SrealityProperty

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    website = "https://www.sreality.cz/en/search/for-sale/houses"
    item_count = 0
    max_count = 500

    def start_requests(self):
        yield scrapy.Request(self.website, meta={'playwright': True})

    async def parse(self, response):
        
        for prop in response.css("div.property.ng-scope"):
            sreality_property = SrealityProperty()

            title = prop.css("span.name.ng-binding::text").get().replace(" ", "") + ", " + prop.css("span.locality.ng-binding::text").get()
            img_urls = []

            for img in prop.css("img"):
                img_url = img.css("::attr(src)").extract_first()
                if img_url != "/img/camera.svg":
                    img_urls.append(img_url)

            self.item_count += 1

            sreality_property["title"] = title
            sreality_property["img_urls"] = img_urls

            yield sreality_property

            if self.item_count >= self.max_count:
                raise scrapy.exceptions.CloseSpider(reason=f"{self.max_count} items scraped.")
        
        next_page = response.css("a.btn-paging-pn.icof.icon-arr-right.paging-next::attr(href)").extract_first()
        
        if next_page:
            yield response.follow(next_page, meta={'playwright': True})