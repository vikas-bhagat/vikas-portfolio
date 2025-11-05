import streamlit as st
from PIL import Image
from base64 import b64encode

# ----------------- PAGE SETTINGS -----------------
st.set_page_config(
    page_title="Vikas Bhagat | Business & Data Analyst Portfolio",
    page_icon="💼",
    layout="wide"
)

# ----------------- BACKGROUND + NAVBAR STYLE -----------------
st.markdown("""
<style>
@keyframes gradientMove {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

[data-testid="stAppViewContainer"] {
  background: linear-gradient(-45deg, #d7e1ec, #ffffff, #e3f2fd, #d7e1ec);
  background-size: 400% 400%;
  animation: gradientMove 12s ease infinite;
  font-family: 'Segoe UI', sans-serif;
  padding: 0px !important;
}

[data-testid="stHeader"], [data-testid="stToolbar"] {
  background: rgba(0,0,0,0);
}

.navbar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
  background-color: rgba(255,255,255,0.9);
  padding: 12px;
  border-radius: 12px;
  margin: 10px auto 30px auto;
  max-width: 95%;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.navbar a {
  text-decoration: none;
  color: #003366;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 8px;
  transition: 0.3s;
}

.navbar a:hover {
  background-color: #003366;
  color: white;
}

.section {
  background-color: white;
  padding: 25px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  margin: 20px auto;
  width: 90%;
  max-width: 900px;
}

@media (max-width: 768px) {
  .section {
    padding: 18px;
  }
}
</style>
""", unsafe_allow_html=True)

# ----------------- FONT FIX (FOR MOBILE + DESKTOP) -----------------
st.markdown("""
<style>
html, body, [class*="css"]  {
  color: #002244 !important;
  font-size: 17px !important;
  line-height: 1.6em;
}

@media (max-width: 768px) {
  html, body, [class*="css"]  {
    font-size: 15px !important;
  }
  h1, h2, h3, h4 {
    color: #001d3d !important;
    font-weight: 600 !important;
    line-height: 1.3em !important;
  }
  p, li {
    color: #002855 !important;
  }
}

.section * {
  color: #002244 !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------- NAVBAR -----------------
st.markdown("""
<div class='navbar'>
  <a href='#home'>Home</a>
  <a href='#about'>About</a>
  <a href='#skills'>Skills</a>
  <a href='#projects'>Projects</a>
  <a href='#education'>Education</a>
  <a href='#certifications'>Certifications</a>
  <a href='#resume'>Resume</a>
  <a href='#contact'>Contact</a>
</div>
""", unsafe_allow_html=True)

# ----------------- IMAGE BASE64 FUNCTION -----------------
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return b64encode(data).decode()

img_base64 = get_base64_image("linkedin photo 1.png")

# ----------------- HOME SECTION -----------------
st.markdown(f"""
<style>
#home {{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 30px 20px;
}}

#home img {{
  border-radius: 50%;
  width: 230px;
  height: 230px;
  object-fit: cover;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  margin-bottom: 20px;
}}

@media (max-width: 768px) {{
  #home img {{
    width: 180px;
    height: 180px;
  }}
}}
</style>

<div id="home">
  <img src="data:image/png;base64,{img_base64}" alt="Vikas Bhagat">
  <h1 style="color:#003366;">Vikas Bhagat</h1>
  <h3 style="color:#444;">Final Year BCA Student | Aspiring Business & Data Analyst</h3>
  <p style="max-width:650px; color:#333;">Driven and analytical professional skilled in <b>Power BI, Excel, SQL, Python, and Tableau</b>, focused on transforming data into business insights.</p>
</div>
""", unsafe_allow_html=True)

# ----------------- ABOUT SECTION -----------------
st.markdown("<div id='about' class='section'>", unsafe_allow_html=True)
st.header("👨‍💼 About Me")
st.write("""
Hello! I'm *Vikas Bhagat, currently pursuing **Bachelor of Computer Applications (Final Year)*.  
I have a deep interest in *Business Analytics* and enjoy building dashboards, analyzing datasets, and helping businesses make *data-driven decisions*.  
I combine logical thinking with creativity to turn raw data into meaningful insights.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- SKILLS -----------------
st.markdown("<div id='skills' class='section'>", unsafe_allow_html=True)
st.header("💡 Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    - 🐍 Python (Data Handling, Data Analysis)
    - 💾 SQL (Joins, Queries, Subqueries)
    - 📊 Power BI (DAX, KPI Dashboarding)
    - 📗 Excel (Pivot Tables, Charts)
    """)
with col2:
    st.markdown("""
    - 📉 Tableau (Storytelling Dashboards)
    - 🧹 Data Cleaning & Analysis
    - 🧠 Business Decision Making
    - 💬 Communication & Collaboration
    """)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- PROJECTS -----------------
st.markdown("<div id='projects' class='section'>", unsafe_allow_html=True)
st.header("📂 Projects")
st.markdown("""
### 🏦 Banking Stakeholder Dashboard (Tableau)
Interactive Tableau Dashboard for banking stakeholders to track loan performance, customer engagement, and branch profitability.  
*Tools:* Tableau, Excel  
*Skills:* Data Visualization, Storytelling, Business Analytics  

---

### 🛒 E-Commerce Sales Dashboard (Power BI)
Advanced Power BI dashboard for sales and profit analysis across regions and product categories.  
*Tools:* Power BI, SQL  
*Skills:* DAX, Data Modelling, KPI Insights  

---

### 📈 Regional Sales Performance (Excel + Power BI)
Performed regional-level sales analysis using Excel and visualized results using Power BI to highlight growth trends.  
*Tools:* Excel, Power BI  
*Skills:* Data Analysis, Reporting, Business Insights
""")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- EDUCATION -----------------
st.markdown("<div id='education' class='section'>", unsafe_allow_html=True)
st.header("🎓 Education")
st.write("""
*Bachelor of Computer Applications (BCA)*  
Yashwantrao Chavan Maharashtra Open University | Final Year (2023–26)  
*CGPA:* 7.64 / 10  
""")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- CERTIFICATIONS -----------------
st.markdown("<div id='certifications' class='section'>", unsafe_allow_html=True)
st.header("📜 Certifications")
st.write("""
- Data Analytics with Excel – Simplilearn  
- Power BI Masterclass – Workshop  
- Data Analytics – LearnTube  
- English Communication – Speakwell Academy  
""")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- RESUME -----------------
st.markdown("<div id='resume' class='section'>", unsafe_allow_html=True)
st.header("📄 Resume")
with open("RESUME VIKAS.docx", "rb") as file:
    st.download_button(
        label="⬇ Download My Resume",
        data=file,
        file_name="Vikas_Bhagat_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- CONTACT -----------------
st.markdown("<div id='contact' class='section'>", unsafe_allow_html=True)
st.header("📞 Contact Me")
st.write("""
📧 *Email:* [vikasbhagat3011@gmail.com](mailto:vikasbhagat3011@gmail.com)  
📍 *Location:* Badlapur, Maharashtra  
🔗 *LinkedIn:* [linkedin.com/in/vikasbhagat](https://linkedin.com)  
📱 *Phone:* +91 9960143420  
""")
# ----------------- FIX DOWNLOAD BUTTON COLOR (MOBILE FRIENDLY) -----------------
st.markdown("""
<style>
div.stDownloadButton > button {
    background: linear-gradient(90deg, #004080, #0073e6);
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    padding: 12px 28px !important;
    border: none !important;
    font-size: 16px !important;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    transition: 0.3s ease-in-out;
}
div.stDownloadButton > button:hover {
    background: linear-gradient(90deg, #0059b3, #339cff);
    transform: scale(1.05);
}
@media (max-width: 600px) {
    div.stDownloadButton > button {
        font-size: 15px !important;
        padding: 10px 22px !important;
        background: linear-gradient(90deg, #0059b3, #33adff);
        color: #ffffff !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------- FOOTER -----------------
st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2025 Vikas Bhagat | Built with ❤ using Python & Streamlit</p>", unsafe_allow_html=True)