from common import *
NUM, FILE = "12", "12_Advanced_and_Specialised_Topics"
TITLE = "Advanced & Specialised AI Topics"
DESC = "Everything else on the road to mastery: causal inference, probabilistic ML, AutoML, time series with DL, privacy, robotics, quantum and more."
TOPICS = [
 T("Causal inference", A, "Correlation is not causation. Use randomised experiments, DAGs, propensity scores, difference-in-differences, instrumental variables, uplift modelling (DoWhy, EconML).", "Correlation != causation. Causal inference: DAG, propensity score.",
   "# import dowhy; model=dowhy.CausalModel(data=df,treatment='t',outcome='y',graph=g)", yt_q="causal inference for data science"),
 T("Probabilistic programming and Bayesian ML (PyMC, Stan, Pyro)", A, "Specify generative models and infer posteriors with MCMC / variational inference; Gaussian processes; Bayesian neural nets.", "PyMC-la Bayesian models.",
   "import pymc as pm\nwith pm.Model():\n    mu=pm.Normal('mu',0,1);pm.Normal('y',mu,1,observed=[0.2,0.4,0.1]);idata=pm.sample(200)"),
 T("Deep learning for time series (LSTM, TCN, Transformers, N-BEATS, TimesFM)", A, "Windowed supervised learning, multi-horizon forecasting, foundation models for time series; avoid leakage with time-aware splits.", "LSTM / Transformers time series forecast.",
   "import numpy as np\ns=np.sin(np.arange(200)/5)\nX=np.array([s[i:i+20] for i in range(len(s)-20)]);y=s[20:]\nprint(X.shape,y.shape)"),
 T("AutoML and neural architecture search", A, "Automate preprocessing, model choice and tuning (AutoGluon, FLAML, H2O, auto-sklearn, Optuna).", "AutoML: automatic model selection.",
   "# from autogluon.tabular import TabularPredictor; TabularPredictor('y').fit(train)"),
 T("Federated learning, differential privacy, secure ML", A, "Train across devices without centralising data; add calibrated noise (DP-SGD); homomorphic encryption.", "Federated learning, differential privacy.",
   yt_q="federated learning explained differential privacy"),
 T("Explainable and trustworthy AI", A, "Interpretability methods (SHAP, LIME, Grad-CAM, attention analysis, mechanistic interpretability), fairness metrics (demographic parity, equalised odds), robustness and adversarial attacks.", "Explainable AI, fairness, adversarial robustness.",
   yt_q="explainable ai shap grad-cam"),
 T("Robotics & embodied AI", A, "Perception, planning, control, SLAM, simulation (Isaac, MuJoCo), imitation learning, vision-language-action models.", "Robotics + AI.",
   yt_q="robot learning introduction"),
 T("Knowledge graphs and semantic web", A, "Entities and relations (RDF, Neo4j), graph embeddings, GraphRAG.", "Knowledge graph, Neo4j, GraphRAG.",
   "import networkx as nx\nG=nx.DiGraph();G.add_edge('Chennai','TamilNadu',rel='in');print(list(G.edges(data=True)))"),
 T("Optimisation & operations research for ML (LP, MIP, genetic algorithms, simulated annealing)", A, "Linear/integer programming, metaheuristics for scheduling, routing and hyper-parameter search (PuLP, OR-Tools, DEAP).", "Optimization problems solve panna OR-Tools, PuLP.",
   "from scipy.optimize import linprog\nprint(linprog([-1,-2],A_ub=[[1,1]],b_ub=[4],bounds=[(0,3),(0,3)]).x)"),
 T("Quantum machine learning (overview)", A, "Quantum circuits as models (variational classifiers, kernels) using Qiskit / PennyLane. Mostly research-level today.", "Quantum ML - research stage.",
   yt_q="quantum machine learning introduction"),
 T("Neuro-symbolic AI, AGI, and AI safety / alignment", A, "Combine neural nets with logic/search; study alignment, interpretability, scalable oversight and governance.", "Neuro-symbolic, AI safety, alignment.",
   yt_q="ai alignment introduction"),
 T("AI in domains: healthcare, finance, agriculture, education, manufacturing, NLP for Tamil", I, "Domain knowledge + data constraints + regulation decide success. Examples: credit scoring, medical imaging, crop disease detection, predictive maintenance, Tamil speech and OCR.", "Domain-la AI apply: health, finance, agriculture, Tamil NLP.",
   yt_q="ai applications in agriculture healthcare finance"),
 T("Reading and reproducing research papers", A, "Read abstract -> figures -> method -> experiments; implement the core idea; use arXiv, Papers with Code alternatives (Hugging Face Papers), Connected Papers, Semantic Scholar.", "Paper padikka: abstract, figures, method. Reproduce pannunga.",
   yt_q="how to read an ml research paper", refs=[("arXiv cs.LG", "https://arxiv.org/list/cs.LG/recent"), ("HF Papers", "https://huggingface.co/papers")]),
 T("Writing, portfolio, blogging and open-source contributions", B, "Document projects with README, results, diagrams; publish on GitHub, Kaggle, Hugging Face Spaces; write blog posts; contribute to open-source issues labelled 'good first issue'.", "GitHub portfolio, blog, open-source contribution.",
   yt_q="data science portfolio projects tips"),
]
