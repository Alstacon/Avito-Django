import csv
import json


def csv_to_json(csv_file: str, json_file: str, model: str):
    entries = []
    with open(f"{csv_file}", encoding="utf-8") as csv_file:
        csv_data = csv.DictReader(csv_file)

        for row in csv_data:
            to_add = {'model': model,
                      'pk': int(row['id'] if 'Id' in row else row['id']),
                      }
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'lat' in row:
                row['latitude'] = row['lat']
                del row['lat']
            if 'lng' in row:
                row['longitude'] = row['lng']
                del row['lng']

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            entries.append(to_add)

    with open(f"{json_file}", "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(entries, indent=4, ensure_ascii=False))


csv_to_json('../datasets/ad.csv', 'ads.json', 'ads.ad')
csv_to_json('../datasets/category.csv', 'categories.json', 'ads.category')
csv_to_json('../datasets/location.csv', 'locations.json', 'users.location')
csv_to_json('../datasets/user.csv', 'users.json', 'users.user')
