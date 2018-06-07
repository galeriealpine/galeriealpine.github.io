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

# don't use the relationship bounds check
session.set_relationship_bounds(
    enabled=False
)

# follow everyone we like
session.set_do_follow(
    enabled=True,
    percentage=100,
    times=2
)

# unfollow users who don't follow us
session.unfollow_users(
    amount=250,
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

# like anything posted here
try:
    session.like_by_locations(
        [
            # actual places
            '216921418/villars/',
            '241218410/villars-vaud-switzerland/',
            '670455/villars-sur-ollon/',
            '293286136/bretaye/',
            '256352451/gryon-switzerland/',
            '259527434/bex-vaud/',
            '564436973/gare-bvb-de-villars-sur-ollon/',
            '1026860107/arveyes/',
            '220496208/les-diablerets/',
            '1208293649218937/les-ecovets/',
            '155754398365410/cookiedeli/',
            '218608989/les-mazots-meilleret/',
            '248169446/ollon-switzerland/',
            '227090360/glacier-3000-diablerets-gstaad/',
            '307552668/les-diablerets-switzerland/',
            '518992906/le-chamossaire/',
            '558567636/ormont-dessus/',
            '221078477/aigle-switzerland/',
            '830232215/aigle-castle/',

            # restaurants, hotels, schools, etc
            '1020387703/givengain-foundation/',
            '1023825820/restaurant-le-sporting/',
            '10246817/le-sporting/',
            '1025781378/villars-big-international-big-band-meeting/',
            '1027509796/villars-ski-school/',
            '1038845906153230/villars-bristol-apartment/',
            '1326011394177026/hotel-du-golf-spa-villars-ch/',
            '152006388774332/club-med-villars-sur-ollon/',
            '1788630878061539/la-gourmandine/'
            '186149958596417/les-mazots-du-clos-luxury-guesthouse-spa/',
            '213218600/club-med-villars-sur-ollon/',
            '221256543/chalet-royalp-hotel-spa/',
            '299962000/la-garenne-international-school/',
            '304782561/restaurant-lalchimiste/',
            '321774021624847/villars-vanguard-live-music-club/',
            '577417879055907/eurotel-victoria-villars/',
            '664786822/vieux-villars/',
            '685940077/prefleuri-international-alpine-school-switzerland/',
            '688732577/coop-villars-sur-ollon/',
            '7782826/aiglon-college/',
            '833046550/eurotel-victoria-les-diablerets/',
        ],
        amount=25,
        skip_top_posts=False
    )
except:
    print "Problem"

try:
    # like all photos with these tags (note, no ollon or bex as too many
    # false positives from outside the area in those, ditto aigle)
    session.like_by_tags(
        [
            'villars',
            'villarssurollon',
            'villarsgryon',
            'villarsgryondiablerets',
            'villarsurollon',
            'villarsskischool',
            'lesdiablerets',
            'essvillars',
            'bretaye',
            'lesecovets',
            'chesieres',
            'glacier3000',
        ],
        skip_top_posts=False,
        amount=25
    )
except:
    print "Problem"

# end the bot session
session.end()
