import streamlit as st
from transformers import pipeline

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="Thai Question Answering App", page_icon="💬")

# ส่วนหัวข้อ (ตามแบบเป๊ะๆ)
st.markdown("## 💬 Thai Question Answering App")
st.write("ระบบตอบคำถามอัตโนมัติด้วยโมเดล WangchanBERTa (ภาษาไทย)")

# 2. โหลดโมเดล (ตามโจทย์ #Practice)
@st.cache_resource
def load_qa_model():
    # ใช้โมเดลตามที่กำหนดในสไลด์
    model_name = "airesearch/wangchanberta-base-wiki-20210520-spm-finetune-qa"
    return pipeline("question-answering", model=model_name)

qa_pipeline = load_qa_model()

# 3. ส่วนรับข้อมูลแบบ "ช่องเปล่า" (Empty Fields)
# ใช้ placeholder แทน value เพื่อให้เป็นช่องว่างแต่ยังมีคำแนะนำจางๆ
question = st.text_input("❓ คำถามของคุณ:", placeholder="พิมพ์คำถามที่นี่...")

context = st.text_area("📖 เนื้อหาหรือบริบท:", 
                       placeholder="วางเนื้อหาหรือบทความที่นี่เพื่อให้ AI หาคำตอบ...", 
                       height=200)

# 4. ปุ่มกดค้นหา
if st.button("🔍 หาคำตอบ"):
    if question and context:
        with st.spinner("กำลังหาคำตอบ..."):
            # ประมวลผล
            result = qa_pipeline(question=question, context=context)
            
            # 5. ส่วนแสดงผลคำตอบสีเขียว
            st.success("✅ คำตอบที่พบ:")
            st.write(result['answer'])
            
            # แสดงค่าความมั่นใจ
            st.write(f"**ความมั่นใจ:** {result['score']:.2f}")
    else:
        # แจ้งเตือนถ้าลืมกรอกข้อมูล
        st.warning("⚠️ กรุณากรอกทั้ง 'คำถาม' และ 'เนื้อหา' ก่อนกดปุ่ม")