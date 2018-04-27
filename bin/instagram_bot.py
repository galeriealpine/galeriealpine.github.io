import sys
sys.path.append('/Users/leejohnson/working/InstaPy')

from instapy import InstaPy

insta_username = ''
insta_password = ''

for line in open( '/Users/leejohnson/working/.ga_instagram_bot.cred' ):
    if insta_username == '':
        insta_username = line.rstrip()
    else:
        insta_password = line.rstrip()

# set headless_browser=True if you want to run InstaPy on a server
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=True
)
session.login()

# follow everyone we like
session.set_do_follow(
    enabled=True,
    percentage=100,
    times=2
)

# don't follow anyone with > 10000 followers
session.set_upper_follower_count( limit=10000 )

# unfollow users who don't follow us
session.unfollow_users(
    amount=100,
    onlyNotFollowMe=True,
    onlyInstapyMethod='FIFO',
    sleep_delay=60
)

# but don't unfollow if they've liked one of our last 3 posts
session.set_dont_unfollow_active_users(
    enabled=True,
    posts=3
)

# note - keep sum of all likes to < 300 per hour

# like anything posted here. TODO: les diablerets, chesieres, ollon, etc
try:
    session.like_by_locations(
        [
            '670455/villars-sur-ollon/',
            '241218410/villars-vaud-switzerland/',
            '216921418/villars/'
            '564436973/gare-bvb-de-villars-sur-ollon/',
            '293286136/bretaye/',
            '518992906/le-chamossaire/',
            '664786822/vieux-villars/',
            '1020387703/givengain-foundation/',
            '688732577/coop-villars-sur-ollon/',
            '1023825820/restaurant-le-sporting/',
            '577417879055907/eurotel-victoria-villars/',
            '1027509796/villars-ski-school/',
            '1025781378/villars-big-international-big-band-meeting/',
            '186149958596417/les-mazots-du-clos-luxury-guesthouse-spa/',
            '1788630878061539/la-gourmandine/'
            '321774021624847/villars-vanguard-live-music-club/',
            '213218600/club-med-villars-sur-ollon/',
            '221256543/chalet-royalp-hotel-spa/',
            '1326011394177026/hotel-du-golf-spa-villars-ch/'
        ],
        amount=25,
        skip_top_posts=False
    )
except:
    print "Problem"

try:
    # like all photos with these tags, TODO: more tags
    session.like_by_tags(
        [
            'villars',
            'villarssurollon',
            'villarsgryon',
            'bretaye'
        ],
        skip_top_posts=False,
        amount=25
    )
except:
    print "Problem"

# end the bot session
session.end()
