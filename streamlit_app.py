import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe

newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .css-1v3fvcr{background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }
                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }
                .css-nlntq9.e16nr0p33{}
                .block-container.css-12oz5g7.egzxvld2{background-color:white;
                    border:5px solid black;
                    border-radius:15px;
                    margin-top:67px;
                }

                .title{}
                .css-1cpxqw2.edgvbvh5{background-color:orange;
                    color: white;
                }
            
            </style>
            <body> 
            </body
        """
st.markdown(newhtml,unsafe_allow_html=True)


# names = ['MARIA	TERZI','Στεριανή Αβράμη','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','Μαρία Αγάθου']
# usernames = ['Maria-terzi@hotmail.com','stella-a88@hotmail.com','depi1970@hotmail.com','magathou@hotmail.com']
# passwords = ['tSYcA8GPCJ','hj2cJpZLXG','u46UXerHf9','pJH9CA7L2g']

html_logo = "<img style='display:block; margin-left:auto; margin-right:auto; text-align:center;' src='http://inclusiveeducation.eu/wp-content/uploads/2021/03/logoiam400x400.png'  width=300 height=300>"



st.markdown(html_logo, unsafe_allow_html=True)

names = ['ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ','ΜΑΡΙΑ-ΕΙΡΗΝΗ ΓΑΛΕΡΑΚΗ','ΚΟΥΛΑ ΑΜΠΕΛΙΟΤΗ','ΕΙΡΗΝΗ ΑΝΑΤΣΟΥΤΣΟΥΛΑ','ΤΑΤΙΑΝΑ ΕΛΕΟΝΩΡΑ ΑΝΑΓΝΩΣΤΙΔΟΥ','ΕΥΓΕΝΙΑ ΤΡΑΓΑΚΗ','ΣΠΥΡΙΔΩΝ ΒΑΛΒΗΣ','ΣΟΦΙΑ ΓΙΔΑΡΗ','ΔΗΜΗΤΡΗΣ ΑΡΒΑΝΙΤΗΣ','ΠΑΝΑΓΙΩΤΑ ΒΑΣΙΛΕΙΟΥ','ΕΜΜΑΝΟΥΕΛΑ ΒΑΣΙΛΕΙΑΔΗ','ΜΑΡΙΑ ΓΟΥΡΓΙΩΤΗ','ΕΛΠΙΔΑ ΓΟΥΚΟΥ','ΜΑΡΙΑ ΤΕΡΖΟΥΔΗ','ΓΕΩΡΓΙΑ ΒΕΛΟΥΔΟΥ','ΜΑΡΙΑ ΤΕΡΖΗ','ΜΑΡΙΑ ΓΕΩΡΓΟΠΟΥΛΟΥ','ΒΑΣΣΟ ΑΝΔΡΟΥΤΣΟΥ','ΧΡΗΣΤΙΝΑ ΑΛΒΑΝΗ','ΘΕΟΔΩΡΑ ΓΚΟΥΝΑ','ΜΑΡΙΑ ΑΓΑΘΟΥ','ΑΛΕΞΙΟΣ ΑΡΦΑΝΗΣ','ΕΥΑΓΓΕΛΙΑ ΒΑΡΣΑΜΑ','ΧΡΗΣΤΙΝΑ ΒΟΥΛΓΑΡΙΔΟΥ','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','ΑΛΕΞΑΝΔΡΑ ΑΛΤΙΠΑΡΜΑΚΗ','ΛΟΥΙΖΑ ΑΛΕΞΙΑΔΟΥ','ΒΕΖΑΣΗΣ ΕΥΘΥΜΙΟΣ','ΕΛΛΗ ΑΓΓΕΛΑΚΟΠΟΥΛΟΥ','ΒΑΣΙΛΙΚΗ ΛΑΖΟΥ','ΑΝΔΡΙΑΝΑ ΔΕΛΕΓΚΟΥ','ΑΠΟΣΤΟΛΙΑ ΠΛΙΑΣΣΑ','ΑΝΑΣΤΑΣΙΑ ΧΑΤΖΗΓΕΩΡΓΙΟΥ','ΑΛΙΚΗ ΒΑΒΟΥΓΥΙΟΥ','ΜΕΛΙΝΑ ΑΛΕΞΙΑΔΟΥ','ΤΣΑΡΟΥΧΑΣ ΝΕΚΤΑΡΙΟΣ','ΜΠΟΤΣΩΛΗ ΑΙΚΑΤΕΡΙΝΗ','ΑΙΚΑΤΕΡΙΝΗ ΓΚΑΓΚΑΛΗ','ΔΕΣΠΟΙΝΑ ΧΑΤΖΗΔΡΟΣΟΥ']
 
usernames = ['labrianatsiak@icloud.com','nikosmariagr@hotmail.com','kampel85@yahoo.gr','spaeirhnh@hotmail.com','tatianapsychology@yahoo.gr','eugenia.tragaki@gmail.com','nsvalv@gmail.com','sofiagidari@yahoo.gr','darv009@hotmail.com','vgiota83@hotmail.com','emmavasi76@gmail.com','maria.gr.bl@hotmail.com','elpidagoukou@yahoo.gr','terzoydi@gmail.com','tzovel72@yahoo.gr','maria-terzi@hotmail.com','mgeorgopoulou@gmail.com','vandrout@yahoo.gr','christina.albani@yahoo.gr','theodoragouna@gmail.com','magathou@hotmail.com','alexiosarfanis@gmail.com','lillyvarsama@yahoo.com','voulgaridou.christina@gmail.com','depi1970@hotmail.com','alexandralt@yahoo.com','louiza.alex@gmail.com','efthymis.v@gmail.com','elliaggel@gmail.com','lazouvaso@yahoo.gr','delegouandriana@yahoo.gr','litsapliassa@gmail.com','anastasiachatz3012@gmail.com','alikakiv_1986@hotmail.com','melinalexiadou@gmail.com','nectsarou@yahoo.gr','botsoli@yahoo.gr','kgkagkali@gmail.com','deppy.h@hotmail.com']

passwords = ['kKw63vspMq','AV2wPELFZS','BK259LtGwu','a6BzbdXRJu','mLTcrCs6a9','Jv37HCYAMX','j8m7Dn4VHQ','AXJLQHhw7d','ZUc9n2gWVp','Hvuk4aspx7','MLVTdK26SB','UpZcq6hKTC','paT7jEgSAw','eH6ZDwbk2N','Wzp96ykNeD','tSYcA8GPCJ','w3XjgRETsL','Hy26wLYmzk','GsBEYywW9n','TpSe6atkf2','pJH9CA7L2gs','L4UWEuD8MA','Q2GTuYE8ch','xcA43GJWaf','u46UXerHf9','prF4k9VXb2','E8L4MjXsWe','UxYV7bNfv4','Aax5Xe3pTK','X94bWctMj5','TEahK53skD','YFDHf4cB8n','jPsvBFte7z','ZuAf4sPJUw','wWgcxYk7M2','M5Dr8aJxhy','zPeaCyw3nq','j9zVgvyn2w','h6eacUSGrK']



hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)


name, authentication_status = authenticator.login('Login','main')

if authentication_status:
        newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .css-1v3fvcr{background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }
                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }
                .css-nlntq9.e16nr0p33{}
                .block-container.css-12oz5g7.egzxvld2{background-color:white;
                    border:5px solid black;
                    border-radius:15px;
                    margin-top:67px;
                }

                .title{}
                .css-1cpxqw2.edgvbvh5{background-color:orange;
                    color: white;
                }
            
            </style>
            <body> 
            </body
        """

        html2="""
            <!DOCTYPE html>
            <header></header>
            <style>
               
            
            </style>
            <body> 
                <ul>
                    <li>Πατήστε στο κουμπί "δημιουργία πιστοποιητικού" για να δημιουργήσεται το πιστοποιητικό σας</li>
                    <li>Αφού δημιουργήσεται το πιστοποιητικό σας πατήστε στο κουμπί "παραλαβή πιστοποιητικού" για να κατεβάσεται το πιστοποιητικό σας</li>
                </ul>
            </body
        """
        html3="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .diploma h3 {text-align:center;}
            
            </style>
            <body> 
               <h3 class="diploma">🎓 Εκτυπώστε το πιστοποιητικό σας</h3>
            </body
        """
        st.markdown(newhtml,unsafe_allow_html=True)
        st.write('Καλησπέρα, *%s*' % (name))
        # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
        st.markdown(html3,unsafe_allow_html=True)

        st.markdown(html2,unsafe_allow_html=True)

        left, right = st.columns(2)

        right.write("Here's the template we'll be using:")

        right.image("http://inclusiveeducation.eu/wp-content/uploads/2022/04/diploma2.png", width=300)

        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")


        left.write("Fill in the data:")
        form = left.form("template_form")
        student = name
        course="Report Generation in Streamlit"
        grade = 100
        submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

        if submit:
            html = template.render(
                student=student,
                course=course,
                grade=f"{grade}/100",
                date=date.today().strftime("%B %d, %Y"),
            )

            pdf = pdfkit.from_string(html, False)
            st.balloons()

            right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
            # st.write(html, unsafe_allow_html=True)
            # st.write("")
            right.download_button(
                "⬇️ Παραλαβή πιστοποιητικού",
                data=pdf,
                file_name="diploma.pdf",
                mime="application/octet-stream",
            )

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password')