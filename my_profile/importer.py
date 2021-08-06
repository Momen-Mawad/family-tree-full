import csv, datetime
from family_tree.models import familyData, accessRecord

with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = familyData.objects.get_or_create(
            id=row[0],
            first=row[1],
            second=row[2],
            third=row[3],
            last=row[4],
            father=row[5],
            partner=row[6],
            picture=row[7],
        )

        key = familyData.objects.get(index=row[0])

        _, created = accessRecord.objects.get_or_create(
            name=key,
            date=datetime.datetime.utcnow()
        )

        # creates a tuple of the new object or
        # current object and a boolean of if it was created