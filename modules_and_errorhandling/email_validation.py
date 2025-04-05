from validation import Validation as vld

def main():
    email=input('Email: ')
    while email.isdigit() or (not '') :
        email=input("enter you emil ")
        if (('.' and'@' not in email) or (email.count('@')!=1) or (email.index('@')==0)or (email[-1]=='.')or (email.index('.')==0)):
            print('UnValid')
            continue
        elif('@.'  in email):
            print('UnValid')
            continue
        else:
            uname=email.split('@')[0]
            if( (email.split('@')[1].count('.')>1) ):
                print('UnValid')
                continue
            else:
                print(f'Valid Email. Welcome ({uname})')
                break

if __name__ == "main":
    main()