
# * FOR FUNCTIONS RELATED TO MAIL
# * made this file to verify emails
def verifymail(mail):
    from validate_email import validate_email
    print(validate_email(mail))
    return validate_email(mail)
