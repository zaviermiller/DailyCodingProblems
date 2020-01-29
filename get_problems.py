# This program logs into a gmail account and gets all DCP emails
# Will optimize with search in the future

import imaplib
import email
import os


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return (msg.get_payload(None, True)).decode('utf-8')


def format_day(day):
    if len(day) != 3:
        return format_day('0' + day)
    else:
        return day


email_user = os.environ.get('DCP_GMAIL')
email_pass = os.environ.get('DCP_PASS')
print("connecting to imap server...")

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(email_user, email_pass)
M.select('Inbox')
print("connected!")

typ, data = M.search(None, 'ALL')

print('beginning email processing...')
for num in data[0].split():
    status, data = M.fetch(num, '(RFC822)')
    email_msg = data[0][1]
    raw = email.message_from_bytes(email_msg)
    if "Daily Coding Problem: Problem #" in raw['subject']:
        parsed = get_body(raw)
        body = parsed.split('This problem was ')[1].split(
            "\r\n\r", 1)[1].split("--------", 1)[0].split("\r\n\r\r\n\r", 1)[0].split("\r\n\r\n\r\n")[0]
        day = format_day(raw['subject'].split("#")[1].split(" ")[0])
        difficulty = raw['subject'][::-1].split(' ', 2)[1][::-1]
        if f'dcp_{day}.py' not in os.listdir():
            file = open(f'dcp_{day}.py', "w")
            file.write(
                f'# =-=-=-= DAY { raw["subject"].split("#")[1].split(" ")[0] } {difficulty} =-=-=-=\n#\n')
            lines = body.split("\r\n")
            for line in lines:
                if "\n" in line:
                    line = line.split("\n")[1]
                file.write("# " + line)
                file.write("\n")
            file.close()
            print(f'Created dcp_{day}.py')
print("processed all emails")

M.close()
M.logout()
