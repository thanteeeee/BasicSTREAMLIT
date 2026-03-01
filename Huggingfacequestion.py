import streamlit as st
from transformers import pipeline

# 1. ตั้งค่าหน้าจอและหัวข้อ (ตามแบบในรูปตัวอย่าง)
st.set_page_config(page_title="Thai QA App", page_icon="💬")

# ส่วนหัวข้อพร้อมไอคอน
st.markdown("# 💬 Thai Question Answering App")
st.write("ระบบตอบคำถามอัตโนมัติด้วยโมเดล WangchanBERTa (ภาษาไทย)")

# 2. ฟังก์ชันโหลดโมเดล WangchanBERTa (ตามโจทย์ที่กำหนด)
@st.cache_resource
def load_qa_model():
    # โมเดลจากรูปที่ระบุในโจทย์ #Practice
    model_name = "airesearch/wangchanberta-base-wiki-20210520-spm-finetune-qa"
    return pipeline("question-answering", model=model_name)

# เรียกใช้ pipeline
qa_pipeline = load_qa_model()

# 3. ส่วนรับข้อมูล (Input) พร้อมไอคอนด้านหน้า
question = st.text_input("❓ คำถามของคุณ:", value="ปราจีนบุรีมีมรดกโลกกี่แห่ง")

context = st.text_area("📖 เนื้อหาหรือบริบท:", 
                       value="""ปราจีนบุรี (เดิมสะกดว่า ปราจิณบุรี) เป็นจังหวัดในภาคตะวันออกของประเทศไทย เป็นเมืองที่มีประวัติศาสตร์ยาวนาน มีการพบซากโบราณสถานในหลายพื้นที่ของจังหวัด นอกจากนี้ ยังมีแหล่งท่องเที่ยวทางธรรมชาติหลายแห่ง มีมรดกโลกทางธรรมชาติคือพื้นที่กลุ่มป่าดงพญาเย็น-เขาใหญ่""", 
                       height=200)

# 4. ปุ่มกดค้นหา
if st.button("🔍 หาคำตอบ"):
    if question and context:
        with st.spinner("กำลังหาคำตอบ..."):
            # ประมวลผล
            result = qa_pipeline(question=question, context=context)
            
            # 5. ส่วนแสดงผลคำตอบ (ไฮไลท์สีเขียวตามรูปตัวอย่าง)
            st.success("✅ คำตอบที่พบ:")
            
            # แสดงข้อความคำตอบ
            st.write(result['answer'])
            
            # แสดงค่าความมั่นใจ (Score)
            st.write(f"**ความมั่นใจ:** {result['score']:.2f}")
    else:
        st.warning("กรุณากรอกทั้งคำถามและเนื้อหา")