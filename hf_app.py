import streamlit as st
from transformers import pipeline

# โหลดโมเดลจาก Hugging Face
@st.cache_resource  # เพื่อไม่ต้องโหลดใหม่ทุกครั้ง
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="poom-sci/WangchanBERTa-finetuned-sentiment"
    )

classifier = load_model()

# ส่วนของหน้าเว็บ

st.title("🔍 Thai Sentiment Analysis App")
st.write("วิเคราะห์ความคิดเห็นด้วยโมเดล WangchanBERTa")
#ตกแต่งหน้าจอด้วย css ในส่วนของข้อความใน text input
st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    font-family: "Prompt", sans-serif;
}
</style>
""", unsafe_allow_html=True)

# รับข้อมูลจากผู้ใช้
user_input = st.text_input("พิมพ์ข้อความภาษาไทยที่นี่:", "อาหารร้านนี้อร่อยมาก")

if st.button("วิเคราะห์ความรู้สึก"):
    if user_input.strip() == "":
        st.warning("กรุณาใส่ข้อความที่ต้องการวิเคราะห์ความรู้สึก")
    else:
        result = classifier(user_input)
        label = result[0]['label']
        score = result[0]['score']

        st.write("**ผลการวิเคราะห์ความรู้สึก :**", label)
        st.write("**ค่าความมั่นใจ:**", f"{score:.2f}")
