import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title('Prediksi Diabetes')

gender = st.text_input('Masukan Jenis Kelamin (0=Perempuan, 1=Laki-Laki)')

age = st.text_input('Masukan Usia')

hypertension = st.text_input('Hipertensi (0=Tidak, 1=Ya)')

heart_disease = st.text_input('Penyakit Jantung (0=Tidak, 1=Ya)')

smoking_history = st.text_input('Riwayat Meroko (0=Tidak Meroko, 1=Mantan Meroko, 2=Kadang Meroko, 3=Sering Meroko, 4=Tidak Diketahui )')

bmi = st.text_input('Indeks Masa Tubuh (BMI)')

HbA1c_level = st.text_input('Tingkat HbA1c')

blood_glucose_level = st.text_input('Kadar Gula Darah')

#code untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Cek Prediksi Diabetes'):
    diab_prediction = diabetes_model.percection([gender, age, hypertension, heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Terindikasi Terkena Diabetes'
    else : 
        diab_diagnosis = 'Tidak Terindikasi Terkena Diabetes'
    st.success(diab_diagnosis)
