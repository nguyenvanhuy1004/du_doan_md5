import streamlit as st
import hashlib

def tinh_tong_md5(md5_str):
    so = [int(md5_str[i:i+2], 16) for i in range(0, 30, 2)]
    tong = sum(so)
    return tong

def du_doan_tai_xiu(tong):
    return "Tài" if tong >= 100 else "Xỉu"

st.title("🔮 Dự đoán Tài/Xỉu từ mã MD5")
md5_input = st.text_input("Nhập mã MD5 (32 ký tự):")

if len(md5_input) == 32:
    tong = tinh_tong_md5(md5_input)
    ket_qua = du_doan_tai_xiu(tong)
    st.success(f"Tổng = {tong} → Dự đoán: {ket_qua}")
else:
    st.warning("Vui lòng nhập đúng 32 ký tự mã MD5.")
