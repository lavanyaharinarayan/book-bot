from abc import ABCMeta, abstractmethod, abstractproperty
import requests

from bs4 import BeautifulSoup

class Extract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self):
        pass


class GutenbergPlaintext(Extract):
	start = "*** START OF THIS PROJECT GUTENBERG EBOOK "
	end = "*** END OF THIS PROJECT GUTENBERG EBOOK"

	def __init__(self, link):
		self.link = link

	def _extract_text(self):
		html = requests.get(self.link).content
		start_index = self.start

		soup = BeautifulSoup(html, features="html.parser")
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out

		text = soup.body.get_text()

		start_index = text.find(self.start)+len(self.start)
		end_index = text.find(self.end)

		return text[start_index:end_index]

	def _split(self, text):
		# Split paragraphs
		paragraph = "\r\n\n\r\n"
		space = "\r\n"
		text = text.split(paragraph)
		return [paragraph.replace(space, " ").replace("  ", " ") for paragraph in text]

	def parse(self):
		return self._split(self._extract_text())

