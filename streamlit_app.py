import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe
import time
import pandas as pd




def main():
    st.header("Test Bug Download 404")
    html_logo ="<img style='background-color:black;display:block; margin-left:auto; margin-right:auto; text-align:center;' src='https://healthcare-management.gr/wp-content/uploads/2022/10/MicrosoftTeams-image-16.png'  width=400 height=143>"
    st.markdown(html_logo, unsafe_allow_html=True)

    input_form = st.sidebar.form("input_form")
    input_form.write("Email")

    title = st.text_input('Email', '')
    submit_button = input_form.form_submit_button("Submit")

    if submit_button is True:
        st.write(title)
        df=pd.read_json('datalist2.json')
        # df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

        st.dataframe(df)


        if title in df['email'].values:
        
            number=df.loc[df.isin([title]).any(axis=1)].index
            index=number.tolist()[0]
            st.write(index)
            st.write("\n  name is exists in DataFrame")

            # st.markdown(newhtml,unsafe_allow_html=True)
            st.write('Καλησπέρα, *%s*' % (df['name'][index]))
            # perds=period_counter(names,periods,name)

            # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")


            left, right = st.columns(2)

            # right.write("Here's the template we'll be using:")

            right.image("http://healthcare-management.gr/wp-content/uploads/2022/10/certificate.jpg", width=300)

            env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
            template = env.get_template("template.html")


            # left.write("Fill in the data:")
            form = left.form("template_form")
            student = df['name'][index]
            course="Report Generation in Streamlit"
            grade = 100
            # period=perds
            # submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

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
            submit_button=False
        







# df=pd.read_json('datalist2.json')
# st.write(df)


# html_logo ="<img style='background-color:black;display:block; margin-left:auto; margin-right:auto; text-align:center;' src='https://healthcare-management.gr/wp-content/uploads/2022/10/MicrosoftTeams-image-16.png'  width=400 height=143>"


# st.markdown(html_logo, unsafe_allow_html=True)


# title = st.text_input('Email', '')




    

# # name='ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ'


#     # # Find 'Reema' in name column
#     # if title in df['email'].values:
#     #     number=df.loc[df.isin([title]).any(axis=1)].index
#     #     index=number.tolist()[0]
#     #     st.write(index)
#     #     st.write("\n  name is exists in DataFrame")

# if title in df['email'].values:
        
#         number=df.loc[df.isin([title]).any(axis=1)].index
#         index=number.tolist()[0]
#         st.write(index)
#         st.write("\n  name is exists in DataFrame")

#         # st.markdown(newhtml,unsafe_allow_html=True)
#         st.write('Καλησπέρα, *%s*' % (df['name'][index]))
#         # perds=period_counter(names,periods,name)

#         # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")


#         left, right = st.columns(2)

#         # right.write("Here's the template we'll be using:")

#         right.image("http://healthcare-management.gr/wp-content/uploads/2022/10/certificate.jpg", width=300)

#         env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
#         template = env.get_template("template.html")


#         # left.write("Fill in the data:")
#         form = left.form("template_form")
#         student = df['name'][index]
#         course="Report Generation in Streamlit"
#         grade = 100
#         # period=perds
#         submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

#         if submit:
#             html = template.render(
#                 student=student,
#                 course=course,
#                 grade=f"{grade}/100",
#                 date=date.today().strftime("%B %d, %Y"),
#             )

#             pdf = pdfkit.from_string(html, False)
#             st.balloons()

#             right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
#             # st.write(html, unsafe_allow_html=True)
#             # st.write("")
#             right.download_button(
#                 "⬇️ Παραλαβή πιστοποιητικού",
#                 data=pdf,
#                 file_name="diploma.pdf",
#                 mime="application/octet-stream",
#             )
            


# else:
#     if (title!=''):
#         st.write("Not exist in db")
#     if (title==''):
#         st.write("Please type email on the field")


    
   


if __name__ == "__main__":
    main()