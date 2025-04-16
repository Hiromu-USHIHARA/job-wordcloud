import streamlit as st
from get_job_titles import get_job_titles
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("地域別求人ジャンル可視化アプリ")

place=st.text_input("地名を入力してください")
if st.button("ワードクラウド生成"):
    if not place:
        st.warning("地名を入力してください")
    else:
        with st.status("{0}の求人情報を取得中...".format(place), expanded=True) as status:
            titles=get_job_titles(place, max_pages=5)
            if not titles:
                st.error("求人情報を取得できませんでした．地名を再確認してください．")
                status.update("求人情報を取得できませんでした", state="error")
            else:
                text=" ".join(titles)

                wordcloud=WordCloud(
                    font_path="fonts/NotoSansCJK-Regular.ttc",
                    width=800,
                    height=400,
                    background_color="white"
                ).generate(text)

                st.subheader("職種ワードクラウド")
                fig, ax=plt.subplots(figsize=(16,9))
                ax.imshow(wordcloud, interpolation="bilinear")
                ax.axis("off")
                st.pyplot(fig)

                status.update(label="求人情報の取得と可視化が完了しました", state="complete")