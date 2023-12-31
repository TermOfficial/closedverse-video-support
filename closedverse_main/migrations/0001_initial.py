# Generated by Django 3.2.19 on 2023-06-30 00:14

import closedverse_main.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('has_mh', models.BooleanField(default=False)),
                ('avatar', models.CharField(blank=True, default='', max_length=1200)),
                ('level', models.SmallIntegerField(default=0)),
                ('role', models.SmallIntegerField(choices=[(0, 'normal'), (1, 'bot'), (2, 'administrator'), (3, 'moderator'), (4, 'openverse'), (5, 'donator'), (6, 'cool'), (7, 'urapp'), (8, 'owner'), (9, 'badgedes'), (10, 'jack'), (11, 'verified')], default=0)),
                ('addr', models.CharField(blank=True, max_length=64, null=True)),
                ('hide_online', models.BooleanField(default=False)),
                ('color', closedverse_main.models.ColorField(blank=True, default='', max_length=18, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feeling', models.SmallIntegerField(choices=[(0, 'normal'), (1, 'happy'), (2, 'wink'), (3, 'surprised'), (4, 'frustrated'), (5, 'confused'), (38, 'japan'), (69, 'easter egg')], default=0)),
                ('body', models.TextField(null=True)),
                ('screenshot', models.CharField(blank=True, default='', max_length=1200, null=True)),
                ('drawing', models.CharField(blank=True, max_length=200, null=True)),
                ('spoils', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('befores', models.TextField(blank=True, null=True)),
                ('has_edit', models.BooleanField(default=False)),
                ('is_rm', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(choices=[(0, 'ok'), (1, 'delete by user'), (2, 'delete by authority'), (3, 'delete by mod'), (4, 'delete by admin'), (5, 'account pruge')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('ico', models.CharField(blank=True, max_length=255)),
                ('banner', models.CharField(blank=True, max_length=255)),
                ('type', models.SmallIntegerField(choices=[(0, 'general'), (1, 'game'), (2, 'special'), (3, 'hide')], default=0)),
                ('platform', models.SmallIntegerField(choices=[(0, 'none'), (1, '3ds'), (2, 'wii u'), (3, 'both')], default=0)),
                ('tags', models.CharField(blank=True, choices=[('announcements', 'main announcement community'), ('changelog', 'main changelog'), ('activity', 'Activity Feed posting community')], max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_rm', models.BooleanField(default=False)),
                ('is_feature', models.BooleanField(default=False)),
                ('allowed_users', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'communities',
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conv_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conv_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('able_vote', models.BooleanField(default=True)),
                ('choices', models.TextField(default='[]')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feeling', models.SmallIntegerField(choices=[(0, 'normal'), (1, 'happy'), (2, 'wink'), (3, 'surprised'), (4, 'frustrated'), (5, 'confused'), (38, 'japan'), (69, 'easter egg')], default=0)),
                ('body', models.TextField(null=True)),
                ('drawing', models.CharField(blank=True, max_length=200, null=True)),
                ('screenshot', models.CharField(blank=True, default='', max_length=1200, null=True)),
                ('video', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('url', models.URLField(blank=True, default='', max_length=1200, null=True)),
                ('spoils', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('befores', models.TextField(blank=True, null=True)),
                ('has_edit', models.BooleanField(default=False)),
                ('is_rm', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(choices=[(0, 'ok'), (1, 'delete by user'), (2, 'delete by authority'), (3, 'delete by mod'), (4, 'delete by admin'), (5, 'account pruge')], default=0)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.community')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.poll')),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='closedverse_main.user')),
                ('ua', models.TextField(blank=True, default='', null=True)),
                ('latest', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'submitted'), (1, 'viewed'), (2, 'accepted'), (3, 'decline'), (4, 'ignore')], default=0)),
            ],
            bases=('closedverse_main.user',),
        ),
        migrations.CreateModel(
            name='Yeah',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('type', models.SmallIntegerField(choices=[(0, 'post'), (1, 'comment')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.post')),
            ],
        ),
        migrations.CreateModel(
            name='UserBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('full', models.BooleanField(default=False)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.SmallIntegerField(choices=[(0, 'Prevent yeah'), (1, 'Prevent follow'), (2, 'Prevent comment')])),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restriction_by', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restriction_comment', to='closedverse_main.comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restriction_post', to='closedverse_main.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restriction_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RedFlag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.SmallIntegerField(choices=[(0, 'Post'), (1, 'Comment'), (2, 'User')])),
                ('reason', models.SmallIntegerField(choices=[(0, 'Actual harassment'), (1, 'Spam'), (2, "I don't like this"), (3, 'Personal info'), (4, 'Obscene use of swearing'), (5, 'NSFW where not allowed'), (6, 'Overly advertising/spam'), (7, 'Please delete this')])),
                ('reasoning', models.TextField(blank=True, default='', null=True)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('origin_id', models.CharField(blank=True, max_length=16, null=True)),
                ('origin_info', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, default='')),
                ('country', models.CharField(blank=True, default='', max_length=120)),
                ('id_visibility', models.SmallIntegerField(choices=[(0, 'show'), (1, 'friends only'), (2, 'hide')], default=0)),
                ('pronoun_is', models.IntegerField(choices=[(0, "I don't know"), (1, 'He/him'), (2, 'She/her'), (3, 'He/she'), (4, 'They/them'), (5, 'It')], default=0)),
                ('let_friendrequest', models.SmallIntegerField(choices=[(0, 'show'), (1, 'friends only'), (2, 'hide')], default=0)),
                ('yeahs_visibility', models.SmallIntegerField(choices=[(0, 'show'), (1, 'friends only'), (2, 'hide')], default=0)),
                ('comments_visibility', models.SmallIntegerField(choices=[(0, 'show'), (1, 'friends only'), (2, 'hide')], default=2)),
                ('weblink', models.CharField(blank=True, default='', max_length=1200)),
                ('external', models.CharField(blank=True, default='', max_length=255)),
                ('let_yeahnotifs', models.BooleanField(default=True)),
                ('let_freedom', models.BooleanField(default=True)),
                ('limit_post', models.SmallIntegerField(default=0)),
                ('cannot_edit', models.BooleanField(default=False)),
                ('email_login', models.SmallIntegerField(choices=[(0, 'Do not allow'), (1, 'Okay'), (2, 'Only allow')], default=1)),
                ('favorite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PollVote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('done', models.DateTimeField(auto_now_add=True)),
                ('choice', models.SmallIntegerField(default=0)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('read', models.BooleanField(default=False)),
                ('type', models.SmallIntegerField(choices=[(0, 'Yeah on post'), (1, 'Yeah on comment'), (2, 'Comment on my post'), (3, "Comment on others' post"), (4, 'Follow to me'), (5, 'New Announcement')])),
                ('merges', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('latest', models.DateTimeField(auto_now=True)),
                ('context_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.comment')),
                ('context_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.post')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feeling', models.SmallIntegerField(choices=[(0, 'normal'), (1, 'happy'), (2, 'wink'), (3, 'surprised'), (4, 'frustrated'), (5, 'confused'), (38, 'japan'), (69, 'easter egg')], default=0)),
                ('body', models.TextField(null=True)),
                ('drawing', models.CharField(blank=True, max_length=200, null=True)),
                ('screenshot', models.CharField(blank=True, default='', max_length=1200, null=True)),
                ('url', models.URLField(blank=True, default='', max_length=1200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('is_rm', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.conversation')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('success', models.BooleanField(default=False)),
                ('addr', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('latest', models.DateTimeField(auto_now=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('read', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConversationInvite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('read', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.conversation')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convinvite_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convinvite_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.SmallIntegerField(choices=[(0, 'Bug report'), (1, 'Suggestion'), (2, 'Want')])),
                ('body', models.TextField(blank=True, default='')),
                ('sex', models.SmallIntegerField(choices=[(0, 'girl'), (1, 'privileged one'), (2, '(none)')], null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityFavorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.community')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.community'),
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='original_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.post'),
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.SmallIntegerField(choices=[(0, 'Post delete'), (1, 'Comment delete'), (2, 'User edit'), (3, 'Generate passwd reset'), (4, 'User delete'), (5, 'Image delete'), (6, 'Purge 1'), (7, 'Purge 2'), (8, 'Purge 3'), (9, 'Purge 4'), (10, 'Purge 5'), (11, 'Un-purge 1')])),
                ('reasoning', models.TextField(blank=True, default='', null=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_by', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audit_comment', to='closedverse_main.comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audit_post', to='closedverse_main.post')),
                ('reversed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audit_reverse_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audit_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
