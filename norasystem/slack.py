from slacker import Slacker
import celery

from backend_test.celery import app
from backend_test.envtools import getenv

###
#
# Slack API Implementation
#
###

slack = Slacker(getenv("SLACK_TOKEN"))


def send_message_channel(self, channel, message):
    json = self.slack.chat.post_message(channel, message)


def send_direct_message(self, user_id, message):
    private_channel_id = self.slack.im.open(user=user_id).body["channel"]["id"]
    self.slack.chat.post_message(channel, message)


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
     sender.add_periodic_task(
        crontab(hour=8, minute=30, day_of_week="mon-fri"),
        send_reminder.s()
     )


@app.task()
def send_reminder(arg):
    """
    Send a remainder directly  from Monday to 
    friday at 8:30 using the latest menu available.
    """
    employess = Employee.objects.all()
    for employee in employees:
        name = employee.full_name
        menu = Menu.objects.all().order_by("-created_at")[:1]
        base_url = getenv("domain_url")
        path = "/api/menu/"
        complete_path = base_url + path + menu.uuid
        message = f'Hello {name}! This is Nora. Choose a dish from the menu at {complete_path} before 11am. Thanks'
        send_direct_message(employee.slack_id,message)
