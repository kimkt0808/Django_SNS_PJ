from notifications.models import Notification


def notifications(request):
    if request.user.is_authenticated:
        unread_notifications_count = Notification.objects.unread().filter(recipient=request.user).count()
    else:
        unread_notifications_count = 0

    return {'unread_notifications_count': unread_notifications_count}
