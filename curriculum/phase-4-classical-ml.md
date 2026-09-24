# Phase 4 — Classical Machine Learning

**Plan weeks 20–27 · 8 weeks · Difficulty ★★★☆☆ · Badge: ML Practitioner**

## Why this phase matters
Most machine learning running in companies today is not LLMs. It's fraud scores, churn prediction, demand forecasts, credit risk and anomaly detection on tables of data. These "classical" methods (regression, trees, gradient boosting, clustering) are fast, cheap, explainable, and very often the right answer. They also teach the discipline that separates engineers from demo-builders: proper validation, honest metrics, no data leakage, error analysis. Everything here carries straight into deep learning and LLM evaluation.

Everything in this phase runs on your laptop (scikit-learn on small data) or on Kaggle CPU notebooks (30 GB RAM) for bigger datasets.

## Before you start
- Phase 3 passed (gradient descent, probability, statistics).
- Comfortable with Pandas and pytest.

## You will be able to
- Frame a business problem as an ML problem, choosing the target, features and metric.
- Train and compare linear models, trees, random forests, gradient boosting, k-NN, Naive Bayes and SVMs with scikit-learn.
- Validate properly: train/validation/test splits, cross-validation, no leakage.
- Choose metrics by cost: precision, recall, F1, ROC-AUC, PR-AUC, MAE, RMSE.
- Engineer features, including LLM embeddings as features.
- Cluster, reduce dimensions and detect anomalies.
- Explain models (permutation importance, SHAP), check fairness, and serve a model behind an API.

---

## Week 1 (plan week 20) — ML framing and first models

#### P4-W1-L1 · What machine learning is (~60 min)
- **Learn:** [StatQuest — A Gentle Introduction to Machine Learning](https://www.youtube.com/watch?v=Gv9_4yMHFhI), then the Linear Regression module of [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course).
- **Key concepts:** supervised vs unsupervised learning; features and labels; training vs inference; loss; a model as a function with learned parameters.
- **Quiz seeds:** Name a supervised and an unsupervised problem from your company's domain. What exactly does "training" change?

#### P4-W1-L2 · Your first scikit-learn models (~75 min)
- **Learn:** [Kaggle Learn — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning), lessons 1–4 (How models work; Basic data exploration; Your first machine learning model; Model validation).
- **Key concepts:** the scikit-learn `fit` / `predict` pattern; mean absolute error; why you validate on data the model never saw.
- **Quiz seeds:** Why is error measured on the training data misleading?

#### P4-W1-L3 · Logistic regression and classification (~75 min)
- **Learn:** the Logistic Regression and Classification modules of [Google MLCC](https://developers.google.com/machine-learning/crash-course), plus [StatQuest — Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8).
- **Key concepts:** the sigmoid turns a score into a probability; log loss; the decision threshold; accuracy and why it can mislead.
- **Quiz seeds:** Why is logistic regression called "regression" if it classifies? What changes if you move the threshold from 0.5 to 0.2?

#### P4-W1-L4 · Generalisation and overfitting (~75 min)
- **Learn:** the MLCC module "Datasets, Generalization, and Overfitting", then Kaggle Intro to ML lessons 5–7 (Underfitting and overfitting; Random forests; Machine learning competitions).
- **Key concepts:** underfitting vs overfitting; model complexity; train, validation and test sets; why the test set is touched once.
- **Quiz seeds:** Training error 1%, validation error 25%. What's happening and what do you try first?

#### P4-W1-B · Weekend build
Enter the [Kaggle Titanic competition](https://www.kaggle.com/competitions/titanic) with a simple, documented baseline. Write down your validation score and your leaderboard score.

---

## Week 2 (plan week 21) — Evaluation done right

#### P4-W2-L1 · Cross-validation and leakage (~75 min)
- **Learn:** [StatQuest — Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw), then the Cross-Validation and Data Leakage lessons of [Kaggle Learn — Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning).
- **Key concepts:** k-fold cross-validation; stratified and time-based splits; target leakage and train–test contamination; fitting preprocessing on training folds only.
- **Quiz seeds:** You scaled the whole dataset before splitting. Why is that leakage? Why can't you shuffle time-series data for validation?

#### P4-W2-L2 · Classification metrics (~75 min)
- **Learn:** StatQuest [The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o), [Sensitivity and Specificity](https://www.youtube.com/watch?v=vP06aMoz4v8) and [ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJemM).
- **Key concepts:** true/false positives and negatives; precision, recall, F1; ROC-AUC; PR-AUC for imbalanced data; choosing the threshold by business cost.
- **Quiz seeds:** For a cancer screening test, which error is worse, and which metric do you watch? Why can ROC-AUC look great on very imbalanced data?

#### P4-W2-L3 · Bias and variance (~60 min)
- **Learn:** [StatQuest — Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA), then scikit-learn's [learning curves](https://scikit-learn.org/stable/modules/learning_curve.html) page.
- **Key concepts:** bias (too simple) vs variance (too sensitive to the training data); learning curves show which one you have; more data helps high variance, not high bias.
- **Quiz seeds:** Both training and validation error are high and close together. More data or a more complex model?

#### P4-W2-L4 · Regularisation (~60 min)
- **Learn:** StatQuest [Ridge (L2) Regression](https://www.youtube.com/watch?v=Q81RR3yKn30), [Lasso (L1) Regression](https://www.youtube.com/watch?v=NGf0voTMlcs) and [Ridge vs Lasso, Visualized](https://www.youtube.com/watch?v=Xm2C_gTAl8c).
- **Key concepts:** penalising large weights; L2 shrinks weights, L1 can set them to exactly zero (feature selection); the regularisation strength as a hyperparameter.
- **Quiz seeds:** Why does Lasso produce sparse models? Why must features be scaled before regularising?

#### P4-W2-B · Weekend build
On an imbalanced dataset (for example credit-card fraud on Kaggle): compare accuracy with PR-AUC, then pick a threshold using a cost you define (for example, a missed fraud costs 100 times as much as a false alarm).

---

## Week 3 (plan week 22) — Trees and ensembles

#### P4-W3-L1 · Decision trees (~60 min)
- **Learn:** StatQuest [Decision and Classification Trees](https://www.youtube.com/watch?v=_L39rN6gz7Y) and [Regression Trees](https://www.youtube.com/watch?v=g9c66TUylZ4).
- **Key concepts:** splitting by impurity (Gini/entropy); tree depth and overfitting; trees need no feature scaling; they're easy to explain.
- **Quiz seeds:** Why does an unlimited-depth tree overfit? How does a tree choose a split?

#### P4-W3-L2 · Random forests (~60 min)
- **Learn:** StatQuest [Random Forests Part 1](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) and [Part 2](https://www.youtube.com/watch?v=sQ870aTKqiM).
- **Key concepts:** bagging (bootstrap samples); random feature subsets; averaging reduces variance; out-of-bag error; impurity-based feature importance can mislead.
- **Quiz seeds:** Why does averaging many overfit trees give a good model?

#### P4-W3-L3 · Boosting (~75 min)
- **Learn:** StatQuest [AdaBoost](https://www.youtube.com/watch?v=LsK-xG1cLYA), [Gradient Boost Part 1](https://www.youtube.com/watch?v=3CC4N4z3GJc) and [Part 3 (classification)](https://www.youtube.com/watch?v=jxuNLH5dXCs).
- **Key concepts:** boosting builds trees one after another, each fixing the previous errors; learning rate and number of trees; bagging reduces variance, boosting reduces bias.
- **Quiz seeds:** What does each new tree in gradient boosting try to predict?

#### P4-W3-L4 · XGBoost in practice (~75 min)
- **Learn:** [StatQuest — XGBoost Part 1](https://www.youtube.com/watch?v=OtD8wVaFm6E), then the XGBoost lesson of Kaggle Intermediate ML.
- **Key concepts:** early stopping; key hyperparameters (`n_estimators`, `learning_rate`, `max_depth`); why gradient-boosted trees win most tabular competitions.
- **Quiz seeds:** How does early stopping protect you? Which three hyperparameters would you tune first?

#### P4-W3-B · Weekend build
Compare linear, random forest and XGBoost models on one tabular dataset with 5-fold cross-validation. One table, one conclusion.

---

## Week 4 (plan week 23) — More algorithms and proper pipelines

#### P4-W4-L1 · k-NN and Naive Bayes (~60 min)
- **Learn:** StatQuest [K-nearest neighbors](https://www.youtube.com/watch?v=HVXime0nQeI) and [Naive Bayes](https://www.youtube.com/watch?v=O2L2Uv9pdDA).
- **Key concepts:** distance-based prediction and the need for scaling; the "naive" independence assumption; why Naive Bayes is still a strong text baseline.
- **Build:** A spam filter with Naive Bayes on a public SMS spam dataset.

#### P4-W4-L2 · Support vector machines (~60 min)
- **Learn:** [StatQuest — Support Vector Machines Part 1](https://www.youtube.com/watch?v=efR1C6CvhmE) (Parts [2](https://www.youtube.com/watch?v=Toet3EiSFcM) and [3](https://www.youtube.com/watch?v=Qc5IyLW_hns) optional).
- **Key concepts:** maximum-margin boundaries; support vectors; soft margins; kernels as a way to draw curved boundaries.
- **Quiz seeds:** What are the "support vectors"? Why might an SVM struggle with a million rows?

#### P4-W4-L3 · Pipelines (~75 min)
- **Learn:** the Missing Values, Categorical Variables and Pipelines lessons of [Kaggle Intermediate ML](https://www.kaggle.com/learn/intermediate-machine-learning), then scikit-learn's [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html).
- **Key concepts:** `Pipeline` and `ColumnTransformer`; imputation; one-hot vs ordinal encoding; pipelines prevent leakage and make deployment simple.
- **Quiz seeds:** Why put the scaler *inside* the pipeline that cross-validation runs?

#### P4-W4-L4 · Hyperparameter tuning (~60 min)
- **Learn:** scikit-learn's [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html).
- **Key concepts:** grid vs random search; nested cross-validation (conceptually); `random_state` for reproducibility; tuning on validation data only.
- **Quiz seeds:** Why can heavy tuning overfit the validation set?

#### P4-W4-B · Weekend build
Refactor your best Week 3 model into a single `Pipeline` with a tuned `RandomizedSearchCV`, saved with `joblib`.

---

## Week 5 (plan week 24) — Feature engineering, including text

#### P4-W5-L1 · Feature engineering I (~75 min)
- **Learn:** [Kaggle Learn — Feature Engineering](https://www.kaggle.com/learn/feature-engineering), lessons 1–3 (What is feature engineering; Mutual information; Creating features).
- **Key concepts:** why features beat fancier models; mutual information; ratios, counts, date parts, group statistics.

#### P4-W5-L2 · Feature engineering II (~75 min)
- **Learn:** Kaggle Feature Engineering, lessons 4–6 (Clustering with k-means; Principal component analysis; Target encoding).
- **Key concepts:** cluster labels as features; PCA features; target encoding and its leakage risk (use cross-fitting).
- **Quiz seeds:** Why can target encoding leak, and how do you prevent it?

#### P4-W5-L3 · Text classification with TF-IDF (~60 min)
- **Learn:** scikit-learn's [text feature extraction guide](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) (bag of words, TF-IDF), then build the classifier yourself.
- **Key concepts:** bag of words; TF-IDF; n-grams; linear models on sparse text features are fast, strong baselines.
- **Quiz seeds:** What does TF-IDF down-weight, and why?

#### P4-W5-L4 · LLM embeddings as features (~60 min)
- **Learn:** reuse your Phase 2 embedding code: encode texts with `all-MiniLM-L6-v2`, then train logistic regression on the vectors.
- **Key concepts:** embeddings capture meaning that TF-IDF misses (synonyms, paraphrases); the cost and latency trade-off; combining both.
- **Quiz seeds:** When would TF-IDF still win?

#### P4-W5-B · Weekend build
A support-ticket classifier (public or synthetic tickets): TF-IDF vs embeddings vs both, on the same split, with macro-F1.

---

## Week 6 (plan week 25) — Unsupervised learning and anomalies

#### P4-W6-L1 · k-means (~60 min)
- **Learn:** [StatQuest — K-means clustering](https://www.youtube.com/watch?v=4b5d3muPQmA), then scikit-learn's [silhouette analysis example](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html).
- **Key concepts:** centroids; choosing k with the elbow and silhouette methods; k-means' love of round, similar-size clusters; scaling first.

#### P4-W6-L2 · Hierarchical clustering and DBSCAN (~60 min)
- **Learn:** [StatQuest — Hierarchical Clustering](https://www.youtube.com/watch?v=7xHsRkOdVwo), then scikit-learn's [clustering guide](https://scikit-learn.org/stable/modules/clustering.html) section on DBSCAN.
- **Key concepts:** dendrograms; density-based clusters of any shape; noise points.
- **Quiz seeds:** Which algorithm would you use for oddly shaped clusters with outliers?

#### P4-W6-L3 · PCA and t-SNE (~75 min)
- **Learn:** [StatQuest — PCA, Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) and [t-SNE, Clearly Explained](https://www.youtube.com/watch?v=NEaUSP4YerM).
- **Key concepts:** PCA finds directions of maximum variance (the eigenvectors from Phase 3); explained variance; t-SNE for visualisation only; don't read distances between t-SNE clusters.
- **Quiz seeds:** How does PCA connect to eigenvectors? Why shouldn't you use t-SNE output as model features?

#### P4-W6-L4 · Anomaly detection (~60 min)
- **Learn:** scikit-learn's [novelty and outlier detection guide](https://scikit-learn.org/stable/modules/outlier_detection.html) (Isolation Forest).
- **Key concepts:** isolation forests; contamination; evaluating anomalies without labels; an IT-operations use case (unusual server metrics or log volumes).
- **Build:** Isolation Forest on synthetic server metrics with injected incidents. How many did it catch?

#### P4-W6-B · Weekend build
Customer segmentation or log-anomaly mini-project, with a one-page summary for a non-technical reader.

---

## Week 7 (plan week 26) — Explainability, fairness and serving

#### P4-W7-L1 · Explaining models (~75 min)
- **Learn:** [Kaggle Learn — Machine Learning Explainability](https://www.kaggle.com/learn/machine-learning-explainability) (permutation importance, partial dependence plots, SHAP values).
- **Key concepts:** global vs local explanations; permutation importance; partial dependence; SHAP; explanations describe the model, not the world.
- **Quiz seeds:** Why can permutation importance mislead when two features are strongly correlated?

#### P4-W7-L2 · Fairness and responsible ML (~60 min)
- **Learn:** the ML Fairness module of [Google MLCC](https://developers.google.com/machine-learning/crash-course), then selected lessons of [Kaggle Learn — Intro to AI Ethics](https://www.kaggle.com/learn/intro-to-ai-ethics).
- **Key concepts:** types of bias (historical, sampling, measurement); proxy features; fairness metrics conflict with each other; documenting limitations.
- **Quiz seeds:** You removed "gender" from a loan model. Why might it still discriminate?

#### P4-W7-L3 · Serving a model with FastAPI (~75 min)
- **Learn:** [FastAPI tutorial — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) and [Request Body](https://fastapi.tiangolo.com/tutorial/body/).
- **Key concepts:** loading a saved pipeline once at start-up; a `/predict` endpoint; Pydantic request validation; the automatic `/docs` page; returning probabilities, not just labels.
- **Quiz seeds:** Why load the model at start-up rather than on every request? What should happen when a request is missing a feature?

#### P4-W7-L4 · Competition workflow and production thinking (~60 min)
- **Learn:** the Production ML Systems module of [Google MLCC](https://developers.google.com/machine-learning/crash-course); then browse a Kaggle [Playground Series](https://www.kaggle.com/competitions?search=playground) competition and read two top public notebooks.
- **Key concepts:** trusting your local cross-validation over the public leaderboard; learning from others' notebooks ethically; training–serving skew; what changes when a model meets real users.

#### P4-W7-B · Weekend: start Project 4

---

## Week 8 (plan week 27) — Project 4 and exam
#### P4-W8-L1 to L4 · Project 4 work
#### P4-W8-B · Weekend: `/submit`, then `/exam`

## Project 4 — "End-to-End Predictor" (`projects/pr4-end-to-end-predictor/`)
A tabular problem you care about. Ideas: loan default, customer churn, used-car prices in your country, crop yield, flight delays.

**Must-haves**
- [ ] An EDA summary with 5 key insights, and a simple baseline model.
- [ ] At least 3 model families compared with proper cross-validation; the metric chosen and justified by business cost.
- [ ] The final model is a tuned scikit-learn `Pipeline`; you explain how you checked for leakage.
- [ ] Error analysis: which segments fail, with a confusion matrix or residual plots.
- [ ] Explainability: permutation importance or SHAP, plus 2 plain-language insights.
- [ ] A fairness check on one sensitive attribute, or a clear reason why it doesn't apply.
- [ ] A FastAPI `/predict` endpoint with Pydantic validation, plus a simple UI (Streamlit or Gradio), deployed for free (Streamlit Community Cloud, Render, or a Hugging Face ZeroGPU Space; see [guides/free-compute.md](../guides/free-compute.md)).
- [ ] A model card section in the README: intended use, data, metrics, limitations.
- [ ] A submission to an active Kaggle Playground competition, with your score and what you learned.

**Stretch:** calibrated probabilities; a cost-based threshold; a monitoring plan.

**Viva focus:** why this metric; how you know there's no leakage; one segment where the model is unreliable and what you'd do about it.

## Exam EX4
- **Part A (concepts):** splits and cross-validation, leakage, metrics, bias–variance, regularisation, trees and boosting, pipelines, clustering, PCA, explainability.
- **Part B (live coding, 25 min):** build a pipeline with cross-validation on a given dataset and report one metric correctly.
- **Part C (stakeholder):** "Explain precision vs recall to a bank manager for a fraud model, and which one they should care about."
- **Part D (judgment):** "The fraud model is 99% accurate. Ship it?"

---

## Optional and deeper
- [An Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/) (free PDF) and its [labs](https://github.com/intro-stat-learning/ISLP_labs).
- Aurélien Géron's free notebooks for *Hands-On ML with Scikit-Learn and PyTorch*: [ageron/handson-mlp](https://github.com/ageron/handson-mlp) (Colab-ready).
- [Microsoft — ML for Beginners](https://github.com/microsoft/ML-For-Beginners) (26 lessons).
- [freeCodeCamp — Machine Learning for Everybody](https://www.youtube.com/watch?v=i_LwzRVP7bg) (4 h).
- [Stanford CS229 (Andrew Ng, 2018)](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU), for the maths behind the methods.
- [DataTalksClub — ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp): free and project-based. Self-paced any time (no certificate), or join the live cohort that starts each September for a certificate.
- [Kaggle Learn — Time Series](https://www.kaggle.com/learn/time-series).
- Andrew Ng's Machine Learning Specialization on [Coursera](https://www.coursera.org/specializations/machine-learning-introduction): the first module of each course is free; Coursera Financial Aid (about 15 days per course) covers the rest.
- **Regional-language options (Hindi):** [CampusX — 100 Days of Machine Learning](https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH); [codebasics — ML for Beginners](https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw); [Krish Naik — Complete ML](https://www.youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe); NPTEL [Introduction to Machine Learning, IIT Madras](https://nptel.ac.in/courses/106106139) (free videos; the certificate exam costs about ₹1,000).
