from celery import shared_task

from django.core.mail import send_mail





@shared_task
def send_welcome_email_to_employee(email):
	send_mail(
		'Employee Added',
		'Your Email Added',
		'emaployee@employee.com',
		[email]
		)
	return None