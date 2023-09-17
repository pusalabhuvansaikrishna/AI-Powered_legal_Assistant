import streamlit as st
import streamlit_authenticator as stauth
from dependencies import sign_up, fetch_users
from streamlit_option_menu import option_menu
import glob


st.set_page_config(page_title='Streamlit', page_icon='🐍', initial_sidebar_state='collapsed')


try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Welcome {username}')
                Authenticator.logout('Log Out', 'sidebar')

                selected_menu=option_menu(
                menu_title='SIMPLILEGAL',
                options=['Home','Create DOC','DOC Summary'],
                icons=['house','file-break-fill','file-break'],
                menu_icon='broadcast',
                default_index=0,
                orientation='horizontal',)

                if selected_menu=='Home':
                  st.title("This is Home Page")
                  
                elif selected_menu=="Create DOC":
                  def load_images():
                    image_files=glob.glob('/content/*.jpeg')
                    #st.write(len(image_files))
                    manuscripts=[]
                    for image_file in image_files:
                      #st.write(image_file)
                      parts=image_file.split("/")
                      if parts[1] not in manuscripts:
                        manuscripts.append(parts[1])

                    manuscripts.sort()
                    return image_files,manuscripts

                  st.title("Legal Documents")
                  image_files,manuscripts = load_images()
                  view_manuscripts=st.multiselect("Select ManuScripts(s)", manuscripts)
                  n=st.number_input('Select Grid Width',1,5,3)
                  view_images=[]
                  for image_file in image_files:
                    if any(manuscript in image_file for manuscript in view_manuscripts):
                      view_images.append(image_file)

                  groups=[]
                  for i in range(0,len(view_images),n):
                    groups.append(view_images[i:i+n])
                  
                  for group in groups:
                    cols=st.columns(n)
                    for i,image_file in enumerate(group):
                      cols[i].image(image_file)

                
                elif selected_menu=='DOC Summary':
                  st.subheader("ASK YOUR QUESTIONS TO AI")
                  uploaded_file=st.file_uploader("Upload your PDF File",type="pdf")
                  if uploaded_file is not None:
                    st.title("Heyy")

                st.markdown(
                    """
                    ---
                    Made by ⚙️ Engineers
                    
                    """
                )

            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')


except:
    st.success('Refresh Page')