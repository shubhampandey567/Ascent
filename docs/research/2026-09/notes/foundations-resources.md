# Foundations resources for a zero-budget AI learning path: verified catalogue (as of 2026-09-24)

**How this was checked (2026-09-24).** Every YouTube video and playlist ID below was checked against the YouTube oEmbed endpoint (`https://www.youtube.com/oembed?url=<url>&format=json`), which returns the real title and channel only for valid public IDs. Playlist contents, video counts and total lengths were read from the live playlist pages. Publish dates, lengths and "playable/embeddable" status come from the live watch pages. Websites were checked with an HTTP fetch (final URL, HTTP status, page title, key text) and GitHub repos through the GitHub API (archived flag, last push date, stars). Titles are given **exactly as they appear on YouTube today** (several have been renamed since first upload). A linked title means it was verified. Anything that could not be verified is marked **UNVERIFIED**. Durations are rounded (h = hours, m = minutes). "Primary" and "alternate" labels are my curriculum recommendations and appear only in the *Inferences* sections.

Learner constraints this catalogue was filtered for: an absolute beginner in AI with basic Java/Python, a zero budget, a weak laptop (~8 GB RAM, no NVIDIA GPU) and probably based in India. Resources that run in the browser, on Google Colab or on Kaggle are flagged.

---

## Q1. 3Blue1Brown: Essence of Linear Algebra, Essence of Calculus, Neural Networks (incl. 2024–2026 transformer/LLM chapters and "LLMs explained briefly"), Bayes, CLT, convolution

### Takeaway
All 3Blue1Brown IDs are live and verified. The **"Neural networks" playlist now has 10 videos (~3h37m)**. Beyond Chapters 1–7 and "Large Language Models explained briefly", it now includes **"But what is cross-entropy? | Compression is Intelligence Part 2" (2026-07-16)** and a **Welch Labs guest video on AI image/video generation (2025-07-25)**. Part 1 of the new "Compression is Intelligence" series ("Reinventing Entropy", 2026-06-07) exists but is *not* in that playlist. Several chapters have been renamed: Ch3 is now "Backpropagation, intuitively", Ch5 "Transformers, the tech behind LLMs", and Ch6 "Attention in transformers, step-by-step". 3b1b is free, has no exercises and no certificate. It is the best *intuition-first* resource for linear algebra, calculus and neural networks.

### Cited Findings
**Essence of linear algebra.** Creator: 3Blue1Brown (Grant Sanderson). Format: animated video series, 16 videos, ~3h00m total. Prerequisite: high-school algebra. Playlist: [Essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- Ch1 ["Vectors | Chapter 1, Essence of linear algebra"](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- Ch2 ["Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra"](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- Ch3 ["Linear transformations and matrices | Chapter 3, Essence of linear algebra"](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- Ch4 ["Matrix multiplication as composition | Chapter 4, Essence of linear algebra"](https://www.youtube.com/watch?v=XkY2DOUCWMU)
- Ch5 ["Three-dimensional linear transformations | Chapter 5, Essence of linear algebra"](https://www.youtube.com/watch?v=rHLEWRxRGiM)
- Ch6 ["The determinant | Chapter 6, Essence of linear algebra"](https://www.youtube.com/watch?v=Ip3X9LOh2dk)
- Ch7 ["Inverse matrices, column space and null space | Chapter 7, Essence of linear algebra"](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- Ch8 ["Nonsquare matrices as transformations between dimensions | Chapter 8, Essence of linear algebra"](https://www.youtube.com/watch?v=v8VSDg_WQlA)
- Ch9 ["Dot products and duality | Chapter 9, Essence of linear algebra"](https://www.youtube.com/watch?v=LyGKycYT2v0)
- Ch10 ["Cross products | Chapter 10, Essence of linear algebra"](https://www.youtube.com/watch?v=eu6i7WJeinw)
- Ch11 ["Cross products in the light of linear transformations | Chapter 11, Essence of linear algebra"](https://www.youtube.com/watch?v=BaM7OCEm3G0)
- Ch12 ["Cramer's rule, explained geometrically | Chapter 12, Essence of linear algebra"](https://www.youtube.com/watch?v=jBsC34PxzoM)
- Ch13 ["Change of basis | Chapter 13, Essence of linear algebra"](https://www.youtube.com/watch?v=P2LTAUO1TdA)
- Ch14 ["Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra"](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- Ch15 ["A quick trick for computing eigenvalues | Chapter 15, Essence of linear algebra"](https://www.youtube.com/watch?v=e50Bj7jn9IQ)
- Ch16 ["Abstract vector spaces | Chapter 16, Essence of linear algebra"](https://www.youtube.com/watch?v=TgKwz5Ikpc8)

**Essence of calculus.** 12 videos, ~3h11m. Playlist: [Essence of calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- Ch1 ["The essence of calculus"](https://www.youtube.com/watch?v=WUvTyaaNkzM)
- Ch2 ["The paradox of the derivative | Chapter 2, Essence of calculus"](https://www.youtube.com/watch?v=9vKqVkMQHKk)
- Ch3 ["Derivative formulas through geometry | Chapter 3, Essence of calculus"](https://www.youtube.com/watch?v=S0_qX4VJhMQ)
- Ch4 ["Visualizing the chain rule and product rule | Chapter 4, Essence of calculus"](https://www.youtube.com/watch?v=YG15m2VwSjA) (the chain-rule chapter needed for backprop)
- Ch5 ["What's so special about Euler's number e? | Chapter 5, Essence of calculus"](https://www.youtube.com/watch?v=m2MIpDrF7Es)
- Ch6 ["Implicit differentiation, what's going on here? | Chapter 6, Essence of calculus"](https://www.youtube.com/watch?v=qb40J4N1fa4)
- Ch7 ["Limits, L'Hôpital's rule, and epsilon delta definitions | Chapter 7, Essence of calculus"](https://www.youtube.com/watch?v=kfF40MiS7zA)
- Ch8 ["Integration and the fundamental theorem of calculus | Chapter 8, Essence of calculus"](https://www.youtube.com/watch?v=rfG8ce4nNh0)
- Ch9 ["What does area have to do with slope? | Chapter 9, Essence of calculus"](https://www.youtube.com/watch?v=FnJqaIESC2s)
- Ch10 ["Higher order derivatives | Chapter 10, Essence of calculus"](https://www.youtube.com/watch?v=BLkz5LGWihw)
- Ch11 ["Taylor series | Chapter 11, Essence of calculus"](https://www.youtube.com/watch?v=3d6DsjIBzJ4)
- Ch12 ["The other way to visualize derivatives | Chapter 12, Essence of calculus"](https://www.youtube.com/watch?v=CfW845LNObM)

**Neural networks.** 10 videos, ~3h37m, in current playlist order: [Neural networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi). Companion page: [3blue1brown.com/topics/neural-networks](https://www.3blue1brown.com/topics/neural-networks)
1. ["But what is a neural network? | Deep learning chapter 1"](https://www.youtube.com/watch?v=aircAruvnKk) (18m)
2. ["Gradient descent, how neural networks learn | Deep Learning Chapter 2"](https://www.youtube.com/watch?v=IHZwWFHWa-w) (20m)
3. ["Backpropagation, intuitively | Deep Learning Chapter 3"](https://www.youtube.com/watch?v=Ilg3gGewQ5U) (12m; older title "What is backpropagation really doing?")
4. ["Backpropagation calculus | Deep Learning Chapter 4"](https://www.youtube.com/watch?v=tIeHLnjs5U8) (10m)
5. ["Large Language Models explained briefly"](https://www.youtube.com/watch?v=LPZh9BOjkQs) (7m; published 2024-11-20)
6. ["Transformers, the tech behind LLMs | Deep Learning Chapter 5"](https://www.youtube.com/watch?v=wjZofJX0v4M) (27m)
7. ["Attention in transformers, step-by-step | Deep Learning Chapter 6"](https://www.youtube.com/watch?v=eMlx5fFNoYc) (26m)
8. ["How might LLMs store facts | Deep Learning Chapter 7"](https://www.youtube.com/watch?v=9-Jl0dxWQs8) (22m)
9. ["But what is cross-entropy? | Compression is Intelligence Part 2"](https://www.youtube.com/watch?v=GlYgs6v2YfU) (33m; **NEW, 2026-07-16**)
10. ["But how do AI images and videos actually work? | Guest video by Welch Labs"](https://www.youtube.com/watch?v=iv-5mZ_9CPY) (37m; **NEW, 2025-07-25**)
- Not in the playlist: ["Reinventing Entropy | Compression is Intelligence Part 1"](https://www.youtube.com/watch?v=l6DKRf-fAAM) (32m; **NEW, 2026-06-07**). It builds entropy / −log₂(p) coding from Shannon's question and connects prediction with compression, per a description of the series in [a post on X](https://x.com/felixudr/status/2077786214833242225).

**Probability and convolution videos**
- ["Bayes theorem, the geometry of changing beliefs"](https://www.youtube.com/watch?v=HZGCoVF3YvM) (15m; 2019-12-22)
- ["The medical test paradox, and redesigning Bayes' rule"](https://www.youtube.com/watch?v=lG4VkPoG3ko) (Bayes follow-up; useful for sensitivity/specificity intuition)
- ["But what is the Central Limit Theorem?"](https://www.youtube.com/watch?v=zeJD6dqJ5lo) (31m; 2023-03-14)
- CLT follow-ups: ["Why π is in the normal distribution (beyond integral tricks)"](https://www.youtube.com/watch?v=cy8r7WSuT1I), ["A pretty reason why Gaussian + Gaussian = Gaussian"](https://www.youtube.com/watch?v=d_qvLDhkg00), ["Convolutions | Why X+Y in probability is a beautiful mess"](https://www.youtube.com/watch?v=IaSGqQa5O-M)
- ["Binomial distributions | Probabilities of probabilities, part 1"](https://www.youtube.com/watch?v=8idr1WZ1A7Q)
- ["But what is a convolution?"](https://www.youtube.com/watch?v=KuXjwB4LzSA) (23m; 2022-11-18; covers image blurring/kernels, the core CV-basics intuition)

### Inferences
- **Primary** for LA and calculus intuition: 3b1b. Assign LA Ch1–4, 9, 13–14 and calculus Ch1–4 as the minimum ML-relevant set, and pair them with practice from Khan Academy (Q4) or the MML book (Q6). 3b1b has no exercises.
- **Primary** first exposure to neural networks: NN videos 1–4. Videos 5–8 (~80 min) make a strong LLM-literacy block that also suits the AI-literacy stage. Video 5 ("LLMs explained briefly") is the gentlest on-ramp.
- The "Compression is Intelligence" Part 1 + Part 2 pair (~65 min) is an excellent optional bridge from probability (entropy) to the cross-entropy loss. Because Part 1 is not in the NN playlist, link it directly.
- "But what is a convolution?" is the best **primary** intuition video for CNN kernels. Follow it with StatQuest's CNN video (Q2) as the **alternate**/concrete explanation.

### Gaps
- Per-chapter durations for the LA and calculus series were not captured (playlist totals only).
- It is unconfirmed whether a Part 3 of "Compression is Intelligence" has been released (one post calls it a "trilogy"; only Parts 1–2 were found).

---

## Q2. StatQuest (Josh Starmer): playlists and individual videos

### Takeaway
All three StatQuest playlists and **every requested topic video ID are verified live**. The NN/DL playlist now has 33 videos. Recent additions include "Encoder-Only Transformers (like BERT) for RAG" (2024-11-17), "The matrix math behind transformer neural networks" (2024-04-07) and "RLHF" (2025-05-04). Two different videos share the title "Linear Regression, Clearly Explained!!!". Use the **2022 remake (7ArmBVF2dCs)**, not the 2017 original (nk2CQITm_eo). StatQuest is free on YouTube with no certificate. It is the best *worked-numbers* explainer for statistics and classical ML concepts.

### Cited Findings
**Playlists** (creator: StatQuest with Josh Starmer)
- [Statistics Fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9): 62 videos, ~10h47m
- [Machine Learning](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF): 106 videos (the first 100 total ~27h22m, so ~28–29h overall)
- [Neural Networks / Deep Learning](https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1): 33 videos, ~10h51m
- Topic index on the author's site: [statquest.org/video-index/](https://statquest.org/video-index/) (now serves a "Redirecting to new page" stub)

**Statistics: individual videos** (exact titles)
- Histograms: ["StatQuest: Histograms, Clearly Explained"](https://www.youtube.com/watch?v=qBigTkBLU6g)
- Mean/variance/SD: ["Calculating the Mean, Variance and Standard Deviation, Clearly Explained!!!"](https://www.youtube.com/watch?v=SzZ6GpcfoQY)
- Population vs sample: ["Population and Estimated Parameters, Clearly Explained!!!"](https://www.youtube.com/watch?v=vikkiwjQqfU)
- Normal distribution: ["The Normal Distribution, Clearly Explained!!!"](https://www.youtube.com/watch?v=rzFX5NWojp0)
- SD vs SE: ["Standard Deviation vs Standard Error, Clearly Explained!!!"](https://www.youtube.com/watch?v=A82brFpdr9g)
- Expected values: ["Expected Values, Main Ideas!!!"](https://www.youtube.com/watch?v=KLs_7b7SKi4)
- p-values: ["p-values: What they are and how to interpret them"](https://www.youtube.com/watch?v=vemZtEM63GY) and ["How to calculate p-values"](https://www.youtube.com/watch?v=JQc3yx0-Q9E)
- Hypothesis testing: ["Hypothesis Testing and The Null Hypothesis, Clearly Explained!!!"](https://www.youtube.com/watch?v=0oc49DyA3hU)
- Power: ["Statistical Power, Clearly Explained!!!"](https://www.youtube.com/watch?v=Rsc5znwR5FA)
- Probability vs likelihood: ["In Statistics, Probability is not Likelihood."](https://www.youtube.com/watch?v=pYxNSUDSFH4)
- Maximum likelihood: ["Maximum Likelihood, clearly explained!!!"](https://www.youtube.com/watch?v=XepXtl9YKwc)
- CLT: ["The Central Limit Theorem, Clearly Explained!!!"](https://www.youtube.com/watch?v=YAlJCEDH2uY)
- Bayes: ["Bayes' Theorem, Clearly Explained!!!!"](https://www.youtube.com/watch?v=9wCnvr7Xw4E)
- Covariance: ["Covariance, Clearly Explained!!!"](https://www.youtube.com/watch?v=qtaqvPAeEJY)
- Correlation: ["Pearson's Correlation, Clearly Explained!!!"](https://www.youtube.com/watch?v=xZ_z8KWkhXE)
- R²: ["R-squared, Clearly Explained!!!"](https://www.youtube.com/watch?v=2AQKmw14mHM)
- Odds: ["Odds and Log(Odds), Clearly Explained!!!"](https://www.youtube.com/watch?v=ARfXDSkQf1Y)

**Machine learning: individual videos**
- Intro: ["A Gentle Introduction to Machine Learning"](https://www.youtube.com/watch?v=Gv9_4yMHFhI)
- Least squares: ["The Main Ideas of Fitting a Line to Data (The Main Ideas of Least Squares and Linear Regression.)"](https://www.youtube.com/watch?v=PaFPbb66DxQ)
- Linear regression: ["Linear Regression, Clearly Explained!!!"](https://www.youtube.com/watch?v=7ArmBVF2dCs) (2022-11-18). Same-title older version (2017-07-24): [nk2CQITm_eo](https://www.youtube.com/watch?v=nk2CQITm_eo)
- Logistic regression: ["StatQuest: Logistic Regression"](https://www.youtube.com/watch?v=yIYKR4sgzI8), ["Logistic Regression Details Pt1: Coefficients"](https://www.youtube.com/watch?v=vN5cNN2-HWE), ["Logistic Regression Details Pt 2: Maximum Likelihood"](https://www.youtube.com/watch?v=BfKanl1aSG0)
- Gradient descent: ["Gradient Descent, Step-by-Step"](https://www.youtube.com/watch?v=sDv4f4s2SB8) (2019-02-05, 23m), ["Stochastic Gradient Descent, Clearly Explained!!!"](https://www.youtube.com/watch?v=vMh0zPT0tLI)
- Chain rule: ["The Chain Rule, Clearly Explained!!!"](https://www.youtube.com/watch?v=wl1myxrtQHQ) (18m)
- Cross-validation: ["Machine Learning Fundamentals: Cross Validation"](https://www.youtube.com/watch?v=fSytzGwwBVw)
- Confusion matrix: ["Machine Learning Fundamentals: The Confusion Matrix"](https://www.youtube.com/watch?v=Kdsp6soqA7o)
- Sensitivity/specificity: ["Machine Learning Fundamentals: Sensitivity and Specificity"](https://www.youtube.com/watch?v=vP06aMoz4v8)
- ROC/AUC: ["ROC and AUC, Clearly Explained!"](https://www.youtube.com/watch?v=4jRBRDbJemM)
- Bias–variance: ["Machine Learning Fundamentals: Bias and Variance"](https://www.youtube.com/watch?v=EuBBz3bI-aA)
- Ridge: ["Regularization Part 1: Ridge (L2) Regression"](https://www.youtube.com/watch?v=Q81RR3yKn30). Lasso: ["Regularization Part 2: Lasso (L1) Regression"](https://www.youtube.com/watch?v=NGf0voTMlcs). Elastic net: ["Regularization Part 3: Elastic Net Regression"](https://www.youtube.com/watch?v=1dKRdX9bfIo). Comparison: ["Ridge vs Lasso Regression, Visualized!!!"](https://www.youtube.com/watch?v=Xm2C_gTAl8c)
- Decision trees: ["Decision and Classification Trees, Clearly Explained!!!"](https://www.youtube.com/watch?v=_L39rN6gz7Y), ["Regression Trees, Clearly Explained!!!"](https://www.youtube.com/watch?v=g9c66TUylZ4)
- Random forests: ["StatQuest: Random Forests Part 1 - Building, Using and Evaluating"](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ), ["StatQuest: Random Forests Part 2: Missing data and clustering"](https://www.youtube.com/watch?v=sQ870aTKqiM)
- AdaBoost: ["AdaBoost, Clearly Explained"](https://www.youtube.com/watch?v=LsK-xG1cLYA)
- Gradient boost: ["Gradient Boost Part 1 (of 4): Regression Main Ideas"](https://www.youtube.com/watch?v=3CC4N4z3GJc), ["Gradient Boost Part 2 (of 4): Regression Details"](https://www.youtube.com/watch?v=2xudPOBz-vs), ["Gradient Boost Part 3 (of 4): Classification"](https://www.youtube.com/watch?v=jxuNLH5dXCs), ["Gradient Boost Part 4 (of 4): Classification Details"](https://www.youtube.com/watch?v=StWY5QWMXCw)
- XGBoost: ["XGBoost Part 1 (of 4): Regression"](https://www.youtube.com/watch?v=OtD8wVaFm6E), ["XGBoost Part 2 (of 4): Classification"](https://www.youtube.com/watch?v=8b1JEDvenQU), ["XGBoost Part 3 (of 4): Mathematical Details"](https://www.youtube.com/watch?v=ZVFeW798-2I), ["XGBoost Part 4 (of 4): Crazy Cool Optimizations"](https://www.youtube.com/watch?v=oRrKeUCEbq8)
- SVM: ["Support Vector Machines Part 1 (of 3): Main Ideas!!!"](https://www.youtube.com/watch?v=efR1C6CvhmE), ["Support Vector Machines Part 2: The Polynomial Kernel (Part 2 of 3)"](https://www.youtube.com/watch?v=Toet3EiSFcM), ["Support Vector Machines Part 3: The Radial (RBF) Kernel (Part 3 of 3)"](https://www.youtube.com/watch?v=Qc5IyLW_hns)
- Naive Bayes: ["Naive Bayes, Clearly Explained!!!"](https://www.youtube.com/watch?v=O2L2Uv9pdDA), ["Gaussian Naive Bayes, Clearly Explained!!!"](https://www.youtube.com/watch?v=H3EjCKtlVog)
- k-NN: ["StatQuest: K-nearest neighbors, Clearly Explained"](https://www.youtube.com/watch?v=HVXime0nQeI)
- k-means: ["StatQuest: K-means clustering"](https://www.youtube.com/watch?v=4b5d3muPQmA)
- Hierarchical clustering: ["StatQuest: Hierarchical Clustering"](https://www.youtube.com/watch?v=7xHsRkOdVwo)
- PCA: ["StatQuest: Principal Component Analysis (PCA), Step-by-Step"](https://www.youtube.com/watch?v=FgakZw6K1QQ). Short version: ["StatQuest: PCA main ideas in only 5 minutes!!!"](https://www.youtube.com/watch?v=HMOI_lkzW08)
- t-SNE: ["StatQuest: t-SNE, Clearly Explained"](https://www.youtube.com/watch?v=NEaUSP4YerM)
- Cosine similarity: ["Cosine Similarity, Clearly Explained!!!"](https://www.youtube.com/watch?v=e9U0QAFbfLI)

**Neural Networks / Deep Learning playlist** (full current order, lengths): [playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1)
1. "Happy Halloween (Neural Networks Are Not Scary)" (<1m, zxagGtF9MeU)
2. ["The Essential Main Ideas of Neural Networks"](https://www.youtube.com/watch?v=CqOfi41LfDw) (18m): neural networks part 1
3. ["The Chain Rule, Clearly Explained!!!"](https://www.youtube.com/watch?v=wl1myxrtQHQ) (18m)
4. ["Gradient Descent, Step-by-Step"](https://www.youtube.com/watch?v=sDv4f4s2SB8) (23m)
5. ["Neural Networks Pt. 2: Backpropagation Main Ideas"](https://www.youtube.com/watch?v=IN2XmBhILt4) (17m)
6. ["Backpropagation Details Pt. 1: Optimizing 3 parameters simultaneously."](https://www.youtube.com/watch?v=iyn2zdALii8) (18m)
7. ["Backpropagation Details Pt. 2: Going bonkers with The Chain Rule"](https://www.youtube.com/watch?v=GKZoOHXGcLo) (13m)
8. ["Neural Networks Pt. 3: ReLU In Action!!!"](https://www.youtube.com/watch?v=68BZ5f7P94E) (8m)
9. ["Neural Networks Pt. 4: Multiple Inputs and Outputs"](https://www.youtube.com/watch?v=83LYR-1IcjA) (13m)
10. ["Neural Networks Part 5: ArgMax and SoftMax"](https://www.youtube.com/watch?v=KpKog-L9veg) (14m)
11. ["The SoftMax Derivative, Step-by-Step!!!"](https://www.youtube.com/watch?v=M59JElEPgIg) (7m)
12. ["Neural Networks Part 6: Cross Entropy"](https://www.youtube.com/watch?v=6ArSys5qHAU) (9m)
13. ["Neural Networks Part 7: Cross Entropy Derivatives and Backpropagation"](https://www.youtube.com/watch?v=xBEh66V9gZo) (22m)
14. ["Neural Networks Part 8: Image Classification with Convolutional Neural Networks (CNNs)"](https://www.youtube.com/watch?v=HGwBXDKFk9I) (15m)
15. ["Recurrent Neural Networks (RNNs), Clearly Explained!!!"](https://www.youtube.com/watch?v=AsNTP8Kwu80) (16m)
16. ["Long Short-Term Memory (LSTM), Clearly Explained"](https://www.youtube.com/watch?v=YCzL96nL7j0) (20m)
17. ["Word Embedding and Word2Vec, Clearly Explained!!!"](https://www.youtube.com/watch?v=viZrOnJclY0) (16m)
18. ["Sequence-to-Sequence (seq2seq) Encoder-Decoder Neural Networks, Clearly Explained!!!"](https://www.youtube.com/watch?v=L8HKweZIOmg) (16m)
19. ["Attention for Neural Networks, Clearly Explained!!!"](https://www.youtube.com/watch?v=PSs6nxngL6k) (15m)
20. ["Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!"](https://www.youtube.com/watch?v=zxQyTK8quyY) (36m)
21. ["Decoder-Only Transformers, ChatGPTs specific Transformer, Clearly Explained!!!"](https://www.youtube.com/watch?v=bQ5BoolX9Ag) (36m)
22. ["Encoder-Only Transformers (like BERT) for RAG, Clearly Explained!!!"](https://www.youtube.com/watch?v=GDN649X_acE) (18m; 2024-11-17)
23. ["Reinforcement Learning with Neural Networks: Essential Concepts"](https://www.youtube.com/watch?v=9hbQieQh7-o) (24m)
24. ["Reinforcement Learning with Neural Networks: Mathematical Details"](https://www.youtube.com/watch?v=DVGmsnxB2UQ) (25m)
25. ["Reinforcement Learning with Human Feedback (RLHF), Clearly Explained!!!"](https://www.youtube.com/watch?v=qPN_XZcJf_s) (18m; 2025-05-04)
26. ["Tensors for Neural Networks, Clearly Explained!!!"](https://www.youtube.com/watch?v=L35fFDpwIM4) (9m)
27. ["Essential Matrix Algebra for Neural Networks, Clearly Explained!!!"](https://www.youtube.com/watch?v=ZTt9gsGcdDo) (30m)
28. ["The matrix math behind transformer neural networks, one step at a time!!!"](https://www.youtube.com/watch?v=KphmOJnLAdI) (23m; 2024-04-07)
29. ["The StatQuest Introduction to PyTorch"](https://www.youtube.com/watch?v=FHdlXe1bSe4) (23m)
30. ["Introduction to Coding Neural Networks with PyTorch and Lightning"](https://www.youtube.com/watch?v=khMzi6xPbuM) (20m)
31. ["Long Short-Term Memory with PyTorch + Lightning"](https://www.youtube.com/watch?v=RHGiXPuo_pI) (33m)
32. ["Word Embedding in PyTorch + Lightning"](https://www.youtube.com/watch?v=Qf06XDYXCXI) (32m)
33. ["Coding a ChatGPT Like Transformer From Scratch in PyTorch"](https://www.youtube.com/watch?v=C9QSpl5nmrY) (31m)

### Inferences
- StatQuest videos are short (mostly 5–25 min), so link them **per concept** next to the matching exercise instead of assigning whole playlists. A "must-watch" statistics core for ML is ~15 videos (~3–4h): mean/variance/SD, normal distribution, SD vs SE, p-values, hypothesis testing, probability vs likelihood, MLE, CLT, Bayes, covariance, correlation and R².
- **Primary** for classical-ML concepts: StatQuest (worked numeric examples). The **alternate** for rigor is ISLP chapters (Q6) or CS229 (Q5).
- For neural networks, 3b1b NN Ch1–4 comes first (intuition), then StatQuest NN items 2–13 (worked arithmetic of backprop, ReLU, softmax, cross-entropy). Karpathy's micrograd (Q3) is the code-first alternate. The three complement each other rather than duplicate.
- StatQuest #29 ("The StatQuest Introduction to PyTorch") is a gentle 23-min bridge into PyTorch before the official "Learn the Basics" tutorial (Q5).

### Gaps
- Per-video durations for the statistics and ML individual videos were not captured (playlist totals only).
- StatQuest sells optional PDF study guides and books (not needed; all videos are free). Current prices were not checked.

---

## Q3. Andrej Karpathy: "Neural Networks: Zero to Hero"

### Takeaway
The playlist is verified live with **10 videos (~19h21m)**, including "State of GPT | BRK216HFS" (a 2023 Microsoft Build talk) between the GPT build and the tokenizer video. It is free, with no certificate. It is the best **build-from-scratch** deep-learning resource but *advanced for an absolute beginner*. Place it after 3b1b/StatQuest NN basics and some Python/NumPy. The micrograd/makemore videos run on CPU or free Colab. The GPT-2 reproduction needs serious GPUs, so watch it rather than run it at full scale.

### Cited Findings
- Playlist [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) (10 videos, ~19h21m). Course page (live): [karpathy.ai/zero-to-hero.html](https://karpathy.ai/zero-to-hero.html). Code: [github.com/karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) (not archived; last push 2024-08-18; ~24.5k stars)
  1. ["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0) (2h25m)
  2. ["The spelled-out intro to language modeling: building makemore"](https://www.youtube.com/watch?v=PaCmpygFfXo) (1h57m)
  3. ["Building makemore Part 2: MLP"](https://www.youtube.com/watch?v=TCH_1BHY58I) (1h15m)
  4. ["Building makemore Part 3: Activations & Gradients, BatchNorm"](https://www.youtube.com/watch?v=P6sfmUTpUmc) (1h55m)
  5. ["Building makemore Part 4: Becoming a Backprop Ninja"](https://www.youtube.com/watch?v=q8SA3rM6ckI) (1h55m)
  6. ["Building makemore Part 5: Building a WaveNet"](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) (56m)
  7. ["Let's build GPT: from scratch, in code, spelled out."](https://www.youtube.com/watch?v=kCc8FmEb1nY) (1h56m)
  8. ["State of GPT | BRK216HFS"](https://www.youtube.com/watch?v=bZQun8Y4L2A) (42m; 2023-05-25)
  9. ["Let's build the GPT Tokenizer"](https://www.youtube.com/watch?v=zduSFxRajkE) (2h13m)
  10. ["Let's reproduce GPT-2 (124M)"](https://www.youtube.com/watch?v=l8pRSuU81PU) (4h01m)
- Karpathy's general-audience LLM talks (verified; good for the AI-literacy stage): ["[1hr Talk] Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g), ["Deep Dive into LLMs like ChatGPT"](https://www.youtube.com/watch?v=7xTGNNLPyMI), ["How I use LLMs"](https://www.youtube.com/watch?v=EWvNQjAaOHw)

### Inferences
- Video 1 (micrograd) is the best **code-first alternate** explanation of backpropagation. Assign it right after 3b1b Ch3–4 and StatQuest's backprop videos. Videos 2–3 teach the PyTorch tensor mindset. Videos 7–10 are optional for a foundations track and fit a later "LLMs" phase.
- "How I use LLMs" plus "Intro to LLMs" are strong, zero-math **primary** picks for AI literacy (alongside Elements of AI, Q5).

### Gaps
- None for IDs. Videos added after 2026-09-24 are unknown.

---

## Q4. Khan Academy (linear algebra, multivariable calculus incl. gradient, statistics & probability)

### Takeaway
All four Khan Academy URLs return HTTP 200 as of 2026-09-24. Khan Academy is free, with exercises, and is the natural **practice companion** to 3b1b. The pages are JavaScript-rendered, so unit-level structure could not be machine-verified.

### Cited Findings
- Linear algebra: [khanacademy.org/math/linear-algebra](https://www.khanacademy.org/math/linear-algebra) (HTTP 200)
- Multivariable calculus: [khanacademy.org/math/multivariable-calculus](https://www.khanacademy.org/math/multivariable-calculus) (HTTP 200)
- "The gradient" article: [khanacademy.org/.../partial-derivative-and-gradient-articles/a/the-gradient](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/the-gradient) (HTTP 200)
- Statistics and probability: [khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability) (HTTP 200)
- Alternate rigorous linear algebra course (live): [MIT OCW 18.06SC Linear Algebra (Fall 2011)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)
- Alternate long-form videos (freeCodeCamp, verified): ["Linear Algebra - Full College Course"](https://www.youtube.com/watch?v=JnTa9XtvmfI), ["Calculus 1 - Full College Course"](https://www.youtube.com/watch?v=HfACrKJ_Y2w), ["Statistics - A Full University Course on Data Science Basics"](https://www.youtube.com/watch?v=xxpc-HPKN28)

### Inferences
- Use Khan Academy for **exercises**, not as the first explanation. Recommended use: after each 3b1b chapter, do the matching Khan unit. For multivariable calculus, only partial derivatives, the gradient and the directional derivative are essential for ML foundations.
- Khan's multivariable-calculus videos are widely known to be presented by Grant Sanderson (3b1b). This was not re-verified today.

### Gaps
- Unit names/counts inside the Khan courses are UNVERIFIED (JS-rendered pages). Khan does not issue certificates (not re-verified).

---

## Q5. Courses: fast.ai, MIT 6.S191, Stanford CS229/CS230/CS231n, Google MLCC, Kaggle Learn, Daniel Bourke PyTorch, PyTorch "Learn the Basics", CS50 AI, Elements of AI, Microsoft "For Beginners", freeCodeCamp, Corey Schafer, MIT Missing Semester, Learn Git Branching, GitHub Skills, Pro Git

### Takeaway
All of these resources are live. Notable 2025–2026 changes:
- **MIT 6.S191 has a 2026 edition** (in-person Jan 5–9, 2026; lectures released online weekly from 2026-03-30 to 2026-05-25).
- **Stanford CS231n Spring 2025** lectures are on YouTube (18 lectures, ~21h13m, published from 2025-09-02).
- **MIT Missing Semester has a 2026 edition** (9 lectures, incl. "Agentic Coding"; AI tools folded into each lecture).
- fast.ai is still the **2022** "Practical Deep Learning for Coders" and uses **Kaggle notebooks with free GPUs** (phone verification required).
- **freeCodeCamp's "Data Analysis with Python" and "Machine Learning with Python" certifications are now classified as *legacy*** in freeCodeCamp's own source code.
- **GitHub Skills (skills.github.com) now redirects to GitHub Learn**.
- **PyTorch tutorials moved to docs.pytorch.org**.
- CS229 (2018) videos have **embedding disabled**, so link to YouTube and do not embed.

### Cited Findings

**fast.ai: "Practical Deep Learning for Coders" (Jeremy Howard)**
- Site [course.fast.ai](https://course.fast.ai/): "A free course designed for people with some coding experience". Part 1 is "Practical Deep Learning for Coders 2022 part 1, recorded at the University of Queensland". The site says "There are 9 lessons, and each lesson is around 90 minutes long", "You don't need any special hardware or software", and "You don't need any university math either". Part 2 is "Deep Learning Foundations to Stable Diffusion" (lessons 9–25 plus bonus 9a/9b) — [course.fast.ai](https://course.fast.ai/)
- Platform: "We'll mainly use Kaggle Notebooks and Paperspace Gradient". "We strongly suggest not using your own computer for training models" — [course.fast.ai](https://course.fast.ai/). "Kaggle provides access to GPUs for free… In order to use a GPU on Kaggle, your account must be phone verified" — [course.fast.ai/Resources/kaggle.html](https://course.fast.ai/Resources/kaggle.html). Lesson pages link "Kaggle notebooks for this lesson" and a "Help: Using Colab or Kaggle" page — [lesson 1 page](https://course.fast.ai/Lessons/lesson1.html)
- YouTube playlist [Practical Deep Learning for Coders](https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU) (8 videos, ~12h34m):
  - L1 ["Practical Deep Learning for Coders: Lesson 1"](https://www.youtube.com/watch?v=8SF_h3xF3cE) (1h22m)
  - L2 [F4tvM4Vb3A0](https://www.youtube.com/watch?v=F4tvM4Vb3A0) (1h16m)
  - L3 [hBBOjCiFcuo](https://www.youtube.com/watch?v=hBBOjCiFcuo) (1h30m)
  - L4 [toUgBQv1BT8](https://www.youtube.com/watch?v=toUgBQv1BT8) (1h34m)
  - L5 [_rXzeWq4C6w](https://www.youtube.com/watch?v=_rXzeWq4C6w) (1h42m)
  - L6 [AdhG64NF76E](https://www.youtube.com/watch?v=AdhG64NF76E) (1h42m)
  - L7 [p4ZZq0736Po](https://www.youtube.com/watch?v=p4ZZq0736Po) (1h46m)
  - L8 [htiNBPxcXgo](https://www.youtube.com/watch?v=htiNBPxcXgo) (1h36m)
  - L2–L8 are titled "Lesson N: Practical Deep Learning for Coders 2022"
- Free book as notebooks: [github.com/fastai/fastbook](https://github.com/fastai/fastbook) (last push 2026-09-13; ~25.3k stars). Course notebooks: [github.com/fastai/course22](https://github.com/fastai/course22) (last push 2024-10-08)

**MIT 6.S191: Introduction to Deep Learning**
- Site [introtodeeplearning.com](https://introtodeeplearning.com/): "The 2026 in-person edition has completed". The schedule lists "Mon Jan 5 - Fri Jan 9, 2026" (in-person) and "Mon Mar 30 - Mon May 25, 2026" (online). "New lectures, slides, and labs will be open-sourced every week starting March 30 at 10AM ET". The site lists 9 lectures (Mar 30, Apr 6, 13, 20, 27, May 4, 11, 18, 25) plus Software Labs 1–3 — [introtodeeplearning.com](https://introtodeeplearning.com/)
- Labs repo moved: [github.com/aamini/introtodeeplearning](https://github.com/aamini/introtodeeplearning) now 301-redirects to [github.com/MITDeepLearning/introtodeeplearning](https://github.com/MITDeepLearning/introtodeeplearning) ("Lab Materials for MIT 6.S191"; last push 2026-01-04)
- Playlist [MIT 6.S191: Introduction to Deep Learning](https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI) (channel: Alexander Amini; 90 videos spanning 2018–2026)
- **2026 edition** (titles carry no year; ~8h15m total):
  - L1 ["MIT Introduction to Deep Learning | 6.S191"](https://www.youtube.com/watch?v=II4giR4vOOo) (56m; 2026-03-30)
  - L2 ["MIT 6.S191: Recurrent Neural Networks, Transformers, and Attention"](https://www.youtube.com/watch?v=d02VkQ9MP44) (57m; 2026-04-06)
  - L3 ["MIT 6.S191: Convolutional Neural Networks"](https://www.youtube.com/watch?v=pqIcoskUuWs) (56m; 2026-04-13)
  - L4 ["MIT 6.S191: Deep Generative Modeling"](https://www.youtube.com/watch?v=R8V8CbuxryI) (49m)
  - L5 ["MIT 6.S191: Reinforcement Learning"](https://www.youtube.com/watch?v=1ij3dweHu-0) (59m)
  - L6 ["MIT 6.S191: Language Models and New Frontiers"](https://www.youtube.com/watch?v=ev7cLSd-ySE) (56m)
  - L7 ["MIT 6.S191: The Three Laws of AI"](https://www.youtube.com/watch?v=XKOpA7iaJvg) (51m; 2026-05-11)
  - L8 ["MIT 6.S191: AI for Science"](https://www.youtube.com/watch?v=rZACoZD8AG8) (59m)
  - L9 ["MIT 6.S191: Secrets of Massively Parallel Training"](https://www.youtube.com/watch?v=UZZD9d9YqnQ) (52m; 2026-05-25)
- **2025 edition** (~9h39m):
  - ["MIT Introduction to Deep Learning (2025) | 6.S191"](https://www.youtube.com/watch?v=alfdI7S6wCY) (1h09m; 2025-03-03)
  - ["MIT 6.S191 (2025): Recurrent Neural Networks, Transformers, and Attention"](https://www.youtube.com/watch?v=GvezxUdLrEk)
  - ["MIT 6.S191 (2025): Convolutional Neural Networks"](https://www.youtube.com/watch?v=oGpzWAlP5p0)
  - ["MIT 6.S191 (2025): Deep Generative Modeling"](https://www.youtube.com/watch?v=SdTZAMDKrNY)
  - ["MIT 6.S191 (2025): Reinforcement Learning"](https://www.youtube.com/watch?v=to-lHJfK4pw)
  - ["MIT 6.S191 (2025): Language Models and New Frontiers"](https://www.youtube.com/watch?v=HLKo4fJx_7k)
  - Guest lectures: ["(2025): Large Language Models (Google)"](https://www.youtube.com/watch?v=ZNodOsz94cc), ["(2025): Large Language Models (Liquid AI)"](https://www.youtube.com/watch?v=_HfdncCbMOE), ["(2025): A Hipocratic Oath, for *your* AI (Comet ML)"](https://www.youtube.com/watch?v=CyCUZAf8xSU), ["(2025): AI for Biology (Microsoft)"](https://www.youtube.com/watch?v=SSzSOeGP87I)

**Stanford (on YouTube)**
- **CS229 Machine Learning (Andrew Ng, Autumn 2018)**: playlist ["Stanford CS229: Machine Learning led by Andrew Ng | Autumn 2018"](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) (21 videos, ~27h51m). Lecture 1: ["Stanford CS229: Machine Learning Lecture 1 - Andrew Ng (Autumn 2018)"](https://www.youtube.com/watch?v=jGwO_UgTS7I) (1h15m) is playable but has **embedding disabled** (oEmbed 401; watch page `playableInEmbed:false`). Course site [cs229.stanford.edu](https://cs229.stanford.edu/) (live; currently a Summer 2026 offering; no newer public YouTube series was found).
- **CS230 Deep Learning (Autumn 2018)**: playlist ["Stanford CS230: Deep Learning | Autumn 2018"](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb) (10 videos, ~12h23m). The site [cs230.stanford.edu](https://cs230.stanford.edu/) says current lectures are on Canvas and still links "Lecture videos (Fall 2018)". Its core content is modules of the deeplearning.ai Deep Learning Specialization on Coursera.
- **CS231n Deep Learning for Computer Vision, Spring 2025 (NEW)**: playlist ["Stanford CS231N Deep Learning for Computer Vision I 2025"](https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16) (Stanford Online; 18 lectures, ~21h13m; L1 published 2025-09-02)
  - L1 ["...Spring 2025 | Lecture 1: Introduction"](https://www.youtube.com/watch?v=2fq9wYslV0A) (1h02m)
  - L2 "Image Classification with Linear Classifiers" [pdqofxJeBN8](https://www.youtube.com/watch?v=pdqofxJeBN8)
  - L3 "Regularization and Optimization" [dyNGd06MWn4](https://www.youtube.com/watch?v=dyNGd06MWn4)
  - L4 "Neural Networks and Backpropagation" [25zD5qJHYsk](https://www.youtube.com/watch?v=25zD5qJHYsk)
  - L5 "Image Classification with CNNs" [f3g1zGdxptI](https://www.youtube.com/watch?v=f3g1zGdxptI)
  - L6 "CNN Architectures" [aVJy4O5TOk8](https://www.youtube.com/watch?v=aVJy4O5TOk8)
  - L7 "Recurrent Neural Networks" [kG2lAPBF7zA](https://www.youtube.com/watch?v=kG2lAPBF7zA)
  - L8 "Attention and Transformers" [RQowiOF_FvQ](https://www.youtube.com/watch?v=RQowiOF_FvQ)
  - L9 "Object Detection, Image Segmentation, Visualizing" [PTypu6GqEd4](https://www.youtube.com/watch?v=PTypu6GqEd4)
  - L10 "Video Understanding" [wElqklprhPE](https://www.youtube.com/watch?v=wElqklprhPE)
  - L11 "Large Scale Distributed Training" [9MvD-XsowsE](https://www.youtube.com/watch?v=9MvD-XsowsE)
  - L12 "Self-Supervised Learning" [4howBU7THbM](https://www.youtube.com/watch?v=4howBU7THbM)
  - L13 "Generative Models 1" [zbHXQRUNlH0](https://www.youtube.com/watch?v=zbHXQRUNlH0)
  - L14 "Generative Models 2" [Edr4uZFh4EE](https://www.youtube.com/watch?v=Edr4uZFh4EE)
  - L15 "3D Vision" [7lxrKDKtykM](https://www.youtube.com/watch?v=7lxrKDKtykM)
  - L16 "Vision and Language" [mQOK0Mfyrkk](https://www.youtube.com/watch?v=mQOK0Mfyrkk)
  - L17 "Robot Learning" [XSfmOH_xVSU](https://www.youtube.com/watch?v=XSfmOH_xVSU)
  - L18 "Human-Centered AI" [g8UaBfj6Sh8](https://www.youtube.com/watch?v=g8UaBfj6Sh8)
  - Site [cs231n.stanford.edu](https://cs231n.stanford.edu/) (Spring 2026 offering; its videos are Canvas-only, and "recordings from previous years are available on YouTube")
- CS231n Spring 2017 (older, still live): ["Lecture Collection | Convolutional Neural Networks for Visual Recognition (Spring 2017)"](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv) (16 videos, ~19h30m)

**Google Machine Learning Crash Course**: [developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course) (live). Current modules, per the page:
- ML Models: Linear Regression; Logistic Regression; Classification
- Data: Working with Numerical Data; Working with Categorical Data; Datasets, Generalization, and Overfitting
- Advanced ML models: Neural Networks; Embeddings; Intro to Large Language Models ("from tokens to Transformers")
- Real-world ML: Production ML Systems; AutoML; ML Fairness
- "Each Machine Learning Crash Course module is self-contained" — [MLCC](https://developers.google.com/machine-learning/crash-course)

**Kaggle Learn (free micro-courses, in-browser notebooks)**: [kaggle.com/learn](https://www.kaggle.com/learn) (live but bot-protected). Kaggle's own text as indexed by search: "Kaggle courses are provided at no cost to you, and you can now earn certificates"; certificates page [kaggle.com/learn-course-certificates](https://www.kaggle.com/learn-course-certificates) — [search index of kaggle.com/learn](https://www.kaggle.com/learn). Class Central lists **16 Kaggle courses** ("Free course", "With certificate"). 13 were captured with hours — [Class Central: Kaggle](https://www.classcentral.com/provider/kaggle):
- Python (5h)
- Pandas (4h)
- Data Visualization (4h)
- Intro to Machine Learning (3h)
- Intermediate Machine Learning (4h)
- Data Cleaning (4h)
- Intro to Deep Learning (4h; "Use TensorFlow and Keras…")
- Computer Vision (4h)
- Time Series (5h)
- Intro to SQL (2h)
- Advanced SQL (4h)
- Geospatial Analysis (4h)
- Intro to AI Ethics (4h)
- Course URL: [kaggle.com/learn/python](https://www.kaggle.com/learn/python) is confirmed by search index. Other course URLs follow the pattern `kaggle.com/learn/<slug>` (e.g., `/learn/pandas`, `/learn/intro-to-machine-learning`), but those slugs are **UNVERIFIED** (Kaggle blocks automated fetches).

**Daniel Bourke / Zero to Mastery: "Learn PyTorch for Deep Learning"**
- Online book [learnpytorch.io](https://www.learnpytorch.io/) ("Zero to Mastery Learn PyTorch for Deep Learning"): "All of the course materials are available for free in an online book". "The code is all written via Google Colab Notebooks". "Last update: April 16 2023". "Videos are done for chapters: 00 … 09 (all chapters!)" (the full video course is on the paid ZTM Academy). "First five sections on YouTube: … the first 25-hours of material". Certificates exist only via the paid ZTM videos — [learnpytorch.io](https://www.learnpytorch.io/)
- Repo [github.com/mrdbourke/pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning) (last push 2026-02-11; ~19.1k stars)
- Free YouTube, freeCodeCamp upload: ["PyTorch for Deep Learning & Machine Learning – Full Course"](https://www.youtube.com/watch?v=V_xro1bcAuA) (25h37m; 2022-10-06)
- Free YouTube, Daniel Bourke's own upload: ["Learn PyTorch for deep learning in a day. Literally."](https://www.youtube.com/watch?v=Z_ikDlimN6A) (25h36m; 2022-07-23)

**PyTorch official "Learn the Basics"**: [docs.pytorch.org/tutorials/beginner/basics/intro.html](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) (page title "Learn the Basics — PyTorch Tutorials 2.14.0+cu130 documentation"; the old pytorch.org/tutorials URL redirects here). The sections are:
- 0. Quickstart
- 1. Tensors
- 2. Datasets and DataLoaders
- 3. Transforms
- 4. Build Model
- 5. Autograd
- 6. Optimization Loop
- 7. Save, Load and Use Model
- "Each section has a 'Run in Google Colab' link at the top" — [PyTorch docs](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

**Harvard CS50's Introduction to AI with Python**: [cs50.harvard.edu/ai/](https://cs50.harvard.edu/ai/). It is free via OpenCourseWare ("seven weeks of material": 0 Search, 1 Knowledge, 2 Uncertainty, 3 Optimization, 4 Learning, 5 Neural Networks, 6 Language). Prerequisite: CS50x/CS50P "or at least one year of experience with Python". A paid verified certificate is available at cs50.edx.org/ai ([edX page](https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python)) and a professional certificate at cs50.edx.org/programs/ai. The page also links a "CS50 Certificate" option. The page states no edition year — [CS50 AI](https://cs50.harvard.edu/ai/)
- YouTube playlist ["CS50's Introduction to Artificial Intelligence with Python 2023"](https://www.youtube.com/playlist?list=PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm) (8 videos, ~11h50m):
  - Introduction [gR8QvFmNuLE](https://www.youtube.com/watch?v=gR8QvFmNuLE)
  - ["Search - Lecture 0"](https://www.youtube.com/watch?v=WbzNRTTrX0g) (1h49m)
  - ["Knowledge - Lecture 1"](https://www.youtube.com/watch?v=HWQLez87vqM)
  - ["Uncertainty - Lecture 2"](https://www.youtube.com/watch?v=D8RRq3TbtHU)
  - ["Optimization - Lecture 3"](https://www.youtube.com/watch?v=qK46ET1xk2A)
  - ["Learning - Lecture 4"](https://www.youtube.com/watch?v=-g0iJjnO2_w)
  - ["Neural Networks - Lecture 5"](https://www.youtube.com/watch?v=J1QD9hLDEDY)
  - ["Language - Lecture 6 - … 2023"](https://www.youtube.com/watch?v=QAZc9xsQNjQ) (1h05m)
  - Lectures 0–5 are 2020 recordings (re-uploaded 2023-07-24). The original 2020 upload of Lecture 0 [D5aJNFWsWew](https://www.youtube.com/watch?v=D5aJNFWsWew) is also live.

**Elements of AI (University of Helsinki + MinnaLearn)**: [elementsofai.com](https://www.elementsofai.com/). "Introduction to AI is a free online course for everyone… with no complicated math or programming required". "Building AI is a free online course… Some basic Python programming skills are recommended". "Over 2 million students have signed up" — [elementsofai.com](https://www.elementsofai.com/). Course apps: [course.elementsofai.com](https://course.elementsofai.com/) and [buildingai.elementsofai.com](https://buildingai.elementsofai.com/) (both HTTP 200). The FAQ includes "I have passed an Elements of AI course, where is my certificate?", "Which payment methods are available for the Building AI certificate?", "How can I get ECTS credits?" and "How to share your certificate in LinkedIn?" — [FAQ](https://www.elementsofai.com/faq). The home page also promotes a separate MinnaLearn "Get AI Ready 2026" course: "Earn a certificate on general AI literacy in 60 mins" — [elementsofai.com](https://www.elementsofai.com/)

**Microsoft "For Beginners" curricula (GitHub, free, notebook-based)**
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners): "12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all" (not archived; last push 2026-09-15; ~90.9k stars)
- [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners): "12 Weeks, 24 Lessons, AI for All!" (last push 2026-09-16; ~68.9k stars)
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners): "10 Weeks, 20 Lessons, Data Science for All!" (last push 2026-09-13; ~37.3k stars)
- Related: [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners): "21 Lessons" (last push 2026-09-24; ~120k stars)

**freeCodeCamp**
- YouTube (verified):
  - ["Machine Learning for Everybody – Full Course"](https://www.youtube.com/watch?v=i_LwzRVP7bg) (3h53m; 2022-09-26)
  - ["Data Analysis with Python - Full Course for Beginners (Numpy, Pandas, Matplotlib, Seaborn)"](https://www.youtube.com/watch?v=r-uOLxNrNk8) (4h22m; 2020-04-15)
  - ["Python NumPy Tutorial for Beginners"](https://www.youtube.com/watch?v=QUT1VHiLmmI) (58m; Keith Galli on the freeCodeCamp channel)
  - ["Git and GitHub for Beginners - Crash Course"](https://www.youtube.com/watch?v=RGOj5yH7evk)
  - The PyTorch full course is listed above
- Certifications: [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) and [Machine Learning with Python](https://www.freecodecamp.org/learn/machine-learning-with-python/) pages still resolve (HTTP 200). In freeCodeCamp's source (`certification-settings.ts`, main branch), `DataAnalysisPy = 'data-analysis-with-python-v7'` and `MachineLearningPy = 'machine-learning-with-python-v7'` are both listed in `legacyCertifications`. `currentCertifications` includes `PythonV9 = 'python-v9'`, and `FullStackDeveloperV9` is "upcoming" — [freeCodeCamp GitHub source](https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/packages/shared/src/config/certification-settings.ts). A code comment says "'Legacy' certifications are another class of standard certifications" — [same source](https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/packages/shared/src/config/certification-settings.ts)

**Python data stack on YouTube (NumPy/Pandas/Matplotlib)**
- Corey Schafer ["Pandas Tutorials"](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) (11 videos, ~5h19m)
- Corey Schafer ["Matplotlib Tutorials"](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) (10 videos, ~3h33m)
- Corey Schafer ["Python Programming Beginner Tutorials"](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)
- Keith Galli ["Complete Python Pandas Data Science Tutorial! (2025 Updated Edition)"](https://www.youtube.com/watch?v=2uvysYbKdjM) (1h34m; published 2024-06-29)
- codebasics ["Pandas Tutorial (Data Analysis In Python)"](https://www.youtube.com/playlist?list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy)

**Git and command line**
- **MIT "The Missing Semester of Your CS Education"**: [missing.csail.mit.edu](https://missing.csail.mit.edu/) now features the **2026** edition. Per the site: "we've instead folded the use of the latest applicable AI tools and techniques into each lecture directly", supported "as part of SIPB IAP 2026".
- YouTube ["Missing Semester IAP 2026"](https://www.youtube.com/playlist?list=PLyzOVJj3bHQunmnnTXrNbZnBaCA-ieK4L) (9 videos, ~10h02m):
  - L1 ["Lecture 1: Course Overview + Introduction to the Shell"](https://www.youtube.com/watch?v=MSgoeuMqUmU) (1h14m)
  - L2 "Command-line Environment" [ccBGsPedE9Q](https://www.youtube.com/watch?v=ccBGsPedE9Q)
  - L3 "Development Environment and Tools" [QnM1nVzrkx8](https://www.youtube.com/watch?v=QnM1nVzrkx8)
  - L4 "Debugging and Profiling" [8VYT9TcUmKs](https://www.youtube.com/watch?v=8VYT9TcUmKs)
  - L5 ["Lecture 5: Version Control and Git"](https://www.youtube.com/watch?v=9K8lB61dl3Y) (1h09m)
  - L6 "Packaging and Shipping Code" [KBMiB-8P4Ns](https://www.youtube.com/watch?v=KBMiB-8P4Ns)
  - L7 "Agentic Coding" [sTdz6PZoAnw](https://www.youtube.com/watch?v=sTdz6PZoAnw)
  - L8 "Beyond the Code" [2DOEATfXT8k](https://www.youtube.com/watch?v=2DOEATfXT8k)
  - L9 "Code Quality" [XBiLUNx84CQ](https://www.youtube.com/watch?v=XBiLUNx84CQ)
  - Older editions: ["Missing Semester IAP 2020"](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J) (11 videos, ~10h13m; L1 ["Lecture 1: Course Overview + The Shell (2020)"](https://www.youtube.com/watch?v=Z56Jmr9Z34Q)) and ["Hacker Tools 2019"](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuiujH1lpn8cA9dsyulbYRv) (18 videos)
- **Learn Git Branching** (interactive, in-browser): [learngitbranching.js.org](https://learngitbranching.js.org/) (live)
- **Pro Git** (free book, 2nd ed. online): [git-scm.com/book/en/v2](https://git-scm.com/book/en/v2) (live)
- **GitHub Skills**: [skills.github.com](https://skills.github.com/) is now a meta-refresh redirect to [learn.github.com/skills](https://learn.github.com/skills) ("GitHub Learn"). The org page [github.com/skills](https://github.com/skills) is live. The starter course [skills/introduction-to-github](https://github.com/skills/introduction-to-github) ("Get started using GitHub in less than an hour.") was last pushed 2026-06-22.
- Short Git videos: Corey Schafer ["Git Tutorial for Beginners: Command-Line Fundamentals"](https://www.youtube.com/watch?v=HVsySz-h9r4) and Programming with Mosh ["Git Tutorial for Beginners: Learn Git in 1 Hour"](https://www.youtube.com/watch?v=8JJ101D3knE)

### Inferences
**Weak-laptop fit.** Everything in the deep-learning part should run on **Kaggle Notebooks** (free GPU after phone verification; required by fast.ai) or **Google Colab** ("Run in Google Colab" links in the PyTorch tutorials, learnpytorch.io, Géron's notebooks, Think Stats). The local 8 GB laptop is fine for Python, NumPy, pandas, scikit-learn, Jupyter, Git and Kaggle Learn (browser).

**Recommended primary and alternate resources by topic** (my recommendations):

| Topic | Primary | Alternate |
|---|---|---|
| **AI literacy** | Elements of AI "Introduction to AI" (free, no math/code), then 3b1b "LLMs explained briefly" and Karpathy "How I use LLMs" | Google MLCC "Intro to LLMs" module; MIT 6.S191 2026 L1; AI For Everyone (Coursera: only the first module is free, see Q8) |
| **Python for data** | Kaggle Learn "Python", "Pandas", "Data Visualization" (browser-based, free certificates); VanderPlas's *Python Data Science Handbook* (Q6) as reference | Corey Schafer Pandas + Matplotlib playlists; Keith Galli pandas (2025 edition); freeCodeCamp "Data Analysis with Python" full course; codebasics Pandas |
| **Git/CLI** | Missing Semester 2026 L1 (shell) + L5 (Git), plus Learn Git Branching (interactive practice) | Pro Git chapters 1–3; GitHub Skills "Introduction to GitHub"; Corey Schafer or Mosh short videos |
| **Classical ML** | Kaggle "Intro to ML" + "Intermediate ML" (hands-on), StatQuest per concept, and ISLP or Géron notebooks (Q6) for scikit-learn depth | Google MLCC (modern, concise); Microsoft ML-For-Beginners; freeCodeCamp ML for Everybody; CS229 2018 (math-heavy, later) |
| **Deep learning and PyTorch** | 3b1b NN 1–4, then StatQuest NN, then PyTorch "Learn the Basics" (Colab), then **fast.ai Part 1** (Kaggle GPU) or learnpytorch.io chapters 00–04 | Karpathy Zero to Hero (from-scratch); MIT 6.S191 2026 lectures (compact survey); d2l.ai / UDL (Q6) |
| **Computer-vision basics** | 3b1b convolution video, then StatQuest CNN video, then Kaggle "Computer Vision" course and fast.ai lessons 1–2 (build and deploy an image classifier) | CS231n Spring 2025 L1–L6 (rigorous); MIT 6.S191 2026 L3 (CNNs) |

**freeCodeCamp certifications.** A learner can still take "Data Analysis with Python" and "Machine Learning with Python" as free project-based courses. A curriculum should describe their certificates as "legacy" and prefer the current `python-v9` certification if a freeCodeCamp credential is wanted. The claimability of legacy certs was inferred from source comments, not tested.

### Gaps
- MIT 6.S191 2026 L4–L6 and L8 publish dates were not individually fetched (their order and titles were). Whether the 6.S191 labs run on Colab in 2026 is UNVERIFIED. Whether 6.S191 offers any certificate to online learners is UNVERIFIED.
- fast.ai's site says Part 1 has "9 lessons", but the YouTube playlist has 8 lesson videos (Lessons 1–8). The discrepancy was not resolved. fast.ai offers no certificate (not stated on the pages fetched; UNVERIFIED).
- Google MLCC's total hours and whether it issues any certificate or badge were not verified.
- 3 of the 16 Kaggle course names and all Kaggle course slugs except `/learn/python` are UNVERIFIED.
- Elements of AI: whether the *Introduction to AI* certificate is still free is UNVERIFIED. The FAQ's mention of payment methods for the *Building AI* certificate suggests that one is paid.
- CS50 AI: the edition year is not stated on the page. Whether the free "CS50 Certificate" applies to CS50 AI in 2026 is UNVERIFIED.
- No newer public YouTube recordings of CS229 (after 2018) or CS230 (after 2018) were found. Absence is not proven.

---

## Q6. Free books (and their companion notebooks)

### Takeaway
All book sites are live and free to read online. Key 2023–2026 updates:
- **Aurélien Géron's new "Hands-On Machine Learning with Scikit-Learn and PyTorch" (1st edition)** has an active notebook repo (**ageron/handson-mlp**, last push 2026-09-03, Colab-ready). The TF/Keras 3rd-edition repo (handson-ml3) is still maintained.
- **Understanding Deep Learning's free PDF was updated 09 Feb 2026**.
- d2l.ai is v1.0.3 (Cambridge University Press 2023; PyTorch/JAX/TF/MXNet).
- ISLP (Python edition, 2023) has a free PDF.
- Think Stats is in its **3rd edition** with every chapter runnable on Colab.

### Cited Findings
- **Python Data Science Handbook** (Jake VanderPlas): [jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/). "Full text… available on GitHub in the form of Jupyter notebooks". The text is CC-BY-NC-ND and the code is MIT. The site shows "© 2012-2017" (i.e., the free site is the 1st-edition text). Repo [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) (last push 2024-06-26; ~50k stars)
- **Think Stats, 3rd edition** (Allen Downey): [allendowney.github.io/ThinkStats/](https://allendowney.github.io/ThinkStats/). "The third edition is available now". "This book is available under a Creative Commons license". Chapters 1–14 each have "Click here to run Chapter N on Colab". Repo [AllenDowney/ThinkStats](https://github.com/AllenDowney/ThinkStats) ("Notebooks for the third edition of Think Stats"; last push 2026-09-16)
- **Seeing Theory** (Brown University; interactive probability/statistics visualizations): [seeing-theory.brown.edu](https://seeing-theory.brown.edu/) (live)
- **Mathematics for Machine Learning** (Deisenroth, Faisal, Ong): [mml-book.github.io](https://mml-book.github.io/). "Published by Cambridge University Press (published April 2020)". "We will keep PDFs of this book freely available". It offers an up-to-date PDF plus "Jupyter notebook tutorials (for learning)" and solutions.
- **An Introduction to Statistical Learning, with Applications in Python (ISLP)**: [statlearning.com](https://www.statlearning.com/). "The Python edition (ISLP) was published in 2023". "Download ISL with Python". Free PDF: [hastie.su.domains/ISLP/ISLP_website.pdf.download.html](https://hastie.su.domains/ISLP/ISLP_website.pdf.download.html) (HTTP 200). Resources: [statlearning.com/resources-python](https://www.statlearning.com/resources-python). Labs: [intro-stat-learning/ISLP_labs](https://github.com/intro-stat-learning/ISLP_labs) ("Up-to-date version of labs for ISLP"; last push 2026-05-18)
- **Dive into Deep Learning** (Zhang et al.): [d2l.ai](https://d2l.ai/) ("Dive into Deep Learning 1.0.3 documentation"). "Implemented with PyTorch, NumPy/MXNet, JAX, and TensorFlow". Cambridge University Press (bibtex year 2023). Chapters on running it free in "Using Google Colab" and SageMaker Studio Lab. Repo [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en) (last push 2024-08-18)
- **Understanding Deep Learning** (Simon J.D. Prince; The MIT Press): [udlbook.github.io/udlbook/](https://udlbook.github.io/udlbook/). Its site bundle shows "Download full PDF (09 Feb 2026)", bibtex year 2023, and per-chapter figure downloads. Repo [udlbook/udlbook](https://github.com/udlbook/udlbook) (last push 2026-07-18; ~9.9k stars)
- **Deep Learning** (Goodfellow, Bengio, Courville): [deeplearningbook.org](https://www.deeplearningbook.org/) (live; free HTML)
- **Neural Networks and Deep Learning** (Michael Nielsen): [neuralnetworksanddeeplearning.com](http://neuralnetworksanddeeplearning.com/) (live; served over HTTP)
- **Hands-On ML (Géron)**:
  - [ageron/handson-ml3](https://github.com/ageron/handson-ml3): notebooks for "Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow (3rd edition)" with Colab (recommended) and Kaggle launch links (last push 2026-05-19; ~14.2k stars)
  - **NEW** [ageron/handson-mlp](https://github.com/ageron/handson-mlp): "example code and solutions to the exercises in the first edition of my new O'Reilly book Hands-on Machine Learning with Scikit-Learn and PyTorch (1st edition)", with an "Open In Colab (recommended)" link (last push 2026-09-03; ~2.0k stars)
  - The book itself is paid (O'Reilly). The notebooks are free.

### Inferences
**Primary and alternate reading by role** (my recommendations):

| Role | Primary | Alternate |
|---|---|---|
| Math reference | *MML* chapters 2 (Linear Algebra), 5 (Vector Calculus) and 6 (Probability), after 3b1b | Khan exercises (Q4) |
| Statistics | *Think Stats 3e* (code-first, Colab) and *Seeing Theory* (interactive) | — |
| Classical ML with scikit-learn | *ISLP* (free PDF + labs) for concepts, or Géron's **handson-mlp** notebooks (scikit-learn + PyTorch, matching the PyTorch track) | handson-ml3 (TF/Keras); **avoid mixing it with a PyTorch track** |
| Deep-learning text | *UDL* (modern, free, updated 2026) or *d2l.ai* (runnable PyTorch code) | Nielsen (gentle, older); Goodfellow (reference only, too dense for beginners) |

### Gaps
- The chapter lists of handson-mlp and the book's exact publication date were not verified.
- The Python Data Science Handbook 2nd edition (2022, O'Reilly) is not the free online version. The free site appears to be the 1st-edition text (inferred from "© 2012-2017").

---

## Q7. Meta-learning and orientation: Barbara Oakley's "Learning How to Learn", her TEDx talk, and Andrew Ng's "AI for Everyone"

### Takeaway
- The **TEDx talk is verified** (17m).
- **"Learning How to Learn" is still fully free on Coursera** in 2026. Class Central (Aug 2026) lists it among 6 courses with full free access and an optional paid certificate.
- **"AI For Everyone" is NOT free to complete** in 2026. It costs $49 for a certificate. Coursera's page shows "Free trial", only Preview Mode (first module) is free, and financial aid is available.

### Cited Findings
- Barbara Oakley ["Learning how to learn | Barbara Oakley | TEDxOaklandUniversity"](https://www.youtube.com/watch?v=O96fE1E-rf8) (17m; 2014-08-05)
- Coursera ["Learning How to Learn: Powerful mental tools to help you master tough subjects"](https://www.coursera.org/learn/learning-how-to-learn). The page shows "4 modules" (1: Focused & Diffuse; 2: Chunking; 3: Procrastination and Memory; 4: Renaissance Learning and Unlocking Your Potential) and "Join for Free".
- Class Central (dated Aug 12th, 2026) describes a set of courses where "After completing the course, you can optionally purchase a certificate. This is different from 'Full course, no certificate'… Currently, we know of 6 courses with this option", and lists "Learning How to Learn: Powerful mental tools to help you master tough subjects" among them — [Class Central report](https://www.classcentral.com/report/coursera-free-online-courses/)
- Coursera ["AI For Everyone"](https://www.coursera.org/learn/ai-for-everyone) shows "4 modules", "7 hours to complete" and "Status: Free trial". Its FAQ says: "To access course materials, assignments, and earn a Certificate, you'll need to purchase the Certificate experience… Eligible learners may also have the option to start with a Free Trial" and "Financial aid available" — [Coursera AI For Everyone](https://www.coursera.org/learn/ai-for-everyone)
- DeepLearning.AI's page: "It typically takes 4 weeks, 2-3 hours per week", "The course costs $49 for 180 days of certificate eligibility", "Coursera provides financial aid to learners who cannot afford the fee. Apply for it by clicking on the Financial Aid link beneath the 'Enroll' button" — [deeplearning.ai/courses/ai-for-everyone](https://www.deeplearning.ai/courses/ai-for-everyone/)
- AI For Everyone is **not** in Class Central's fully-free list. It appears only in a sponsored link block on that page — [Class Central report](https://www.classcentral.com/report/coursera-free-online-courses/)

### Inferences
- **Primary** meta-learning: the TEDx talk (17 min) on day 1, then Learning How to Learn (free, ~4 modules) in week 1–2 alongside Python practice.
- **AI literacy**: substitute Elements of AI "Introduction to AI" (free) for AI For Everyone as the primary. AI For Everyone becomes an optional alternate: first module via Preview, or the full course via Financial Aid (see Q8).

### Gaps
- Coursera's displayed pace for Learning How to Learn was captured ambiguously ("2 weeks at 10 hours a week"), so the total hours are UNVERIFIED.

---

## Q8. Coursera in 2026: can Andrew Ng's ML Specialization, the Deep Learning Specialization and DeepLearning.AI's "Mathematics for ML and Data Science" be audited free? Does Financial Aid still exist?

### Takeaway
**No, they can't be taken free.** In mid-2025 Coursera **replaced free Audit mode with "Preview Mode"**, which gives the **first module free (including graded items)**. Each of the three Specializations now states on its own page: "**Can I take the course for free? No, you cannot take this course for free… If you cannot afford the fee, you can apply for financial aid.**" **Financial Aid still exists.** Third-party 2026 guides describe an application with a short essay (~150 words), roughly **15 days** of review, and 180 days of access after approval.

### Cited Findings
- "In mid-2025, Coursera replaced free audit mode with Preview Mode, which gives free access to only the first module of a course. A small number of courses still offer full free access under the label 'Full Course, No Certificate'." "Preview Mode lets you access the first module of a course including graded items, for free, without entering payment details. Look for the 'Preview' link at the bottom of the enrollment pop-up." "Out of Coursera's 21,000+ active courses, we found more than 470 fully free courses." (report dated Aug 12th, 2026) — [Class Central](https://www.classcentral.com/report/coursera-free-online-courses/)
- A 7-day free trial is available for Specializations and Coursera Plus — [Class Central, via search summary](https://www.classcentral.com/report/coursera-free-online-courses/)
- **Machine Learning Specialization** ([page](https://www.coursera.org/specializations/machine-learning-introduction)): "3 course series", "2 months at 10 hours a week", course lengths "33 hours / 34 hours / 28 hours". Prerequisites: "basic coding (for loops, functions, if/else statements) and high school-level math". FAQ: "Can I take the course for free? No, you cannot take this course for free… If you cannot afford the fee, you can apply for financial aid." Also: "There is a limit of 180 days of certificate eligibility"
- **Deep Learning Specialization** ([page](https://www.coursera.org/specializations/deep-learning)): "5 course series", "3 months at 10 hours a week", "4.8 from 147,259 reviews". FAQ: "Can I take the course for free? No, you cannot take this course for free…"
- **Mathematics for Machine Learning and Data Science** ([page](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science)): "3 course series", "12 weeks to complete at 5 hours a week", "4.6 from 3,251 reviews". FAQ: "Can I take the course for free? No, you cannot take this course for free…"
- Financial aid is still offered. The Specialization pages say "Financial aid available". The Help Center article "Apply for financial aid" is live ([coursera.support](https://www.coursera.support/s/article/learner-000001455?language=en_US), JS-rendered; text not extracted). DeepLearning.AI: "Apply for it by clicking on the Financial Aid link beneath the 'Enroll' button" — [DeepLearning.AI](https://www.deeplearning.ai/courses/ai-for-everyone/)
- Process details (secondary sources): "The application… takes about 15 to 20 minutes, and requires a short essay with a minimum of 150 words". "Processing usually takes about 15 days… Coursera states 15 business days". "You have 180 days… to complete the course". "Your financial aid application will be canceled if you start a free trial… while it is being reviewed" — [search summary of 2026 guides incl. upskillwise.com](https://upskillwise.com/coursera-financial-aid/), [missiongraduatenm.org](https://missiongraduatenm.org/coursera-financial-aid/), [certififree.com](https://certififree.com/guides/how-to-apply-coursera-financial-aid.html)

### Inferences
- For a zero-budget learner, the practical options are:
  - **Preview** the first module of each course for free.
  - **Apply for Financial Aid course-by-course.** Aid is per course, so a 3-course Specialization needs 3 applications, and the ~15-day wait means applying well ahead.
  - **Don't start a free trial while an application is pending**, because that cancels it.
  - Use free substitutes:
    - For the ML Specialization: StatQuest + Kaggle Learn + Google MLCC + CS229 2018 on YouTube.
    - For the DL Specialization: 3b1b + fast.ai + MIT 6.S191 + CS230 2018 on YouTube.
    - For the math Specialization: 3b1b + Khan + MML book.
- Unofficial re-uploads of Andrew Ng's Coursera lectures exist on YouTube, but they were not verified and may violate copyright. Don't link them.

### Gaps
- Coursera's official blog posts on the Preview change returned HTTP 400 to automated fetch, so the exact announcement date was not verified. "Mid-2025" comes from Class Central.
- The official Financial Aid help article could not be text-extracted. The 15-day timeline and 150-word essay details come from third-party guides and should be treated as approximate.

---

## Q9. DataTalksClub ML Zoomcamp: 2026 cohort, self-paced option, certificate rules

### Takeaway
The **2026 cohort started 14 September 2026**. As of 2026-09-24 the learner is ~10 days late, which is still viable. Lectures are pre-recorded. The course is free. The **certificate requires two passing projects plus peer reviews during the live cohort** (Midterm due 9 Nov 2026, Capstone 1 due 4 Jan 2027, Capstone 2 due 18 Jan 2027). Homework is graded for the leaderboard but is not required for the certificate. **The self-paced route has no certificate.**

### Cited Findings
- Repo [DataTalksClub/machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) ("Learn ML engineering for free in 4 months!"; last push 2026-09-23; ~14.6k stars). README: "Start date | September 14, 2026". Links: "[Sign up for the free 2026 cohort](https://courses.datatalks.club/register/ml-zoomcamp/)", course platform [courses.datatalks.club/ml-zoomcamp-2026/](https://courses.datatalks.club/ml-zoomcamp-2026/) (both HTTP 200), and videos playlist ["Machine Learning Zoomcamp"](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) (DataTalksClub; 97 videos, ~26h35m) — [README](https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/README.md)
- Live vs self-paced: "Live Cohort: Start September 14, 2026; Homework Graded; Certificate eligibility Yes" vs "Self-Paced: Start Anytime; Homework Available, but not scored; Certificate eligibility No". Also: "'Live cohort' does not mean mandatory live classes. Lectures are pre-recorded." "To earn a certificate, you must submit two qualifying projects and complete the required peer reviews during a live cohort." Hardware: the course does not require "A powerful computer or local GPU. The deep learning modules use cloud resources" — [README](https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/README.md)
- Modules: 1 Introduction to ML (CRISP-DM), 2 ML for Regression, 3 ML for Classification, 4 Evaluation Metrics for Classification, 5 Deploying ML Models, 6 Decision Trees and Ensemble Learning, Midterm Project, 8 Neural Networks and Deep Learning, 9 Serverless Deep Learning, 10 Kubernetes and TensorFlow Serving, Capstone 1, optional Capstone 2 — [README](https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/README.md)
- 2026 deadlines (Mondays 23:00 UTC) — [cohorts/2026 README](https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2026/README.md):

| Item | Deadline |
|---|---|
| Module 1 homework | 21 Sep 2026 |
| Module 2 homework | 28 Sep 2026 |
| Module 3 homework | 5 Oct 2026 |
| Module 4 homework | 12 Oct 2026 |
| Module 5 homework | 19 Oct 2026 |
| Module 6 homework | 26 Oct 2026 |
| Midterm project (submit / peer reviews) | 9 Nov 2026 / 16 Nov 2026 |
| Module 8 homework | 23 Nov 2026 |
| Module 9 homework | 30 Nov 2026 |
| Module 10 homework | 7 Dec 2026 |
| Capstone 1 (submit / peer reviews) | 4 Jan 2027 / 11 Jan 2027 |
| Capstone 2 (submit / peer reviews) | 18 Jan 2027 / 25 Jan 2027 |

  - "You need two passing projects for a certificate: midterm and one capstone, or both capstones." "Skipping the peer reviews fails the project."

### Inferences
- **Recommended**: register for the 2026 cohort now. Missing the Module 1 homework deadline only costs leaderboard points. The certificate depends on projects, and a late starter can still hit the Midterm (9 Nov) or use Capstones 1+2.
- Prerequisites implied by the curriculum are Python + NumPy/pandas basics. The Zoomcamp is a strong **primary "apply it" track** for classical ML plus deployment, run in parallel with the StatQuest/Kaggle concept work.
- Module 10 uses TensorFlow Serving, which may clash with a PyTorch-first track. Treat the deep-learning modules as optional.

### Gaps
- The deep-learning framework used in Module 8 in 2026 (Keras vs PyTorch) was not verified.
- The rules for joining mid-cohort (e.g., whether late homework submissions are accepted) were not verified.

---

## Q10. India-specific free options: NPTEL (IIT) ML/DL courses; Hindi/Hinglish YouTube (CampusX, codebasics, Krish Naik)

### Takeaway
All listed YouTube playlists are verified live. **CampusX is Hindi** (video titles say "in Hindi"). NPTEL's **July 2026 semester started 20 July 2026, and enrollment closed 3 and 17 Aug 2026**. A late-September 2026 starter can therefore only use NPTEL's **always-free archived lecture videos** now, and target the Jan 2027 semester for a certificate. The certificate needs a proctored exam, reported at **₹1,000 per course**. The run dates below come from search snippets, not from NPTEL's own pages.

### Cited Findings
**Hindi/Hinglish and Indian-English YouTube**
- CampusX ["100 Days of Machine Learning"](https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH): 134 videos (first 100 ≈ 44h56m). The description calls it "one of the most watched and most trusted and Evergreen Machine Learning playlists on Indian YouTube". Video 2 is titled "AI Vs ML Vs DL for Beginners in Hindi". First video: ["What is Machine Learning? | 100 Days of Machine Learning"](https://www.youtube.com/watch?v=ZftI2fEz0Fw)
- CampusX ["100 Days of Deep Learning"](https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn): 84 videos, ~52h12m ("A complete end-to-end playlist on Deep Learning where topics like ANN, CNN, and RNN are covered")
- codebasics ["Machine Learning Tutorial Python | Machine Learning For Beginners"](https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw): 42 videos, ~12h00m (English titles; e.g., "Machine Learning Tutorial Python -1: What is Machine Learning?")
- codebasics ["Deep Learning With Tensorflow 2.0, Keras and Python"](https://www.youtube.com/playlist?list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO): 58 videos, ~18h28m (TensorFlow/Keras, not PyTorch)
- codebasics ["Pandas Tutorial (Data Analysis In Python)"](https://www.youtube.com/playlist?list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy)
- Krish Naik ["Complete Machine Learning playlist"](https://www.youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe): 153 videos (first 100 ≈ 24h48m)
- Krish Naik ["Complete Deep Learning"](https://www.youtube.com/playlist?list=PLZoTAELRMXVPGU70ZGsckrMdr0FteeRUi): 88 videos, ~30h21m
- Krish Naik ["Statistics in Machine Learning"](https://www.youtube.com/playlist?list=PLZoTAELRMXVMhVyr3Ri9IQ-t5QPBtxzJO): 44 videos, ~23h56m

**NPTEL / SWAYAM (IIT courses)**
- Portals: [nptel.ac.in](https://nptel.ac.in/) and [onlinecourses.nptel.ac.in](https://onlinecourses.nptel.ac.in/) (live; JS-rendered)
- July 2026 semester: 1,055 courses. The start date for NPTEL courses in the July 2026 semester was **July 20, 2026**. Enrollment closed **August 3, 2026** (4-week/8-week Set 1) and **August 17, 2026** (12-week etc.) — [Careers360](https://www.careers360.com/courses-certifications/articles/nptel-course-registration-2026), [Careers360 list](https://www.careers360.com/courses-certifications/articles/nptel-courses-for-july-2026-semester). Certification needs a proctored exam, registered for by "paying the required fee" — [Careers360](https://www.careers360.com/courses-certifications/articles/nptel-course-registration-2026)
- Exam fee: "The optional certification exam carries a fee of ₹1,000" — [search summary citing MSN/NPTEL pages](https://www.msn.com/en-in/money/news/iit-madras-to-offer-free-machine-learning-course-in-2026-how-to-enrol-what-you-will-learn-who-should-apply/ar-AA1QYca4) (secondary)
- **Deep Learning, IIT Ropar/IIT Madras** (Prof. Mitesh M. Khapra & Prof. Sudarshan Iyengar):
  - 2026 course page [noc26_cs66](https://onlinecourses.nptel.ac.in/noc26_cs66/preview). A search snippet reports ~16.6k learners and an exam on 17 Apr 2026, which implies the Jan–Apr 2026 run.
  - A **July 2026 run** is indicated by third-party "Week-1 assignment answers… July" (published 2026-07-18) and "Week 4" (2026-08-11) videos ([6SMG8tbUs34](https://www.youtube.com/watch?v=6SMG8tbUs34), [NFxw5wTigYQ](https://www.youtube.com/watch?v=NFxw5wTigYQ)). Its course code is UNVERIFIED.
  - Free archived videos: [nptel.ac.in/courses/106106184](https://nptel.ac.in/courses/106106184) (HTTP 200)
  - Unofficial YouTube mirror: ["DeepLearning - Mitesh Khapra, SKS Iyengar || IIT Ropar and Madras - NPTEL"](https://www.youtube.com/playlist?list=PLEAYkSg4uSQ1r-2XrJ_GBzzS6I-f8yfRU) (uploaded by "Rahul Madhavan", **not an official NPTEL channel**)
- **Introduction to Machine Learning, IIT Madras** (Prof. Balaraman Ravindran):
  - Course page [noc26_cs74](https://onlinecourses.nptel.ac.in/noc26_cs74/preview). A search snippet reports ~62k learners, a run from 17 Nov 2025 to 26 Jan 2026, and an exam on 13 Feb 2026.
  - Free archived videos: [nptel.ac.in/courses/106106139](https://nptel.ac.in/courses/106106139) (HTTP 200)
  - Instructor page: [cse.iitm.ac.in/~ravi/nptel-courses/intro-to-machine-learning/](https://www.cse.iitm.ac.in/~ravi/nptel-courses/intro-to-machine-learning/) (live)
  - Tamil-language variant: [noc26_cs73](https://onlinecourses.nptel.ac.in/noc26_cs73/preview)

### Inferences
- **Hindi-medium learners**: use CampusX "100 Days of ML" as a **primary alternate** to StatQuest + Kaggle for classical ML, and "100 Days of DL" for deep learning. Both are very long (~45–60h and ~52h), so assign selected days rather than whole playlists.
- **English-first learners**: use codebasics ML (12h) as a compact, practical alternate.
- **NPTEL**: its value is the **IIT certificate for résumés in India**. For a Sept 2026 starter, the realistic plan is to watch the archived Deep Learning / Intro to ML videos for free now and register for the Jan 2027 semester's exam-backed run (registration typically opens late in the year; the 2027 dates are UNVERIFIED).
- **Framework caution**: codebasics DL and the Zoomcamp DL modules use TensorFlow/Keras. Keep them as alternates if the track is PyTorch-first.

### Gaps
- It is UNVERIFIED whether Krish Naik's and codebasics' listed playlists are spoken in English or Hindi (titles are English; audio language was not checked). Krish Naik's separate Hindi-channel playlists were not researched.
- The exact July–Dec 2026 NPTEL course codes and exam dates for Deep Learning and Intro to ML are UNVERIFIED (NPTEL pages are JS-rendered). The dates above come from search snippets.
- The ₹1,000 exam fee comes from a secondary source. It was not confirmed on NPTEL's own site today.
