# collect email from user
# split the eamil using the @, the first part as the user name, the second part is gonna be saved as domain
# split the doamin using .,
def main():
    print('Welcome to the email slicer')
    print("")

    email_input = input('input your email addrress: ')
    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

while True:
    main()