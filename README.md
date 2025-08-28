# 🌍 Tripplaner  

> Jobs fill your pockets, but adventures fill your soul ✨  

**Tripplaner** is a travel website built with **Django, HTML, and CSS** that helps users explore the world and plan adventures.  

---

## 🚀 Features
- 🗺️ Explore destinations with beautiful UI  
- 🔑 User authentication (Login/Signup)  
- 📱 Responsive design  
- ⚡ Built with Django, HTML, and CSS  

---

## 🛠️ Tech Stack
- [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)  
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)  
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)  

---

## 📂 Project Structure
Tripplaner/
├── Tripplaner/ # Django project folder (settings, urls, wsgi)
├── Website/ # Main app
│ ├── migrations/
│ ├── static/ # CSS, images
│ ├── templates/ # HTML templates
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── signup.html
│ │ └── ...
│ ├── views.py
│ ├── models.py
│ └── ...
├── db.sqlite3 # Database
├── manage.py
└── requirements.txt

---

## 📸 Screenshot
![Tripplaner Screenshot](./Website/static/img/screenshot.png)

---

## ⚡ Setup Instructions
1. Clone this repo  
   ```bash
   git clone https://github.com/your-username/tripplaner.git
   cd tripplaner
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   http://127.0.0.1:8000/
---

## 📌 Author
👤 **S. Balamurugan**  


