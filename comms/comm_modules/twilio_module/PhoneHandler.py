# einnuJ HackRU 2015

import twilio
from twilio import twiml


class TextSender:
    """
    A wrapper for Twilio's Rest Client to push messages; will raise
    Exceptions at the first sign of trouble.

    Attributes:
    __account_sid__: a unique value representing a text message.
    __auth_token__: a unique value representing the owener of the Twilio
        account.
    __twilio_client: the TwilioRestClient that takes care of the actual
        technical details.
    """

    def __init__(self, sid, auth_token):
        self.__account_sid__ = None
        self.__auth_token__ = None
        self.__twilio_client__ = None

        try:
            self.set_account_sid(sid)
            self.set_auth_token(auth_token)
            self.__twilio_client__ = twilio.rest.TwilioRestClient(
                account=self.__account_sid__, token=self.__auth_token__)

        except:
            raise

    def get_account_sid(self):
        if self.__account_sid__:
            return self.__account_sid__

    def set_account_sid(self, new_sid):
        if new_sid:
            if 34 == len(new_sid) and new_sid.isalnum():
                self.__account_sid__ = new_sid
            else:
                raise ValueError("Invalid format for Account SID!")
        else:
            raise TypeError("No new SID specified on set_account_sid()!")

    def get_auth_token(self):
        if self.__auth_token__:
            return self.__auth_token__

    def set_auth_token(self, new_token):
        if new_token:
            if 32 == len(new_token) and new_token.isalnum():
                self.__auth_token__ = new_token
            else:
                raise ValueError("Invalid format for Auth Token!")
        else:
            raise TypeError("No new Auth Token specified on set_auth_token()!")

    def get_text_status(self, text_sid, query):
        if isinstance(text_sid, twilio.rest.resources.messages.Message) and \
                isinstance(query, str):

            return self.__twilio_client__.messages.get(text_sid).status

    def create_and_send_text(self, send_to_number, twilio_number, message):
        """
        Method that will create and send a provided message, so long as the
        numbers are valid and the message is of type integer, binary,
        string, or sequence.

        :param send_to_number: the target/recipient phone number
        :param twilio_number: the registered Twilio number to text from
        :param message: the text message to send
        :return: a unique 34char-ID representing the text
        """

        try:
            new_text = self.__twilio_client__.messages.create(body=message,
                                                          to=send_to_number,
                                                          from_=twilio_number)
            return new_text.sid

        except:
            raise


class TextToSpeechCaller:

    def __init__(self, sid, auth_token):
        self.__account_sid__ = None
        self.__auth_token__ = None
        self.__twilio_client__ = None

        try:
            self.set_account_sid(sid)
            self.set_auth_token(auth_token)
            self.__twilio_client__ = twilio.rest.TwilioRestClient(
                account=self.__account_sid__, token=self.__auth_token__)

        except:
            raise

    def generate_twiml_file(self, drug_name, msg=None):
        """
        Method that generates a perfectly formed TwiML document that the
        call will access to read from.

        :param drug_name: name of the drug updated
        :param msg: None by default; will output standard speech.
        :return: the String value of the formed twiML.
        """
        response = twiml.Response()

        if msg:
            response.say(msg)
        else:
            response.say("Hello! RxCheck is calling to inform you that the "
                         "drug %s has had new discoveries made about it. "
                         "Please contact as and your healthcare professional at "
                         "your earliest convenience for your well-being." %
                         drug_name)

        return str(response)

    def make_phone_call(self, call_to_number, call_from_number, url):
        """
        Makes a phone call using the url as its TwiML basis.

        :param call_to_number: the number to call
        :param call_from_number: the Twilio number to call from
        :param url: the page hosting the TwiML document
        :return: the unique sid of the call
        """

        try:
            new_call = self.__twilio_client__.calls.create(call_to_number,
                                                call_from_number, url)
            return new_call.sid

        except:
            raise