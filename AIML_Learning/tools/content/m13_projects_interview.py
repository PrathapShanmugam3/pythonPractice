from common import *
NUM, FILE = "13", "13_Projects_Interview_and_Career"
TITLE = "Projects, Interview Preparation & Career"
DESC = "Project ideas from beginner to expert, interview question bank and a Kaggle strategy."
TOPICS = [
 T("Beginner projects (Weeks 1-8)", B, "1) Student marks analysis (pandas). 2) Titanic survival. 3) House price regression. 4) Iris / wine classification. 5) Spam SMS classifier. 6) Customer segmentation (K-Means). 7) Movie dashboard (Streamlit). 8) Data-cleaning pipeline.", "Beginner projects list: Titanic, house price, spam classifier, K-Means segmentation.",
   yt_q="beginner machine learning projects with source code"),
 T("Intermediate projects (Weeks 9-24)", I, "1) Churn prediction with XGBoost + SHAP. 2) Credit-card fraud (imbalanced). 3) Sales forecasting. 4) Movie recommender. 5) CNN image classifier with transfer learning. 6) Sentiment analysis with BERT. 7) Resume parser (NER). 8) Deploy model with FastAPI + Docker.", "Churn, fraud, recommender, CNN, BERT sentiment, deploy.",
   yt_q="intermediate machine learning projects"),
 T("Advanced projects (Weeks 25-52)", A, "1) YOLO custom object detector. 2) Tamil speech-to-text with Whisper fine-tune. 3) RAG chatbot with citations and evals. 4) LoRA-fine-tuned LLM. 5) Multi-agent assistant with tools. 6) Real-time anomaly detection pipeline. 7) Diffusion fine-tune. 8) End-to-end MLOps project with monitoring.", "YOLO, Tamil ASR, RAG, LoRA, agents, MLOps.",
   yt_q="advanced ai projects llm rag yolo"),
 T("Kaggle strategy", I, "Start with Getting Started comps; study top notebooks; build a strong CV; feature engineering + GBDT + ensembling; track experiments; learn from post-competition write-ups.", "Kaggle: CV strong, feature engineering, ensembling.",
   yt_q="kaggle competition strategy tips", refs=[("Kaggle Learn", "https://www.kaggle.com/learn")]),
 T("Interview: Python & coding", I, "Common: list vs tuple, deep vs shallow copy, GIL, generators, decorators, mutable defaults, time complexity, two-sum, sliding window, string manipulation, SQL joins/window functions.", "Python interview: GIL, decorators, generators, copy.",
   yt_q="python interview questions for data science"),
 T("Interview: statistics & maths", I, "Explain p-value, CLT, bias-variance, MLE, confidence interval, Bayes problem, correlation vs causation, PCA/eigenvectors, gradient descent, regularisation.", "p-value, CLT, MLE, PCA, gradient descent.",
   yt_q="statistics interview questions data science"),
 T("Interview: machine learning", I, "Bagging vs boosting, overfitting fixes, L1 vs L2, precision vs recall, ROC-AUC, handle imbalance & missing data, feature selection, cross-validation, explain random forest/XGBoost/SVM/KNN, leakage, cold start.", "ML interview: bagging vs boosting, metrics, imbalance.",
   yt_q="machine learning interview questions and answers"),
 T("Interview: deep learning & LLMs", A, "Backprop, vanishing gradients, BatchNorm vs LayerNorm, attention complexity, positional encoding, LoRA, RAG design, hallucination mitigation, tokenisation, KV cache, evaluation of LLM apps.", "DL/LLM interview: backprop, attention, LoRA, RAG.",
   yt_q="deep learning llm interview questions"),
 T("Interview: ML system design", A, "Clarify goal -> metrics -> data -> features -> model -> training pipeline -> serving (latency, scale) -> monitoring -> iteration. Practice: recommender, fraud detection, search ranking, ad CTR, chatbot.", "ML system design framework.",
   yt_q="machine learning system design interview"),
 T("Resume, LinkedIn, GitHub and job search", B, "Quantify impact in bullet points, link live demos, keep a strong GitHub README, network, apply to internships, use job boards (LinkedIn, Wellfound, Naukri).", "Resume-la impact numbers sollunga, GitHub clean-a vaingka.",
   yt_q="data science resume tips"),
 T("Certifications & degrees (optional)", B, "Useful: Google/IBM/DeepLearning.AI certificates, AWS ML Specialty, TensorFlow Developer, Azure AI Engineer. Projects matter more than certificates.", "Certificates help, aana projects-dhaan mukkiyam.",
   yt_q="best machine learning certifications"),
]
