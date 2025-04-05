
# email=''
# while email.isdigit() or (not '') :
#     email=input("enter you emil ")
#     if (('.' and'@' not in email) or (email.count('@')!=1) or (email.index('@')==0)or (email[-1]=='.')or (email.index('.')==0)):
#         print('UnValid')
#         continue
#     elif('@.'  in email):
#         print('UnValid')
#         continue
#     else:
#         uname=email.split('@')[0]
#         if( (email.split('@')[1].count('.')>1) ):
#             print('UnValid')
#             continue
#         else:
#             print(f'Valid Email. Welcome ({uname})')
#             break
# else:
#     print('Not Valid Email!')


def validate_email():
    counter=0
    while True:
        counter+=1
        try:
            input('enter your email address').split('@')
            if counter >=5:
                raise ("Invalid email for  times. you have been blocked")
        except ValueError:
            print('Invalid Email')
            # continue
        else:
            return print('valid email')
        
validate_email()