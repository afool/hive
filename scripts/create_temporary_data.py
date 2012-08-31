import popquotes
from accounts.models import UserProfile
from django.contrib.auth.models import User
from posts.models import Post
from timelines.models import Timeline
import random
import datetime
def get_random_quote():
	c = popquotes.open()
	r = c.db.execute("select * from quotes order by random() limit 1")
	return r.fetchone()

for x in range(100):
	User.objects.create_user("test" + str(x) , "test" + str(x) + "@test.com , "test" + str(x))
for user in User.objects.all():
	UserProfile.objects.create( user = user )

for x in range(10):
	now = datetime.datetime.now()
	users = User.objects.order_by("?").all()
	for user in users:
		rq = get_random_quote()
		now = now + datetime.timedelta(minutes=1)
		post = Post.objects.create( contents = rq[2] , create_time = now , writer = user , author = user.username )
		Timeline.objects.create( writer = user , post = post )

