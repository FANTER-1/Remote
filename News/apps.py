from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News'
class AppointmentConfig(AppConfig):
    name = 'appointment'

    def ready(self):
        import appointment.signal

        from .tasks import send_mails
        from .scheduler import appointment_scheduler
        print('started')

        appointment_scheduler.add_job(
            id='mail send',
            func=send_mails,
            trigger='interval',
            seconds=10,
        )
        appointment_scheduler.start()
