# Phase 5 — Deep Learning

**Plan weeks 29–36 · 8 weeks · Difficulty ★★★★☆ · Badge: Deep Learning Practitioner**

## Why this phase matters
Deep learning powers LLMs, image recognition, speech and most modern AI. In this phase you build a neural network's learning engine (backpropagation) from scratch, then learn the tool the whole industry uses (PyTorch), then train real image models with transfer learning. After this, LLMs stop being magic: in Phase 6 you'll see they are the same building blocks at a larger scale.

**Hardware plan:** micrograd and small experiments run on your laptop CPU. Everything with a GPU runs on Kaggle (30 free GPU hours per week) or Colab. Debug on CPU with tiny data, then switch the GPU on for the real run.

## Before you start
- Phase 4 passed.
- Kaggle phone verification done (GPU access).
- Recall from Phase 3: chain rule, gradients, gradient descent, cross-entropy.

## You will be able to
- Explain neurons, layers, activations, loss, backpropagation and gradient descent, with numbers.
- Build a small autograd engine and neural network from scratch.
- Write PyTorch training loops: tensors, autograd, `nn.Module`, `DataLoader`, GPU, saving and loading.
- Diagnose training: initialisation, activations, BatchNorm, learning rates, optimisers, regularisation.
- Train CNNs and use transfer learning for image classification on your own dataset.
- Explain RNNs, embeddings, sequence-to-sequence and attention: the bridge to transformers.

> **AI-assistance policy from here:** AI may write boilerplate (plots, argument parsing, file handling), marked `# AI-assisted`. Model, training and algorithm code is yours.

---

## Week 1 (plan week 29) — Neural networks, visually

#### P5-W1-L1 · What a neural network is (~60 min)
- **Learn:** [3Blue1Brown — But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) (18 min) and [StatQuest — The Essential Main Ideas of Neural Networks](https://www.youtube.com/watch?v=CqOfi41LfDw) (18 min).
- **Key concepts:** neurons as weighted sums plus a bias, passed through an activation; layers; weights and biases as learned parameters; a network as one big function.
- **Quiz seeds:** How many parameters does a layer from 784 inputs to 16 neurons have? Why do we need a non-linear activation?

#### P5-W1-L2 · How networks learn (~60 min)
- **Learn:** [3Blue1Brown — Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w) and [StatQuest — ReLU In Action](https://www.youtube.com/watch?v=68BZ5f7P94E).
- **Key concepts:** the cost function over all training examples; gradient descent in thousands of dimensions; ReLU vs sigmoid; what hidden layers seem to learn (and don't).
- **Quiz seeds:** What does the cost function measure? Why is ReLU popular?

#### P5-W1-L3 · Backpropagation, intuitively (~60 min)
- **Learn:** [3Blue1Brown — Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U) and [StatQuest — Backpropagation Main Ideas](https://www.youtube.com/watch?v=IN2XmBhILt4).
- **Key concepts:** each weight's "responsibility" for the error; propagating error backwards layer by layer; mini-batches.
- **Quiz seeds:** Why do we go *backwards* through the network to compute gradients?

#### P5-W1-L4 · Backpropagation calculus, softmax and cross-entropy (~75 min)
- **Learn:** [3Blue1Brown — Backpropagation calculus](https://www.youtube.com/watch?v=tIeHLnjs5U8), then StatQuest [ArgMax and SoftMax](https://www.youtube.com/watch?v=KpKog-L9veg) and [Cross Entropy](https://www.youtube.com/watch?v=6ArSys5qHAU).
- **Key concepts:** the chain rule through a network; softmax turns scores into probabilities; cross-entropy loss for classification (you met entropy in Phase 3).
- **Quiz seeds:** Why softmax instead of just picking the largest score during training? What's the loss when the model gives the correct class probability 1.0?

#### P5-W1-B · Weekend
On paper: the forward and backward pass of a tiny 2-layer network for one example. Then check every number in NumPy.

---

## Week 2 (plan week 30) — Build micrograd
[Karpathy — The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) (2 h 25 min) in four sittings. It runs on your laptop CPU. **Code along; don't just watch.** Minute ranges are approximate, so use the chapter list. Reference code: [karpathy/micrograd](https://github.com/karpathy/micrograd).

#### P5-W2-L1 · Derivatives and the Value object (~75 min)
- **Learn:** **0:00–0:52**.
- **Key concepts:** the derivative as sensitivity to a nudge; a `Value` object that remembers how it was computed; the expression graph; manual backprop through a simple expression.
- **Quiz seeds:** For d = a·b + c, what is ∂d/∂a? Why store the "children" of each Value?

#### P5-W2-L2 · Backprop through a neuron (~75 min)
- **Learn:** **0:52–1:22**.
- **Key concepts:** backprop through tanh; a `_backward` function per operation; the chain rule as "local gradient × gradient from above".
- **Quiz seeds:** What is the local derivative of tanh? What does `+=` in the gradient update protect against?

#### P5-W2-L3 · Automatic backprop (~75 min)
- **Learn:** **1:22–1:51**.
- **Key concepts:** topological sort; the bug when a node is used twice (accumulate gradients); breaking operations into smaller pieces; comparing with PyTorch.
- **Quiz seeds:** Why must gradients be accumulated rather than overwritten?

#### P5-W2-L4 · A neural network library and training loop (~75 min)
- **Learn:** **1:51–end**.
- **Key concepts:** `Neuron`, `Layer`, `MLP` classes; a loss over a tiny dataset; the training loop: forward → zero grads → backward → update; the forgotten `zero_grad` bug.
- **Quiz seeds:** What happens if you forget to zero the gradients? Write the 4 steps of a training loop.

#### P5-W2-B · Weekend build
Extend your micrograd with `pow`, `exp` and `ReLU`, and write pytest tests comparing your gradients with PyTorch on 5 expressions. This becomes Project 5A.

---

## Week 3 (plan week 31) — PyTorch fundamentals

#### P5-W3-L1 · Tensors (~75 min)
- **Learn:** [StatQuest — The StatQuest Introduction to PyTorch](https://www.youtube.com/watch?v=FHdlXe1bSe4), then PyTorch [Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html): Quickstart and Tensors ("Run in Google Colab").
- **Key concepts:** tensors vs NumPy arrays; shapes and dtypes; the device (CPU or GPU); in-place operations.
- **Quiz seeds:** How do you move a tensor to the GPU? What's the difference between `view` and `reshape`?

#### P5-W3-L2 · Data and models (~75 min)
- **Learn:** Learn the Basics: Datasets & DataLoaders, Transforms, Build the Neural Network.
- **Key concepts:** `Dataset` and `DataLoader` (batching, shuffling); transforms; `nn.Module` with `__init__` and `forward`; `nn.Sequential`.
- **Quiz seeds:** Why shuffle training data but not test data?

#### P5-W3-L3 · Autograd and the optimisation loop (~75 min)
- **Learn:** Learn the Basics: Automatic Differentiation, Optimizing Model Parameters, Save and Load the Model.
- **Key concepts:** `requires_grad`; `loss.backward()`; optimisers (`optimizer.step()`, `zero_grad()`); `model.train()` vs `model.eval()`; `torch.no_grad()`; saving `state_dict`.
- **Quiz seeds:** Why call `model.eval()` before validation? How does PyTorch's autograd relate to your micrograd?

#### P5-W3-L4 · A complete workflow on a GPU (~75 min)
- **Learn:** [learnpytorch.io](https://www.learnpytorch.io/) chapters 01 (PyTorch Workflow) and 02 (Neural Network Classification), run on Kaggle with the GPU on.
- **Key concepts:** the end-to-end workflow; device-agnostic code; non-linear decision boundaries; accuracy and loss curves.
- **Build:** An MLP for FashionMNIST on Kaggle's GPU, with training and validation curves, saved and reloaded.

#### P5-W3-B · Weekend
Finish and tidy the FashionMNIST notebook; push it to GitHub with the outputs saved.

---

## Week 4 (plan week 32) — Language modelling with makemore
[Karpathy's makemore series](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ): a character-level model that invents new names. Colab or Kaggle recommended.

#### P5-W4-L1 · Bigrams by counting (~75 min)
- **Learn:** [makemore Part 1](https://www.youtube.com/watch?v=PaCmpygFfXo), **first ~60 minutes**.
- **Key concepts:** a bigram language model; counting and normalising into probabilities; sampling; negative log-likelihood as the loss; smoothing.
- **Quiz seeds:** What does the average negative log-likelihood tell you about a model?

#### P5-W4-L2 · A neural bigram model (~75 min)
- **Learn:** makemore Part 1, **~60 minutes to the end**.
- **Key concepts:** one-hot encoding; a single linear layer; softmax; training by gradient descent reaches the same answer as counting.
- **Quiz seeds:** Why does the neural approach scale better than counting to longer contexts?

#### P5-W4-L3 · An MLP language model (~75 min)
- **Learn:** [makemore Part 2: MLP](https://www.youtube.com/watch?v=TCH_1BHY58I), **first ~40 minutes**.
- **Key concepts:** learned embeddings (a lookup table `C`); a context window of several characters; a hidden layer; `F.cross_entropy`.
- **Quiz seeds:** What is an embedding table, and what does it learn here?

#### P5-W4-L4 · Training it properly (~75 min)
- **Learn:** makemore Part 2, **~40 minutes to the end**.
- **Key concepts:** train/validation/test splits; finding a good learning rate; mini-batches; under- and overfitting; scaling the embedding size.
- **Quiz seeds:** How did Karpathy pick the learning rate?

#### P5-W4-B · Weekend build
Train the makemore MLP on a new list of names (for example names from your own language or culture, from a public dataset) and sample 20 new ones.

---

## Week 5 (plan week 33) — Training deep networks well

#### P5-W5-L1 · Activations and initialisation (~75 min)
- **Learn:** [makemore Part 3: Activations & Gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc), **first ~60 minutes**.
- **Key concepts:** why the initial loss should match a uniform guess; saturated tanh units kill gradients; Kaiming initialisation.
- **Quiz seeds:** What happens to gradients when tanh outputs are near ±1?

#### P5-W5-L2 · BatchNorm and diagnostics (~75 min)
- **Learn:** makemore Part 3, **~60 minutes to the end**.
- **Key concepts:** batch normalisation; its train vs inference behaviour; diagnostic plots (activation and gradient histograms, update-to-data ratios).
- **Quiz seeds:** Why does BatchNorm behave differently at inference time?

#### P5-W5-L3 · Optimisers and learning-rate schedules (~60 min)
- **Learn:** [Understanding Deep Learning](https://udlbook.github.io/udlbook/) (free PDF), chapter 6 "Fitting models".
- **Key concepts:** SGD; momentum; Adam; learning-rate schedules and warm-up.
- **Quiz seeds:** What problem does momentum solve? Why is Adam a common default?

#### P5-W5-L4 · Regularisation (~60 min)
- **Learn:** Understanding Deep Learning, chapter 9 "Regularization".
- **Key concepts:** weight decay; dropout; data augmentation; early stopping; why big networks can still generalise.
- **Quiz seeds:** Why is dropout switched off at inference?

#### P5-W5-B · Weekend build
Experiment grid on your FashionMNIST MLP: 3 optimisers × 2 learning rates, logged with [Weights & Biases](https://docs.wandb.ai/quickstart) (free) or TensorBoard. One chart, one conclusion.

---

## Week 6 (plan week 34) — CNNs and computer vision

#### P5-W6-L1 · Convolutions (~60 min)
- **Learn:** [3Blue1Brown — But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA) and [StatQuest — Image Classification with CNNs](https://www.youtube.com/watch?v=HGwBXDKFk9I).
- **Key concepts:** kernels sliding over an image; feature maps; pooling; why CNNs need far fewer parameters than MLPs for images.
- **Quiz seeds:** Why is a CNN better than an MLP for images? What does a 3×3 kernel "look for"?

#### P5-W6-L2 · Your first CNN (~75 min)
- **Learn:** learnpytorch.io chapter 03 (PyTorch Computer Vision), on Kaggle's GPU.
- **Key concepts:** `Conv2d`, `MaxPool2d`; channels and output shapes; a TinyVGG-style model; confusion matrices for images.
- **Quiz seeds:** An input of shape (1, 28, 28) goes through a 3×3 conv with 10 filters and padding 1. What's the output shape?

#### P5-W6-L3 · A real image classifier with fast.ai (~90 min)
- **Learn:** [Practical Deep Learning for Coders — Lesson 1](https://www.youtube.com/watch?v=8SF_h3xF3cE), using the lesson's Kaggle notebook from [course.fast.ai](https://course.fast.ai/).
- **Key concepts:** building a dataset from web images; pretrained models; fine-tuning in a few lines; "get something working end to end, then improve".
- **Quiz seeds:** Why can a model trained on millions of general images learn your 3 classes from a few hundred?

#### P5-W6-L4 · Transfer learning in PyTorch (~75 min)
- **Learn:** learnpytorch.io chapter 06 (Transfer Learning), plus [fast.ai Lesson 2](https://www.youtube.com/watch?v=F4tvM4Vb3A0) for data cleaning and deployment ideas.
- **Key concepts:** pretrained backbones (ResNet, EfficientNet); freezing and unfreezing layers; data augmentation; cleaning the dataset using the model's worst mistakes.
- **Quiz seeds:** When would you unfreeze the whole network?

#### P5-W6-B · Weekend
Start collecting your dataset for Project 5B: at least 5 classes, 100+ images per class.

---

## Week 7 (plan week 35) — Sequences, embeddings and good experiment habits

#### P5-W7-L1 · RNNs and LSTMs (~60 min)
- **Learn:** StatQuest [Recurrent Neural Networks](https://www.youtube.com/watch?v=AsNTP8Kwu80) and [Long Short-Term Memory](https://www.youtube.com/watch?v=YCzL96nL7j0).
- **Key concepts:** processing sequences step by step; vanishing and exploding gradients over long sequences; gates in LSTMs; why sequential processing is slow to train.

#### P5-W7-L2 · Embeddings and sequence-to-sequence (~60 min)
- **Learn:** StatQuest [Word Embedding and Word2Vec](https://www.youtube.com/watch?v=viZrOnJclY0) and [Sequence-to-Sequence Encoder-Decoder Networks](https://www.youtube.com/watch?v=L8HKweZIOmg).
- **Key concepts:** learned word embeddings; encoder–decoder models for translation; the bottleneck of squeezing a whole sentence into one vector.

#### P5-W7-L3 · Attention: the bridge to transformers (~75 min)
- **Learn:** [StatQuest — Attention for Neural Networks](https://www.youtube.com/watch?v=PSs6nxngL6k), then [MIT 6.S191 (2026) — Recurrent Neural Networks, Transformers, and Attention](https://www.youtube.com/watch?v=d02VkQ9MP44).
- **Key concepts:** attention lets the decoder look at every encoder step; relevance scores; why attention removed the need for recurrence.
- **Quiz seeds:** What bottleneck does attention remove in seq2seq models?

#### P5-W7-L4 · Experiment hygiene (~60 min)
- **Learn:** the [Weights & Biases quickstart](https://docs.wandb.ai/quickstart).
- **Key concepts:** logging configs and metrics; seeds and reproducibility; comparing runs; keeping a short experiment log.

#### P5-W7-B · Weekend: Project 5 work

---

## Week 8 (plan week 36) — Project 5 and exam
#### P5-W8-L1 to L4 · Project 5 work
#### P5-W8-B · Weekend: `/submit` (both parts), then `/exam`

## Project 5
### 5A — "My micrograd" (`projects/pr5-micrograd/`)
**Must-haves**
- [ ] A `Value` class supporting +, −, ×, ÷, power, exp, tanh and ReLU, with backward passes via topological sort.
- [ ] `Neuron`, `Layer` and `MLP` classes, trained on a small toy dataset with a decreasing loss.
- [ ] pytest tests comparing your gradients with PyTorch on at least 5 expressions.
- [ ] README explaining backpropagation in your own words, with a diagram.

### 5B — "An image classifier that ships" (`projects/pr5-image-classifier/`)
A dataset you collect yourself (at least 5 classes, 100+ images per class). Ideas: local street food, plant-leaf diseases, your country's currency notes, local traffic signs.

**Must-haves**
- [ ] Transfer learning in PyTorch (or fast.ai) trained on Kaggle's GPU; train/validation/test split; augmentation.
- [ ] Test-set results with a confusion matrix, plus an error analysis with at least 8 failure examples and your explanation.
- [ ] A model card: data sources, intended use, limits, known biases.
- [ ] A Gradio demo on a Hugging Face ZeroGPU Space, or a Streamlit app running on CPU (see [guides/free-compute.md](../guides/free-compute.md)).
- [ ] The notebook saved with outputs; Kaggle link in the README.

**Stretch:** test on photos taken with your own phone and report the accuracy drop; Grad-CAM heatmaps; export to ONNX.

**Viva focus:** walk through backprop in your micrograd; why your image model fails where it does; what data you'd collect next.

## Exam EX5
- **Part A (concepts):** neurons, activations, loss, backprop, optimisers, initialisation, BatchNorm, regularisation, CNNs, transfer learning, RNNs, attention.
- **Part B (live coding, 20 min):** write a complete PyTorch training loop from memory for a given small model and dataset.
- **Part C (stakeholder):** "Explain to a product manager why the image model needs more varied data before launch."
- **Part D (judgment):** "Validation accuracy is 98%, but the model fails on photos from users' phones. What happened, and what do you do?"

---

## Optional and deeper
- [fast.ai — Practical Deep Learning for Coders](https://course.fast.ai/), the whole of Part 1 ([videos](https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU)), with the free book as notebooks: [fastbook](https://github.com/fastai/fastbook).
- [MIT 6.S191 — Introduction to Deep Learning (2026)](https://introtodeeplearning.com/): 9 compact lectures and labs.
- [learnpytorch.io](https://www.learnpytorch.io/): the remaining chapters, or Daniel Bourke's [25-hour PyTorch course](https://www.youtube.com/watch?v=V_xro1bcAuA).
- Karpathy's [makemore Part 4 (Becoming a Backprop Ninja)](https://www.youtube.com/watch?v=q8SA3rM6ckI) and [Part 5 (Building a WaveNet)](https://www.youtube.com/watch?v=t3YJ5hKiMQ0).
- Free books: [Understanding Deep Learning](https://udlbook.github.io/udlbook/), [Dive into Deep Learning](https://d2l.ai/) (runnable PyTorch), [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) (gentle), [Deep Learning](https://www.deeplearningbook.org/) (reference).
- [Stanford CS231n (Spring 2025)](https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16), lectures 1–6, for rigorous computer vision.
- **Regional-language options (Hindi):** [CampusX — 100 Days of Deep Learning](https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn); [Krish Naik — Complete Deep Learning](https://www.youtube.com/playlist?list=PLZoTAELRMXVPGU70ZGsckrMdr0FteeRUi); NPTEL [Deep Learning (IIT Ropar/Madras, Mitesh Khapra)](https://nptel.ac.in/courses/106106184) (free videos).
