import comms.CommsHandler as CommsHandler

if __name__ == '__main__':
    cHandler = CommsHandler.CommsHandler()

    try:
        cHandler.send_text("+FAKENUMBER", "+TWILIONUMBER", "MSG")

    except Exception as e:
        print("Something bad: " + e.args[0])

    print("SCRIPT IS DONE TEXTING")