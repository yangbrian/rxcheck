# einnuJ HackRU 2015

import comms.CommsHandler as CommsHandler

if __name__ == '__main__':
    recipient = ["FILL_THIS_IN@NOT_JOKING.COM"]
    recipients = ["SERIOUSLY@FILLMEIN.COM", "SILENTLY.YELLING@VOCAL.COM",
                  "THETHIRDELEMENT@NOTAMOVIE.COM"]

    comms_handler = CommsHandler.CommsHandler()

    try:
        comms_handler.send_email(recipient, True, "Tylenol")
        comms_handler.send_email(recipients, False, "Ibuprofen", "My Custom "
                                                                 "Message")
    except Exception as e:
        print("Well...")

    print("That's the end of the script!")