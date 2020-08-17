import csv
import subprocess

# Source: https://github.com/janjur/readable-pylint-messages/blob/master/readable_pylint_messages/generate_markdown.py
output = subprocess.check_output(['pylint', '--list-msgs'], stderr=subprocess.PIPE).decode('utf-8')
messages = output[1:].split('\n:')
new_messages = []
for message in messages:
    end_of_name = message.find(' ')
    name = message[:end_of_name]
    end_of_code = message.find(')', end_of_name)
    code = message[end_of_name + 2:end_of_code]
    end_of_brief = message.find('\n', end_of_code)
    brief = message[end_of_code + 4:end_of_brief - 1]
    desc = ' '.join([line.strip() for line in message[end_of_brief + 1:].splitlines()])
    new_messages.append(dict(name=name, code=code, brief=brief, description=desc))

# Source: https://realpython.com/python-csv/
with open("pylint.csv", mode="w") as csv_file:
    csv_header = ["code", "name", "brief", "description"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_header)

    csv_writer.writeheader()
    for new_message in new_messages:
        csv_writer.writerow(new_message)
