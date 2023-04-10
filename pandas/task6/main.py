import pandas as pd

# df = pd.read_csv('https://github.com/bykov-alexei/data-science-course/blob/master/Pandas/app_store_reviews.csv')
df = pd.read_csv('file.csv')

# print(df.isna().head(10))

# print(df[(df.app_name == 'whatsapp-messenger')&(df.rating == 5)].shape[0])

# print(df[(df.app_name == 'talking-tom-cat-2')].rating.mean())

# print(df['developerResponse'].count())
# print(df.count())

# print(df.groupby('app_name').mean())

# print(df.iloc[df.review.apply(len).idxmax()].review)

# print(df.review.apply(lambda s: len(s.split())).mean())

# print(df.groupby('crawled_at').review.count().idxmax())

print(df[df.app_name == 'talking-tom-cat-2'].rating.median())
