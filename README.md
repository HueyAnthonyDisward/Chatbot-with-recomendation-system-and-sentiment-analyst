# 📖 Dự án Cuối Kỳ - Môn Xử lý Ngôn ngữ Tự nhiên (NLP) 2024-2025

## 📝 Giới thiệu
Dự án cuối kỳ môn học **Xử lý Ngôn ngữ Tự nhiên (NLP)** trong học kỳ 2, năm học 2024-2025. Dự án tập trung vào việc xây dựng một **chatbot tư vấn mua hàng**, tích hợp hệ thống khuyến nghị thông minh để gợi ý sản phẩm phù hợp cho người dùng. Ngoài ra, dự án còn bao gồm phân tích cảm xúc dựa trên phản hồi và bình luận, cùng với một **trang chủ web thương mại điện tử** được phát triển bằng **Django**.

### 📂 Cấu trúc thư mục
- **dataset**: Chứa các tập dữ liệu, cùng các thao tác tiền xử lý và làm sạch dữ liệu.
- **collaborative recommendations**: Thư mục chứa phương pháp xây dựng hệ khuyến nghị dựa trên cảm xúc từ bình luận và điểm đánh giá.
- **sentiment**: Thư mục thực hiện phân tích cảm xúc từ dữ liệu người dùng.
- **sentiment_user**: Thư mục nhận diện cảm xúc của người dùng.
- **Web**: Thư mục chính chứa mã nguồn của chatbot và trang chủ sản phẩm bán hàng.

## 🚀 Yêu cầu
Để chạy dự án, đảm bảo máy đã cài đặt **Django** cùng với các thư viện Python sau:

### 📦 1. Thư viện chuẩn của Python (Standard Library)
- `json`
- `re`
- `pathlib.Path`

### 📊 2. Xử lý dữ liệu & mô hình
- `pandas` as `pd`
- `joblib`
- `pickle`
- `sklearn.metrics.pairwise.cosine_similarity`

### 🧠 3. Xử lý ngôn ngữ tự nhiên (NLP)
- `spacy`

### 🌍 4. Django (Framework Web)
- `from django.shortcuts import render`
- `from django.http import JsonResponse`
- `from django.views.decorators.csrf import csrf_exempt`
- `from .models import ChatMessage`
- `from django.db.models import Count`

## 🛠️ Cài đặt
1. Đảm bảo đã cài đặt **Python** (phiên bản 3.8 trở lên khuyến nghị).
2. Cài đặt các thư viện cần thiết bằng lệnh:
   ```bash
   pip install django pandas joblib scikit-learn spacy
   ```
3. Cài đặt mô hình ngôn ngữ cho `spacy` (ví dụ: mô hình tiếng Việt hoặc tiếng Anh):
   ```bash
   python -m spacy download en_core_web_sm  # Hoặc mô hình phù hợp
   ```

## ▶️ Cách chạy
1. Vào thư mục **Web**.
2. Mở terminal và chạy lệnh:
   ```bash
   python manage.py runserver
   ```
3. Truy cập trang web tại địa chỉ được hiển thị (ví dụ: `http://127.0.0.1:8000`).

## ⚠️ Lưu ý
- Đảm bảo tất cả thư viện đã được cài đặt trước khi chạy.
- Nếu gặp lỗi, kiểm tra lại cấu hình Django hoặc các mô hình `spacy`.

## 📧 Liên hệ
Nếu có vấn đề hoặc thắc mắc, vui lòng nhắn tin qua email:  
Email: hieuanthonydisward@gmail.com

## 🔗 Link dự án
[https://github.com/HueyAnthonyDisward/Chatbot-with-recomendation-system-and-sentiment-analyst](https://github.com/HueyAnthonyDisward/Chatbot-with-recomendation-system-and-sentiment-analyst)

---

# 📚 Final Project - Natural Language Processing (NLP) Course 2024-2025

## 📝 Overview
This is the final project for the **Natural Language Processing (NLP)** course in Semester 2 of the 2024-2025 academic year. The project focuses on developing a **shopping advisory chatbot**, integrated with a smart recommendation system to suggest suitable products for users. Additionally, it includes sentiment analysis based on feedback and comments, along with a **e-commerce website homepage** built using **Django**.

### 📂 Folder Structure
- **dataset**: Contains datasets along with data preprocessing and cleaning operations.
- **collaborative recommendations**: Folder with methods for building a recommendation system based on sentiment from comments and ratings.
- **sentiment**: Folder for sentiment analysis from user data.
- **sentiment_user**: Folder for user sentiment recognition.
- **Web**: Main folder containing the chatbot and product sales homepage code.

## 🚀 Requirements
To run the project, ensure that **Django** and the following Python libraries are installed:

### 📦 1. Python Standard Library
- `json`
- `re`
- `pathlib.Path`

### 📊 2. Data Processing & Modeling
- `pandas` as `pd`
- `joblib`
- `pickle`
- `sklearn.metrics.pairwise.cosine_similarity`

### 🧠 3. Natural Language Processing (NLP)
- `spacy`

### 🌍 4. Django (Web Framework)
- `from django.shortcuts import render`
- `from django.http import JsonResponse`
- `from django.views.decorators.csrf import csrf_exempt`
- `from .models import ChatMessage`
- `from django.db.models import Count`

## 🛠️ Installation
1. Ensure **Python** is installed (version 3.8 or higher recommended).
2. Install the required libraries with the command:
   ```bash
   pip install django pandas joblib scikit-learn spacy
   ```
3. Install a language model for `spacy` (e.g., English or Vietnamese model):
   ```bash
   python -m spacy download en_core_web_sm  # Or a suitable model
   ```

## ▶️ How to Run
1. Navigate to the **Web** folder.
2. Open a terminal and run the command:
   ```bash
   python manage.py runserver
   ```
3. Access the website at the displayed address (e.g., `http://127.0.0.1:8000`).

## ⚠️ Notes
- Ensure all libraries are installed before running.
- If errors occur, check Django configuration or `spacy` models.

## 📧 Contact
For any issues or inquiries, please reach out via email:  
Email: hieuanthonydisward@gmail.com

## 🔗 Project Link
[https://github.com/HueyAnthonyDisward/Chatbot-with-recomendation-system-and-sentiment-analyst](https://github.com/HueyAnthonyDisward/Chatbot-with-recomendation-system-and-sentiment-analyst)
