import streamlit as st 
st.markdown("# :red [🏋️แอปพลิเคชั่นคำนวนค่าดัชนีมวลกาย BMI]")
st.write("💵กรอกข้อมูลน้ำหนักส่วนสูงของคุณเพื่อเช็คสุขภาพเบื้องต้น")

weight = st.number_input ("กรอกน้ำหนักของคุณ (กิโลกรัม) : ")
hight_cm = st.number_input ("กรอกส่วนสู.ของคุณ (เซนติเมตร) :  ")

if st.button("คำนวนค่า BMI "):
    height_m = hight_cm / 100
    bmi = weight / (height_m ** 2)


    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ : **{bmi:.2f}**")

if bmi < 18.5:
   st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0: 
   st.succees("🎉คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif 23.0 <- bmi < 25.0: 
   st.info("💡คุณมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
   st.error(" 🚨คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพเเเละออกกำลังกาย")


st.divider()
st.write("นายบรรพรต ทางศรี ม.4/6 เลขที่ 4")
