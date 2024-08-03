from google_play_scraper import app, reviews, Sort, reviews_all

scrapreview = reviews (
    'com.gojek.app',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=10000
)

import csv

with open('ulasan_gojek.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrapreview:
        writer.writerow([review['content']])