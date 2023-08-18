from django.db import migrations, models
import django.db.models.deletion

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from closedverse import settings
from closedverse_main.models import User, Role

def update_passwords(apps, schema_editor):
	#User = apps.get_model('closedverse_main', 'User')
	users = User.objects.filter(password__startswith='$bcrypt-sha256')
	count = users.count()
	if not count:
		return
	print('\nNOW MIGRATING PASSWORDS!!!: basically just removing the first dollar sign which hashers_passlib.bcrypt_sha256 needs to be compatible.')
	print('please view ' + __file__ + ' for details')
	for user in users:
		# remove first dollar sign from bcrypt-sha256 passwords
		# this will make them compatible with hashers_passlib.bcrypt_sha256
		user.password = user.password[1:]
		user.save()
	print('updated ' + str(count) + ' passwords successfully, hopefully...')

	# update sessions as well to add hashes otherwise everyone gets logged out
	#Session = apps.get_model('sessions', 'Session')
	sessions = Session.objects.all()
	logged_in = [s.session_key for s in sessions if s.get_decoded().get('_auth_user_id')]
	# look up our sessions in session store
	for session_key in logged_in:
		s = SessionStore(session_key=session_key)
		try:
			# will fail if the user doesn't exist but that's it
			user = User.objects.get(id=s['_auth_user_id'])
			s['_auth_user_hash'] = user.get_session_auth_hash()
		except:
			continue
		s.save()
	print('updated ' + str(len(logged_in)) + ' sessions')


# replace this with first and second dicts from your own models.py
first = {
	1: 'cool',
	2: 'administrator',
	3: 'moderator',
	4: 'openverse',
	5: 'donator',
	6: 'cool',
	7: 'urapp',
	8: 'developer',
	9: 'badgedes',
	10: 'jack',
	11: 'verifiedd',
}
second = {
	1: "Bot",
	2: "Administrator",
	3: "Moderator",
	4: "O-PHP-enverse Man",
	5: "Donator",
	6: "Cool Person",
	7: "cave story is okay",
	8: "owner guy",
	9: "Badge Designer",
	10: "stupid man",
	11: "Verified",
}

# populate roles in the db if anyone uses them
def populate_roles(apps, schema_editor):
	User = apps.get_model('closedverse_main', 'User')
	# update role id 0 to NULL
	# so that it doesn't try to associate 0 with an actual role id GOD!
	User.objects.filter(role__lte=0).update(role=None)
	if not User.objects.filter(role__gte=1).count():
		return
	#Role = apps.get_model('closedverse_main', 'Role')
	#	print('no populate needed, as there were no role users found...')
	print('\nnow populating roles table...')
	for key in first.keys():
		image_url = 'img/' + first[key] + '.png'
		organization = second[key]
		role = Role.objects.create(id=key, is_static=True, image=image_url, organization=organization)
		# not sure why this returns "Role object (1)", etc. instead of the actual __str__
		print('saved role ' + first[key])
	print('all done')

class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0004_auto_20230818_1345'),
    ]

    operations = [
				# first make roles nullable before doing anything else
				migrations.AlterField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.RunPython(populate_roles),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='closedverse_main.role'),
        ),


    		# run password migration
        migrations.RunPython(update_passwords),
    ]
