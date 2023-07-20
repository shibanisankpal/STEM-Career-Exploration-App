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




# Function to display virtual job shadowing
def display_virtual_job_shadowing():
    st.subheader("Virtual Job Shadowing")
    
    st.write("Experience a day in the life of a Software Engineer:")
    st.write("Watch a day in the life of a Software Engineer as she works on real-world projects.")
 
    # hyperlink to the video on YouTube
    video_url = "https://www.youtube.com/watch?v=1LSXEC0Clow&list=PL6qIzGkkiXFG-uelSxKpgSz4x3CYLc4DE&index=22"
    st.write(f"[Watch the video here]({video_url})")

    st.write("Video credit: [Indeed's YouTube Channel](https://www.youtube.com/user/IndeedJobs)")
import streamlit as st

# Function to display skill assessment for Software Engineer role
def skill_assessment_software_engineer():
    st.write("Skill Assessment for Software Engineer")
    st.write("1. Which programming language is commonly used for web development?")
    st.write("   a) Python")
    st.write("   b) JavaScript")
    st.write("   c) Java")
    st.write("   d) C++")
    correct_answer_q1 = "b"

    st.write("2. What is version control used for in software development?")
    st.write("   a) Managing project timelines")
    st.write("   b) Tracking changes in code")
    st.write("   c) Generating test cases")
    st.write("   d) Designing user interfaces")
    correct_answer_q2 = "b"

    st.write("3. Which database system is known for its scalability and high availability?")
    st.write("   a) MySQL")
    st.write("   b) SQLite")
    st.write("   c) MongoDB")
    st.write("   d) PostgreSQL")
    correct_answer_q3 = "d"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Data Scientist role
def skill_assessment_data_scientist():
    st.write("Skill Assessment for Data Scientist")
    st.write("1. What is the primary goal of data cleaning in the data science process?")
    st.write("   a) Reduce the size of the dataset")
    st.write("   b) Prepare data for visualization")
    st.write("   c) Ensure data is accurate and consistent")
    st.write("   d) Combine data from different sources")
    correct_answer_q1 = "c"

    st.write("2. Which machine learning algorithm is used for classification problems?")
    st.write("   a) K-Means")
    st.write("   b) Decision Trees")
    st.write("   c) Linear Regression")
    st.write("   d) Principal Component Analysis (PCA)")
    correct_answer_q2 = "b"

    st.write("3. What is the process of feeding labeled data to a machine learning algorithm for training?")
    st.write("   a) Feature engineering")
    st.write("   b) Model validation")
    st.write("   c) Model evaluation")
    st.write("   d) Supervised learning")
    correct_answer_q3 = "d"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Biomedical Researcher role
def skill_assessment_biomedical_researcher():
    st.write("Skill Assessment for Biomedical Researcher")
    st.write("1. What is a common technique used to study biological molecules?")
    st.write("   a) Polymerase Chain Reaction (PCR)")
    st.write("   b) Regression Analysis")
    st.write("   c) Network Security")
    st.write("   d) Data Visualization")
    correct_answer_q1 = "a"

    st.write("2. What is the primary goal of biomedical research?")
    st.write("   a) Develop new software applications")
    st.write("   b) Improve healthcare services")
    st.write("   c) Design civil infrastructure")
    st.write("   d) Analyze financial data")
    correct_answer_q2 = "b"

    st.write("3. Which of the following is used to visualize biological structures?")
    st.write("   a) Statistical Analysis")
    st.write("   b) 3D Printing")
    st.write("   c) Artificial Intelligence")
    st.write("   d) Machine Learning")
    correct_answer_q3 = "b"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score



# Function to display skill assessment for Civil Engineer role
def skill_assessment_civil_engineer():
    st.write("Skill Assessment for Civil Engineer")
    st.write("1. What is the primary goal of civil engineering?")
    st.write("   a) Develop software applications")
    st.write("   b) Build and maintain infrastructure")
    st.write("   c) Analyze biological data")
    st.write("   d) Design user interfaces")
    correct_answer_q1 = "b"

    st.write("2. Which engineering principle is used to ensure the stability of structures?")
    st.write("   a) Newton's Laws of Motion")
    st.write("   b) Ohm's Law")
    st.write("   c) Hooke's Law")
    st.write("   d) Bernoulli's Principle")
    correct_answer_q2 = "c"

    st.write("3. What type of civil engineering project involves designing transportation systems?")
    st.write("   a) Structural Engineering")
    st.write("   b) Environmental Engineering")
    st.write("   c) Geotechnical Engineering")
    st.write("   d) Transportation Engineering")
    correct_answer_q3 = "d"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for UX/UI Designer role
def skill_assessment_ux_ui_designer():
    st.write("Skill Assessment for UX/UI Designer")
    st.write("1. What is the main focus of UX/UI design?")
    st.write("   a) Analyzing financial data")
    st.write("   b) Developing web applications")
    st.write("   c) Enhancing user experience")
    st.write("   d) Designing civil infrastructure")
    correct_answer_q1 = "c"

    st.write("2. What is the purpose of wireframing in the design process?")
    st.write("   a) Create 3D models")
    st.write("   b) Present design ideas")
    st.write("   c) Generate financial reports")
    st.write("   d) Test software applications")
    correct_answer_q2 = "b"

    st.write("3. Which design principle focuses on how elements are arranged on a page?")
    st.write("   a) Contrast")
    st.write("   b) Alignment")
    st.write("   c) Proximity")
    st.write("   d) Repetition")
    correct_answer_q3 = "b"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Environmental Scientist role
def skill_assessment_environmental_scientist():
    st.write("Skill Assessment for Environmental Scientist")
    st.write("1. What is the primary goal of environmental science?")
    st.write("   a) Design user interfaces")
    st.write("   b) Analyze financial data")
    st.write("   c) Develop new software applications")
    st.write("   d) Study interactions between organisms and their environment")
    correct_answer_q1 = "d"

    st.write("2. What is the study of past climates based on tree ring analysis?")
    st.write("   a) Paleontology")
    st.write("   b) Geology")
    st.write("   c) Dendrochronology")
    st.write("   d) Ecology")
    correct_answer_q2 = "c"

    st.write("3. Which environmental issue involves the excessive buildup of greenhouse gases?")
    st.write("   a) Deforestation")
    st.write("   b) Ozone depletion")
    st.write("   c) Ocean acidification")
    st.write("   d) Global warming")
    correct_answer_q3 = "d"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Aerospace Engineer role
def skill_assessment_aerospace_engineer():
    st.write("Skill Assessment for Aerospace Engineer")
    st.write("1. What is the primary focus of aerospace engineering?")
    st.write("   a) Study of living organisms")
    st.write("   b) Design and development of aircraft and spacecraft")
    st.write("   c) Analysis of financial markets")
    st.write("   d) Construction of civil infrastructure")
    correct_answer_q1 = "b"

    st.write("2. Which aerospace engineering field involves the study of flight principles?")
    st.write("   a) Aerodynamics")
    st.write("   b) Geotechnical Engineering")
    st.write("   c) Environmental Engineering")
    st.write("   d) Structural Engineering")
    correct_answer_q2 = "a"

    st.write("3. What is the purpose of wind tunnel testing in aerospace engineering?")
    st.write("   a) Generate financial reports")
    st.write("   b) Test rockets in space")
    st.write("   c) Analyze the aerodynamic performance of models")
    st.write("   d) Create 3D models of aircraft")
    correct_answer_q3 = "c"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Biotechnology Researcher role
def skill_assessment_biotechnology_researcher():
    st.write("Skill Assessment for Biotechnology Researcher")
    st.write("1. What is the primary goal of biotechnology research?")
    st.write("   a) Study of civil infrastructure")
    st.write("   b) Development of financial models")
    st.write("   c) Improvement of medical treatments")
    st.write("   d) Design of user interfaces")
    correct_answer_q1 = "c"

    st.write("2. Which technique is used to amplify DNA in biotechnology experiments?")
    st.write("   a) Polymerase Chain Reaction (PCR)")
    st.write("   b) Principal Component Analysis (PCA)")
    st.write("   c) Newton's Laws of Motion")
    st.write("   d) Regression Analysis")
    correct_answer_q2 = "a"

    st.write("3. What is the purpose of gene editing in biotechnology?")
    st.write("   a) Analyze financial data")
    st.write("   b) Improve healthcare services")
    st.write("   c) Design web applications")
    st.write("   d) Modify the genetic code of organisms")
    correct_answer_q3 = "d"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Network Security Specialist role
def skill_assessment_network_security_specialist():
    st.write("Skill Assessment for Network Security Specialist")
    st.write("1. What is the primary focus of network security?")
    st.write("   a) Design of civil infrastructure")
    st.write("   b) Analysis of financial data")
    st.write("   c) Protection of computer networks and systems")
    st.write("   d) Development of web applications")
    correct_answer_q1 = "c"

    st.write("2. Which type of attack involves capturing and analyzing network traffic?")
    st.write("   a) Brute force attack")
    st.write("   b) Phishing attack")
    st.write("   c) Denial-of-Service (DoS) attack")
    st.write("   d) Packet sniffing attack")
    correct_answer_q2 = "d"

    st.write("3. What security measure involves verifying the identity of a user?")
    st.write("   a) Intrusion Detection System (IDS)")
    st.write("   b) Encryption")
    st.write("   c) Multi-factor authentication")
    st.write("   d) Firewall")
    correct_answer_q3 = "c"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score

# Function to display skill assessment for Robotics Engineer role
def skill_assessment_robotics_engineer():
    st.write("Skill Assessment for Robotics Engineer")
    st.write("1. What is the primary focus of robotics engineering?")
    st.write("   a) Analyze financial data")
    st.write("   b) Design and development of robots")
    st.write("   c) Study of living organisms")
    st.write("   d) Create 3D models")
    correct_answer_q1 = "b"

    st.write("2. Which field of robotics involves programming robots to perform tasks?")
    st.write("   a) Mechatronics")
    st.write("   b) Computer Vision")
    st.write("   c) Artificial Intelligence")
    st.write("   d) Controls and Kinematics")
    correct_answer_q2 = "c"

    st.write("3. What is the purpose of sensors in robotics?")
    st.write("   a) Analyze the aerodynamic performance of models")
    st.write("   b) Generate financial reports")
    st.write("   c) Capture and process environmental data")
    st.write("   d) Test rockets in space")
    correct_answer_q3 = "c"

    total_questions = 3
    user_answers = {
        "1": st.session_state.get("q1", "").lower(),
        "2": st.session_state.get("q2", "").lower(),
        "3": st.session_state.get("q3", "").lower()
    }

    if st.button("Submit"):
        # Check the answers
        score = 0

        if user_answers["1"] == correct_answer_q1:
            score += 1
        if user_answers["2"] == correct_answer_q2:
            score += 1
        if user_answers["3"] == correct_answer_q3:
            score += 1

        # Display the score
        st.write(f"You scored {score} out of {total_questions}.")
        st.session_state.score = score




def display_skill_assessment():
    # Set page title and layout
    st.set_page_config(page_title="STEM Career Exploration App", layout="wide")
    
    # Display app title and description
    st.title("STEM Career Exploration App")
    st.write("Explore various STEM career options and resources.")
    
    # Create a sidebar menu for app navigation
    menu_options = {
        "Career Profiles": display_career_profile,
        "Skill Assessment - Software Engineer": skill_assessment_software_engineer,
        "Skill Assessment - Data Scientist": skill_assessment_data_scientist,
        "Skill Assessment - Biomedical Researcher": skill_assessment_biomedical_researcher,
        "Skill Assessment - Civil Engineer": skill_assessment_civil_engineer,
        "Skill Assessment - UX/UI Designer": skill_assessment_ux_ui_designer,
        "Skill Assessment - Environmental Scientist": skill_assessment_environmental_scientist,
        "Skill Assessment - Aerospace Engineer": skill_assessment_aerospace_engineer,
        "Skill Assessment - Biotechnology Researcher": skill_assessment_biotechnology_researcher,
        "Skill Assessment - Network Security Specialist": skill_assessment_network_security_specialist,
        "Skill Assessment - Robotics Engineer": skill_assessment_robotics_engineer
    }
    menu_selection = st.sidebar.radio("Menu", list(menu_options.keys()))
    
    # Based on the menu selection, call the corresponding function
    menu_options[menu_selection]()



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
