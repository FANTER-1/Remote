import redis
from django.apps import AppConfig

red = redis.Redis(
    host='redis-17594.c323.us-east-1-2.ec2.cloud.redislabs.com',
    port='17594',
    password='A4msy7if4ajgpb97ykns6dzbr8hxwd490u9a2gnljm1mt5z9due',
)


class AppointmentConfig(AppConfig):
    name = 'appointment'

    # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import appointment.signals