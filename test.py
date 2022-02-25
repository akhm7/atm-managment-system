from exchangelib import DELEGATE, Account, Credentials, Configuration,Message,Mailbox, FileAttachment
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
BaseProtocol.SESSION_POOLSIZE = 1
import datetime

print('begin request {0}'.format(datetime.datetime.now()))
def send_email(account, subject, body, recipients, attachments=None):
    try:
        to_recipients = []
        for recipient in recipients:
            to_recipients.append(Mailbox(email_address=recipient))
        m = Message(account=account,
                    folder=account.sent,
                    subject=subject,
                    body=body,
                    to_recipients=to_recipients)

        # attach files
        for attachment_name, attachment_content in attachments or []:
            file = FileAttachment(name=attachment_name, content=attachment_content)
            m.attach(file)
        m.send_and_save()
    except Exception as e:
        print(e)
        print("\nCouldn't connect.")

credentials = Credentials(
    username = 'aloqabank\\atm', #or myusername@email.com
    password = '~!QAZxsw2'
)

config = Configuration(server='10.31.51.235:443', credentials=credentials)

test_account = Account(
    primary_smtp_address = 's.d@aloqabank.uz',
    config = config,
    autodiscover = False,
    access_type = DELEGATE
)


# print('inbox request {0}'.format(datetime.datetime.now()))
# #Print first 100 inbox messages in reverse order
# for item in test_account.inbox.all().order_by('-datetime_received')[:100]:
#    print(item.subject, item.body, item.attachments)


#attachments = []
#with open('filestorage/numbers-test-document.pdf', 'rb') as f:
#    content = f.read()
#attachments.append(('whatever.pdf', content))
print('sending request {0}'.format(datetime.datetime.now()))
try:
    send_email(test_account, 'Test', 'Че не работаете? 😂😂', ['hojiakbar.ahmedov@aloqabank.uz'])
except Exception as e:
    print(e)
    print("\nCouldn't connect.")
print('end request {0}'.format(datetime.datetime.now()))
