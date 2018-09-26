from extract import GutenbergPlaintext

frankenstein = GutenbergPlaintext("https://www.gutenberg.org/files/84/84-h/84-h.htm")
txt = frankenstein.parse()
