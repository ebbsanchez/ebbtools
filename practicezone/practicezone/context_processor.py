def user_data_plus(request):
    try:
        user_groups = []
        for group in request.user.groups.all():
            user_groups.append(group)

    except Exception as e:
        print('TEMPLATE_CONTEXT_PROCESSORS ERROR: ', e)
    context = {
        'request_user': request.user,
        'request_user_groups':  user_groups,
    }

    return context
