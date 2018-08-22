from django.template import Template, Context
from django.contrib.auth import get_user_model
from celeryWithDjango.celery import app
from publish.models import Post

REPORT_TEMPLATE = """
Here's how you did till now:

{% for post in posts %}
        "{{ post.title }}": viewed {{ post.view_count }} times |

{% endfor %}
"""


@app.task(bind=True, default_retry_delay=30 * 60)
def send_view_count_report(self):
    try:
        UserModel = get_user_model()
        for user in UserModel.objects.all():
            posts = Post.objects.filter(author=user)
            if not posts:
                continue

            template = Template(REPORT_TEMPLATE)

            print(
                'Your QuickPublisher Activity',
                template.render(context=Context({'posts': posts})),
                'from@quickpublisher.dev',
                [user.email]
            )
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
