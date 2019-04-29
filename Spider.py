import HtmlDownloader
import HtmlOutputer
import HtmlParser
import UrlManager

#爬虫主函数
class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.outputer = HtmlOutputer.HtmlOutputer()
    #抓取过程函数
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count = count+1
            except:
                print('craw failed')
        self.outputer.into_mysql()
if __name__ == '__main__':
    rooturl = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(rooturl)