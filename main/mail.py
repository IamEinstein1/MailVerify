
# * FOR FUNCTIONS RELATED TO MAIL
# * made this file to verify emails
def verifymail(mail):
    from validate_email import validate_email
    print(validate_email(mail))
    return validate_email(mail)


def send__mail(mail):
    EMAIL_HOST = 'smtp.mailtrap.io'
    EMAIL_HOST_PASSWORD = '407f4156f197b3'
    EMAIL_HOST_USER = '9b4c1049781f9b'
    EMAIL_PORT = '2525'
    from django.core.mail import send_mail
    print(send_mail("VERIFY YOUR ID", "CONTENT", recipient_list=[
        "vermarishit039@gmail.com "]))
