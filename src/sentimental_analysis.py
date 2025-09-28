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

#SLIDING WINDOW(MergedDataset)
def best_worst_window(scores, k: int):
    """Return ((best_sum, L, R), (worst_sum, L, R)) for fixed window k over scores."""
    n = len(scores)
    if k <= 0 or k > n:
        return None, None
    win = sum(scores[:k])
    best_sum = win; best_L = 0
    worst_sum = win; worst_L = 0
    for i in range(k, n):
        win += scores[i] - scores[i-k]
        if win > best_sum:
            best_sum, best_L = win, i - k + 1
        if win < worst_sum:
            worst_sum, worst_L = win, i - k + 1
    return (best_sum, best_L, best_L + k), (worst_sum, worst_L, worst_L + k)

k = 2  # tweak as needed
best_win, worst_win = best_worst_window(scores, k)
if best_win:
    bsum, bL, bR = best_win
    wsum, wL, wR = worst_win
    print(f"Best {k}-sentence window:", bsum, "→", " ".join(sentences[bL:bR]))
    print(f"Worst {k}-sentence window:", wsum, "→", " ".join(sentences[wL:wR]))
else:
    print(f"Not enough sentences for k={k}.")
