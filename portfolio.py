import streamlit as st
#Set page title and icon

st.set_page_config(page_title="Student Portfolio",page_icon="🎓")

#Sidebar naviagtion

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:",
	   ["Home","Projects","Skills","Testimonials","Contact"])
#Home section
if page =="Home":
	st.title("🎓 Student Portfolio")
	#Profile image
	uploaded_image = st.file_uploader("Uplaod Profile Picture", type=["jpg","png"])
	if uploaded_image is not None:
		st.image(uploaded_image, width=150, caption="Uploaded image")
	else:
		st.image("personn.jpg", width=150, caption="Default image")
		#Student details (Editable!)
	name = st.text_input("Name: ", "Ishimwe Delice")
	location = st.text_input("Location: ", "Musanze,Rwanda")
	field_of_study = st.text_input("Field of Study: ", 
	                               "Computer Science, SWE")
	university = st.text_input("University: ", "INES - Ruhengeri")

	st.write(f"📍{location}")
	st.write(f"📚{field_of_study}")
	st.write(f"🎓{university}")

	# Resume download button
	with open("resume.pdf", "rb") as file:
		resume_bytes = file.read()
	st.download_button(label="📄Download Resume",
		data=resume_bytes,file_name="resume.pdf", 
		mime="resume/pdf")

	st.markdown("---")
	st.subheader("About Me")
	about_me = st.text_area("Short introduction about myself:",
		"I am a passionate AI look forward engineer!")
	st.write(about_me)

#Projects section

elif page == "Projects":
    st.title("💻 My Projects")

    st.subheader("⏳ Timeline of Academic & Project Milestones")
    milestones = [
        "✅ Year 2023: Web Design project completed",
        "🏆 Year 2024: hotel Management System",
        "💼 14/07/2025: banking System",
        "📖 Year 2025: Dissertation submission"
    ]
    for milestone in milestones:
        st.write(f" {milestone}")

    # Project Filtering System
    category = st.selectbox("Filter projects by category:", ["All", "Year 1 Project", "Year 2 Project", "Year 3 Project", "Dissertation"])

    project_data = {
        "Year 1 Project": {
            "📊 Data Analysis Project": {
                "type": "Individual",
                "description": "A project analyzing trends of Rwanda GDP accounts using Pandas and Matplotlib.",
                
            }
        },
        "Year 2 Project": {
            "🤖 AI Chatbot": {
                "type": "Group",
                "description": "Developed an AI-powered chatbot using Python and NLP techniques.",
                
            }
        },
        "Year 3 Project": {
            "🌐 Natural Oil": {
                "type": "Group",
                "description": "Designed and developed a website for Beautiful Lady .",
            
            }
        },
        "Dissertation": {
            "🌍 PARENT-APPROVED VISITOR Management System": {
                "type": "Individual",
                "description": "Designed and developed a website for a SCHOOL.",
                
            }
        }
    }

    filtered_projects = project_data.get(category, {}) if category != "All" else {k: v for cat in project_data.values() for k, v in cat.items()}

    for project, details in filtered_projects.items():
        with st.expander(project, expanded=False):
            st.write(f"Type: {details['type']}")
            st.write(f"Description: {details['description']}")
            if details.get("link"):
                st.markdown(f"[🔗 Link to Code]({details['link']})")

    st.markdown("---")
elif page =="Skills":
	st.title("⚡ Skills and Achievements")

	st.subheader("Programming Skills")
	skill_python = st.slider("Python",0,100,90)
	st.progress(skill_python)

	skill_js = st.slider("Web design",0,100,75)
	st.progress(skill_js)
	skill_AI = st.slider("HTML and css",0,100,65)
	st.progress(skill_AI)

	st.subheader("Cerfications & Achievements")
	st.write("✔ Completed AI&ML in Business Cerfication")
	st.write("✔ Certified AI in Research and Course Preparation for Education")

# Student Testimonials Section
elif page == "Testimonials":
    st.title("🗣 Student Testimonials")

    st.subheader("💬 Testimonial:")
    st.write("rachel is a brilliant problem solver! Her final year project is truly innovative. – Mclement")
    st.markdown("---")
    st.subheader("✍ Give a Testimonial")
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("How are you related", ["Classmate", "Mentor", "Teammate", "Other"])
        testimonial_message = st.text_area("Your Testimonial")

        if st.form_submit_button("Submit Testimonial") and name and testimonial_message:
            st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
            st.write(f"🗨 {testimonial_message} — {name} ({relationship})")

elif page =="Contact":
	st.title("📬 Contact Me")

	with st.form("contact_form"):
		name = st.text_input("Your Name")
		email = st.text_input("Your Email")
		message=st.text_area("Your message")

		submitted = st.form_submit_button("Send Message")
		if submitted:
			st.success("✅ Message sent successfully")

		st.write("📧 Email: ishimwedelice12@gmail.com")
		st.write("[🔗LinkedIn](ishimwe delice)")
		st.write("[📂GitHub](ishimwedelice12@gmail.com)")
	st.sidebar.write("---")
	st.sidebar.write("🔹 Made with ❤ using My pome")