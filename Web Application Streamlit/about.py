import streamlit as st

def app():
    st.markdown("""
        <h1>About Me</h1>
    """, unsafe_allow_html=True)
    # Profile Picture
    st.image("heroImage.png", width=200)
    
    # Introduction
    st.markdown("""

        Hi there! I am Naman Jain, currently pursuing my M.Tech in Data Science at Delhi Technological University, New Delhi. With a solid foundation in Computer Engineering from Arya College of Engineering and IT, Jaipur, I have developed a keen interest in machine learning, deep learning, and data analytics.

        My journey in the tech world includes practical experience as a Software Engineer at APBundle Technologies, where I honed my skills in ReactJS, NodeJS, and Redux, and as a Software Engineer Intern at WisdmLabs, focusing on PHP, WordPress, and MySQL. My technical expertise spans across various programming languages like Python, C++, and JavaScript, and I am proficient in using tools such as Docker, Git, and Power BI.

        In my latest project, "Machine Predictive Maintenance," I have utilized machine learning algorithms to predict machine failures and identify specific failure types. This project not only highlights my ability to develop robust machine learning models but also showcases my proficiency in data visualization and analytics using Streamlit and Power BI.


    """)

    # Project Background
    st.subheader("Project Background")
    st.markdown("""
    The **Machine Predictive Maintenance** project aims to predict machine failures and identify the type of failure, 
    enhancing operational efficiency and reducing downtime. This project utilizes various machine learning algorithms 
    including Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine to achieve high accuracy in predictions.
    """)

    # Technologies Used
    st.subheader("Technologies Used")
    st.markdown("""
    - **Programming Languages**: Python
    - **Libraries**: Pandas, NumPy, Scikit-learn, Streamlit
    - **Visualization Tools**: Matplotlib, Seaborn, Power BI
    - **Machine Learning Algorithms**: Logistic Regression, Decision Tree, Random Forest, Support Vector Machine
    """)

    # Contact Information
    st.subheader("Contact Information")
    st.markdown("""
    - **Email**: namanjn619@gmail.com
    - **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/namanjn619)
    - **GitHub**: [GitHub](https://github.com/namanjn619)
    """)

    
