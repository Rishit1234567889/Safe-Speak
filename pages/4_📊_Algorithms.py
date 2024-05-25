# import streamlit as st
# from PIL import Image



# hide_menu = """
# <style>
# #MainMenu{
#     visibility:hidden;
# }

# footer{
#     visibility:hidden;
# }
# </style>
# """

# showWarningOnDirectExecution = False
# image = Image.open('icons/logo.png')


# st.set_page_config(page_title = "Algorithms", page_icon = image)

# st.markdown(hide_menu, unsafe_allow_html=True)

 
# st.sidebar.image(image , use_column_width=True, output_format='auto')


# st.sidebar.markdown("---")


# st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | SafeSpeak </h1>", unsafe_allow_html=True)




# st.title("Algorithms📊")
# st.markdown("---")
# st.markdown("<br>", unsafe_allow_html=True)

# all_Datasets = ["Select a Dataset","Cyber Bullying Types Dataset", "Cyber Troll Dataset","Classified Tweets Dataset","Cyberbulling Classification Dataset","Cyber Bullying Types Dataset + Cyber Troll Dataset","Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset"]
# data_choice = st.selectbox("Dataset", all_Datasets)
# all_Vectorizers = ["Select a Vectorizer", "TF-IDF", "CountVectorizer"]
# vect_choice = st.selectbox("Vectorizer", all_Vectorizers)
# all_ML_models = ["Select a Machine Learning Algorithm", "Logistic Regression", "Decision Tree", "Random Forest", "XGBoost", "Naive Bayes", "Support Vector Machine", "Bagging Decision Tree", "Boosting Decision Tree"]
# model_choice = st.selectbox("Machine Learning Algorithm", all_ML_models)
# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown("---")

# if data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select **_Dataset_**]")
# elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select **_Vectorizer_**]")
# elif data_choice != "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select **_Machine Learning Algorithm_**]")
# elif data_choice == "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select **_Dataset_** and **_Vectorizer_**]")
# elif data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select **_Dataset_** and **_Machine Learning Algorithm_**]")
# elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
#     st.warning(":white[You should select **_Vectorizer_** and **_Machine Learning Algorithm_**]")
# else:
#     if data_choice == "Cyber Bullying Types Dataset":
#     # if token_choice == "Tokenizing":
#         if vect_choice == "TF-IDF":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.88%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_87.38%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.71%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_87.38%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_88.78%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.71%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_88.08%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_87.38%_**]")
#         elif vect_choice == "CountVectorizer":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.65%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.71%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.18%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.95%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.88%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.88%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.25%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.01%_**]")
#     elif   data_choice == "Cyber Troll Dataset":
#         if vect_choice == "TF-IDF":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_76.08%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_85.92%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.70%_**]")
#                 # model used
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_76.00%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_78.20%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_80.50%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.87%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.22%_**]")
#         elif vect_choice == "CountVectorizer":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_81.57%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.60%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.47%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_73.48%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_79.73%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_83.72%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_81.75%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.35%_**]")
#     elif   data_choice == "Classified Tweets Dataset":
#         if vect_choice == "TF-IDF":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.52%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.10%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.45%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.95%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_87.89%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.30%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.17%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.24%_**]")
#         elif vect_choice == "CountVectorizer":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.07%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_88.90%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.92%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_91.38%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.39%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.24%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.95%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.40%_**]")
#     elif   data_choice == "Cyberbulling Classification Dataset":  
#         if vect_choice == "TF-IDF":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.10%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_82.23%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.12%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.26%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.67%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.27%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.61%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_83.54%_**]")
#         elif vect_choice == "CountVectorizer":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.10%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_82.07%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.43%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.26%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.67%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_86.27%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.19%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_83.55%_**]")
#     elif   data_choice == "Cyber Bullying Types Dataset + Cyber Troll Dataset":
#         if vect_choice == "TF-IDF":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_78.12%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_85.45%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.29%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_75.52%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_79.95%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_80.60%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.84%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_90.06%_**]")
#         elif vect_choice == "CountVectorizer":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_81.89%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_83.60%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_85.52%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_73.51%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_79.58%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_83.24%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_82.45%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_89.16%_**]")
#     elif   data_choice == "Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset": 
#         if vect_choice == "TF-IDF":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.57%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_80.03%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_81.77%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.50%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_74.90%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.72%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_82.69%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_80.65%_**]")
#         elif vect_choice == "CountVectorizer":
#             if model_choice == "Logistic Regression":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.57%_**]")
#             elif model_choice == "Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_80.11%_**]")
#             elif model_choice == "Random Forest":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_82.03%_**]")
#             elif model_choice == "XGBoost":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.50%_**]")
#             elif model_choice == "Naive Bayes":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_74.90%_**]")
#             elif model_choice == "Support Vector Machine":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_84.72%_**]")
#             elif model_choice == "Bagging Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_82.65%_**]")
#             elif model_choice == "Boosting Decision Tree":
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.subheader("Evaluation Metrics")
#                 st.success(":green[Accuracy: **_80.48%_**]")

import streamlit as st
from PIL import Image
from typing import Optional

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')

st.set_page_config(page_title="Algorithms", page_icon=image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.image(image, use_column_width=True, output_format='auto')

st.sidebar.markdown("---")

st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | SafeSpeak </h1>", unsafe_allow_html=True)

st.title("Algorithms📊")
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

all_Datasets = ["Select a Dataset", "Cyber Bullying Types Dataset", "Cyber Troll Dataset", "Classified Tweets Dataset", "Cyberbulling Classification Dataset", "Cyber Bullying Types Dataset + Cyber Troll Dataset", "Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset"]
data_choice: Optional[str] = st.selectbox("Dataset", all_Datasets)
all_Vectorizers = ["Select a Vectorizer", "TF-IDF", "CountVectorizer"]
vect_choice: Optional[str] = st.selectbox("Vectorizer", all_Vectorizers)
all_ML_models = ["Select a Machine Learning Algorithm", "Logistic Regression", "Decision Tree", "Random Forest", "XGBoost", "Naive Bayes", "Support Vector Machine", "Bagging Decision Tree", "Boosting Decision Tree"]
model_choice: Optional[str] = st.selectbox("Machine Learning Algorithm", all_ML_models)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

if not all([data_choice, vect_choice, model_choice]):
    missing_choices = [c for c in ["Dataset", "Vectorizer", "Machine Learning Algorithm"] if not eval(f"{c.lower().replace(' ', '_')}_choice")]
    st.warning(f":white[You should select **_{', '.join(missing_choices)}_**]")
else:
    accuracy_mapping = {
        ("Cyber Bullying Types Dataset", "TF-IDF", "Logistic Regression"): "90.88%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "Decision Tree"): "87.38%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "Random Forest"): "89.71%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "XGBoost"): "87.38%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "Naive Bayes"): "88.78%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "Support Vector Machine"): "89.71%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "Bagging Decision Tree"): "88.08%",
        ("Cyber Bullying Types Dataset", "TF-IDF", "Boosting Decision Tree"): "87.38%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Logistic Regression"): "90.65%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Decision Tree"): "89.71%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Random Forest"): "90.18%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "XGBoost"): "89.95%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Naive Bayes"): "90.88%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Support Vector Machine"): "90.88%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Bagging Decision Tree"): "89.25%",
        ("Cyber Bullying Types Dataset", "CountVectorizer", "Boosting Decision Tree"): "89.01%",
        ("Cyber Troll Dataset", "TF-IDF", "Logistic Regression"): "76.08%",
        ("Cyber Troll Dataset", "TF-IDF", "Decision Tree"): "85.92%",
        ("Cyber Troll Dataset", "TF-IDF", "Random Forest"): "91.70%",
        ("Cyber Troll Dataset", "TF-IDF", "XGBoost"): "76.00%",
        ("Cyber Troll Dataset", "TF-IDF", "Naive Bayes"): "78.20%",
        ("Cyber Troll Dataset", "TF-IDF", "Support Vector Machine"): "80.50%",
        ("Cyber Troll Dataset", "TF-IDF", "Bagging Decision Tree"): "84.87%",
        ("Cyber Troll Dataset", "TF-IDF", "Boosting Decision Tree"): "91.22%",
        ("Cyber Troll Dataset", "CountVectorizer", "Logistic Regression"): "81.57%",
        ("Cyber Troll Dataset", "CountVectorizer", "Decision Tree"): "84.60%",
        ("Cyber Troll Dataset", "CountVectorizer", "Random Forest"): "86.47%",
        ("Cyber Troll Dataset", "CountVectorizer", "XGBoost"): "73.48%",
        ("Cyber Troll Dataset", "CountVectorizer", "Naive Bayes"): "79.73%",
        ("Cyber Troll Dataset", "CountVectorizer", "Support Vector Machine"): "83.72%",
        ("Cyber Troll Dataset", "CountVectorizer", "Bagging Decision Tree"): "81.75%",
        ("Cyber Troll Dataset", "CountVectorizer", "Boosting Decision Tree"): "89.35%",
        ("Classified Tweets Dataset", "TF-IDF", "Logistic Regression"): "90.52%",
        ("Classified Tweets Dataset", "TF-IDF", "Decision Tree"): "89.10%",
        ("Classified Tweets Dataset", "TF-IDF", "Random Forest"): "91.45%",
        ("Classified Tweets Dataset", "TF-IDF", "XGBoost"): "90.95%",
        ("Classified Tweets Dataset", "TF-IDF", "Naive Bayes"): "87.89%",
        ("Classified Tweets Dataset", "TF-IDF", "Support Vector Machine"): "91.30%",
        ("Classified Tweets Dataset", "TF-IDF", "Bagging Decision Tree"): "91.17%",
        ("Classified Tweets Dataset", "TF-IDF", "Boosting Decision Tree"): "90.24%",
        ("Classified Tweets Dataset", "CountVectorizer", "Logistic Regression"): "91.07%",
        ("Classified Tweets Dataset", "CountVectorizer", "Decision Tree"): "88.90%",
        ("Classified Tweets Dataset", "CountVectorizer", "Random Forest"): "90.92%",
        ("Classified Tweets Dataset", "CountVectorizer", "XGBoost"): "91.38%",
        ("Classified Tweets Dataset", "CountVectorizer", "Naive Bayes"): "90.39%",
        ("Classified Tweets Dataset", "CountVectorizer", "Support Vector Machine"): "90.24%",
        ("Classified Tweets Dataset", "CountVectorizer", "Bagging Decision Tree"): "90.95%",
        ("Classified Tweets Dataset", "CountVectorizer", "Boosting Decision Tree"): "24%",

        ("Cyberbulling Classification Dataset", "TF-IDF", "Logistic Regression"): "90.52%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "Decision Tree"): "89.10%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "Random Forest"): "91.45%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "XGBoost"): "90.95%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "Naive Bayes"): "87.89%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "Support Vector Machine"): "91.30%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "Bagging Decision Tree"): "91.17%",
        ("Cyberbulling Classification Dataset", "TF-IDF", "Boosting Decision Tree"): "90.24%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Logistic Regression"): "91.07%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Decision Tree"): "88.90%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Random Forest"): "90.92%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "XGBoost"): "91.38%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Naive Bayes"): "90.39%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Support Vector Machine"): "90.24%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Bagging Decision Tree"): "90.95%",
        ("Cyberbulling Classification Dataset", "CountVectorizer", "Boosting Decision Tree"): "34%",


        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Logistic Regression"): "90.52%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Decision Tree"): "89.10%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Random Forest"): "91.45%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "XGBoost"): "90.95%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Naive Bayes"): "87.89%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Support Vector Machine"): "91.30%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Bagging Decision Tree"): "91.17%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Boosting Decision Tree"): "90.24%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Logistic Regression"): "91.07%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Decision Tree"): "88.90%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Random Forest"): "90.92%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "XGBoost"): "91.38%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Naive Bayes"): "90.39%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Support Vector Machine"): "90.24%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Bagging Decision Tree"): "90.95%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Boosting Decision Tree"): "23%",



        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Logistic Regression"): "90.52%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Decision Tree"): "89.10%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Random Forest"): "91.45%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "XGBoost"): "90.95%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Naive Bayes"): "87.89%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Support Vector Machine"): "91.30%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Bagging Decision Tree"): "91.17%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Boosting Decision Tree"): "90.24%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Logistic Regression"): "91.07%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Decision Tree"): "88.90%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Random Forest"): "90.92%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "XGBoost"): "91.38%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Naive Bayes"): "90.39%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Support Vector Machine"): "90.24%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Bagging Decision Tree"): "90.95%",
        ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Boosting Decision Tree"): "32%"
    }
        