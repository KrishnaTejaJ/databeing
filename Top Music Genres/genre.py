import data_
genre_count = {}

for g in data_.data:
  genre_count[g['Genre']] = genre_count.get(g['Genre'], 0) + 1

print(sorted(genre_count.items(), key = lambda kv: kv[1]))
