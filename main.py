from tkinter import *
import pyqrcode
from fpdf import FPDF
from tkinter import messagebox

window = Tk()


class PDFCV(FPDF):
    def header(self):
        self.image("mywebsite.png", 10, 8, 33, title="Portfolio Site")

    def footer(self):
        pass

    def generate_cv(self, name, website, email, phone_number, address, experience_list, education_list, skills, about_me):
        self.add_page()
        self.ln(20)

        # Displaying the name
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, name, new_x="LMARGIN", new_y="NEXT", align="C")

        # Adding contact information
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "Contact Information", new_x="LMARGIN", new_y="NEXT", align="L")

        # Adding the contact information
        self.set_font("helvetica", "", 10)
        self.cell(0, 5, f"Email: {email}", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, f"Phone: {phone_number}", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, f"Address: {address}", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, f"Website: {website}", new_x="LMARGIN", new_y="NEXT")

        # Skills
        self.ln(10)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "Skills", new_x="LMARGIN", new_y="NEXT", align="L")

        self.set_font("helvetica", "", 10)
        for skill in skills:
            self.cell(0,5, "-{}".format(skill), new_x="LMARGIN", new_y="NEXT")

        # Work experience
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "Work Experience", new_x="LMARGIN", new_y="NEXT", align="L")

        self.set_font("helvetica", "", 10)
        for experience in experience_list:
            self.cell(0, 5, "{}:{}".format(experience["title"], experience["description"]), new_x="LMARGIN", new_y="NEXT")

        # Education
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT", align="L")

        self.set_font("helvetica", "", 10)
        for education in education_list:
            self.cell(0, 5, "{}:{}".format(education["degree"], education["university"]), new_x="LMARGIN",
                      new_y="NEXT")

        # About Me
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "About Me", new_x="LMARGIN", new_y="NEXT", align="L")

        self.set_font("helvetica", "", 10)
        self.multi_cell(0,5, about_me)

        self.output("myresume.pdf")


# For functions
def generate_resume_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    website = entry_website.get()
    address = entry_address.get()
    skills = entry_skills.get('1.0', END).strip().split('\n')
    about_me = entry_about_me.get('1.0', END)

    education_list = []
    experience_list = []
    educations = entry_education.get("1.0", END).strip().split('\n')
    for education in educations:
        education = education.split(':')
        degree = education[0]
        university = education[1]
        education_list.append({'degree': degree.strip(), 'university': university.strip()})

    experiences = entry_experience.get("1.0", END).strip().split('\n')
    for experience in experiences:
        experience = experience.split(':')
        job_title = experience[0]
        description = experience[1]
        experience_list.append({'title': job_title.strip(), 'description': description.strip()})

    # Create a QR code
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not website or \
            not email or not phone_number or \
            not address or not skills or not about_me:
        messagebox.showerror("Error", "No input can be empty!")
        return

    cv = PDFCV()
    cv.generate_cv(name, website, email,
                   phone_number, address, experience_list,
                   education_list, skills, about_me)


window.title("CV Generator")

label_name = Label(window, text="Name: ")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(window, text="Email: ")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone_number = Label(window, text="Phone Number: ")
label_phone_number.pack()
entry_phone_number = Entry(window)
entry_phone_number.pack()

label_address = Label(window, text="Address: ")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()

label_website = Label(window, text="Website: ")
label_website.pack()
entry_website = Entry(window)
entry_website.pack()

# For Skills
label_skills = Label(window, text="Skill(Enter one skill per line)")
label_skills.pack()
entry_skills = Text(window, height=5)
entry_skills.pack()

# For education
label_education = Label(window, text="Education(One per line in  format 'Degree: University')")
label_education.pack()
entry_education = Text(window, height=5)
entry_education.pack()

# For experience
label_experience = Label(window, text="Experience(One per line in  format 'Job title: Description')")
label_experience.pack()
entry_experience = Text(window, height=5)
entry_experience.pack()

# For about me
label_about_me = Label(window, text="Give a description about yourself")
label_about_me.pack()
entry_about_me = Text(window, height=5)
entry_about_me.pack()

generate_button = Button(text="Generate Resume", command=generate_resume_pdf)
generate_button.pack()

window.mainloop()

