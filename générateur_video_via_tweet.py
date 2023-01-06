from tweetcapture import TweetCapture
import asyncio
import snscrape.modules.twitter as sntwitter
import moviepy.editor as mp

users_name = ['_Confessfantasm','OnePieceAnime','CerfiaFR']
tweets_list1 = []
video = mp.VideoFileClip("AestheticaSunset.mp4")
tweet = TweetCapture()
c = 0
x = ''
for n, k in enumerate(users_name):
    for i,tweet2 in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(users_name[n])).get_items()):
        if i>9:
            break
        c += 1
        print(x)
        asyncio.run(tweet.screenshot(
            f'{tweet2.url}', str(c)+".png", mode=2, night_mode=1))

        logo = (mp.ImageClip(str(tweet2.id)+".png")
                .set_duration(video.duration)
                .resize(height=400) # if you need to resize...
                .margin(right=8, top=8, opacity=3) # (optional) logo-border padding
                .set_pos(("center")))

        final = mp.CompositeVideoClip([video, logo])
        final.write_videofile(str(tweet2.id)+".mp4")