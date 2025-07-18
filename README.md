# afzal-portfolio

This is my personal portfolio website built using Flask (Python) and TailwindCSS. It shows my skills, projects, certificates, blog, and a contact form.

 Live Website  https://afzal-portfolio.onrender.com
 View Portfolio on Render

 Technologies Used
Frontend: HTML, TailwindCSS, JavaScript, Flowbite/DaisyUI

Backend: Flask (Python), Jinja2

Deployment: Render

Other Tools: Git, GitHub

#Features
Animated homepage with profile and social links

Projects section with interactive cards

About, Skills, Tools, and Certificates sections

Blog page

Contact form (prints message to console)

Resume download option

# Folder Structure
csharp
Copy
Edit
afzal-portfolio/
├── app.py
├── requirements.txt
├── render.yaml
├── routes/
│   └── main.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── blog.html
├── static/
│   └── assets/
└── README.md


Run Locally
bash
Copy
Edit
git clone https://github.com/Afzal1222khan/afzal-portfolio.git
cd afzal-portfolio
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
Then open http://localhost:5000 in your browser.


