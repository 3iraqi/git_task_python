
def valid_email():
    count = 0
    while True:
        count += 1
        if count >=5:
                raise ("You are blocked!")
        email = input("Enter your email: ")

        try:
            # this check if there is @ or not
            username, domain = email.split('@')

            # check if valid domain or not
            if '.' not in domain:
                raise ValueError("Missing '.' in domain")

            
            if email.index('@') == 0 or email[-1] == '.' or email.index('.') == 0:
                raise ValueError("Invalid email format")

            
            if '@.' in email:
                raise ValueError("Invalid sequence '@.' in email")

            
            if domain.count('.') > 1:
                raise ValueError("Too many '.' in domain")

            
            
            print(f'Valid Email. Welcome ({username})')
            return email
            

        except ValueError as e:
            print(f"UnValid: {e}")
