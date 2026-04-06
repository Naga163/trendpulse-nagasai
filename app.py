import streamlit as st   # 👈 FIRST

st.set_page_config(
    page_title="TrendPulse Dashboard",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 👇 THEN your existing imports
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="TrendPulse Dashboard", layout="wide")

st.title("TrendPulse Dashboard")
st.caption("What's Actually Trending Right Now")

# Load analysed data
df = pd.read_csv("data/trends_analysed.csv")

# KPI values
total_posts = len(df)
avg_score = round(df["score"].mean(), 2)
avg_comments = round(df["num_comments"].mean(), 2)
top_category = df["category"].value_counts().idxmax()

# KPI row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Posts", total_posts)
col2.metric("Average Score", avg_score)
col3.metric("Average Comments", avg_comments)
col4.metric("Top Category", top_category)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Posts per Category")
    category_counts = df["category"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    category_counts.plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Number of Posts")
    ax1.set_title("Posts per Category")
    st.pyplot(fig1)

with right:
    st.subheader("Score vs Comments")
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    ax2.scatter(df["num_comments"], df["score"])
    ax2.set_xlabel("Number of Comments")
    ax2.set_ylabel("Score")
    ax2.set_title("Score vs Comments")
    st.pyplot(fig2)

st.divider()

st.subheader("Top 10 Trending Posts by Score")
top_posts = df.sort_values(by="score", ascending=False).head(10)

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.barh(top_posts["title"], top_posts["score"])
ax3.set_xlabel("Score")
ax3.set_ylabel("Post Title")
ax3.set_title("Top 10 Trending Posts by Score")
ax3.invert_yaxis()
plt.tight_layout()
st.pyplot(fig3)

st.divider()
st.subheader("Dataset Preview")
st.dataframe(df)
