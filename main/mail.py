
# * FOR FUNCTIONS RELATED TO MAIL
# * made this file to verify emails
def verifymail(mail):
    from validate_email import validate_email
    print(validate_email(mail))
    return validate_email(mail)


def send__mail(mail):
    from django.core.mail import send_mail
    print(send_mail("VERIFY YOUR ID", "CONTENT", recipient_list=[
        "vermarishit039@gmail.com "]))
