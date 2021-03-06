import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    #ExStart: SavingMessageFromIMAPServer
    conn =  ImapClient("imap.gmail.com", 993, "username", "password")
    conn.select_folder("Inbox")
    for msgInfo in conn.list_messages():
        msg = conn.fetch_message(msgInfo.unique_id)
        msg.save(dataDir + msgInfo.unique_id + "_out.msg", aspose.email.SaveOptions.default_msg_unicode)
    #ExEnd: SavingMessageFromIMAPServer
if __name__ == '__main__':
    run()
