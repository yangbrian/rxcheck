# einnuJ HackRU 2015

import comms.CommsHandler as CommsHandler

if __name__ == '__main__':
    recipient = ["HAHAHAH@HEHEHEHEHE.HOO"]
    recipients = ["REPLACE_THIS@FAKEMAIL.COM", "OTHERFAKE@EMAIL.COM"]

    comms_handler = CommsHandler.CommsHandler()

    try:
        comms_handler.send_email(recipient, True, "Tylenol")
        comms_handler.send_email(recipients, False, "Ibuprofen", "My Custom "
                                                                 "Message")
    except Exception as e:
        print("Well: " + e.args[0])

    print("That's the end of the script!")