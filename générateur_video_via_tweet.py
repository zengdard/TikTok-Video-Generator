from tweetcapture import TweetCapture
import asyncio
import snscrape.modules.twitter as sntwitter
import moviepy.editor as mp

users_name = ['Your Twitter Account Here']


tweets_list1 = []
video = mp.VideoFileClip("your background video here")
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
            f'{tweet2.url}', str(c)+".png", mode=0, night_mode=1))

        logo = (mp.ImageClip(str(c)+".png")
                .set_duration(video.duration)
                .resize(height=420) # if you need to resize...
                .margin(right=8, top=8, opacity=3) # (optional) logo-border padding
                .set_pos(("center")))

        final = mp.CompositeVideoClip([video, logo])
        final.write_videofile(str(c)+".mp4")