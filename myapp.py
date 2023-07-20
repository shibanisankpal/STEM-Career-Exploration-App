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
    st.write("Watch a day in the life of a Software Engineer as she works on real-world projects.")
 
    # hyperlink to the video on YouTube
    video_url = "https://www.youtube.com/watch?v=1LSXEC0Clow&list=PL6qIzGkkiXFG-uelSxKpgSz4x3CYLc4DE&index=22"
    st.write(f"[Watch the video here]({video_url})")

    st.write("Video credit: [Indeed's YouTube Channel](https://www.youtube.com/user/IndeedJobs)")


# Function to display educational pathways
def display_educational_pathways():
    st.subheader("Educational Pathways")
    
    # Educational pathways
    careers_educational_pathways = {
        "Software Engineer": "Bachelor's degree in Computer Science or Software Engineering",
        "Data Scientist": "Bachelor's or Master's degree in Computer Science, Data Science, Statistics, or a related field",
        "Biomedical Researcher": "Bachelor's degree in Biology, Biochemistry, Biotechnology, or a related field",
        "Civil Engineer": "Bachelor's degree in Civil Engineering or a related field",
        "UX/UI Designer": "Bachelor's degree in Design, Interaction Design, or a related field",
        "Environmental Scientist": "Bachelor's degree in Environmental Science, Environmental Engineering, or a related field",
        "Aerospace Engineer": "Bachelor's degree in Aerospace Engineering or a related field",
        "Biotechnology Researcher": "Bachelor's or Master's degree in Biotechnology, Biochemistry, or a related field",
        "Network Security Specialist": "Bachelor's degree in Computer Science, Information Security, or a related field with a focus on network security",
        "Robotics Engineer": "Bachelor's or Master's degree in Robotics, Mechanical Engineering, or a related field with a focus on robotics and automation"
    }
    
    selected_career = st.selectbox("Select a career:", list(careers_educational_pathways.keys()))
    
    if selected_career:
        st.write(f"**{selected_career}**")
        st.write(careers_educational_pathways[selected_career])


# Function to display mentorship connections
def display_mentorship_connections():
    st.subheader("Mentorship Connections")
    st.write("Connect with experienced professionals in your field of interest:")
    st.write("Find mentors who can guide you in your career and provide valuable insights.")
    
    # Fake mentors with diverse representation for different roles
    mentors_by_role = {
        "Software Engineer": [
            {"name": "Emily Johnson", "title": "Senior Software Engineer at TechGenius"},
            {"name": "Alex Williams", "title": "Lead Software Developer at InnovateTech"},
            {"name": "Jennifer Lee", "title": "Full Stack Engineer at CodeCrafters"},
            {"name": "Michael Chen", "title": "Software Architect at DataTech Solutions"},
            {"name": "Sarah Taylor", "title": "Software Engineer at Innovators Corp"},
            {"name": "Rahul Gupta", "title": "Software Engineer at SoftTech Solutions"},
            {"name": "Ananya Patel", "title": "Software Developer at InnovateMinds"}
        ],
        "Data Scientist": [
            {"name": "Dr. Sarah Thompson", "title": "Data Science Manager at InsightAnalytics"},
            {"name": "Rachel Liu", "title": "Machine Learning Engineer at AI Innovations"},
            {"name": "Jessica Adams", "title": "Data Analyst at DataMinds Co."},
            {"name": "Daniel Wilson", "title": "Senior Data Scientist at TechData Labs"},
            {"name": "Maria Sanchez", "title": "Data Scientist at TechnoAnalytica"},
            {"name": "Ankit Sharma", "title": "Data Scientist at DataGenius"},
            {"name": "Priya Patel", "title": "Machine Learning Specialist at AIInnovations"}
        ],
        "Biomedical Researcher": [
            {"name": "Dr. Emily Roberts", "title": "Research Scientist at BioTechResearch"},
            {"name": "Sophia Zhang", "title": "Biotechnology Consultant at BiotechSolutions"},
            {"name": "Robert Johnson", "title": "Medical Researcher at HealthDiscoveries"},
            {"name": "Olivia Lee", "title": "Biomedical Engineer at BiomedTech Innovations"},
            {"name": "Linda Patel", "title": "Biomedical Research Associate at HealthGenetics"},
            {"name": "Aryan Sharma", "title": "Biomedical Research Scientist at BioTechSolutions"},
            {"name": "Neha Gupta", "title": "Biotechnology Researcher at BioGenius"}
        ],
        "Civil Engineer": [
            {"name": "David Chen", "title": "Senior Civil Engineer at BuildItRight Construction"},
            {"name": "Jennifer Wang", "title": "Structural Engineer at ConstructTech"},
            {"name": "Andrew Smith", "title": "Transportation Engineer at UrbanInfra"},
            {"name": "Ella Brown", "title": "Environmental Engineer at GreenBuild Solutions"},
            {"name": "Maria Rodriguez", "title": "Civil Engineer at CivilTech Group"},
            {"name": "Rahul Gupta", "title": "Civil Engineer at UrbanPlanners"}
        ],
        "UX/UI Designer": [
            {"name": "Sophie Johnson", "title": "Senior UX Designer at DigitalDesign Studio"},
            {"name": "Emma Roberts", "title": "Product Designer at UserExperience Labs"},
            {"name": "Grace Chen", "title": "UI/UX Architect at WebCrafters"},
            {"name": "Julia Lee", "title": "Interaction Designer at UXInnovations"},
            {"name": "Linda Patel", "title": "UX Designer at DesignSolutions"},
            {"name": "Ananya Patel", "title": "UX/UI Designer at CreativeMinds"}
        ],
        "Environmental Scientist": [
            {"name": "Dr. Samantha Adams", "title": "Environmental Researcher at EarthScience Institute"},
            {"name": "Lucas Wilson", "title": "Sustainability Consultant at GreenTech Solutions"},
            {"name": "Sophia Brown", "title": "Conservation Scientist at NatureAware"},
            {"name": "Oliver Zhang", "title": "Environmental Engineer at EcoTech Innovations"},
            {"name": "Maria Lopez", "title": "Environmental Analyst at EcoSolutions"},
            {"name": "Aryan Sharma", "title": "Environmental Scientist at GreenEarth Research"}
        ],
        "Aerospace Engineer": [
            {"name": "Dr. Christopher Johnson", "title": "Aerospace Engineering Manager at AeroTech Innovations"},
            {"name": "Sarah Lee", "title": "Aircraft Systems Engineer at SkyWings Aerospace"},
            {"name": "Kevin Chen", "title": "Spacecraft Designer at SpaceTech Solutions"},
            {"name": "Isabella Smith", "title": "Aerospace Testing Engineer at AeroLabs"},
            {"name": "Juan Martinez", "title": "Aerospace Researcher at AeroInnovations"},
            {"name": "Rahul Gupta", "title": "Aerospace Engineer at SpaceFlight Technologies"}
        ],
        "Biotechnology Researcher": [
            {"name": "Dr. Laura Roberts", "title": "Senior Biotechnology Researcher at BioTechDiscoveries"},
            {"name": "Sophia Johnson", "title": "Biotechnology Analyst at BioTechSolutions"},
            {"name": "Robert Lee", "title": "Biomedical Engineering Specialist at BiomedTech Innovations"},
            {"name": "Jessica Adams", "title": "Research Scientist at BioInnovate Labs"},
            {"name": "Maria Lopez", "title": "Biotechnology Consultant at BioTechExperts"},
            {"name": "Aryan Sharma", "title": "Biotechnology Researcher at BiotechInnovations"}
        ],
        "Network Security Specialist": [
            {"name": "Sarah Chen", "title": "Cybersecurity Analyst at SecureTech Solutions"},
            {"name": "David Wilson", "title": "Network Security Engineer at CyberGuardians"},
            {"name": "Emily Johnson", "title": "Information Security Specialist at InfoSec Group"},
            {"name": "Michael Brown", "title": "Security Solutions Architect at SecureData Systems"},
            {"name": "Juan Martinez", "title": "Cybersecurity Consultant at CyberDefenders"},
            {"name": "Ananya Patel", "title": "Network Security Specialist at CyberSecurity Solutions"}
        ],
        "Robotics Engineer": [
            {"name": "Dr. Sophia Zhang", "title": "Robotics Research Scientist at RoboTech Labs"},
            {"name": "John Lee", "title": "Robotics Systems Engineer at AI Robotics"},
            {"name": "Oliver Smith", "title": "Autonomous Robotics Specialist at RoboInnovations"},
            {"name": "Julia Roberts", "title": "AI and Robotics Developer at RoboGenius"},
            {"name": "Maria Lopez", "title": "Robotics Programmer at RoboTech Solutions"},
            {"name": "Rahul Gupta", "title": "Robotics Engineer at RoboTech Innovations"}
        ]
    }
    
    st.write(" ")
    st.write("Select your preferred role to find mentors:")
    selected_role = st.selectbox("Select a role:", list(mentors_by_role.keys()))
    
    if selected_role:
        st.write(f"**Mentors for {selected_role}:**")
        for mentor in mentors_by_role[selected_role]:
            st.write(f"- {mentor['name']}, {mentor['title']}")


# Function to display industry insights and news
def display_industry_insights():
    st.subheader("Industry Insights and News")
    
    st.write("Stay up-to-date with the latest trends and advancements in Data Science:")
    st.write("Read articles, news, and case studies to gain insights into the industry.")

# Function to display networking and community
def display_networking_community():
    st.subheader("Networking and Community")
    st.write("Connect with fellow enthusiasts:")
    st.write("Join groups, attend meetups, and collaborate on projects.")
    

    # Formal and empowering meetup groups for various roles
    meetup_groups = {
        "Software Engineer": [
            "CodeQueens Meetup",
            "TechLadies Network",
            "DevDivas Collective",
            "CodeCrafters Community"
        ],
        "Data Scientist": [
            "DataDivas Meetup",
            "AnalyticsQueens Group",
            "MLWonderWomen Network",
            "DataMavens Community"
        ],
        "Biomedical Researcher": [
            "BioTechLadies Meetup",
            "MedicalWonders Network",
            "BioInnovators Collective",
            "ResearchRocks Community"
        ],
        "Civil Engineer": [
            "CivilQueens Meetup",
            "BuildHerBetter Group",
            "StructuraDivas Network",
            "CivilSuperwomen Community"
        ],
        "UX/UI Designer": [
            "UXSheDesigners Meetup",
            "VisualMavens Network",
            "DesignWonders Collective",
            "UXUIQueens Community"
        ],
        "Environmental Scientist": [
            "EcoLadies Meetup",
            "SustainableSTEM Network",
            "GreenInnovators Collective",
            "EcoWarriorWomen Community"
        ],
        "Aerospace Engineer": [
            "AeroWonders Meetup",
            "SkyHighSTEM Group",
            "SpaceExplorers Network",
            "AeroAmazons Community"
        ],
        "Biotechnology Researcher": [
            "BioTechQueens Meetup",
            "BioGenius Network",
            "BioInnovators Collective",
            "BioTechAmazons Community"
        ],
        "Network Security Specialist": [
            "SecureSheNetworks Meetup",
            "CyberGuardians Group",
            "SecurityWonders Network",
            "SecureSTEMQueens Community"
        ],
        "Robotics Engineer": [
            "RobotTechLadies Meetup",
            "RoboWonderWomen Group",
            "AIandBots Network",
            "RobotSTEMQueens Community"
        ]
    }
    
    st.write(" ")
    st.write("**Discussion Groups for Various STEM Roles:**")

    selected_role = st.selectbox("Select a role:", list(meetup_groups.keys()))
    
    if selected_role:
        st.write(f"**{selected_role}:**")
        for meetup in meetup_groups[selected_role]:
            st.write(f"- {meetup}")



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
