
# * made this file to make database functions  that will work upon the mail
# !BETTER CoMMENTS TO BE USED DOWNLOAD IT HERE -> https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments

def created_time(id):
    import datetime
    now = datetime.datetime.now()
    id.time_created = now
    id.save()
    return "Success"


def check_if_key_is_valid(id, objs):
    import datetime
    created = id.time_created
    then = datetime.datetime(2020, 10, 23, 17)
    dif = then-created
    if dif > datetime.timedelta(hours=2):
        objs.objects.delete(pk=id.id)
