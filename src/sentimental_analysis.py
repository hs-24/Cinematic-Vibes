#most positive and negative text function + sliding window goes here, along with any other req
'''NEGATIVE AND POSITIVE'''
most_pos = merged['sentiment_score'].idxmax(
)  # select sentiment_score column and find max
most_pos_row = merged.loc[most_pos]  # consists of all the rows in the CSV

print("Most Postive Review"
      f"\nMovie: {most_pos_row['movie_title']}",
      f"\nReview: {most_pos_row['text']}",
      f"\nSentiment Score: {most_pos_row['sentiment_score']}"
      )

# select sentiment_score column and find min
most_neg = merged['sentiment_score'].idxmin()
most_neg_row = merged.loc[most_neg]  # consists of all the rows in the CSV
print("\nMost Negative Review"
      f"\nMovie: {most_neg_row['movie_title']}",
      f"\nReview: {most_neg_row['text']}",
      f"\nSentiment Score: {most_neg_row['sentiment_score']}"
