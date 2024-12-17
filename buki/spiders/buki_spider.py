import scrapy

class BukiSpider(scrapy.Spider):
    name = "buki"
    allowed_domains = ["buki-kz.com"]
    start_urls = [f"https://buki-kz.com/repetitor/{i}/" for i in range(1, 100)]

    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }
    
    def parse(self, response):
        cards = response.css("div.styles_card__Yjci5")
        for card in cards:
            experience_text = card.xpath('.//p[contains(@class, "styles_practice__AZyXc")]/text()').get(default='')
            experience_text = experience_text.replace("Опыт: ", "").strip() if experience_text else None
            yield {
                "name": card.css("p.styles_userName__ltIVo span::text").get(),
                "subjects": card.css("span.styles_lessonsItem__v8FAD::text").getall(),
                "degree": card.css("p.styles_education__41VXk span::text").get(),
                "experience": experience_text.replace("Опыт: ", "").strip() if experience_text else None,
                "city": card.css("a.styles_link__5pWac::text").get(),
                "price": int(''.join(filter(str.isdigit, card.css("span.topCeil::text").get(default='0')))) if card.css("span.topCeil::text") else None,
                "canWorkOnline": bool(card.css("p.styles_workOnline__p4t8f")),
                "shortDescription": card.css("span.styles_shortDescription__9jRi6::text").get(),
                "rating": card.css("div.styles_reviewsBlock__FNrPL span::text").re_first(r"(\d\.\d)"),
                "reviewCount": card.css("div.styles_reviewsBlock__FNrPL span.styles_reviewsCount__EAIh6::text").re_first(r"\d+"),
            }