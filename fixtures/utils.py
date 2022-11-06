import csv
import json


def csv_to_json(csv_file: str, json_file: str, model: str):
    entries = []
    with open(f"{csv_file}", encoding="utf-8") as csv_file:
        csv_data = csv.DictReader(csv_file)

        for row in csv_data:
            entries.append({
                'model': model,
                'pk': row['id'],
                'fields': row
            })

    with open(f"{json_file}", "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(entries, indent=4, ensure_ascii=False))


csv_to_json('ads.csv', 'ads.json', 'ads.ad')
csv_to_json('categories.csv', 'categories.json', 'ads.category')

