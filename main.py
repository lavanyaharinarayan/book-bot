from extract import GutenbergPlaintext

frankenstein = GutenbergPlaintext("https://www.gutenberg.org/files/84/84-h/84-h.htm")
txt = frankenstein.parse()

def divide(text):
	tweets = []
	splitters = [",", "-", "--"]
	return [para.split(",") for para in text]

def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

y = flatten(divide(txt))
for x in range(100, 120):
	print(y[x])