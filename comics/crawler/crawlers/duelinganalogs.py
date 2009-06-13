from comics.crawler.crawlers import BaseComicCrawler

class ComicCrawler(BaseComicCrawler):
    def _get_url(self):
        self.parse_feed(
            'http://feeds2.feedburner.com/DuelingAnalogs?format=xml')

        for entry in self.feed.entries:
            if self.timestamp_to_date(entry.updated_parsed) == self.pub_date:
                self.title = entry.title
                pieces = entry.summary.split('"')
                for i, piece in enumerate(pieces):
                    if (piece.count('src=')
                        and pieces[i + 1].startswith(
                            'http://www.duelinganalogs.com/comics/')):
                        self.url = pieces[i + 1]
                        return