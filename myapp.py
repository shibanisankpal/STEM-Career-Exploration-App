import streamlit as st

# Function to display career profiles
def display_career_profile():
    st.subheader("Career Profiles")
    
    careers = {
        "Software Engineer": "Software engineers design, develop, and test software applications. They work on a wide range of projects, from web applications to mobile apps and software systems.",
        "Data Scientist": "Data scientists analyze and interpret complex data to extract valuable insights. They use statistical techniques and machine learning algorithms to solve real-world problems.",
        "Biomedical Researcher": "Biomedical researchers conduct scientific studies to explore medical and biological phenomena. They contribute to advancements in healthcare and medical treatments.",
        "Civil Engineer": "Civil engineers design and oversee the construction of infrastructure projects, such as roads, bridges, buildings, and water systems.",
        "UX/UI Designer": "UX/UI designers focus on creating user-friendly and visually appealing digital experiences. They collaborate with development teams to enhance user satisfaction and usability.",
        "Environmental Scientist": "Environmental scientists study the environment and its interactions with human activities. They work to develop solutions for environmental issues and promote sustainable practices.",
        "Aerospace Engineer": "Aerospace engineers design and develop aircraft, spacecraft, and related systems. They conduct research to improve flight safety and efficiency.",
        "Biotechnology Researcher": "Biotechnology researchers work on cutting-edge projects to develop new drugs, therapies, and medical technologies. They combine biology and technology to address medical challenges.",
        "Network Security Specialist": "Network security specialists protect computer networks and systems from cyber threats. They implement security measures to safeguard sensitive data and prevent unauthorized access.",
        "Robotics Engineer": "Robotics engineers design and build robots for various applications, such as manufacturing, healthcare, and exploration. They focus on creating efficient and safe robotic systems."

    }
    
    selected_career = st.selectbox("Select a career:", list(careers.keys()))
    
    if selected_career:
        st.write(f"**{selected_career}**")
        st.write(careers[selected_career])


# Function to display skill assessment
def display_skill_assessment():

    # Define the quiz question and correct answer
    quiz_question = "What programming languages are commonly used in data analysis?"
    correct_answer = "Python"
    
    # Display the quiz question
    st.write(quiz_question)
    
    # Display multiple choice options
    options = ["Python", "Java", "C++", "Ruby"]
    selected_option = st.radio("Select an option:", options)
    
    # Check the answer
    if selected_option == correct_answer:
        st.write("Congratulations! Your answer is correct.")
    else:
        st.write("Sorry, your answer is incorrect. The correct answer is:", correct_answer)

# Function to display virtual job shadowing
def display_virtual_job_shadowing():
    st.subheader("Virtual Job Shadowing")
    
    st.write("Experience a day in the life of a Software Engineer:")
    st.write("Watch video interviews and demos from Software Engineers as they work on real-world projects.")
 
    # hyperlink to the video on YouTube
    video_url = "https://www.youtube.com/watch?v=1LSXEC0Clow&list=PL6qIzGkkiXFG-uelSxKpgSz4x3CYLc4DE&index=22"
    st.write(f"[Watch the video here]({video_url})")

    st.write("Video credit: [Indeed's YouTube Channel](https://www.youtube.com/user/IndeedJobs)")


# Function to display educational pathways
def display_educational_pathways():
    st.subheader("Educational Pathways")
    
    st.write("Explore various educational pathways to enter the field of Data Science:")
    st.write("- Bachelor's degree in Computer Science")
    st.write("- Master's degree in Data Science")
    st.write("- Online certifications in Machine Learning")

# Function to display mentorship connections
def display_mentorship_connections():
    st.subheader("Mentorship Connections")
    
    st.write("Connect with experienced professionals in the field of Data Science:")
    st.write("Find mentors who can guide you in your career and provide valuable insights.")

# Function to display industry insights and news
def display_industry_insights():
    st.subheader("Industry Insights and News")
    
    st.write("Stay up-to-date with the latest trends and advancements in Data Science:")
    st.write("Read articles, news, and case studies to gain insights into the industry.")

# Function to display networking and community
def display_networking_community():
    st.subheader("Networking and Community")
    st.write("Connect with fellow Data Science enthusiasts:")
    st.write("Join discussion forums, attend meetups, and collaborate on projects.")

# Function to display scholarships and internship opportunities
def display_scholarships_internships():
    st.subheader("Scholarships and Internships")
    # Add your code here to showcase scholarships and internships
    st.write("Explore scholarships and internship opportunities in Data Science:")
    st.write("Access information on available programs and application processes.")

# Main function
def main():
    # Set page title and layout
    st.set_page_config(page_title="STEM Career Exploration App", layout="wide")
    
    # Display app title and description
    st.title("STEM Career Exploration App")
    st.write("Explore various STEM career options and resources.")
    
    # sidebar menu for app navigation
    menu_options = {
        "Career Profiles": display_career_profile,
        "Skill Assessment": display_skill_assessment,
        "Virtual Job Shadowing": display_virtual_job_shadowing,
        "Educational Pathways": display_educational_pathways,
        "Mentorship Connections": display_mentorship_connections,
        "Industry Insights and News": display_industry_insights,
        "Networking and Community": display_networking_community,
        "Scholarships and Internships": display_scholarships_internships
    }
    menu_selection = st.sidebar.radio("Menu", list(menu_options.keys()))
    
    # Based on the menu selection, call the corresponding function
    menu_options[menu_selection]()

# Run the app
if __name__ == "__main__":
    main()
