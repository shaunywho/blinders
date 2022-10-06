
from django.contrib.auth.hashers import make_password

from models import User, Profile

Profile.objects.all().delete()
User.objects.all().delete()


# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger(__name__)

# # python manage.py seed --mode=refresh

# """ Clear all data and creates addresses """
# MODE_REFRESH = 'refresh'

# """ Clear all data and do not create any object """
# MODE_CLEAR = 'clear'

# class Command(BaseCommand):
#     help = "seed database for testing and development."

#     def add_arguments(self, parser):
#         parser.add_argument('--mode', type=str, help="Mode")

#     def handle(self, *args, **options):
#         self.stdout.write('seeding data...')
#         run_seed(self, options['mode'])
#         self.stdout.write('done.')


# def clear_data():
#     """Deletes all the table data"""
#     logger.info("Delete User instances")
#     User.objects.all().delete()


# def create_user():
#     """Creates a user object combining different elements from the list"""
#     logger.info("Creating User")

#     user = User(
#         password=make_password("Komalsfit1"),
#         username="shaun",
#         first_name="Shaun",
#         last_name = "Ho",
#         email = "shaunhohoho@gmail.com"
#     )
#     user.save()
#     logger.info("{} user created.".format(user))
#     return user

# def run_seed(self, mode):
#     """ Seed database based on mode

#     :param mode: refresh / clear 
#     :return:
#     """
#     # Clear data from tables
#     clear_data()
#     if mode == MODE_CLEAR:
#         return

#     # Creating 15 addresses
#     create_user()