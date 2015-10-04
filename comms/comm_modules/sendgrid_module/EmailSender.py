# einnuJ HackRU 2015

import sendgrid


class EmailSender:
    """
    This class loosely wraps the SendGridClient, taking care of sending with a
    basic template already set out.
    """

    def __init__(self, api, send_to):
        # This ensures that Exceptions will be raised to us.
        self.__sg_client__ = sendgrid.SendGridClient(api, raise_errors=True)
        self.__recipients__ = []

        for recipient in send_to:
            self.__recipients__.append(recipient)

    def get_recipients(self):
        return self.__recipients__

    def set_recipients(self, send_to):
        if isinstance(send_to, list):
            self.__recipients__ = send_to
        else:
            raise TypeError("set_recipients() takes list-type only!")

    def add_recipients(self, send_to):
        if isinstance(send_to, list):
            for i in send_to:
                self.__recipients__.append(i)

        else:
            self.__recipients__.append(send_to)

    def send_new_drug_info_msg(self, drug, msg=None):
        if msg:
            self.send(msg)
        else:
            new_drug_info_msg = "Hello; apologies for the intrusion, " \
                                   "but the drug \'%s\' has been updated " \
                                   "with new information! Please visit our " \
                                   "web-app for the full break-down!" % drug
            self.send(new_drug_info_msg)

    def send_recall_msg(self, drug, msg=None):
        if msg:
            self.send(msg)
        else:
            recall_msg = "Hello; this is a message from RxCheck to let you " \
                         "know that the drug \'%s\' has been recalled. For " \
                         "more information, please visit our website." % drug
            self.send(recall_msg)

    def send(self, text):
        """
        This method fills out the basic attributes of an HTTP Email. It has
        the ability to CC, BCC, send attachments, and more - but it is not
        implemented yet in this class.

        :param text: the body of the message to send
        """

        message = sendgrid.Mail()
        message.add_to(self.__recipients__)
        message.set_subject("RXCheck Alert!")
        message.set_html(text)
        message.set_text(text)
        message.set_from('RXCheck Development Team <DevMD@RXCheck.com>')

        # The SendGrid API does not parse for the reasoning behind the
        # errors, just their origination point.
        # And neither will we.

        try:
            self.__sg_client__.send(message)
        except sendgrid.SendGridClientError as e:
            print("Client error CODE: " + e.code + ", " + e.args[0])
        except sendgrid.SendGridServerError as e:
            print("Server error CODE: " + e.code + ", " + e.args[0])
