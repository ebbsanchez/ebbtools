from django.contrib.auth.models import User, Group

import random

#### It is broken ### 

def init_guest_instance():
    # G1 = User(username='Guest1')
    # G2 = User(username='Guest2')
    # G3 = User(username='Guest3')
    # G4 = User(username='Guest4')
    # G1.save()
    # G2.save()
    # G3.save()
    # G4.save()

    # guest_group = Group(name='Guests')
    # guest_group.save()
    # guest_group.user_set.add(G1, G2, G3, G4)
    # guest_group.save()

    return


def get_random_guest_user():
    # try:
    #     guest_group = Group.objects.get(name='Guests')
    #     guest = guest_group.user_set.all()[random.randint(0, 3)]
    # except IndexError:
    #     init_guest_instance()
    #     guest_group = Group.objects.get(name='Guests')
    #     guest = guest_group.user_set.all()[random.randint(0, 3)]
    return guest
