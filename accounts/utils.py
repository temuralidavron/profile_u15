from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import random
from django.core.mail import EmailMultiAlternatives


def send_simple_email(to_user_email):

    send_mail(

        subject="Django email sinovi",

        message="Realchilarga mazza",

        from_email=EMAIL_HOST_USER,

        recipient_list=[to_user_email],

        fail_silently=False,

    )


def verification_code():
    code=random.randint(100000, 999999)
    return str(code)






def send_html_email(code,to_user,username):
    subject = "Passwordni yangilash uchun"

    from_email = "aliyer.temur95@gmail.com"

    to = [to_user]

    text_content = "Bu oddiy email matni."

    html_content = f"""<h1>Salom</h1><p>Bu <strong>HTML</strong>
    <a href="http://127.0.0.1:8000/accounts/done/?name={username}">Link</a>
    
    <p>{code}</p?


    email. < / p > """

    email = EmailMultiAlternatives(subject, text_content,
                                   from_email, to)

    email.attach_alternative(html_content, "text/html")

    email.send()