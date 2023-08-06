from scrapy import exceptions, Spider, FormRequest
from scrapy.crawler import CrawlerProcess
from midpay.settings import VA_LINKS


def get_mid_simulator_class(va_name, va_number):
    MidSimulatorSpider.va_links = VA_LINKS[va_name]
    MidSimulatorSpider.va_number = va_number
    return MidSimulatorSpider


class MidSimulatorSpider(Spider):
    name = "midpay"

    va_number = ""
    va_links = {
        "inquiry_url": "",
        "payment_url": "",
    }

    def start_requests(self):
        yield FormRequest(
                self.va_links["inquiry_url"],
                formdata={
                    'va_number': self.va_number,
                },
                callback=self.parse_inquiry
            )

    def parse_inquiry(self, response):
        total_amount = response.css('[name="total_amount"]::attr(value)').get()
        if not total_amount:
            exceptions.CloseSpider("total_amount not found")

        company_code = response.css('[name="company_code"]::attr(value)').get()
        customer_number = response.css('[name="customer_number"]::attr(value)').get()
        customer_name = response.css('[name="customer_name"]::attr(value)').get()
        currency_code = response.css('[name="currency_code"]::attr(value)').get()

        yield FormRequest(
            url=self.va_links["payment_url"],
            formdata={
                'total_amount': total_amount,
                'company_code': company_code,
                'customer_number': customer_number,
                'customer_name': customer_name,
                'currency_code': currency_code,
            },
            callback=self.parse_payment
        )

    def parse_payment(self, response):
        success_msg = response.css('.alert-success::text').get()
        if success_msg:
            yield {
                'msg': success_msg,
            }


def do_process(spider_class):
    process = CrawlerProcess(
        settings={
            'LOG_ENABLED': False,
        }
    )
    process.crawl(spider_class)
    process.start()
