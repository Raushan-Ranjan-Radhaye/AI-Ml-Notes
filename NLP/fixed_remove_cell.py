def remove(txt):
  words = txt.split()
  cleaned = []
  for i in words:
    if i not in stop_words:
      cleaned.append(i)
  return ' '.join(cleaned)

