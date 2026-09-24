# Learning Science & Spaced-Repetition Algorithms for a Self-Paced, AI-Tutored Technical Learning System (working adult, ~10 h/week)

Scope note: evidence current to 2026-09-24. Preprints and company (non-peer-reviewed) studies are flagged. Numbers were checked against primary sources or abstracts this session unless marked "(cited from the paper's DOI; not re-fetched this session)".

## Q1. Memory and forgetting: Ebbinghaus, Murre & Dros (2015), and retention after 1 day and 1 week without review

### Takeaway
Forgetting is steepest in the first hours and days, then flattens (a power-law-like curve).

- **Nonsense syllables:** "savings" (how much faster relearning is) fell to about 32-34% after 1 day and about 17-25% after 6 days, in both Ebbinghaus's data and the 2015 replication.
- **Meaningful prose:** students who only reread lost 52% of what they could recall at 5 minutes within one week. Students who practised retrieval three times lost only 14% (Roediger & Karpicke 2006).

So the system should trigger the first retrieval within about 24 hours and another within the first week.

### Cited Findings
- **Ebbinghaus's original savings data (1880/1885) as tabulated by Murre & Dros:** 20 min 58%, 1 h 44%, 9 h 36%, 1 day 33%, 2 days 28%, 6 days 25%, 31 days 21%. — [Murre & Dros (2015), *PLOS ONE* 10(7): e0120644, DOI 10.1371/journal.pone.0120644](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644)
- **Replication savings, from Table 3.** The table compares Ebbinghaus, two earlier-replication subjects (Mack, Seitz) and the new subject (Dros, a 22-year-old man):

  | Interval | Dros | Mack | Seitz |
  |---|---|---|---|
  | 20 min | 47.2% | 54.4% | 44.2% |
  | 1 h | 37.3% | 43.2% | 32.5% |
  | 9 h | 27.6% | 28.5% | 27.0% |
  | 1 day | 31.7% | 31.6% | 27.0% |
  | 2 days | 23.0% | 36.5% | 28.6% |
  | 6 days | 16.8% | 30.9% | 20.5% |
  | 31 days | 4.1% | 25.8% | 20.1% |

  Source: [Murre & Dros 2015, PMC full text, Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/)
- **Why Dros's 31-day value is so low:** "The greatest deviation is by Dros at 31 days; his savings score is much lower than any of the other three." The authors suggest that Ebbinghaus and Heller et al. learned "far fewer intermediary lists… and hence much less interference." In other words, heavy interference from learning many similar lists accelerates forgetting. — [Murre & Dros 2015 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/)
- **List structure:** each list had 104 syllables, arranged as 8 rows of 13. There were 70 lists in total. — [Murre & Dros 2015 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/)
- **Method:** one subject spent about 70 hours learning lists of nonsense syllables to one perfect reproduction, then relearned them after 20 min, 1 h, 9 h, 1 day, 2 days, 6 days or 31 days. The authors conclude Ebbinghaus's curve "has indeed been replicated." — [Murre & Dros 2015 (PLOS)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644); [PMC mirror](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4492928/)
- **The curve is not smooth.** It "most probably shows a jump upwards starting at the 24 hour data point." The authors say sleep-consolidation research would predict this, but they call that interpretation speculative for this paradigm. — [Murre & Dros 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644)
- **Curve fitting:** a power function, a summed exponential and the Memory Chain Model all fit about equally well. — [Murre & Dros 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644)
- **Savings is not the same as recall.** Savings measures faster relearning, not the percentage recalled. Items at the start and end of a list showed little forgetting on savings but substantial forgetting on direct recall. — [Murre & Dros 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644)
- **Meaningful prose, Experiment 1 (Roediger & Karpicke 2006; figures read from the paper's PDF):**

  | Final test after | Restudy | One recall test (no feedback) | Effect size |
  |---|---|---|---|
  | 5 min | 81% | 75% | d = 0.52, restudy better |
  | 2 days | 54% | 68% | d = 0.95, testing better |
  | 1 week | 42% | 56% | d = 0.83, testing better |

  Source: [Roediger & Karpicke (2006), *Psychological Science* 17(3):249-255, DOI 10.1111/j.1467-9280.2006.01693.x](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x); [PDF](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf)
- **Meaningful prose, Experiment 2 (180 undergraduates):**

  | Condition | Recall at 5 min | Recall at 1 week | Forgetting over the week |
  |---|---|---|---|
  | SSSS (study ×4) | 83% | 40% | 52% |
  | SSST (study ×3, test ×1) | 78% | 56% | 28% |
  | STTT (study ×1, test ×3) | 71% | 61% | 14% |

  Forgetting is measured as (initial − final)/initial. The SSSS students read the passage 14.2 times on average; the STTT students read it 3.4 times. — [Roediger & Karpicke 2006 (PDF)](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf)

### Inferences
- Popular claims like "we forget 70% in 24 hours" come from savings scores for meaningless syllables. They are not recall rates for technical concepts, and the notes should not repeat them.
- The practical rule is robust anyway: without retrieval, most accessible memory is lost within days. Schedule retrieval at about 1 day and about 1 week after first exposure. A night of sleep before the first review is likely helpful (see Q7).
- Memory for a video-lecture concept watched once and never retrieved should be assumed to be poor after a week. The system should never treat "watched" as "learned."
- **Interference risk.** The Dros 31-day result warns that cramming many similar items (for example, many near-identical API names or hyperparameters) without spaced review accelerates forgetting.

### Gaps
- There is no authoritative single figure for "percent retained after 1 day / 1 week" for technical or conceptual material. It depends on degree of original learning, test type (recognition vs recall) and material. The Roediger & Karpicke prose data are the closest well-controlled benchmark.
- Two automated summaries of Murre & Dros gave conflicting numbers. The values above come from a verbatim reproduction of Table 3.

## Q2. Spacing: Cepeda et al. (2006, 2008), optimal gap as a fraction of the retention interval, expanding vs uniform schedules, successive relearning

### Takeaway
Spaced practice reliably beats massed practice, and the best gap grows with how long you need to remember. Cepeda et al. (2008) put the optimal gap at about 20-40% of the retention interval for a 1-week horizon, falling to about 5-10% for a 1-year horizon. Overshooting the gap costs less than undershooting it. Expanding schedules are not reliably better than uniform ones; what matters is spacing plus successful retrieval with feedback. Successive relearning (Rawson & Dunlosky) gives a practical recipe: reach 3 correct recalls in the first session, then relearn 3 times at widely spaced intervals.

### Cited Findings
- **Cepeda et al. (2006) meta-analysis:** 839 assessments of distributed practice in 317 experiments from 184 articles. The inter-study interval (ISI) and the retention interval jointly determine retention, and the ISI that maximizes retention increases as the retention interval increases. — [Cepeda, Pashler, Vul, Wixted & Rohrer (2006), *Psychological Bulletin* 132(3):354-380, DOI 10.1037/0033-2909.132.3.354](https://escholarship.org/uc/item/3rr6q10c); [author page](https://www.yorku.ca/ncepeda/publications/CPVWR2006.html)
- **Cepeda et al. (2008) "temporal ridgeline":** more than 1,350 people learned facts and were reviewed after gaps of up to 3.5 months, with final tests up to 1 year later. At any test delay, lengthening the gap first increased and then gradually reduced final performance. "The optimal gap increased as test delay increased." As a proportion of test delay, the optimal gap "declined from about 20 to 40% of a 1-week test delay to about 5 to 10% of a 1-year test delay." — [Cepeda, Vul, Rohrer, Wixted & Pashler (2008), *Psychological Science* 19(11):1095-1102, DOI 10.1111/j.1467-9280.2008.02209.x](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x); [PubMed](https://pubmed.ncbi.nlm.nih.gov/19076480/); [PDF](https://laplab.ucsd.edu/articles/Cepeda%20et%20al%202008_psychsci.pdf)
- **Latimier, Peyre & Ramus (2021) meta-analysis of spaced retrieval practice:** 29 studies, analysed with meta-regression and robust variance estimation.
  - Spaced retrieval practice beat massed retrieval practice: g = 0.74 (39 effect sizes).
  - There was "no significant difference between expanding and uniform spacing schedules" (g = 0.034; 54 effect sizes).
  - The number of exposures explains inconsistencies: "the more learners are tested, the more beneficial the expanding schedule is compared with the uniform one."
  - Sources: [*Educational Psychology Review* 33:959-987, DOI 10.1007/s10648-020-09572-8](https://link.springer.com/article/10.1007/s10648-020-09572-8); [ERIC abstract](https://eric.ed.gov/?id=EJ1310148)
- **Karpicke & Roediger (2007):** expanding retrieval practice helped short-term retention, but equally spaced retrieval gave better long-term retention (per the paper's title and abstract). — [Karpicke & Roediger (2007), *JEP: Learning, Memory, and Cognition* 33(4):704-719, DOI 10.1037/0278-7393.33.4.704](https://doi.org/10.1037/0278-7393.33.4.704) (cited from DOI; not re-fetched this session)
- **Successive relearning prescription:** practice recalling concepts to an initial criterion of 3 correct recalls, then relearn them 3 times at widely spaced intervals. Recalling each item correctly once in each of 3 spaced sessions produced more than twice the recall of recalling it correctly 3 times in a single session. — [Rawson & Dunlosky (2022), "Successive Relearning: An Underexplored but Potent Technique…," *Current Directions in Psychological Science*, DOI 10.1177/09637214221100484](https://journals.sagepub.com/doi/full/10.1177/09637214221100484); [Dunlosky et al. guide for educators (UNH PDF)](https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-successive-relearning-dunlosky-greve-badali-wissman-rawson.pdf)
- **Successive relearning in real courses:** it improved course-exam performance and long-term retention. — [Rawson, Dunlosky & Sciartelli (2013), "The Power of Successive Relearning…," *Educational Psychology Review*](https://www.researchgate.net/publication/258845409_The_Power_of_Successive_Relearning_Improving_Performance_on_Course_Exams_and_Long-Term_Retention)

### Inferences
- **Rule of thumb for the scheduler:** set the next gap at roughly 10-30% of how long the learner must retain the item. Because the curve is asymmetric, err on the long side once an item has been retrieved successfully 2-3 times.
- **For "use at work months from now":** an item reviewed at day 1, about 4, about 10, about 25, about 60 and about 150 approximately follows an expanding ridgeline. Spaced-repetition software such as FSRS/SM-2 automates this per item.
- **Expanding vs uniform is a second-order choice.** Algorithmic expanding intervals are fine because they cut workload. Just don't claim expansion itself boosts retention.
- **Concept-level mastery rule for the AI tutor:** an idea counts as "mastered" only after 1 correct unaided recall in each of 3 separate spaced sessions (days apart), not after 3 correct answers in one sitting.

### Gaps
- Cepeda-type evidence is mostly verbal and factual (trivia, vocabulary). Direct evidence for optimal gaps on programming or procedural skills is thin, so extrapolation is required.
- Precise optimal gaps for mixed retention horizons (for example, a job interview in 6 weeks plus long-term career use) have not been worked out.

## Q3. Retrieval practice / testing effect, feedback timing, pretesting

### Takeaway
Practising retrieval (quizzing yourself) is among the most robust learning techniques.
- Meta-analytic effects are about g = 0.50-0.61 overall, about 0.51 against restudying and about 0.93 against doing nothing.
- Feedback strengthens the effect (g 0.73 with feedback vs 0.39 without).
- Retrieval beats elaborative concept mapping by a large margin (d = 1.50), and learners consistently mispredict this.
- Prequestions before a video help learning of the specific questioned content (g = 0.66) but not of other content (g = 0.01).

### Cited Findings
- **Roediger & Karpicke (2006):** students studied prose passages and either took free-recall tests without feedback or restudied equally often.
  - At 1 week: 56% (tested) vs 42% (restudied); STTT 61% vs SSSS 40%. At 5 minutes, restudy won (81% vs 75%). Full figures are in Q1.
  - Metacognition misled learners. On a 7-point scale, the SSSS students were the most confident they would remember the passage in a week (4.8, vs 4.2 for SSST and 4.0 for STTT), yet they performed worst.
  - Source: [Roediger & Karpicke (2006), *Psychological Science* 17(3):249-255](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x); [PDF](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf)
- **Karpicke & Blunt (2011), Experiment 1 (80 undergraduates, final test 1 week later):**
  - Retrieval practice scored M = 0.67 vs M = 0.45 for elaborative concept mapping, "about a 50% improvement in long-term retention scores" (d = 1.50).
  - Concept mapping was not significantly better than spending the same extra time rereading.
  - Students predicted that repeated studying would work best and retrieval worst.
  - Source (read from the paper's PDF): [Karpicke & Blunt (2011), *Science* 331(6018):772-775, DOI 10.1126/science.1199327](https://www.science.org/doi/10.1126/science.1199327); [PDF](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf)
- **Karpicke & Blunt (2011), Experiment 2 (120 students, within-subject):**
  - Retrieval beat concept mapping on the short-answer test (d = 1.07). It even won on a final test that required building a concept map (d = 1.01).
  - 101 of 120 students (84%) did better with retrieval practice.
  - 75% believed concept mapping would be as good or better.
  - Source: [Karpicke & Blunt 2011 PDF](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf)
- **Critique of Karpicke & Blunt:** a published *Science* comment challenged the concept-mapping comparison. — [Mintzes et al., Comment, *Science* (2011)](https://www.science.org/doi/10.1126/science.1203698)
- **Adesope, Trevisan & Sundararajan (2017) meta-analysis:** 272 independent effects from 188 experiments. Practice tests vs all comparison conditions g = 0.61; vs restudying g = 0.51; vs filler or no activity g = 0.93. — [*Review of Educational Research* 87(3):659-701, DOI 10.3102/0034654316689306](https://journals.sagepub.com/doi/abs/10.3102/0034654316689306); numbers per [Wing Institute summary](https://www.winginstitute.org/news/effective-practice-tests/)
- **Rowland (2014) meta-analysis (testing vs restudy):** overall g = 0.50. Testing with feedback gave g = 0.73; without feedback, g = 0.39. — [Rowland (2014), *Psychological Bulletin* 140(6):1432-1463](https://pubmed.ncbi.nlm.nih.gov/25150680/); [PDF](https://courseware.epfl.ch/assets/courseware/v1/fdde2f0aa590bf3b1324077a6bf1540c/asset-v1%3AEPFL%2BDEMO%2B2020%2Btype%40asset%2Bblock/Rowland2014-meta-analysis.pdf)
- **Question type should match the goal (Agarwal 2019):** "Initial retrieval practice enhanced final test performance, but only when the initial quiz type (fact or higher-order) matched the final test type." Mixed fact-plus-higher-order quizzes helped on both kinds of test. Fact-only quizzes did not beat restudy on delayed higher-order tests. — [Agarwal (2019), *Journal of Educational Psychology* 111(2):189-209](https://eric.ed.gov/?id=EJ1205208); [Learning Scientists summary](https://www.learningscientists.org/blog/2019/6/27-1)
- **Feedback timing:** evidence is mixed and setting-dependent.
  - In lab studies delayed feedback often wins; in classroom studies immediate feedback often wins.
  - Many studies confound feedback timing with the time left before the final test, which inflates the apparent benefit of delayed feedback.
  - A 2024 medical-education study found immediate and delayed feedback "equally beneficial" for formative multiple-choice testing.
  - Sources: [Review: "Immediate Versus Delayed Feedback on Learning…" (2023)](https://www.researchgate.net/publication/373114533_Immediate_Versus_Delayed_Feedback_on_Learning_Do_People's_Instincts_Really_Conflict_with_Reality); ["Timing's not everything…," *Medical Education* (2024)](https://asmepublications.onlinelibrary.wiley.com/doi/full/10.1111/medu.15287)
- **Hypercorrection:** errors made with high confidence are especially likely to be corrected after feedback. — [Butterfield & Metcalfe (2001), *JEP: LMC* 27(6):1491-1494, DOI 10.1037/0278-7393.27.6.1491](https://doi.org/10.1037/0278-7393.27.6.1491) (cited from DOI; not re-fetched this session)
- **Pretesting and prequestions (Pan & Carpenter 2023 review):** testing learners on content they don't yet know helps "if there is an opportunity to study correct answers afterwards." The effect appears with texts, videos and lectures, and more than 60 peer-reviewed articles exist. — [Pan & Carpenter (2023), *Educational Psychology Review*, DOI 10.1007/s10648-023-09814-5](https://link.springer.com/article/10.1007/s10648-023-09814-5)
- **Prequestion meta-analysis (2025):** prequestions improved learning of the prequestioned information (g = 0.66). There was "no evidence of a general learning benefit" for non-prequestioned information (g = 0.01). — [King-Shepard, Walker, Nokes-Malach et al. (2025), "The Effect of Prequestions on Learning: A Multilevel Meta-Analysis," *Educational Psychology Review* 37:115, DOI 10.1007/s10648-025-10075-7](https://link.springer.com/article/10.1007/s10648-025-10075-7)

### Inferences
- **The AI tutor's core loop should be retrieval-first:**
  1. Ask before telling.
  2. Grade the free-recall answer.
  3. Give explanatory feedback.
  4. Re-ask missed items later.
  Rereading, re-watching and concept-mapping without retrieval should be de-emphasized.
- **Prefer short-answer or explain-in-your-own-words questions** for durable learning, and ask for a confidence rating before revealing the answer. High-confidence errors are the most valuable to correct (hypercorrection).
- **Prequestions should target the video's key concepts only.** They focus attention on exactly what is asked and give no general boost.
- **Feedback timing:** immediate feedback is the pragmatic default for a self-paced adult. Also re-test the same item after a delay (later in the session or the next day). That captures most of the delayed-feedback benefit without the confound.
- **Metacognitive illusion:** learners will feel rereading or re-watching works better. The system should show them their own delayed-test data to counter this.

### Gaps
- Most testing-effect research uses prose or word lists. Evidence for programming-concept quizzes is inferred.
- The outcome of the Social Sciences Replication Project attempt on Karpicke & Blunt (2011) was not verified.

## Q4. Dunlosky et al. (2013) utility ratings for the 10 techniques

### Takeaway
Of the 10 common study techniques, only practice testing and distributed practice earned "high utility." Elaborative interrogation, self-explanation and interleaved practice were "moderate." Summarization, highlighting/underlining, the keyword mnemonic, imagery for text and rereading were "low," yet these are the techniques students use most.

### Cited Findings
- **Ratings by utility:**
  - High: practice testing; distributed practice.
  - Moderate: elaborative interrogation; self-explanation; interleaved practice.
  - Low: summarization; highlighting/underlining; keyword mnemonic; imagery use for text learning; rereading.
  - Source: [Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), "Improving Students' Learning With Effective Learning Techniques," *Psychological Science in the Public Interest* 14(1):4-58, DOI 10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266) (cited from DOI; the classification is widely reproduced)
- **Later evidence supports the "moderate" techniques:**
  - Self-explanation meta-analysis: g = 0.55 (see Q5).
  - Interleaving meta-analysis: g = 0.42, dependent on similarity (see Q5).
  - Sources: [Bisra et al. 2018](https://link.springer.com/article/10.1007/s10648-018-9434-x); [Brunmair & Richter 2019](https://psycnet.apa.org/record/2019-57442-001)

### Inferences
- **For system design:** build spacing plus retrieval into every session, and add self-explanation and elaborative "why/how" prompts inside the tutor dialogue.
- Interleave related-but-confusable topics (for example, different loss functions or different sorting algorithms).
- Don't build features around highlighting, summarizing or re-watching as primary learning activities.

### Gaps
- The 2013 ratings reflect evidence up to 2012. There is no official update, and some "low" ratings (for example, summarization when trained) are debated. No formal re-rating was found.

## Q5. Other techniques: interleaving, elaborative interrogation, self-explanation, generation, desirable difficulties, worked examples and cognitive load theory, learning by teaching ("Feynman"/protégé effect)

### Takeaway
Interleaving helps when categories are similar and easily confused (g = 0.42 overall), but it can hurt for dissimilar word lists. Self-explanation (g = 0.55) and learning by teaching (g = 0.35-0.56) are solid. Worked examples beat unguided problem solving for novices, but the benefit reverses as expertise grows (the expertise-reversal effect). The "Feynman technique" has no direct trials. Its evidence base is self-explanation, learning by teaching and retrieval. Teaching helps most when done from memory and interactively.

### Cited Findings
- **Rohrer & Taylor (2007), interleaving in math:** students learned to compute volumes of four solids. One week later, interleaved practice scored 63% vs 20% for blocked practice. This was despite blocked practice doing better during the practice session (89% vs 60%). — [Rohrer & Taylor (2007), *Instructional Science* 35:481-498](https://link.springer.com/article/10.1007/s11251-007-9015-8)
- **Brunmair & Richter (2019) meta-analysis:** 59 studies, 238 effect sizes. Overall interleaving effect g = 0.42.
  - Paintings: g = 0.67.
  - Math: g = 0.34.
  - Expository texts: ambiguous, non-significant.
  - Words: blocking was better (g = −0.39).
  - Effects were stronger when categories are similar to each other, items within a category vary, and material is complex.
  - Source: [*Psychological Bulletin* 145(11):1029-1052](https://psycnet.apa.org/record/2019-57442-001); [preprint PDF](https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf)
- **Self-explanation meta-analysis:** 69 effect sizes from 64 reports; prompting learners to self-explain gave g = 0.55 across tasks such as problem solving, worked examples and text. — [Bisra, Liu, Nesbit, Salimi & Winne (2018), *Educational Psychology Review* 30:703-725](https://link.springer.com/article/10.1007/s10648-018-9434-x)
- **Original self-explanation studies:** good learners spontaneously self-explain worked examples (1989), and eliciting self-explanations improves understanding (1994). — [Chi et al. (1989), *Cognitive Science* 13(2):145-182, DOI 10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1); [Chi, de Leeuw, Chiu & LaVancher (1994), *Cognitive Science* 18(3):439-477, DOI 10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3) (cited from DOIs)
- **Generation effect:** self-generated items are remembered better than items that are simply read. — [Slamecka & Graf (1978), *JEP: Human Learning and Memory* 4(6):592-604, DOI 10.1037/0278-7393.4.6.592](https://doi.org/10.1037/0278-7393.4.6.592) (cited from DOI)
- **Desirable difficulties:** conditions that make learning feel harder can improve long-term retention and transfer, even though they slow apparent progress. Examples are spacing, interleaving, testing and generation. Bjork's framework distinguishes storage strength from retrieval strength. — [Bjork & Bjork (2011), "Making things hard on yourself, but in a good way," in *Psychology and the Real World*](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)
- **Cognitive load theory:** conventional problem solving (means-ends analysis) imposes heavy cognitive load that can interfere with learning schemas. This is the basis of the worked-example effect. — [Sweller (1988), *Cognitive Science* 12(2):257-285, DOI 10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4) (cited from DOI)
- **Expertise-reversal effect:** guidance that helps novices, such as worked examples, becomes redundant or harmful for more knowledgeable learners. — [Kalyuga, Ayres, Chandler & Sweller (2003), *Educational Psychologist* 38(1):23-31, DOI 10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4) (cited from DOI)
- **Minimal guidance is less effective for novices** than guided instruction (worked examples, process worksheets). This is a caution against unguided "just build a project" learning at the very start. — [Kirschner, Sweller & Clark (2006), *Educational Psychologist* 41(2):75-86, DOI 10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1) (cited from DOI)
- **Learning by teaching meta-analysis:** 28 studies. Preparing to teach: g = 0.35. Teaching after preparing: g = 0.56. Both helped deep and surface learning, including after a delay. Benefits were larger when the teaching was interactive. — [Kobayashi (2019), *Japanese Psychological Research* 61(3), DOI 10.1111/jpr.12221](https://onlinelibrary.wiley.com/doi/10.1111/jpr.12221)
- **Protégé effect:** students put more effort into learning on behalf of a teachable computer agent than for themselves. — [Chase, Chin, Oppezzo & Schwartz (2009), *Journal of Science Education and Technology* 18:334-352, DOI 10.1007/s10956-009-9180-4](https://doi.org/10.1007/s10956-009-9180-4) (cited from DOI; not re-fetched)

### Inferences
- **"Feynman mode" for the AI tutor** should be implemented as:
  1. The learner explains a concept from memory (no notes) to the AI playing a curious novice.
  2. The AI asks "why/how/what if" follow-ups (elaborative interrogation and self-explanation).
  3. The AI flags gaps and misconceptions.
  4. The learner re-explains.
  This combines retrieval, self-explanation and interactive teaching, the strongest-supported ingredients.
- **Interleave within a topic family** where discrimination matters: for example, "which algorithm or loss or data structure fits this case?", or regularization types. Block the first introduction of a brand-new concept, then interleave in later practice and reviews.
- **Novice phase:** use worked examples, then faded worked examples, then independent problems. Reduce guidance as competence grows (expertise reversal).

### Gaps
- There is no controlled study of the "Feynman technique" as such, and no direct meta-analytic effect size for elaborative interrogation was retrieved this session.
- The generation-effect meta-analysis (Bertsch et al. 2007) effect size was not re-verified.
- The effect size of a worked-example meta-analysis for programming or math was not verified this session.

## Q6. Video learning: fluency illusion, interpolated testing, segmenting, video length, note-taking, playback speed

### Takeaway
A polished, fluent video makes learners feel they learned more without improving actual learning. Short quizzes between video segments substantially cut mind-wandering and boost final test scores (90% vs 68%). Learner-paced segmenting helps modestly (d of about 0.3). Shorter videos are more engaging, but the popular "10-minute attention span" and "under 6 minutes" rules are engagement heuristics, not learning laws. Watching at 1.5-2x speed costs little. The handwriting-vs-laptop evidence is contested: a direct replication failed, while a 2024 meta-analysis finds a small advantage for handwriting.

### Cited Findings
- **Fluency illusion (Carpenter et al. 2013):** students watched a roughly 1-minute science video delivered either fluently (confident, eye contact) or disfluently (fumbling, reading notes). Fluency raised perceived learning and ratings of the instructor, but "lecture fluency did not significantly affect the amount of information learned." — [Carpenter, Wilford, Kornell & Mullaney (2013), *Psychonomic Bulletin & Review* 20:1350-1356](https://pubmed.ncbi.nlm.nih.gov/23645413/); [BPS digest](https://www.bps.org.uk/research-digest/engaging-lecturers-can-breed-overconfidence)
- **Interpolated testing (Szpunar, Khan & Schacter 2013):** in an online lecture split into segments with brief tests between them:
  - Mind-wandering: 19% of probes in the tested group vs 39% (restudy) and 41% (non-tested).
  - Final cumulative test: 90% (tested) vs 76% (restudy) vs 68% (non-tested).
  - Tested students took more notes and reported less anxiety about the final test and lower perceived cognitive demand.
  - Source: [Szpunar, Khan & Schacter (2013), *PNAS* 110(16):6313-6317, DOI 10.1073/pnas.1221764110](https://www.pnas.org/doi/10.1073/pnas.1221764110)
- **Segmenting meta-analysis (Rey et al. 2019):** 56 investigations, 88 comparisons. Segmenting improved:
  - retention: d = 0.32, 95% CI [.20, .43] (the search snippet printed ".032", which the CI shows is a typo);
  - transfer: d = 0.36, 95% CI [.24, .48];
  - cognitive load: reduced, d = 0.23.
  It also increased learning time (d = −0.92). Learners with high prior knowledge benefited more for retention. — [Rey, Beege, Nebel et al. (2019), *Educational Psychology Review*, DOI 10.1007/s10648-018-9456-4](https://link.springer.com/article/10.1007/s10648-018-9456-4)
- **Video engagement at scale (Guo, Kim & Rubin 2014):** 6.9 million video-watching sessions across 4 edX courses.
  - "Shorter videos are much more engaging."
  - Informal talking-head footage mixed with slides is more engaging than slides alone.
  - Khan-style tablet drawing is more engaging.
  - High-quality recorded classroom lectures "might not make for engaging online videos."
  - Engagement was measured as watch time and attempts at follow-up problems, not learning.
  - Source: [Guo, Kim & Rubin (2014), L@S '14, DOI 10.1145/2556325.2566239](https://dl.acm.org/doi/10.1145/2556325.2566239); [text](https://pg.ucsd.edu/publications/edX-MOOC-video-production-and-engagement_LAS-2014.txt)
- **"10-minute attention span" is poorly supported** by evidence. — [Wilson & Korn (2007), "Attention during lectures: Beyond ten minutes," *Teaching of Psychology* 34(2):85-89, DOI 10.1080/00986280701291291](https://doi.org/10.1080/00986280701291291) (cited from DOI; not re-fetched)
- **Playback speed (Murphy et al. 2022):** "minimal costs" to comprehension from increasing speed from 1x to 1.5x or 2x, with declines beyond 2x.
  - Watching twice at 2x gave no general advantage.
  - Re-watching at 2x just before the test beat a single 1x viewing a week earlier.
  - Source: [Murphy, Hoover, Agadzhanyan, Kuehn & Castel (2022), *Applied Cognitive Psychology* 36(1), DOI 10.1002/acp.3899](https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.3899)
- **Note-taking, original claim:** laptop note-takers wrote more verbatim notes and did worse on conceptual questions. — [Mueller & Oppenheimer (2014), *Psychological Science* 25(6):1159-1168, DOI 10.1177/0956797614524581](https://doi.org/10.1177/0956797614524581) (cited from DOI)
- **Note-taking, failed direct replication (Urry et al. 2021):** laptop n = 74, longhand n = 68.
  - Laptop users again wrote more words and more verbatim text, but there was "no relationship between typed versus longhand note taking and conceptual recall."
  - Mini meta-analyses of 8 similar studies also found no significant effect on immediate learning.
  - Source: [Urry et al. (2021), *Psychological Science* 32(3), DOI 10.1177/0956797620965541](https://journals.sagepub.com/doi/10.1177/0956797620965541); [APS summary](https://www.psychologicalscience.org/observer/writing-notes)
- **Note-taking, 2024 meta-analysis (Flanigan et al.):** 24 studies from 21 articles. "Taking and reviewing handwritten notes leads to higher achievement (Hedges' g = 0.248)." Typing yields much greater note volume (g = 0.919). — [Flanigan et al. (2024), *Educational Psychology Review*, DOI 10.1007/s10648-024-09914-w](https://link.springer.com/article/10.1007/s10648-024-09914-w)

### Inferences
- **How to watch a video in this system:**
  1. Answer 2-3 prequestions on the key ideas.
  2. Watch in chunks of about 5-10 minutes, pausing at natural topic boundaries.
  3. At each pause, write 2-3 bullet points from memory before resuming (interpolated retrieval).
  4. After the video, take a closed-book AI quiz.
- Speed of 1.25-1.75x is fine. Use the saved time for retrieval, not re-watching.
- **Note-taking medium matters less than processing.** Encourage brief paraphrased notes (by hand if convenient) and closed-book recall. Discourage verbatim transcription and re-watching as study.
- **Warn the learner about fluency:** "This video felt clear" is not evidence of learning. Only the quiz is.

### Gaps
- No rigorous RCT establishes an "optimal video length" for learning, as opposed to engagement. The widely cited "about 6 minutes" figure from Guo et al. was not confirmed from the text fetched.
- Mayer's full principle list and the effect sizes for each were not re-verified this session; only segmenting was.

## Q7. Sleep and consolidation, exercise, breaks/Pomodoro, interleaved study across days

### Takeaway
A night of sleep loss before learning impairs memory by a medium amount (g = 0.62), and sleep loss after learning by a smaller amount (g = 0.28). Learning in the evening and relearning the next morning after sleep halves relearning effort and improves retention at 1 week. Acute exercise gives small-to-moderate memory boosts. Scheduled short breaks (Pomodoro-style) improve mood and focus compared with self-regulated breaks, without better task completion. Micro-breaks raise vigor and cut fatigue but don't reliably raise cognitive performance.

### Cited Findings
- **Sleep deprivation meta-analyses (Newbury et al. 2021):** one night of total sleep loss before encoding impaired memory, g = 0.62 (31 reports, 55 effect sizes, 927 participants). Sleep deprivation after learning: g = 0.277, 95% CI [0.177, 0.377]. — [Newbury, Crowley, Rastle & Tamminen (2021), *Psychological Bulletin* 147(11):1215-1240](https://pubmed.ncbi.nlm.nih.gov/35238586/); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8893218/)
- **Sleep between sessions (Mazza et al. 2016):** 40 participants learned vocabulary to perfect performance in two sessions 12 hours apart. Those who slept between learning (evening) and relearning (next morning) needed about half the relearning practice. They also retained more at 1 week (about 15 vs about 11 word pairs), and the benefit was still visible at 6 months. — [Mazza et al. (2016), *Psychological Science*, DOI 10.1177/0956797616659930](https://journals.sagepub.com/doi/abs/10.1177/0956797616659930); [APS release](https://www.psychologicalscience.org/news/releases/sleep-makes-relearning-faster-and-longer-lasting.html)
- **Exercise meta-analysis (Roig et al. 2013):** 29 acute and 21 long-term studies. Acute exercise had a moderate effect on short-term memory (SMD = 0.26, 95% CI 0.03-0.49); long-term exercise had a small effect (SMD = 0.15). The authors propose that acute exercise "primes" molecular processes of memory formation. — [Roig, Nordbrandt, Geertsen & Nielsen (2013), *Neuroscience & Biobehavioral Reviews* 37(8):1645-1666, DOI 10.1016/j.neubiorev.2013.06.012](https://pubmed.ncbi.nlm.nih.gov/23806438/)
- **Pomodoro vs self-regulated breaks (Biwer et al. 2023):** three conditions compared: self-regulated breaks (n = 35); 24-minute study blocks with 6-minute breaks ("Pomodoro," n = 25); and 12-minute blocks with 3-minute breaks (n = 27).
  - Self-regulators took longer sessions and breaks. This was associated with more fatigue and distraction and with lower concentration and motivation.
  - There was no difference in mental effort or task completion.
  - Systematic breaks had "mood benefits and appeared to have efficiency benefits."
  - Source: [Biwer, Wiradhany, oude Egbrink & de Bruin (2023), *British Journal of Educational Psychology* 93(S2):353-367, DOI 10.1111/bjep.12593](https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/bjep.12593); [PubMed](https://pubmed.ncbi.nlm.nih.gov/36859717/)
- **Micro-breaks of 10 minutes or less (Albulescu et al. 2022):** 22 samples, N = 2,335.
  - Vigor up: d = 0.36. Fatigue down: d = 0.35. Overall performance: d = 0.16, not significant.
  - Performance gains appeared only for less cognitively demanding tasks, and longer breaks gave larger boosts.
  - Source: [Albulescu et al. (2022), *PLOS ONE*, DOI 10.1371/journal.pone.0272460](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0272460)
- **Interleaving and spacing across days:** see Q2 (spacing: Latimier 2021 g = 0.74) and Q5 (interleaving: Rohrer & Taylor 2007; Brunmair & Richter 2019).

### Inferences
- **For a working adult:**
  - Protect sleep. A late-night cram after a short night is the worst case, and pre-learning sleep loss has the largest penalty.
  - Put a short retrieval review at the end of an evening session, then a quick relearn or retrieval the next morning or commute (the Mazza pattern).
  - Deep-learning sessions work best before tiredness sets in. On heavy workdays, do only flashcard reviews.
- Use fixed work/break blocks (for example, 25/5 or 50/10) for mood and focus. Don't expect them to raise learning by themselves.
- A brisk 10-20 minute walk or workout before a study session is a low-cost, plausibly helpful add-on, but the evidence is modest.

### Gaps
- The Roig et al. effect size for acute exercise on long-term memory was not captured from the abstract fetched.
- No direct evidence was found on the optimal study-block length for technical learning. Pomodoro's 25/5 split is a convention, not an evidence-derived optimum.

## Q8. Motivation and habits for working adults: habit formation, implementation intentions, growth mindset, self-efficacy, streaks/gamification, deliberate practice

### Takeaway
Habits take about 2 months to form (median 59-66 days, with a very wide range). Missing a single day does not derail habit formation. "If-then" implementation intentions have a medium-to-large effect on goal attainment (d = 0.65). Growth-mindset interventions have tiny or null average effects on achievement, and the highest-quality studies show about zero, so the system should not promise mindset magic. Gamification has small positive effects. Streak displays motivate while intact, but broken streaks demotivate, and "emergency reserve" skip days increase persistence. Deliberate practice matters but explains far less variance outside structured domains.

### Cited Findings
- **Habit formation (Lally et al. 2010):** new health behaviours took a median of 66 days (range 18-254) to become automatic. "Missing one opportunity to perform the behaviour did not materially affect the habit formation process." — [Lally, van Jaarsveld, Potts & Wardle (2010), *European Journal of Social Psychology* 40(6):998-1009, DOI 10.1002/ejsp.674](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674)
- **Habit formation review (Singh et al. 2024):** median times of 59-66 days, means of 106-154 days, and individual range 4-335 days. — [Singh et al. (2024), "Time to Form a Habit…," *Healthcare* 12(23):2488](https://www.mdpi.com/2227-9032/12/23/2488); [PubMed](https://pubmed.ncbi.nlm.nih.gov/39685110/)
- **Implementation intentions (Gollwitzer & Sheeran 2006):** meta-analysis of 94 independent tests; "if-then" plans had a medium-to-large effect on goal attainment, d = 0.65. — [Gollwitzer & Sheeran (2006), *Advances in Experimental Social Psychology* 38:69-119, DOI 10.1016/S0065-2601(06)38002-1](https://doi.org/10.1016/S0065-2601(06)38002-1) (cited from DOI; not re-fetched)
- **Growth mindset (Sisk et al. 2018):** two meta-analyses. The mindset-achievement association was weak (273 effect sizes, N = 365,915). Interventions averaged d = 0.08 (43 effect sizes, N = 57,155). — [Sisk, Burgoyne, Sun, Butler & Macnamara (2018), *Psychological Science* 29(4):549-571, DOI 10.1177/0956797617739704](https://journals.sagepub.com/doi/10.1177/0956797617739704)
- **Growth mindset (Yeager et al. 2019):** in a national US experiment, a less-than-1-hour online intervention improved grades among lower-achieving students, mainly in schools whose peer norms supported the message. In medium- to low-achieving schools with supportive norms, lower-achievers gained about 0.15 grade points in core courses. — [Yeager et al. (2019), *Nature* 573:364-369, DOI 10.1038/s41586-019-1466-y](https://www.nature.com/articles/s41586-019-1466-y)
- **Growth mindset (Macnamara & Burgoyne 2023):**
  - All studies (63 studies, N = 97,672): d̄ = 0.05, 95% CI [0.02, 0.09], "nonsignificant after correcting for potential publication bias."
  - Studies where the intervention actually changed mindsets (13 studies): d̄ = 0.04, not significant.
  - Highest-quality evidence (6 studies, N = 13,571): d̄ = 0.02, not significant.
  - Authors with a financial incentive reported larger effects.
  - Source: [Macnamara & Burgoyne (2023), *Psychological Bulletin* 149(3-4):133-173, DOI 10.1037/bul0000352](https://artscimedia.case.edu/wp-content/uploads/sites/141/2020/06/26110416/Macnamara-Burgoyne-2023.pdf)
  - Counter-view: commentators argue that heterogeneity-focused analysis shows where effects exist. — [Commentary on Macnamara & Burgoyne (2023) and Burnette et al. (2023)](https://profiles.wustl.edu/en/publications/why-meta-analyses-of-growth-mindset-and-other-interventions-shoul/)
- **Self-efficacy theory:** mastery experiences are the strongest source of self-efficacy. — [Bandura (1977), *Psychological Review* 84(2):191-215, DOI 10.1037/0033-295X.84.2.191](https://doi.org/10.1037/0033-295X.84.2.191) (cited from DOI)
- **Self-efficacy and grades (Richardson, Abraham & Bond 2012):** meta-analysis of 241 data sets and 1,105 correlations covering 50 distinct correlates of university GPA. "Performance self-efficacy" was the strongest correlate (a "large correlation"), ahead of high-school GPA, ACT scores and grade goals. — [Richardson, Abraham & Bond (2012), *Psychological Bulletin* 138(2):353-387, DOI 10.1037/a0026838](https://eric.ed.gov/?id=EJ962899)
- **Gamification meta-analysis (Sailer & Homner 2020):** cognitive outcomes g = 0.49 (k = 19); motivational g = 0.36 (k = 16); behavioral g = 0.25 (k = 9). Cognitive effects were stable in rigorous studies; motivational and behavioral effects were less stable. — [Sailer & Homner (2020), *Educational Psychology Review* 32:77-112](https://eric.ed.gov/?id=EJ1245270)
- **Streaks:** highlighting an intact streak increases continued engagement relative to highlighting a broken one. Even a streak broken by a technical glitch rather than the user's own lapse demotivates. — [Silverman & Barasch (2023), "On or Off Track: How (Broken) Streaks Affect Consumer Decisions," *Journal of Consumer Research* 49(6):1095](https://academic.oup.com/jcr/article-abstract/49/6/1095/6623414)
- **Emergency reserves:** goals with "slack with a cost," such as a 7-day exercise goal with 2 emergency skip days, were preferred and increased persistence, including after a miss. — [Sharif & Shu (2017), *Journal of Marketing Research* 54(3), DOI 10.1509/jmr.15.0231](https://journals.sagepub.com/doi/10.1509/jmr.15.0231); [follow-up on persistence after failure, *OBHDP* 2019](https://www.sciencedirect.com/science/article/abs/pii/S0749597818304187)
- **Deliberate practice, origin:** the theory that expert performance is largely the product of deliberate practice. — [Ericsson, Krampe & Tesch-Römer (1993), *Psychological Review* 100(3):363-406, DOI 10.1037/0033-295X.100.3.363](https://doi.org/10.1037/0033-295X.100.3.363) (cited from DOI)
- **Deliberate practice, meta-analysis (Macnamara, Hambrick & Oswald 2014):** it explained 26% of performance variance in games, 21% in music, 18% in sports, 4% in education and less than 1% in professions. — [*Psychological Science* 25(8):1608-1618, DOI 10.1177/0956797614535810](https://doi.org/10.1177/0956797614535810) (cited from DOI; not re-fetched)
- **Deliberate practice, replication:** a replication of Ericsson et al.'s violinist study did not reproduce the original's strong conclusions (for example, that the best violinists had accumulated more practice than the good ones). — [Macnamara & Maitra (2019), *Royal Society Open Science* 6:190327, DOI 10.1098/rsos.190327](https://doi.org/10.1098/rsos.190327) (cited from DOI; not re-fetched)
- **Public announcements:** publicly announcing identity-related intentions can reduce subsequent effort (premature sense of completeness). — [Gollwitzer, Sheeran, Michalski & Seifert (2009), *Psychological Science* 20(5), DOI 10.1111/j.1467-9280.2009.02336.x](https://doi.org/10.1111/j.1467-9280.2009.02336.x) (cited from DOI)

### Inferences
- **Habit design:**
  - Anchor study to a fixed cue using if-then plans. Example: "If it's 7:00 on a weekday after coffee, then I open the tutor and do 10 minutes of flashcards."
  - Plan for roughly 2-5 months before the routine feels automatic.
  - Frame a missed day as normal, and apply a "never miss twice" rule.
- **Streak mechanics:** use a weekly target with 1-2 built-in "emergency reserve" days rather than a fragile daily streak. Never display "streak broken" shaming.
- **For an AI-anxious learner:** build self-efficacy through visible mastery evidence. Examples are delayed-quiz accuracy curves and small completed projects, not motivational slogans. Growth-mindset messaging is harmless but should not be relied on.
- **Deliberate-practice framing is useful** for skill components with clear feedback, such as coding katas and debugging drills. Don't promise "10,000 hours" outcomes.

### Gaps
- No studies were found specifically on habit formation or streak design for adult self-directed technical learners.
- The exact r for performance self-efficacy in Richardson et al. (2012), often quoted as about .59, was not confirmed from the text retrieved. The evidence is correlational.
- Adult-specific growth-mindset evidence is lacking.

## Q9. AI tutors: evidence that LLM tutors help or harm learning, cognitive offloading concerns, and supported design guardrails

### Takeaway
Unguarded LLM access can raise performance while the AI is available but lower learning once it is removed (−17% on exams in Bastani et al., PNAS 2025). Carefully designed tutors avoid this harm or produce large gains:
- teacher-designed hints with solutions in the prompt (no answers given away);
- a structured, pedagogy-scripted tutor (Harvard physics RCT: more than 2x median gains in less time);
- teacher-guided use (World Bank Nigeria: about 0.3 SD in 6 weeks).

Anthropic's 2026 RCT on learning a new Python library found AI users scored 17 percentage points lower (50% vs 67%). Learners who used AI for conceptual questions and explanations kept their learning; those who delegated coding did not. The guardrails with the best support are retrieval-first, hints-not-answers, solution-grounded prompts, required explanation of any AI output, and periodic no-AI assessments.

### Cited Findings
- **Bastani et al. (PNAS, June 2025), "Generative AI without guardrails can harm learning": design.**
  - Nearly 1,000 high-school students in grades 9-11 across about 50 classrooms in Turkey.
  - Four 90-minute sessions covering about 15% of the math curriculum.
  - Three arms: control; GPT Base (ChatGPT-like GPT-4 interface); GPT Tutor (guardrailed).
  - Sources: [PNAS, DOI 10.1073/pnas.2422633122](https://www.pnas.org/doi/10.1073/pnas.2422633122); [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)
- **Bastani et al.: results.**
  - With AI during practice: GPT Base improved practice grades by 48%, GPT Tutor by 127%.
  - Exam without AI: GPT Base students scored 17% lower than control (statistically significant). GPT Tutor students showed no significant difference from control.
  - Source: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)
- **Bastani et al.: how GPT Tutor worked.**
  - It "provides hints to the student without directly giving them the answer."
  - Its prompt included "one or more (correct) solutions to the practice problem, as well as common student mistakes," prepared with teachers.
  - GPT Base gave a correct answer only 51% of the time (logical errors 42%, arithmetic errors 8%).
  - Source: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)
- **Bastani et al.: crutch behaviour and misperception.** Students used GPT Base as a crutch, asking for and copying solutions, and "only a small fraction of conversations are nonsuperficial." Those students "did not perceive that they performed worse or learned less." — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)
  - A later correction changed only an author affiliation, not findings. — [Correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC12403119/)
  - The working-paper title was "Generative AI Can Harm Learning." — [SSRN 4895486](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486)
- **Kestin et al. (Scientific Reports, 3 June 2025), Harvard physics RCT: design.**
  - 194 students in one Harvard physical-sciences course (PS2), Fall 2023.
  - Crossover design with two lessons in consecutive weeks: surface tension and fluid flow.
  - The AI tutor was compared with an in-class active-learning lesson, itself a strong control that is considered best practice.
  - Sources: [Kestin, Miller, Klales, Milbourne & Ponti (2025), *Scientific Reports* 15:17458, DOI 10.1038/s41598-025-97652-6](https://www.nature.com/articles/s41598-025-97652-6); [design details via ERCT summary](https://erctpapers.com/papers/47-kestin-et-al-2025-ai-tutoring-active-learning.html)
- **Kestin et al.: learning results (from the PMC full text).**
  - Median post-test scores: 4.5 with the AI tutor (N = 142) vs 3.5 in class (N = 174). The combined pre-test baseline was 2.75.
  - Median learning gains were "over double" those of the active-learning class.
  - Effect sizes: 0.63 by linear regression (described as underestimated because of ceiling effects), and "0.73 to 1.3 standard deviations" by quantile regression.
  - Mann-Whitney z = −5.6, p < 10⁻⁸.
  - Source: [Kestin et al. 2025, PMC12179260](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/)
- **Kestin et al.: time, engagement and motivation.**
  - Median AI time was 49 minutes (70% of students used less than 60) vs about 60 minutes of in-class learning. "There was no correlation between the time on task and students' post-test scores."
  - Engagement (5-point scale): 4.1 vs 3.6 (p < 0.0001). Motivation: 3.4 vs 3.1 (p < 0.001).
  - Enjoyment and growth-mindset ratings did not differ significantly.
  - Source: [PMC12179260](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/)
- **Kestin et al.: how the tutor was designed.** Seven pedagogical practices were built into the system prompts:
  1. "facilitating active learning";
  2. "managing cognitive load";
  3. "promoting a growth mindset";
  4. "scaffolding content";
  5. "ensuring accuracy of information and feedback";
  6. delivering feedback in "a targeted and timely fashion";
  7. "allowing for self-pacing."

  The tutor guided students "sequentially through each part of each problem." To avoid hallucinations, the authors "avoided relying solely on GPT-4 to generate solutions" and instead "enriched our prompts with comprehensive, step-by-step answers." 83% of students rated the AI's explanations as good as or better than human instructors'. — [PMC12179260](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/)
- **Kestin et al.: authors' cautions.**
  - Learning objectives were at the "understanding, applying, and analyzing" levels of Bloom's taxonomy.
  - The gains may depend on high-quality instructional videos, a model able to follow complex prompts (GPT-4), and "expert-crafted, question-specific prompts."
  - The authors "do not presume that structured AI tutoring will always outperform in-class active learning," especially for "complex synthesis" and "higher-order critical thinking."
  - "AI tutor should not replace in-person teaching" but should prepare students for class (a flipped model).
  - Source: [PMC12179260](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/)
- **Kestin et al.: external critiques.**
  - Only 2 lessons.
  - Custom (non-standardized) tests.
  - Highly prepared Harvard undergraduates.
  - The intervention was designed by the authors and has no independent replication.
  - Sources: [ERCT summary](https://erctpapers.com/papers/47-kestin-et-al-2025-ai-tutoring-active-learning.html); [ETC Journal review](https://etcjournal.com/2025/11/10/review-of-kestin-et-al-s-june-2025-harvard-study-on-ai-tutoring/)
- **World Bank Nigeria RCT: design.** A 6-week after-school program in mid-2024 in 9 public schools in Benin City, Edo State, for first-year senior-secondary students. Teachers guided students through structured interactions with Microsoft Copilot (GPT-4) on English grammar and writing. — [World Bank blog](https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria); [Policy Research Working Paper, "From Chalkboards to Chatbots…" (De Simone et al. 2025)](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)
- **World Bank Nigeria RCT: results and cost.**
  - Overall learning gain of about 0.3 SD, which the authors call "nearly two years of typical learning in just six weeks."
  - English: +0.24 SD. End-of-term school English exam: +0.21 SD.
  - Cost: about $48 per student.
  - It outperformed about 80% of developing-country education RCTs in a comparison database.
  - Sources: [World Bank blog](https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria); [PDF](https://documents1.worldbank.org/curated/en/099548105192529324/pdf/IDU-c09f40d8-9ff8-42dc-b315-591157499be7.pdf)
  - Caveat: "years of learning" conversions are rough benchmarks.
- **Anthropic RCT (29 Jan 2026), "How AI assistance impacts the formation of coding skills": design and headline result.**
  - Authors: Judy Hanwen Shen and Alex Tamkin.
  - 52 mostly junior engineers (at least 1 year of weekly Python) learning the unfamiliar async library Trio.
  - On a quiz minutes later, the AI-assisted group scored 50% vs 67% for hand-coders (Cohen's d = 0.738, p = 0.01).
  - The AI group was about 2 minutes faster, which was not significant.
  - The largest gap was on debugging questions.
  - Source: [Anthropic research post](https://www.anthropic.com/research/AI-assistance-coding-skills)
- **Anthropic RCT: usage patterns.**
  - High-scoring patterns (65% or more): "conceptual inquiry" (asked only conceptual questions and fixed errors themselves), "generation-then-comprehension" and "hybrid code-explanation."
  - Low-scoring patterns (below 40%): "AI delegation," "progressive reliance" and "iterative AI debugging."
  - Limitations: small n, immediate quiz only, and a company study (no peer review found).
  - Source: [Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills); [InfoQ coverage](https://infoq.com/news/2026/02/ai-coding-skill-formation/)
- **Microsoft Research & CMU (CHI 2025), cognitive offloading survey:**
  - 319 knowledge workers shared 936 first-hand examples of using generative AI at work.
  - "Higher confidence in GenAI is associated with less critical thinking, while higher self-confidence is associated with more critical thinking."
  - The evidence is self-reported and correlational.
  - Source: [Lee, Sarkar, Tankelevitch, Drosos, Rintel, Banks & Wilson (2025), CHI '25, DOI 10.1145/3706598.3713778](https://dl.acm.org/doi/full/10.1145/3706598.3713778); [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf)
- **MIT Media Lab "Your Brain on ChatGPT" (PREPRINT, not peer-reviewed):**
  - Posted to arXiv on 10 June 2025; v2 on 31 December 2025.
  - 54 participants in sessions 1-3, in three essay-writing groups: LLM, search engine, and brain-only. Only 18 completed session 4, which swapped conditions.
  - EEG connectivity was strongest for brain-only, moderate for search and weakest for the LLM group.
  - LLM users reported the lowest ownership of their essays and struggled to quote their own essays.
  - Source: [Kosmyna et al., arXiv:2506.08872](https://arxiv.org/abs/2506.08872)
- **Critiques of the MIT preprint:** a published commentary notes that counting significant connections shows greater beta-band engagement for the LLM condition, "reducing the consistency" of the headline finding. Other limitations: small sample, a single essay task, the 18-person session 4, and EEG connectivity is not a learning outcome. — [Commentary, arXiv:2601.00856](https://arxiv.org/pdf/2601.00856)
- **AI "study modes":** OpenAI launched ChatGPT Study Mode in July 2025, built around Socratic, step-by-step guidance that withholds direct answers. Anthropic launched Claude's "Learning mode" for Claude for Education in April 2025. Google launched Gemini "Guided Learning" in August 2025. — [VentureBeat on Study Mode](https://venturebeat.com/ai/chatgpt-just-got-smarter-openais-study-mode-helps-students-learn-step-by-step); [TechCrunch on Guided Learning](https://techcrunch.com/2025/08/06/google-takes-on-chatgpts-study-mode-with-new-guided-learning-tool-in-gemini/); [Inside Higher Ed](https://www.insidehighered.com/news/tech-innovation/artificial-intelligence/2025/08/07/understanding-value-learning-fuels-chatgpts)

### Inferences
The guardrails below are ranked by strength of support.

**1. Retrieval-first and answer-withholding by default.** The tutor asks the learner to attempt first. It gives graded hints: hint 1 is conceptual, hint 2 is a targeted step, hint 3 is a partial worked step. It reveals the full solution only after a genuine attempt, and then asks the learner to explain it back.
- Support: Bastani GPT Tutor; testing effect; Anthropic's "conceptual inquiry" pattern.

**2. Ground the tutor in verified solutions or references.** For quizzes, have the tutor check against a stored answer key, rubric or reference solution rather than improvising. Raw GPT-4 was wrong about 49% of the time on Bastani's problems.
- Support: Bastani prompt design; Kestin's pre-planned, pedagogy-scripted tutor.
- Practical form: each quiz or practice item carries a stored "solution + common mistakes + rubric" block written or verified once. The tutor walks the learner through problem parts one step at a time and lets them self-pace. This mirrors both the GPT Tutor and the PS2 Pal designs.

**3. Comprehension checks on any AI-generated code.** The learner must predict the output, explain line by line, or modify the code before moving on.
- Support: Anthropic's generation-then-comprehension pattern; self-explanation g = 0.55.

**4. Regular "AI-off" assessments.** Weekly closed-book quizzes and coding tasks without AI measure real learning. Performance with AI overstates learning, and learners don't notice.
- Support: Bastani.

**5. Calibration prompts.** Collect a confidence rating before each answer and show accuracy vs confidence over time. This counters the fluency illusion and over-trust in AI.
- Support: CHI 2025 confidence findings; Carpenter 2013.

**6. Keep the learner as the author.** At work, AI delegation may be fine for productivity. In learning mode, the learner writes first and the AI reviews.
- For an AI-anxious learner, frame this as building the skills AI can't substitute for (debugging, judgment, verification), which is exactly where the Anthropic study found the largest gaps.

### Gaps
- Kestin et al. tested only 2 physics lessons with Harvard students. How well the approach transfers to self-paced adult learners of programming or ML, without expert-written per-question solution prompts, is untested.
- No independent RCTs were found for commercial study modes (ChatGPT Study Mode, Claude learning mode, Gemini Guided Learning).
- No long-term (months) retention RCTs of LLM tutoring for adult self-learners were found.
- The Anthropic study measured only immediate quiz scores.

## Q10. Algorithms and tools: Leitner, SM-2 (exact), Anki's variant, FSRS (parameters, desired retention, benchmarks, 2026 status in Anki), Anki availability/cost, CSV import, flashcard-writing rules

### Takeaway
SM-2 (1987/1990) is a simple, well-specified algorithm:
- ease factor starts at 2.5;
- intervals are 1, 6, then previous interval × EF;
- EF update is EF + (0.1 − (5−q)(0.08 + (5−q)·0.02)), with a floor of 1.3;
- a grade below 3 restarts the repetitions.

FSRS (DSR model, 21 trainable parameters in FSRS-6) predicts recall much better than SM-2: lower log loss for about 99.6% of about 10,000 Anki collections in the community benchmark. FSRS has been in Anki since 23.10.

As of Anki 26.09 (September 2026), FSRS is still enabled with a toggle in deck options. No release note confirms it became the default, despite a December 2024 proposal. FSRS-7 exists in the benchmark but has not been confirmed as shipped.

Desired retention defaults to 90%, and workload climbs steeply above that. Anki desktop and AnkiDroid are free; AnkiMobile on iOS costs a one-time $24.99. CSV import is built in, with header directives.

### Cited Findings

**Leitner system**
- Cards live in numbered boxes. A correct answer promotes a card to the next box, which is reviewed less often; an error sends it back to box 1. — [Leitner system overview (Wikipedia; original: Leitner, *So lernt man lernen*, 1972)](https://en.wikipedia.org/wiki/Leitner_system)

**SM-2, exact specification (Wozniak, 1990; used from Dec 13, 1987 to Mar 9, 1989)**
1. "Split the knowledge into smallest possible items."
2. "With all items associate an E-Factor equal to 2.5."
3. Intervals: "I(1):=1; I(2):=6; for n>2: I(n):=I(n-1)*EF." "If interval is a fraction, round it up to the nearest integer."
4. Grades (verbatim):
   - 5 = "perfect response"
   - 4 = "correct response after a hesitation"
   - 3 = "correct response recalled with serious difficulty"
   - 2 = "incorrect response; where the correct one seemed easy to recall"
   - 1 = "incorrect response; the correct one remembered"
   - 0 = "complete blackout."
5. EF update: "EF':=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))"; "If EF is less than 1.3 then let EF be 1.3."
6. If q < 3, start repetitions from the beginning (I(1), I(2)…) "without changing the E-Factor."
7. After each day's session, repeat all items that scored below 4 until "all of these items score at least four."
- Source: [Wozniak, SM-2 description, super-memory.com](https://super-memory.com/english/ol/sm2.htm)
- Derived EF deltas: q=5: +0.10; q=4: 0.00; q=3: −0.14; q=2: −0.32; q=1: −0.54; q=0: −0.80. These are computed from the formula above; see the same source.

**Anki's SM-2-based ("legacy") scheduler defaults (from the Anki manual)**
- Starting ease "defaults to 2.50."
- Easy bonus default 1.30. Hard interval default 1.20.
- Interval modifier 1.00 ("does nothing").
- New interval 0.00 (a lapsed review card's interval is reset).
- Maximum interval 100 years. Minimum interval 1 day. Minimum ease 130%.
- Uses 4 buttons (Again/Hard/Good/Easy) plus minute-level learning steps, for example "1m 10m 1d."
- Source: [Anki Manual — Deck Options](https://docs.ankiweb.net/deck-options.html)

**How Anki's SM-2 differs from SuperMemo's (Anki FAQ)**
- "Anki uses 4 choices for answering review cards, not 6. There is only one fail choice, not 3."
- Ease changes by button:
  - Again: "the ease is decreased by 20 percentage points."
  - Hard: "decreased by 15 percentage points."
  - Good: "unchanged."
  - Easy: "increased by 15 percentage points."
  - Easy also "adds an extra bonus to the current interval calculation."
- SM-2's fixed 1-day and 6-day starting intervals are replaced by user-configurable learning steps.
- As in SM-2, Again "resets the card interval by default," though users can choose a reduced rather than reset interval.
- "Successive failures while cards are in learning do not result in further decreases to the card's ease."
- Anki has offered two algorithms (SM-2-based and FSRS) since 23.10.
- Source: [Anki FAQ — "What spaced repetition algorithm does Anki use?"](https://faqs.ankiweb.net/what-spaced-repetition-algorithm.html)

**FSRS: what it is**
- The Free Spaced Repetition Scheduler models each card by Difficulty D (1-10), Stability S (days until recall probability falls to 90%) and Retrievability R (current recall probability).
- Grades: 1 Again, 2 Hard, 3 Good, 4 Easy.
- Grounded in papers on stochastic-shortest-path scheduling (KDD 2022) and memory dynamics (IEEE TKDE 2023).
- Source: [FSRS algorithm wiki (awesome-fsrs)](https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm); [older wiki page and paper references](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm)

**FSRS-6 formulas and default parameters (from the FSRS wiki)**
- Forgetting curve: R(t,S) = (1 + factor·t/S)^(−w20), where factor = 0.9^(−1/w20) − 1, so that R(S,S) = 0.9.
  - Before FSRS-6, the decay was fixed at −0.5 and factor = 19/81.
- Interval for a desired retention r (derived by inverting the curve): I = (S/factor)·(r^(−1/w20) − 1). At r = 0.9, I = S.
- Initial stability S0(G) = w[G−1].
- Initial difficulty D0(G) = w4 − e^(w5·(G−1)) + 1.
- Difficulty update:
  - ΔD = −w6·(G−3);
  - D′ = D + ΔD·(10−D)/9 (linear damping);
  - mean reversion D″ = w7·D0(4) + (1−w7)·D′.
- Stability after a successful review, as given in the wiki's FSRS v4 section: S′r(D,S,R,G) = S·(e^(w8)·(11−D)·S^(−w9)·(e^(w10·(1−R)) − 1)·w15 (if G = 2)·w16 (if G = 4) + 1).
  - Here w15 is the Hard penalty and w16 the Easy bonus.
  - The FSRS-6 defaults w15 = 0.6014 (<1) and w16 = 1.8729 (>1) are consistent with this form being retained.
  - Stability grows more when D is low, when S is low, and when R was low at review time (the spacing benefit).
- Stability after a lapse: S′f = w11·D^(−w12)·((S+1)^w13 − 1)·e^(w14·(1−R)).
- Same-day (short-term) review in FSRS-6: S′ = S·e^(w17·(G−3+w18))·S^(−w19).
- FSRS-6 default parameters (21 values, w0-w20): [0.212, 1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194, 0.001, 1.8722, 0.1666, 0.796, 1.4835, 0.0614, 0.2629, 1.6483, 0.6014, 1.8729, 0.5425, 0.0912, 0.0658, 0.1542].
  - Initial stabilities are therefore: Again ≈ 0.21 d, Hard ≈ 1.29 d, Good ≈ 2.31 d, Easy ≈ 8.30 d.
- Source: [FSRS wiki](https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm)

**FSRS in Anki: settings**
- FSRS has been supported since "Anki 23.10, AnkiMobile 23.10." It can "only be enabled globally," and is enabled "under the 'FSRS' section, at the bottom of the deck options page."
- Desired retention: "The default is 90%." "Above 90% the workload increases very quickly, and above 97% the workload can be overwhelming."
- Optimizer: click "Optimize"; "once every month is sufficient." A Health Check option exists.
- Learning steps: "(Re)learning steps of 1 day or greater are not recommended when using FSRS."
- Historical retention: when fitting old reviews, it assumes 90% by default.
- Source: [Anki Manual — Deck Options (FSRS)](https://docs.ankiweb.net/deck-options.html)

**FSRS default-on status**
- On 6 Dec 2024 Anki's developer (dae) proposed: "In the next non-trivial (not 24.11.x) update, I think it's about time we enable FSRS out of the box." — [GitHub issue #3616](https://github.com/ankitects/anki/issues/3616)
- None of the release notes checked mentions FSRS becoming enabled by default:
  - 25.02 (11 Feb 2025) — [Release 25.02](https://github.com/ankitects/anki/releases/tag/25.02)
  - 26.05 — [Release 26.05](https://github.com/ankitects/anki/releases/tag/26.05)
  - 26.09 — [Release 26.09](https://github.com/ankitects/anki/releases/tag/26.09)
- The current manual still tells users to "Enable FSRS under the 'FSRS' section, at the bottom of the deck options page." — [Anki Manual — Deck Options](https://docs.ankiweb.net/deck-options.html)
- 2026 third-party setup guides tell new users to "enable FSRS immediately." Some also wrongly claim FSRS has been the default since 23.10. — [studycardsai (2026)](https://studycardsai.com/blog/anki-fsrs-algorithm); [Flica](https://flica.app/article/anki-fsrs-setup)
- **Best-supported conclusion:** as of September 2026, FSRS is mature and recommended but still appears to be a manual toggle.

**Recent Anki releases (2026)**
- The latest desktop line is 26.09 (26.09.2 and 26.09.3 followed). GitHub shows "Sep 14" without a year, which GitHub does for current-year dates, so this is September 2026.
- 26.09 notes: "Update FSRS to 6.6.2" (the fsrs-rs library), FSRS memory-state fixes, and hiding FSRS-only sort orders when FSRS is disabled. 26.08 moved to fsrs-rs 6.6.1.
- 26.05 added FSRS "Help Me Decide" efficiency-ratio graph rework and a load-balancer sibling-dispersal improvement. It also requires three clicks to unlock FSRS parameter editing.
- Sources: [Anki releases](https://github.com/ankitects/anki/releases); [26.09](https://github.com/ankitects/anki/releases/tag/26.09); [26.05](https://github.com/ankitects/anki/releases/tag/26.05)

**Benchmark (open-spaced-repetition srs-benchmark)**
- Dataset: 10,000 Anki collections, about 727 million reviews. Evaluation used 349,923,850 reviews without same-day reviews and 519,296,315 with them. Metrics: log loss, RMSE(bins), AUC.
- Without same-day reviews:

  | Model | Parameters | Log loss | RMSE(bins) | AUC |
  |---|---|---|---|---|
  | FSRS-6 | 21 | 0.3460 | 0.0653 | 0.7034 |
  | FSRS-5 | — | 0.3561 | 0.0742 | 0.7010 |
  | FSRS-4.5 | — | 0.3625 | 0.0764 | 0.6891 |
  | FSRS-7 | 34 | 0.3401 | 0.0634 | 0.7167 |

- FSRS-7 is newer, designed for fractional-day intervals and realistic same-day predictions. The README says it "should be shipped" in Anki with recency weighting; no release confirmation was found.
- Neural models (LSTM/GRU/RWKV) predict better still, but have thousands to millions of parameters.
- Source: [srs-benchmark README](https://github.com/open-spaced-repetition/srs-benchmark)
- **FSRS vs SM-2:** FSRS-6 with recency weighting has lower log loss than Anki's SM-2 for 99.6% of collections. The author cautions there is "no way to have a truly fair, no caveats, comparison," because SM-2 doesn't natively predict probabilities. The page is marked "(UNFINISHED)." — [Expertium, "Benchmark of Spaced Repetition Algorithms"](https://expertium.github.io/Benchmark.html)

**Anki cost and availability**
- Anki desktop (Windows/Mac/Linux), AnkiWeb sync and AnkiDroid (Android, community-built) are free. AnkiMobile (iOS) is a one-time $24.99 purchase with no subscription. — [AnkiMobile on the App Store](https://apps.apple.com/us/app/ankimobile-flashcards/id373493387); [price explainer, 2026](https://www.flashcardslearn.com/en/blog/how-much-does-anki-cost); [Flica, "Is Anki Free in 2026?"](https://flica.app/article/is-anki-free)

**CSV / text import**
- Plain-text UTF-8 files. The separator (comma, semicolon, tab, space, pipe, colon) is auto-detected or set with a header.
- The number of fields is taken from the first non-comment line. Fields map in order; missing fields are left blank and extra fields ignored.
- Fields that contain the separator or a newline must be quoted, with internal quotes doubled. Alternatively, use `<br>` with "Allow HTML."
- Header directives: `#separator:Comma`, `#html:true`, `#tags:tag1 tag2`, `#columns:Front;Back;Tags`, `#notetype:Basic`, `#deck:AI::ML Basics`, `#notetype column:1`, `#deck column:2`, `#guid column:3`, `#tags column:4`.
- Existing notes are updated by default; duplicates can instead be ignored or imported as new.
- Media files go in `collection.media`.
- Source: [Anki Manual — Importing text files](https://docs.ankiweb.net/importing/text-files.html)

**Flashcard-writing guidance (Matuschak)**
- Good prompts are:
  - "Focused": one detail.
  - "Precise": not vague.
  - "Consistent": same answer each time.
  - "Tractable": you can almost always answer.
  - "Effortful": requires real retrieval.
- For concepts, use several lenses: attributes, similarities and differences, parts and wholes, causes and effects, significance.
- Avoid yes/no prompts and pattern-matchable cloze deletions of long passages.
- Start with "5-10" prompts on what matters most. A prompt costs roughly "10-30 seconds across the entire first year."
- Source: [Andy Matuschak, "How to write good prompts"](https://andymatuschak.org/prompts/)

**Wozniak's "Twenty rules of formulating knowledge" (February 1999)**
1. Do not learn if you do not understand
2. Learn before you memorize
3. Build upon the basics
4. Stick to the minimum information principle
5. Cloze deletion is easy and effective
6. Use imagery
7. Use mnemonic techniques
8. Graphic deletion is as good as cloze deletion
9. Avoid sets
10. Avoid enumerations
11. Combat interference
12. Optimize wording
13. Refer to other memories
14. Personalize and provide examples
15. Rely on emotional states
16. Context cues simplify wording
17. Redundancy does not contradict minimum information principle
18. Provide sources
19. Provide date stamping
20. Prioritize

Source: [Wozniak, SuperMemo](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge)

### Inferences

**Tutor-owned scheduler (for AI quiz items; exact and simple)**
Use SM-2 with 4 buttons mapped to q:

| Button | q |
|---|---|
| Again | 1 |
| Hard | 3 |
| Good | 4 |
| Easy | 5 |

Pseudocode:
```
init: EF=2.5, n=0, I=0
on review(q):
  if q>=3: n+=1; I = 1 if n==1 else 6 if n==2 else ceil(I*EF)
  else:    n=0; I=1            # restart, EF per step 6 unchanged (many implementations still apply the EF update)
  EF = max(1.3, EF + (0.1-(5-q)*(0.08+(5-q)*0.02)))   # apply only when q>=3 to follow spec step 6 literally
  if q<4: requeue same day until q>=4
# Ambiguity: the spec lists the interval rule (step 3) before the EF update (step 5).
# Implementations differ on whether I(n) uses the pre- or post-update EF, and on whether EF changes when q<3.
# Pick one convention and document it.
```
- Better option: use an FSRS library (py-fsrs / ts-fsrs / fsrs-rs) with default FSRS-6 parameters and desired retention 0.85-0.90. Re-optimize parameters monthly once there are at least a few hundred reviews.

**Anki setup for this learner**
- Use Anki desktop + AnkiDroid (free).
- Enable FSRS in deck options, keep desired retention 0.90 (or 0.85 if the review load exceeds about 20 minutes a day), and set learning steps below 1 day (for example, 10m or 15m).
- Cap new cards at about 10/day.
- Have the AI tutor export session cards as a UTF-8 CSV. Example:
  ```
  #separator:Comma
  #html:true
  #notetype:Basic
  #deck:AI::Week03
  #tags column:3
  Front,Back,Tags
  ```

**Card rules to give the AI card generator**
- Only card material that has already been understood.
- One idea per card.
- Prefer "why/how/when would you use X" over definitions.
- Include a code-reading card ("what does this snippet output?") for procedural knowledge.
- Avoid sets and enumerations.
- Add source links.
- Aligns with Wozniak's "20 rules" and Matuschak.

### Gaps
- FSRS default-on status for brand-new installs is not definitively settled. Release notes for 25.02, 25.06/25.07/25.09, 26.02 and 26.08 were not all checked individually. The evidence (manual wording, the open issue, 25.02/26.05/26.09 notes, 2026 setup guides) points to "opt-in toggle."
- Anki's default learning steps ("1m 10m"), graduating interval (1 d), easy interval (4 d), relearning step (10m) and leech threshold (8) are widely reported. They were not quoted verbatim from the manual this session; the manual text fetched only gave "1m 10m 1d" as an example.
- The popular claim that "FSRS gives 20-30% fewer reviews than SM-2 at the same retention" appears on third-party sites without a primary source. It was not verified and should not be quoted as fact.

## Q11. Programming/ML-specific learning: project-based learning, spiral curriculum, Parsons problems and predict-then-run, code reading before writing, "learning in public"

### Takeaway
Project-based learning shows medium-to-large achievement effects in meta-analysis (d = 0.71). Unguided discovery is less effective for novices, however, so projects should come after or alongside worked examples. Parsons problems are a more efficient, equally effective practice format than writing equivalent code. Instruction theory argues for tracing (reading semantics) before writing (Xie et al. 2019). PRIMM (Predict-Run-Investigate-Modify-Make) outperformed control teaching in a 493-student school study. "Learning in public" has no direct evidence. Its plausible benefits run through learning by teaching and portfolio signalling, with a documented caveat that public announcements can reduce effort.

### Cited Findings
- **Project-based learning meta-analysis (Chen & Yang 2019):** 46 effect sizes from 30 articles (1998-2017), 12,585 students in 189 schools across 9 countries; overall d+ = 0.71. — [Chen & Yang (2019), *Educational Research Review* 26:71-81](https://www.sciencedirect.com/science/article/abs/pii/S1747938X19300211)
- **Caution on minimal guidance:** less effective than guided instruction for novices. — [Kirschner, Sweller & Clark (2006), DOI 10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1) (cited from DOI)
- **PRIMM:** evaluated in 13 schools with 493 students aged 11-14 against a control group. PRIMM learners performed better on the post-test. — [Sentance, Waite & Kallia (2019), "Teaching computer programming with PRIMM: a sociocultural perspective," *Computer Science Education* 29(2-3)](https://eric.ed.gov/?id=EJ1217966); [author copy](https://suesentance.net/wp-content/uploads/2020/02/teaching_computer_programming_with_primm__a_sociocultural_perspective_author_copy.pdf)
- **Parsons problems:** solving them (reordering mixed-up code blocks) takes less time than fixing or writing equivalent code, with similar learning. Adaptive Parsons problems were "more efficient, but just as effective" as writing equivalent code, and lowered cognitive load. — [Ericson, Margulieux & Rick (2017), Koli Calling, DOI 10.1145/3141880.3141895](https://dl.acm.org/doi/10.1145/3141880.3141895); [Haynes & Ericson (2021), CHI, DOI 10.1145/3411764.3445292](https://dl.acm.org/doi/fullHtml/10.1145/3411764.3445292)
- **Reading before writing (Xie et al. 2019):** the theory identifies four distinct, incrementally learned skills: tracing (reading semantics), writing syntax, comprehending templates (reusable patterns), and writing code with templates. Explicitly teaching them reduces cognitive demand. The paper argues novices need to be able to read and trace semantics before writing. — [Xie, Loksa, Nelson, Davidson, Dong, Kwik, Tan, Hwa, Li & Ko (2019), "A theory of instruction for introductory programming skills," *Computer Science Education* 29(2-3):205-253, DOI 10.1080/08993408.2019.1565235](https://eric.ed.gov/?id=EJ1218026); [author page](https://www.benjixie.com/publication/cse-2019/)
- **Spiral curriculum:** Bruner's spiral curriculum revisits topics at increasing depth. It is widely adopted (for example, in medical education), but its support is mainly theoretical rather than from RCTs. — [Harden (1999), "What is a spiral curriculum?", *Medical Teacher* 21(2):141-143, DOI 10.1080/01421599979752](https://doi.org/10.1080/01421599979752) (cited from DOI; not re-fetched)
- **"Learning in public"** as a practitioner idea (writing and sharing what you learn). — [swyx, "Learn In Public"](https://www.swyx.io/learn-in-public)
  - Related evidence: preparing and actually teaching improves learning (g = 0.35 / 0.56). — [Kobayashi 2019](https://onlinelibrary.wiley.com/doi/10.1111/jpr.12221)
  - Counter-evidence: publicly announcing identity-relevant intentions can reduce effort. — [Gollwitzer et al. 2009](https://doi.org/10.1111/j.1467-9280.2009.02336.x)
- **AI-assisted learning of a new programming library:** delegation hurt learning, while conceptual questioning did not (see Q9). — [Anthropic 2026](https://www.anthropic.com/research/AI-assistance-coding-skills)

### Inferences
- **Recommended skill progression for each new programming or ML concept:**
  1. Read and trace a worked example (predict the output).
  2. Run and investigate it (PRIMM).
  3. Solve a Parsons problem or faded example.
  4. Modify existing code.
  5. Write from scratch.
  6. Integrate into a weekly mini-project.
  7. Revisit in a later, bigger project (spiral).
- **Learning in public, done safely:** publish artifacts after completing them (for example, a weekly "what I built and what broke" post or a GitHub README), rather than announcing grand intentions up front.

### Gaps
- Xie et al. (2019) is a theory paper with an accompanying evaluation. The empirical correlational studies linking tracing skill to writing skill (for example, Lister et al. 2004; Lopez et al. 2008) were not verified this session.
- No controlled evidence was found specific to ML/AI curricula (for example, fast.ai-style "top-down" teaching) or to adult career-switchers.
- The Chen & Yang sample is mostly K-12 and university classes, not self-directed adults.

## Q12. Concrete protocol for about 10 hours/week alongside a full-time job

### Takeaway
Combine daily 10-15 minute spaced-retrieval reviews (FSRS in Anki), four 60-75 minute weekday "learn" sessions (prequestions, then a segmented video with interpolated recall, then a closed-book AI quiz, then hands-on practice, then a teach-back), one 2.5-3 hour weekend "build and interleave" session, and a 30-minute weekly AI-off check and plan. Mastery means one correct unaided recall in each of 3 spaced sessions. Missed days are handled with a review cap, reserve days and a "never miss twice" rule, not with catch-up binges.

### Cited Findings
- **Evidence behind the protocol components:**
  - Spacing, optimal gaps and expanding intervals: [Cepeda 2008](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x); [Latimier 2021](https://eric.ed.gov/?id=EJ1310148)
  - Retrieval with feedback: [Rowland 2014](https://pubmed.ncbi.nlm.nih.gov/25150680/); [Adesope 2017](https://journals.sagepub.com/doi/abs/10.3102/0034654316689306)
  - Successive relearning criterion: [Rawson & Dunlosky 2022](https://journals.sagepub.com/doi/full/10.1177/09637214221100484)
  - Interpolated testing in videos: [Szpunar 2013](https://www.pnas.org/doi/10.1073/pnas.1221764110)
  - Prequestions: [King-Shepard 2025](https://link.springer.com/article/10.1007/s10648-025-10075-7)
  - Quiz types matching Bloom's levels: [Agarwal 2019](https://eric.ed.gov/?id=EJ1205208)
  - Teaching: [Kobayashi 2019](https://onlinelibrary.wiley.com/doi/10.1111/jpr.12221)
  - Breaks: [Biwer 2023](https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/bjep.12593)
  - Sleep: [Mazza 2016](https://journals.sagepub.com/doi/abs/10.1177/0956797616659930)
  - Habits: [Lally 2010](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674)
  - Emergency reserves: [Sharif & Shu 2017](https://journals.sagepub.com/doi/10.1509/jmr.15.0231)
  - AI-tutor guardrails: [Bastani 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/); [Kestin 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/); [Anthropic 2026](https://www.anthropic.com/research/AI-assistance-coding-skills)
  - FSRS settings: [Anki manual](https://docs.ankiweb.net/deck-options.html)
- **Revised Bloom's taxonomy levels:** Remember, Understand, Apply, Analyze, Evaluate, Create. — [Krathwohl (2002), "A Revision of Bloom's Taxonomy: An Overview," *Theory Into Practice* 41(4):212-218, DOI 10.1207/s15430421tip4104_2](https://doi.org/10.1207/s15430421tip4104_2) (cited from DOI)

### Inferences

**A. Weekly time budget (about 10 h)**

| Block | When | Time/week |
|---|---|---|
| Daily FSRS flashcard review | 7 days, commute or morning (after sleep, per the Mazza pattern) | 10-15 min/day = 1.2-1.75 h |
| "Learn" sessions | 4 weekdays × 60-75 min | 4-5 h |
| "Build and interleave" session | 1 weekend × 2.5-3 h | 2.5-3 h |
| AI-off weekly check and plan | 1 × 30 min | 0.5 h |

- Keep 1-2 days per week as emergency reserves. On those days, do flashcards only, or nothing.

**B. Weekday "Learn" session (60-75 min; work/break blocks of 25/5 or 50/10)**

1. **Warm-up retrieval (5-8 min).** The AI asks 4-6 closed-book questions from earlier weeks (interleaved topics, spaced items due today). Collect a confidence rating (1-5) before each answer. Give explanatory feedback. Log the grade.
2. **Prequestions (2 min).** The AI asks 2-3 questions targeting the key ideas of the upcoming video. The learner guesses; answers are not revealed yet.
3. **Segmented video (20-30 min of content at 1.25-1.75x).** At each natural boundary (about every 5-10 minutes), pause and write 2-3 bullets from memory. Then the AI asks 1 quick question. No rewinding before attempting recall.
4. **Post-video closed-book quiz (10-12 min, 6-10 questions, one at a time).** Mix:
   - about 30% Remember (definitions, key facts);
   - 20% Understand (explain in your own words, compare);
   - 30% Apply/Analyze (trace or predict code output, debug a snippet, choose a method for a scenario);
   - 20% Evaluate/Create (justify a design choice, sketch an approach).

   Prefer short-answer to multiple choice. The AI grades against a stored answer or rubric generated from the video transcript and verified sources, not free-form. Grades map to Again/Hard/Good/Easy. Missed items are re-asked 10+ minutes later in the same session until answered correctly once.
5. **Hands-on practice (15-25 min, AI in hint-only mode).** Follow the progression predict-run → Parsons or faded example → modify → write. Hint ladder: concept → pointer → partial step. The solution is shown only after an attempt, and the learner must explain it back.
6. **Teach-back / Feynman (5 min).** The learner explains the session's core idea to the AI acting as a novice. The AI asks 2 "why/how" probes and names 1 gap.
7. **Card creation and exit (5 min).** The AI drafts 3-8 atomic cards (Matuschak and Wozniak rules). The learner edits and accepts them, and they are exported to CSV for Anki. The learner states tomorrow's if-then plan.

**C. Weekend "Build and interleave" session (2.5-3 h)**

- **Interleaved quiz (20 min).** Mixed problems across the last 2-4 weeks, especially confusable pairs.
- **Mini-project (1.5-2 h).** Apply the week's concepts to a small end-to-end task (for example, a notebook, script or API call). The learner codes first; AI reviews. Run the no-delegation rule.
- **Write-up (20-30 min).** A README or short post ("what I built, what broke, what I'd do differently"). This is learning in public, done after completing the work.

**D. Weekly AI-off check (30 min, Sunday or Monday)**

- A 10-15 question cumulative quiz plus 1 small coding task without AI assistance. Track accuracy vs confidence.
- If AI-off accuracy is below about 70% on last week's material, the next week repeats and consolidates rather than introducing new material.

**E. Review intervals**

- **Flashcards:** Anki with FSRS, desired retention 0.90 (0.85 if daily reviews exceed about 20 minutes), learning steps below 1 day, new cards capped at about 10/day, optimized monthly.
- **Concept-level mastery (tutor-tracked):** day 0 (reach 1-3 correct recalls in-session), day 1, day 3-4, day 7-10, day 21-30, day 60-90. Adjust with SM-2/FSRS grades.
- A concept is "mastered" after correct unaided recall in 3 separate spaced sessions and 1 successful AI-off application task.

**F. Handling missed days**

- **1 missed day:** no penalty. Resume the normal plan the next day and do only due reviews.
- **2-6 missed days:**
  - Pause new cards.
  - Cap daily reviews at about 1.5-2x normal. FSRS computes recall probability from the actual elapsed time, so overdue cards are rescheduled appropriately.
  - Start each session with a 10-minute cumulative quiz.
  - Resume new material after the backlog is under 2 days' worth.
- **At least 1 missed week:** do a 30-45 minute re-entry session: a cumulative closed-book quiz on the last 2 weeks, then re-teach the items that failed. Then continue at 70% of normal new-content pace for 1 week.
- **Motivation:**
  - Show weekly-goal progress, with reserve days, rather than a fragile daily streak.
  - Never show "streak lost" messages.
  - Use if-then plans tied to fixed cues.
  - Expect about 2-5 months before the routine feels automatic.

**G. For an AI-anxious learner**

- Surface mastery evidence weekly: AI-off accuracy trends and projects shipped. Frequent low-stakes quizzing also reduces test anxiety (Szpunar et al. found interpolated testing lowered anxiety about the final test).
- Frame AI as a tutor that makes the learner do the thinking. Explain the Bastani and Anthropic findings to the learner so the guardrails feel purposeful rather than paternalistic.

### Gaps
- No RCT has tested this full composite protocol. Component effects may not add up.
- The specific numbers (session lengths, the Bloom's percentage mix, the 70% threshold, the 10-cards/day cap) are reasoned defaults, not empirically derived optima, and should be tuned from the learner's own data (FSRS retention statistics, AI-off scores).
