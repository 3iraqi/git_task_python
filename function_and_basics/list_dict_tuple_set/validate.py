
def valid_element(message_='Enter Number: '):
    while True:
        try:
            return int(input(message_))
        except ValueError:
            print("invalid Value try again you should input integer")
            continue
