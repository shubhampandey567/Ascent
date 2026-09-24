# Phase 1 — Python & Data Toolkit

**Plan weeks 3–7 · 5 weeks · Difficulty ★★☆☆☆ · Badge: Data Wrangler**

## Why this phase matters
Every AI system starts and ends with data, and almost all AI work happens in Python. You already know some Python; this phase makes you *fluent* in the way data and ML people write it: vectorised NumPy, Pandas, plots, SQL, tests and clean Git habits. Your Java background is an advantage here: you already think in types, classes and tests.

## Before you start
- Phase 0 passed.
- The Mentor's `/start` diagnostic decides whether you can test out of Week 1 (5 quick questions, 85% or more).

## You will be able to
- Write idiomatic Python: comprehensions, dictionaries, classes, type hints, exceptions, virtual environments.
- Use NumPy arrays without loops (vectorisation, broadcasting, masks).
- Load, clean, reshape and summarise real, messy data with Pandas.
- Choose and draw the right chart, and tell a story with data.
- Query data with SQL (DuckDB) and check the result with Pandas.
- Test your code with pytest and work with branches and pull requests.

---

## Week 1 (plan week 3) — Python for data work

#### P1-W1-L1 · Python essentials, fast (~75 min)
- **Learn:** [Kaggle Learn — Python](https://www.kaggle.com/learn/python), lessons 1–3 (Hello Python; Functions and getting help; Booleans and conditionals). In-browser, free certificate.
- **Alt:** [Corey Schafer — Python Programming Beginner Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)
- **Key concepts:** dynamic typing vs Java's static typing; functions and default arguments; `help()`; truthiness; f-strings; indentation instead of braces; everything is an object.
- **Quiz seeds:** Predict the output of a function with a default argument called twice. What values are "falsy" in Python? What does Python do where Java would need an interface?
- **Build:** 10 small exercises the Mentor gives you, written without AI.

#### P1-W1-L2 · Collections and comprehensions (~75 min)
- **Learn:** Kaggle Learn Python, lessons 4–6 (Lists; Loops and list comprehensions; Strings and dictionaries).
- **Key concepts:** lists, tuples, sets, dicts; slicing; list/dict/set comprehensions; `dict.get`; `collections.Counter` and `defaultdict`; `sorted(..., key=...)`; mutable vs immutable.
- **Quiz seeds:** Rewrite a 4-line loop as a comprehension. Why can't a list be a dictionary key? What does `sorted(words, key=len)` return?
- **Build:** A word-frequency counter for a text file: the top 10 words, ignoring case and punctuation.

#### P1-W1-L3 · Modules, environments and files (~75 min)
- **Learn:** Kaggle Learn Python, lesson 7 (Working with external libraries), then the Python tutorial chapter [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html).
- **Key concepts:** `import` and modules; `venv` and `pip`; `requirements.txt`; `pathlib`; reading and writing CSV and JSON; `with` blocks (context managers).
- **Quiz seeds:** Why use one virtual environment per project? What happens if you forget `with` when writing a file?
- **Build:** Read a CSV, filter rows by a condition, and write the result as JSON.

#### P1-W1-L4 · Classes, types, errors and validation (~75 min)
- **Learn:** the Python tutorial sections on [classes](https://docs.python.org/3/tutorial/classes.html) and [errors and exceptions](https://docs.python.org/3/tutorial/errors.html), the [dataclasses](https://docs.python.org/3/library/dataclasses.html) reference, and the [Pydantic](https://docs.pydantic.dev/latest/) home page.
- **Key concepts:** classes compared with Java (no `private`, `self`, dunder methods); `@dataclass`; type hints; `try/except/else/finally` and raising your own exceptions; Pydantic models for validating data (you will use them for LLM outputs in Phase 2).
- **Quiz seeds:** What does `@dataclass` generate for you? What's the difference between a type hint and Pydantic validation?
- **Build:** An `Expense` model with Pydantic (amount > 0, category from a fixed list, date). Show the error message for invalid input.

#### P1-W1-B · Weekend build
A small CLI that downloads JSON from a free public API (for example [Open-Meteo](https://open-meteo.com) weather, no key needed), cleans it into a CSV, and has 3 tests. Learn pytest from its [getting-started page](https://docs.pytest.org/en/stable/getting-started.html).

---

## Week 2 (plan week 4) — Notebooks and NumPy

#### P1-W2-L1 · Notebooks: Jupyter, Kaggle and Colab (~60 min)
- **Learn:** the [Kaggle notebooks docs](https://www.kaggle.com/docs/notebooks) and [guides/free-compute.md](../guides/free-compute.md).
- **Key concepts:** cells and the kernel; hidden state and run order (always "Restart & Run All" before sharing); Markdown cells; `%timeit`; attaching datasets; saving versions; when to use a notebook vs a `.py` file.
- **Quiz seeds:** Why can a notebook work for you but fail for someone else? When should code move from a notebook into a module?
- **Build:** A Kaggle notebook that loads a dataset, shows 5 facts about it, and runs cleanly from top to bottom.

#### P1-W2-L2 · NumPy basics (~75 min)
- **Learn:** [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html), then the first 30 minutes of [Keith Galli — Python NumPy Tutorial for Beginners](https://www.youtube.com/watch?v=QUT1VHiLmmI).
- **Key concepts:** `ndarray`; `dtype`; `shape` and `ndim`; indexing and slicing; `reshape`; the `axis` argument.
- **Quiz seeds:** What is the shape of `np.zeros((3, 4)).sum(axis=0)`? Why are NumPy arrays faster than Python lists?
- **Build:** 15 short array exercises from the Mentor.

#### P1-W2-L3 · Vectorisation and broadcasting (~75 min)
- **Learn:** Python Data Science Handbook sections [Computation on NumPy Arrays: Universal Functions](https://jakevdp.github.io/PythonDataScienceHandbook/02.03-computation-on-arrays-ufuncs.html), [Aggregations](https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html), [Broadcasting](https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html) and [Comparisons, Masks, and Boolean Logic](https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html).
- **Key concepts:** ufuncs; aggregations along an axis; the broadcasting rules; boolean masks; why vectorised code is 10–100× faster than loops.
- **Quiz seeds:** Will a (3, 1) array broadcast with a (4,) array? What's the result's shape? How do you select all values greater than the mean?
- **Build:** Rewrite 3 loops as vectorised code and compare speeds with `%timeit`.

#### P1-W2-L4 · NumPy for ML: randomness, dot products, similarity (~60 min)
- **Learn:** [StatQuest — Cosine Similarity, Clearly Explained](https://www.youtube.com/watch?v=e9U0QAFbfLI), then practise with `np.random.default_rng`, `@`, and `np.linalg.norm`.
- **Key concepts:** random generators and seeds (reproducibility); the dot product; matrix-multiplication shapes; vector length (norm); cosine similarity. This is exactly how embedding search works in Phase 2.
- **Quiz seeds:** Why set a random seed? What is the cosine similarity of two identical vectors, and of two perpendicular ones?
- **Build:** A `cosine_similarity(a, b)` function, then find the most similar of 5 random vectors to a query vector.

#### P1-W2-B · Weekend build
30 exercises from [numpy-100](https://github.com/rougier/numpy-100), without looking at the answers until you've tried.

---

## Week 3 (plan week 5) — Pandas

#### P1-W3-L1 · Pandas I (~75 min)
- **Learn:** [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas), lessons 1–3 (Creating, reading and writing; Indexing, selecting and assigning; Summary functions and maps).
- **Alt:** [Corey Schafer — Pandas Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- **Key concepts:** Series vs DataFrame; `read_csv`; `loc` vs `iloc`; boolean filtering; `describe`, `value_counts`; `map` and `apply`.
- **Quiz seeds:** What's the difference between `df.loc[0]` and `df.iloc[0]`? How do you get rows where city is Pune and price is above 500?
- **Build:** The lesson exercises.

#### P1-W3-L2 · Pandas II (~75 min)
- **Learn:** Kaggle Learn Pandas, lessons 4–6 (Grouping and sorting; Data types and missing values; Renaming and combining).
- **Key concepts:** `groupby` + `agg`; `sort_values`; dtypes and `astype`; `isna`, `fillna`, `dropna`; `concat`, `merge` and join types.
- **Quiz seeds:** Write the Pandas equivalent of `SELECT city, AVG(price) FROM t GROUP BY city`. What does an inner merge drop?
- **Build:** The lesson exercises.

#### P1-W3-L3 · Cleaning real data (~75 min)
- **Learn:** [Kaggle Learn — Data Cleaning](https://www.kaggle.com/learn/data-cleaning), lessons 1–3 (Handling missing values; Scaling and normalization; Parsing dates).
- **Key concepts:** strategies for missing values (drop, fill, flag); duplicates; wrong dtypes; `.str` string methods; parsing dates; outliers; "tidy" data (one row per observation).
- **Quiz seeds:** When is dropping rows with missing values dangerous? Scaling vs normalisation: what's the difference?
- **Build:** Clean a messy column set the Mentor gives you, and write down each decision you made.

#### P1-W3-L4 · Reshaping and SQL thinking (~60 min)
- **Learn:** [Keith Galli — Complete Python Pandas Data Science Tutorial (2025 edition)](https://www.youtube.com/watch?v=2uvysYbKdjM), the merge, pivot and group-by sections; and the handbook's [Pivot Tables](https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html).
- **Key concepts:** `pivot_table` and `melt`; method chaining; vectorised operations vs `apply`; mapping SQL you already know to Pandas.
- **Quiz seeds:** When does `apply` become slow? What does `melt` do?
- **Build:** Translate 5 SQL queries you know into Pandas.

#### P1-W3-B · Weekend build
Pick a messy real dataset from [Kaggle Datasets](https://www.kaggle.com/datasets) or your government's open-data portal (for example [data.gov.in](https://www.data.gov.in) in India or [data.europa.eu](https://data.europa.eu) in Europe). Clean it and write down 5 findings with numbers.

---

## Week 4 (plan week 6) — Visualisation, EDA and SQL

#### P1-W4-L1 · Plotting fundamentals (~75 min)
- **Learn:** [Kaggle Learn — Data Visualization](https://www.kaggle.com/learn/data-visualization), lessons 1–4 (Hello, Seaborn; Line charts; Bar charts and heatmaps; Scatter plots).
- **Alt:** [Corey Schafer — Matplotlib Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- **Key concepts:** Matplotlib figures and axes; line, bar, scatter, histogram and box plots; titles, labels and units; Seaborn as a friendlier layer on Matplotlib.
- **Quiz seeds:** Which chart shows a trend over time? A comparison between categories? A relationship between two numbers?

#### P1-W4-L2 · Distributions and honest charts (~60 min)
- **Learn:** Kaggle Data Visualization lessons 5–7 (Distributions; Choosing plot types and custom styles; Final project), plus [StatQuest — Histograms, Clearly Explained](https://www.youtube.com/watch?v=qBigTkBLU6g).
- **Key concepts:** histograms and bin width; KDE; choosing the chart for the question; misleading charts (truncated axes, dual axes, 3D pie charts).
- **Quiz seeds:** How can a truncated y-axis mislead? How does bin width change a histogram's story?
- **Build:** Make one deliberately misleading chart and its honest version.

#### P1-W4-L3 · The EDA workflow (~75 min)
- **Learn:** [Kaggle Learn — Data Cleaning](https://www.kaggle.com/learn/data-cleaning), lessons 4–5 (Character encodings; Inconsistent data entry), then a guided exploratory data analysis (EDA) of a dataset you choose, following the Mentor's checklist.
- **Key concepts:** EDA as a loop (question → data → clean → explore → visualise → conclude); one variable at a time, then pairs; correlation is not causation; writing down assumptions.
- **Quiz seeds:** Two columns are strongly correlated. Name two reasons that might not mean one causes the other.
- **Build:** An EDA notebook answering 5 questions.

#### P1-W4-L4 · SQL for data work (~75 min)
- **Learn:** [Kaggle Learn — Intro to SQL](https://www.kaggle.com/learn/intro-to-sql), then query CSV files directly with [DuckDB](https://duckdb.org/docs/stable/clients/python/overview) (`pip install duckdb`).
- **Key concepts:** `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `JOIN`, `ORDER BY`; SQL vs Pandas (which is clearer for what); DuckDB runs SQL on files and DataFrames with no server.
- **Quiz seeds:** `WHERE` vs `HAVING`? When would you choose SQL over Pandas?
- **Build:** Answer 5 questions with DuckDB SQL and confirm each result with Pandas.

#### P1-W4-B · Weekend build
Start Project 1: choose the dataset and write your 8–10 questions.

---

## Week 5 (plan week 7) — Engineering habits and Project 1

#### P1-W5-L1 · Git like a professional (~75 min)
- **Learn:** [MIT Missing Semester 2026 — Lecture 5: Version Control and Git](https://www.youtube.com/watch?v=9K8lB61dl3Y), then the first levels of [Learn Git Branching](https://learngitbranching.js.org/).
- **Alt:** [Pro Git](https://git-scm.com/book/en/v2), chapters 1–3
- **Key concepts:** commits as snapshots; branches; merge vs rebase; remotes; `.gitignore`; good commit messages; the pull-request workflow.
- **Quiz seeds:** What happens to your branch when you rebase it? Why should secrets never be committed, even if deleted later?
- **Build:** Branch → pull request on your own repo → review → merge.

#### P1-W5-L2 · Tests and code quality (~60 min)
- **Learn:** [pytest — Get started](https://docs.pytest.org/en/stable/getting-started.html) and [Ruff](https://docs.astral.sh/ruff/) (linter and formatter).
- **Key concepts:** unit tests; fixtures; `@pytest.mark.parametrize`; testing with small fake data; linting and formatting; a `src/` and `tests/` layout.
- **Quiz seeds:** What makes a test useful rather than just present? What does a linter catch that tests don't?
- **Build:** At least 5 tests for your Project 1 cleaning functions.

#### P1-W5-L3 and L4 · Project 1 work
#### P1-W5-B · Weekend: `/submit`, then `/exam`

---

## Project 1 — "Data Detective" (`projects/pr1-data-detective/`)
Pick a real public dataset you care about. Ideas: IPL matches, air quality in Indian cities, Indian startup funding, Zomato restaurants, rainfall in your state, or your own expense export with personal details removed (or the equivalent in your country). Answer 8–10 questions.

**Must-haves**
- [ ] A notebook with a clear *question → method → answer* flow that runs cleanly with Restart & Run All.
- [ ] Cleaning logic in a Python module (`clean.py`) with at least 5 pytest tests; the notebook imports it.
- [ ] At least 6 appropriate charts with titles and labels, plus one misleading chart and its corrected version.
- [ ] At least 2 findings computed with SQL (DuckDB) and cross-checked with Pandas.
- [ ] README: the questions, key findings with numbers, data source and licence, limitations, how to run.
- [ ] `requirements.txt`; no data file over 50 MB in Git (use a download script or link instead).

**Stretch:** an interactive chart; a 5-slide summary for a non-technical audience.

**Viva focus:** every cleaning decision and its effect on the findings; what the data *can't* tell you.

## Exam EX1
- **Part A (concepts):** Python idioms, NumPy broadcasting, Pandas operations, chart choice, SQL, testing, Git.
- **Part B (live coding, 20 min):** clean a small messy CSV and answer 3 questions with Pandas.
- **Part C (stakeholder):** explain one of your Project 1 findings to a manager in 6 sentences.
- **Part D (judgment):** "Average salary in the dataset rose 20% this year, but this year's data includes a new senior-heavy team. Is 'salaries rose 20%' a fair claim?"

---

## Optional and deeper
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/), chapters 2–4 (free online).
- [freeCodeCamp — Data Analysis with Python, full course](https://www.youtube.com/watch?v=r-uOLxNrNk8) (4 h 22 min).
- [Microsoft — Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) (20 lessons).
- [Kaggle Learn — Advanced SQL](https://www.kaggle.com/learn/advanced-sql).
- [MIT Missing Semester 2026](https://www.youtube.com/playlist?list=PLyzOVJj3bHQunmnnTXrNbZnBaCA-ieK4L): command-line environment, debugging and code-quality lectures.
- **Regional-language options (Hindi):** [codebasics — Pandas Tutorial](https://www.youtube.com/playlist?list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy); [CampusX — 100 Days of Machine Learning](https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH) (the early days cover data handling and EDA).
