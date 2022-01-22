#writefile app.py
 
import streamlit as st
import spacy
#nlp=spacy.load("en_core_web_sm")
 

  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(bio):   
    print(bio)
    # loading the trained model
    nlp = spacy.load("loan")
    # Making predictions 
    doc = nlp(bio)
    prediction = doc.cats 
    
    print(prediction)
    Keymax = max(zip(prediction.values(), prediction.keys()))[1]
    if Keymax == "DEFAULT":
        pred = 'DEFAULT'
    else:
        pred = 'NON-DEFAULT'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#3b5998;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Kiva Loan</h1>
    <h5 style ="color:white;text-align:center;">Machine Learning-based Loan Default Prediction Application</h5>
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    user_input = st.text_area("Please enter borrower personal story:", "")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(user_input) 
        if result=="NON-DEFAULT":
            st.success('Based on this borrower\'s personal story, the loan will be in {} category'.format(result))
        else:
            st.error('Based on this borrower\'s personal story, the loan will be in {} category'.format(result))
     
if __name__=='__main__': 
    main()