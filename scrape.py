import instaloader
import  pandas as pd
import sys
sys.setrecursionlimit(10000)

L = instaloader.Instaloader()
L.login("", "")
### add burner account creds below ###
# saiansh's burner acc: u - scraaaaaaaaaaape, pwd - plsscrape123
# 
df=pd.DataFrame()

i=0
for post in instaloader.Profile.from_username(L.context, 'natgeo').get_posts():
    df = df.append({'Caption': post.caption, 'Likes': post.likes, 'URL': post.url  }, ignore_index=True)
    df.to_csv("natgeoraw.csv",index=False)
    i = i+1
    if i>400:
        break
print("Written to file")