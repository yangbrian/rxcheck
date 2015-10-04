# einnuJ HackRU 2015

# Our Custom Classes
import comms.comm_modules.sendgrid_module.EmailSender as EmailSender
import comms.comm_modules.twilio_module.PhoneHandler as PhoneHandler

# This is terrible, I know.
API = "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"
SID = 'AC267df54a3efc64400711ee0c0c910cae'
AUTH = '594cabf89405f8231e32543faac2d547'

class CommsHandler:
    """
    A class that handles the sending of text and emails via Twilio and
    SendGrid API.
    """

    def __init__(self):
        self.__email_sender__ = None
        self.__text_sender__ = None
        self.__tts_caller__ = None

        try:

            self.__email_sender__ = EmailSender.EmailSender(API, [])
            self.__text_sender__ = PhoneHandler.TextSender(SID, AUTH)
            self.__tts_caller__ = PhoneHandler.TextToSpeechCaller(SID, AUTH)

        except:

            raise

    def get_email_sender(self):
        return self.__email_sender__

    def send_text(self, send_to_number, send_from_number, msg):

        try:
            self.__text_sender__.create_and_send_text(send_to_number,
                                                  send_from_number, msg)

        except Exception as e:
            print("Failed to text: " + e.args[0])

    def get_twiml_file(self, drug_name, msg=None):
        return self.__tts_caller__.generate_twiml_file(drug_name, msg)

    def make_text_to_speech_call(self, call_recipient, caller_number, url):

        try:
            self.__tts_caller__.make_phone_call(call_recipient,
                                                caller_number, url)
        except Exception as e:
            print("Failed to call: " + e.args[0])


    def send_email(self, recipients, is_recall, drug, msg=None):

        self.__email_sender__.add_recipients(recipients)

        # This part of the code should've been where the try/catch
        # statements are, not in the classes themselves...?

        if is_recall:
            self.__email_sender__.send_recall_msg(drug, msg)
        else:
            self.__email_sender__.send_new_drug_info_msg(drug, msg)