# Phase 3 — Math for ML

**Plan weeks 14–19 · 6 weeks · Difficulty ★★★☆☆ · Badge: Math Mechanic**

## Why this phase matters
You don't need to become a mathematician. You need the *working* maths that lets you read a model, debug it and reason about it: vectors and matrices (how data and models are stored), derivatives and gradients (how models learn), and probability and statistics (how to trust results). This is the difference between someone who calls APIs and someone who understands what's happening, and it's where many self-taught learners give up. You won't, because every idea here comes intuition first (3Blue1Brown, StatQuest), then practice, then code.

You've already met some of it: cosine similarity in Phase 1, embeddings in Phase 2.

## Before you start
- Phases 0–2 passed; comfortable with NumPy.
- If your math comfort in `tracker/profile.md` is 1–2 out of 5, tell the Mentor: it will add Khan Academy practice and slow this phase to 8 weeks. That is completely fine.

## You will be able to
- Think in vectors, matrices and shapes, and connect matrix multiplication to transformations.
- Explain dot products, projections, eigenvectors and why they matter in ML.
- Use derivatives, the chain rule and gradients, and implement gradient descent from scratch.
- Reason with probability: conditional probability, Bayes' rule, distributions, expectation.
- Use statistics honestly: variance, standard error, likelihood, hypothesis tests, correlation.
- Connect all of it to ML: least squares, loss functions, cross-entropy.

**How to study maths here:** watch the intuition video → pause and predict → do a few exercises by hand (Khan Academy or on paper) → write it in NumPy. Math that you code, you remember.

---

## Week 1 (plan week 14) — Vectors and matrices

#### P3-W1-L1 · Vectors and span (~60 min)
- **Learn:** 3Blue1Brown, Essence of Linear Algebra: [Ch. 1 Vectors](https://www.youtube.com/watch?v=fNk_zzaMoSs) and [Ch. 2 Linear combinations, span, and basis vectors](https://www.youtube.com/watch?v=k7RM-ot2NWY).
- **Practice:** [Khan Academy — Linear algebra](https://www.khanacademy.org/math/linear-algebra), vectors unit.
- **Key concepts:** a vector as an arrow and as a list of numbers; addition and scaling; linear combinations; span; basis; linear independence.
- **Quiz seeds:** What is the span of two vectors pointing in the same direction? Why can any 2D vector be written using the basis î and ĵ?
- **Build:** NumPy functions for vector addition, scaling and linear combinations, with a plot.

#### P3-W1-L2 · Matrices as transformations (~60 min)
- **Learn:** [Ch. 3 Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE) and [Ch. 4 Matrix multiplication as composition](https://www.youtube.com/watch?v=XkY2DOUCWMU).
- **Key concepts:** a matrix's columns = where the basis vectors land; matrix × vector = transforming the vector; matrix × matrix = doing one transformation after another; order matters.
- **Quiz seeds:** Why is AB usually not equal to BA? What does a matrix with columns (0, 1) and (−1, 0) do?
- **Build:** Apply rotation, shear and scaling matrices to a grid of points and plot before and after.

#### P3-W1-L3 · 3D and the determinant (~60 min)
- **Learn:** [Ch. 5 Three-dimensional linear transformations](https://www.youtube.com/watch?v=rHLEWRxRGiM) and [Ch. 6 The determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk).
- **Key concepts:** the determinant as the area (volume) scaling factor; a negative determinant flips orientation; a zero determinant squashes space into a lower dimension.
- **Quiz seeds:** What does det = 0 tell you about a transformation? What happens to area under a matrix with det = 3?
- **Build:** Check your answers with `np.linalg.det`.

#### P3-W1-L4 · Inverses, column space, non-square matrices (~60 min)
- **Learn:** [Ch. 7 Inverse matrices, column space and null space](https://www.youtube.com/watch?v=uQhTuRlWMxw) and [Ch. 8 Nonsquare matrices](https://www.youtube.com/watch?v=v8VSDg_WQlA).
- **Key concepts:** solving Ax = b; the inverse "undoes" a transformation; rank; column space; null space; non-square matrices map between dimensions (as neural-network layers do).
- **Quiz seeds:** When does Ax = b have no solution? What does a 3×2 matrix do to a 2D vector?
- **Build:** Solve a small system with `np.linalg.solve` and check the answer.

#### P3-W1-B · Weekend
Khan Academy practice on matrix multiplication. Then "shape drills": predict the output shape of 15 NumPy expressions, and check each one.

---

## Week 2 (plan week 15) — Dot products, eigenvectors and ML-shaped matrices

#### P3-W2-L1 · Dot products (~60 min)
- **Learn:** [Ch. 9 Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0), then rewatch [StatQuest — Cosine Similarity](https://www.youtube.com/watch?v=e9U0QAFbfLI).
- **Key concepts:** the dot product as projection × length; its sign tells you the angle; cosine similarity = dot product of unit vectors; why embedding search uses it.
- **Quiz seeds:** Two embeddings have a dot product of 0. What does that suggest? Why normalise before comparing?

#### P3-W2-L2 · Change of basis and eigenvectors (~75 min)
- **Learn:** [Ch. 13 Change of basis](https://www.youtube.com/watch?v=P2LTAUO1TdA) and [Ch. 14 Eigenvectors and eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g).
- **Key concepts:** the same vector described in different coordinate systems; eigenvectors keep their direction under a transformation; eigenvalues are how much they stretch. Preview: PCA in Phase 4 finds the eigenvectors of your data's covariance.
- **Quiz seeds:** What is special about an eigenvector? What does an eigenvalue of 0 mean?
- **Build:** `np.linalg.eig` on a symmetric 2×2 matrix; plot the eigenvectors on your transformed grid.

#### P3-W2-L3 · Matrices in neural networks (~60 min)
- **Learn:** [StatQuest — Essential Matrix Algebra for Neural Networks](https://www.youtube.com/watch?v=ZTt9gsGcdDo) and [Tensors for Neural Networks](https://www.youtube.com/watch?v=L35fFDpwIM4).
- **Key concepts:** a dataset as a matrix (rows = examples, columns = features); a layer as matrix multiplication plus bias; batches; tensors as n-dimensional arrays.
- **Quiz seeds:** Inputs have shape (32, 10) and a layer outputs 4 values. What's the weight matrix's shape? What does the 32 mean?

#### P3-W2-L4 · Norms, distances, projections (~60 min)
- **Learn:** [Mathematics for Machine Learning](https://mml-book.github.io/) (free PDF), chapter 3 sections on norms, inner products, lengths, distances and orthogonal projections. Read with a pencil; skip the proofs.
- **Key concepts:** L1 and L2 norms; Euclidean distance; orthogonality; projecting one vector onto another.
- **Quiz seeds:** When would L1 distance be preferred to L2? What does projecting b onto a give you?
- **Build:** A `project(b, a)` function with a test.

#### P3-W2-B · Weekend
Implement matrix multiplication with plain loops, then vectorised; confirm both match `@` and compare their speed.

---

## Week 3 (plan week 16) — Calculus for ML

#### P3-W3-L1 · What a derivative is (~60 min)
- **Learn:** Essence of Calculus [Ch. 1 The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) and [Ch. 2 The paradox of the derivative](https://www.youtube.com/watch?v=9vKqVkMQHKk).
- **Key concepts:** a derivative as a rate of change or slope; the "nudge" intuition (a tiny change in input → change in output); why derivatives let us optimise.
- **Quiz seeds:** The derivative of the loss with respect to a weight is −2. What should you do to the weight to reduce the loss?

#### P3-W3-L2 · Derivative rules and the chain rule (~60 min)
- **Learn:** [Ch. 3 Derivative formulas through geometry](https://www.youtube.com/watch?v=S0_qX4VJhMQ), [Ch. 4 Visualizing the chain rule and product rule](https://www.youtube.com/watch?v=YG15m2VwSjA), and [StatQuest — The Chain Rule](https://www.youtube.com/watch?v=wl1myxrtQHQ).
- **Key concepts:** power rule; sum and product rules; the chain rule: derivatives multiply along a chain of functions. This is the heart of backpropagation.
- **Quiz seeds:** Differentiate (3x + 1)² using the chain rule. Why does the chain rule matter for deep networks?

#### P3-W3-L3 · Partial derivatives and the gradient (~60 min)
- **Learn:** [Khan Academy — The gradient](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/the-gradient) and the partial-derivatives part of [Khan Academy — Multivariable calculus](https://www.khanacademy.org/math/multivariable-calculus).
- **Key concepts:** partial derivatives (change one input, hold the others); the gradient vector points uphill; the negative gradient points downhill.
- **Quiz seeds:** What does the gradient of f(x, y) = x² + 3y tell you at (1, 2)?
- **Build:** A numerical gradient function using finite differences, checked against the gradient you work out by hand.

#### P3-W3-L4 · Gradient descent (~75 min)
- **Learn:** [StatQuest — Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) and [Stochastic Gradient Descent](https://www.youtube.com/watch?v=vMh0zPT0tLI).
- **Key concepts:** step = −learning rate × gradient; learning rate too small (slow) vs too big (diverges); stopping criteria; stochastic and mini-batch gradient descent.
- **Quiz seeds:** Your loss goes up and down wildly. What's the likely cause? Why use mini-batches instead of the full dataset?
- **Build:** Gradient descent minimising f(x, y) = (x − 3)² + (y + 1)², with the path plotted for 3 learning rates.

#### P3-W3-B · Weekend
Optional: [Ch. 5 What's so special about e?](https://www.youtube.com/watch?v=m2MIpDrF7Es). Then: gradient descent for a quadratic loss with analytical vs numerical gradients, and a test that they agree.

---

## Week 4 (plan week 17) — Probability

#### P3-W4-L1 · Probability basics (~60 min)
- **Learn:** [Seeing Theory](https://seeing-theory.brown.edu/) chapters 1 (Basic Probability) and 2 (Compound Probability), with [Khan Academy — Statistics and probability](https://www.khanacademy.org/math/statistics-probability) for practice.
- **Key concepts:** sample space and events; the addition and multiplication rules; conditional probability; independence.
- **Quiz seeds:** P(A) = 0.3, P(B) = 0.5 and A, B are independent. What is P(A and B)? What's the difference between P(A|B) and P(B|A)?

#### P3-W4-L2 · Bayes' theorem (~60 min)
- **Learn:** [3Blue1Brown — Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM), [The medical test paradox](https://www.youtube.com/watch?v=lG4VkPoG3ko), and [StatQuest — Bayes' Theorem](https://www.youtube.com/watch?v=9wCnvr7Xw4E).
- **Key concepts:** prior, likelihood, posterior; base rates; why a 99%-accurate test can still be wrong most of the time for a rare disease.
- **Quiz seeds:** A disease affects 1 in 1,000 people and a test is 99% sensitive and 99% specific. You test positive. Roughly what's the chance you have it?
- **Build:** Simulate that medical test with NumPy for 1,000,000 people and check your answer.

#### P3-W4-L3 · Distributions and expectation (~60 min)
- **Learn:** [StatQuest — The Normal Distribution](https://www.youtube.com/watch?v=rzFX5NWojp0), [Expected Values](https://www.youtube.com/watch?v=KLs_7b7SKi4), and [3Blue1Brown — Binomial distributions](https://www.youtube.com/watch?v=8idr1WZ1A7Q); Seeing Theory chapter 3.
- **Key concepts:** random variables; Bernoulli, binomial and normal distributions; expected value; variance.
- **Quiz seeds:** What is the expected value of one roll of a fair die? What does the binomial distribution model?

#### P3-W4-L4 · The Central Limit Theorem (~60 min)
- **Learn:** [3Blue1Brown — But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo)
- **Alt:** [StatQuest — The Central Limit Theorem](https://www.youtube.com/watch?v=YAlJCEDH2uY)
- **Key concepts:** sums and averages of many random things tend to look normal; the law of large numbers; why averages are more stable than single values.
- **Quiz seeds:** Why does the average of 100 dice rolls vary less than a single roll?
- **Build:** Monte Carlo: plot the distribution of the sum of 1, 2, 5 and 30 dice.

#### P3-W4-B · Weekend
[Think Stats (3rd edition)](https://allendowney.github.io/ThinkStats/), chapters 1–2, run on Colab.

---

## Week 5 (plan week 18) — Statistics you can trust

#### P3-W5-L1 · Spread and uncertainty (~60 min)
- **Learn:** StatQuest [Calculating the Mean, Variance and Standard Deviation](https://www.youtube.com/watch?v=SzZ6GpcfoQY), [Population and Estimated Parameters](https://www.youtube.com/watch?v=vikkiwjQqfU), and [Standard Deviation vs Standard Error](https://www.youtube.com/watch?v=A82brFpdr9g).
- **Key concepts:** mean, median, variance, standard deviation; population vs sample; standard error: the uncertainty of an *estimate*.
- **Quiz seeds:** What's the difference between standard deviation and standard error? Why divide by n − 1 for a sample?

#### P3-W5-L2 · Likelihood and maximum likelihood (~60 min)
- **Learn:** StatQuest [Probability is not Likelihood](https://www.youtube.com/watch?v=pYxNSUDSFH4) and [Maximum Likelihood](https://www.youtube.com/watch?v=XepXtl9YKwc).
- **Key concepts:** probability (fixed model, varying data) vs likelihood (fixed data, varying model); choosing the parameters that make the data most likely. Preview: training a classifier minimises negative log-likelihood, which is cross-entropy.
- **Quiz seeds:** In plain words, what does "maximum likelihood estimate" mean?

#### P3-W5-L3 · Hypothesis tests and p-values (~75 min)
- **Learn:** StatQuest [Hypothesis Testing and The Null Hypothesis](https://www.youtube.com/watch?v=0oc49DyA3hU), [p-values: what they are and how to interpret them](https://www.youtube.com/watch?v=vemZtEM63GY), and [Statistical Power](https://www.youtube.com/watch?v=Rsc5znwR5FA).
- **Key concepts:** null hypothesis; what a p-value is (and isn't); false positives; power and sample size; A/B tests; "peeking" at results inflates false positives.
- **Quiz seeds:** Does p = 0.03 mean there's a 97% chance the new feature works? Why is stopping an A/B test as soon as it's "significant" a problem?

#### P3-W5-L4 · Covariance, correlation, R² (~60 min)
- **Learn:** StatQuest [Covariance](https://www.youtube.com/watch?v=qtaqvPAeEJY), [Pearson's Correlation](https://www.youtube.com/watch?v=xZ_z8KWkhXE), and [R-squared](https://www.youtube.com/watch?v=2AQKmw14mHM).
- **Key concepts:** covariance vs correlation; correlation only measures *linear* relationships; R² as "variance explained"; correlation ≠ causation; Simpson's paradox.
- **Quiz seeds:** Two variables have correlation 0. Can they still be strongly related? How?

#### P3-W5-B · Weekend
Analyse a synthetic A/B test in NumPy: a bootstrap confidence interval for the difference, and a permutation test. Write a 5-line conclusion a manager could act on.

---

## Week 6 (plan week 19) — Math meets ML, and Project 3

#### P3-W6-L1 · Least squares and linear regression (~60 min)
- **Learn:** StatQuest [The Main Ideas of Fitting a Line to Data (least squares)](https://www.youtube.com/watch?v=PaFPbb66DxQ) and [Linear Regression, Clearly Explained](https://www.youtube.com/watch?v=7ArmBVF2dCs).
- **Key concepts:** residuals; minimising the sum of squared residuals; the closed-form (normal equation) solution vs gradient descent; R² and p-values for a fit.
- **Quiz seeds:** Why square the residuals instead of just adding them? When would you prefer gradient descent to the closed-form solution?

#### P3-W6-L2 · Entropy and loss functions (~75 min)
- **Learn:** 3Blue1Brown [Reinventing Entropy (Compression is Intelligence, Part 1)](https://www.youtube.com/watch?v=l6DKRf-fAAM) and [But what is cross-entropy? (Part 2)](https://www.youtube.com/watch?v=GlYgs6v2YfU); [StatQuest — Odds and Log(Odds)](https://www.youtube.com/watch?v=ARfXDSkQf1Y).
- **Key concepts:** information and surprise (−log p); entropy; cross-entropy as the loss for classification; log-odds and the sigmoid; why prediction and compression are linked (this is why "predict the next token" is so powerful).
- **Quiz seeds:** Why does cross-entropy punish a confident wrong answer so heavily? What does the sigmoid turn log-odds into?

#### P3-W6-L3 and L4 · Project 3 work
#### P3-W6-B · Weekend: `/submit`, then `/exam`

---

## Project 3 — "Math Engine" (`projects/pr3-math-engine/`), pure NumPy
**Must-haves**
- [ ] Linear regression on a real dataset two ways: (a) closed form with `np.linalg.lstsq`, (b) gradient descent you implement. Both match scikit-learn within a small tolerance.
- [ ] Loss curves for 3 learning rates, with a paragraph explaining slow convergence and divergence.
- [ ] A gradient check: your analytical gradient agrees with a numerical one, tested with pytest.
- [ ] Logistic regression trained by your gradient descent on a binary task; accuracy compared with scikit-learn.
- [ ] A bootstrap confidence interval for one metric.
- [ ] README, in your own words: gradient descent, the chain rule, and "likelihood → loss", with one diagram.

**Stretch:** mini-batch SGD with momentum; a feature-scaling experiment; an L2 regularisation term.

**Viva focus:** walk through one gradient-descent step with actual numbers; why feature scaling changed convergence.

## Exam EX3
- **Part A (concepts):** matrix multiplication and shapes, dot products, eigenvectors (intuition), the chain rule, gradients, Bayes, distributions, standard error, p-values, correlation, cross-entropy.
- **Part B (live coding, 20 min):** implement gradient descent for a given function, with a numerical gradient check.
- **Part C (stakeholder):** "Explain to a manager, in at most 6 sentences, how a model 'learns' from data."
- **Part D (judgment):** "In an A/B test the team checked results daily and stopped when p dropped below 0.05, at p = 0.04. Ship variant B?"

---

## Optional and deeper
- [Mathematics for Machine Learning](https://mml-book.github.io/) (free book), chapters 2, 5 and 6.
- The rest of [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) and [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr).
- [MIT OCW 18.06SC — Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) (Gilbert Strang), for depth.
- freeCodeCamp full courses: [Linear Algebra](https://www.youtube.com/watch?v=JnTa9XtvmfI), [Calculus 1](https://www.youtube.com/watch?v=HfACrKJ_Y2w), [Statistics](https://www.youtube.com/watch?v=xxpc-HPKN28).
- [StatQuest — Statistics Fundamentals playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9).
- [Think Stats, 3rd edition](https://allendowney.github.io/ThinkStats/) (code-first statistics).
- DeepLearning.AI's *Mathematics for Machine Learning and Data Science* on [Coursera](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science): only the first module of each course is free; apply for Financial Aid (about 15 days, per course) for the rest.
- **Regional-language options (Hindi):** [Krish Naik — Statistics in Machine Learning](https://www.youtube.com/playlist?list=PLZoTAELRMXVMhVyr3Ri9IQ-t5QPBtxzJO).
