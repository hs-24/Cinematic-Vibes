# preprocessing code will go here
import pandas as pd

file_path = "AFINN-en-165.txt"
df = pd.read_csv("metacritic_reviews.csv")
df1 = pd.read_csv("metacritic_movies.csv")

# Drop multiple columns and remove blank cells
df = df[["movie_title", "text"]].dropna()
df1 = df1[["movie_title", "genre"]].dropna()

# merging two csv files with wanted columns
# keeps "movie_title" and "genre" from df1
# on = "movie_title" makes it the column thats wanted | how = "left" keeps all rows from df match "movie_title" from df and df1
merged = pd.merge(df, df1[["movie_title", "genre"]],
                  on="movie_title", how="left")
merged["genre"] = merged["genre"].fillna("No Genre")

# select columns with 'object' (old way) / 'string' (new datatype)
merged_cols = merged.select_dtypes(include=['object', 'string']).columns

# loops through columns in merged
for col in merged.columns:
    merged[col] = (
        merged[col]  # cleaned
        # remove anything that is not LETTER/DIGIT/SPACE, replaced with ""
        .str.replace(r"[^A-Za-z0-9\s]", "", regex=True)
        # \s represents whitespace eg. tab/space | regex = regular expression
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()  # removes space from start of str
    )
