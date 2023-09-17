import streamlit as st
import glob

def load_images():
  image_files=glob.glob('/content/*.JPG')
  #st.write(len(image_files))
  manuscripts=[]
  for image_file in image_files:
    #st.write(image_file)
    parts=image_file.split("/")
    if parts[1] not in manuscripts:
      manuscripts.append(parts[1])

  manuscripts.sort()

  #st.write(manuscripts)

  return image_files,manuscripts

st.title("Demo Image Grid")

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

#cols=st.columns(n)
for group in groups:
  cols=st.columns(n)
  for i,image_file in enumerate(group):
    cols[i].image(image_file)
    #st.write(i,image_file)

  







