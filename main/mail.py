
# * FOR FUNCTIONS RELATED TO MAIL
# * made this file to verify emails
def verifymail(mail):
    from validate_email import validate_email
    return validate_email(mail)

# * Sending the SMTP MAIL (Uses Mailtrap for fake testing , so right now mail wont be sent in real)


def send__mail(pk, mail):
    import smtplib
    from .models import Id
    from email.mime.text import MIMEText
    id = Id.objects.get(pk=pk)
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '9b4c1049781f9b'
    password = "407f4156f197b3"
    message = f"""
        <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
      crossorigin="anonymous"
    />
  
    <form action="/id" method="post" class="bg-light"  style="padding:5%;"  >
    <h1>Hey👋, {id.name}</h1>
    <h2>Welcome to MailVerify</h2>
    Kindly click the below link to Confirm your mail
    <a href="http://127.0.0.1:8000/id/{id.unique_id}" class="btn btn-primary">Verify Mail</a>
    </form>
    """
    sender_email = "email1@example.com"
    reciver_email = mail
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'MailVerify, Verify Your Mail'
    msg['From'] = sender_email
    msg["To"] = reciver_email

    # send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciver_email, msg.as_string())
    print("Mail sent")
