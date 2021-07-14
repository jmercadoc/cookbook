"""
Problem
    You want to sort objects of the same class, but they don't natively support
    comparison operations
"""
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]

print(users)

print(sorted(users,key=lambda x: x.user_id))

"""
Instead of using lambda, an alternative approach is to user
operator.attrgetter():
"""
from operator import attrgetter

print(sorted(users,key=attrgetter('user_id')))