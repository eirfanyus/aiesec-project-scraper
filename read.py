import json
json_data = []
with open('heartbeat.json') as json_file:
    json_data = json.load(json_file)

count = 0
for data in json_data:
    print(f"https://aiesec.org/opportunity/global-volunteer/{data['id']},\"{data['location']}\",", end="")
    for i in data['all_slots({\"sort\":\"start_date\",\"sort_direction\":\"asc\",\"start_date\":\"2024-03-14\"})']['nodes']:
        print(f"{i['start_date']},apps: {i['opportunity_applications_count']}", end=',')
    count += 1
    print(end="\n")

print(count)