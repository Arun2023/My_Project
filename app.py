import streamlit as st
import os
import shutil

st.header("FILE ORGANIZER")
st.write('---')
st.write('This website can be helpful for individuals who have a directory with various types of files and want to organize them into separate folders based on their file types .It can save time and effort that would otherwise be spent manually organizing the files.')
st.write('---')
st.write('Step: 1')
st.write('Copy the exact path location')
st.write('Example')

path = st.text_input("Enter file path")
button_clicked = st.button("Click Me")

# Check if the button is clicked
if button_clicked:
    
    if path!="":
        import os , shutil
        files=os.listdir(path)

    files_type=[]
    for file in files:
        file_type=file[file.find('.')+1:]
        files_type.append(file_type)
    uni_files_type=[]
    for file in files_type:
        if file not in uni_files_type:
            uni_files_type.append(file)
    for size in range(0,len(uni_files_type)):
        if not os.path.exists(path+uni_files_type[size]):
            #print(path+uni_files_type[size])
            os.mkdir(path+uni_files_type[size])
    for file in files:
        for i in range(0,len(uni_files_type)):
            if uni_files_type[i] in file and not os.path.exists(path+uni_files_type[i]+'/'+file):
                shutil.move(path+file,path+uni_files_type[i]+'/'+file)
            
st.header("SUCCESSFULLY MOVED")
    


