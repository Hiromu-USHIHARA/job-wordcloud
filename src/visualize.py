from wordcloud import WordCloud
import matplotlib.pyplot as plt
from get_job_titles import get_job_titles

def create_wordcloud_from_titles(titles):
    text=" ".join(titles)

    wordcloud=WordCloud(
        font_path="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(16,9))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

titles=get_job_titles("東京都", max_pages=5)
create_wordcloud_from_titles(titles=titles)