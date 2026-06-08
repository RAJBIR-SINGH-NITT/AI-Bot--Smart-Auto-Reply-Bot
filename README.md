# Spider ML - Task 1 Submission

## Base Task + Bonus Task
custom branching neural network on Fashion-MNIST, built in PyTorch

**SpidyBranchingNet architecture:**
- input 28x28 image flattened to 784
- shared trunk: 784 - 16
- left branch: 16 - 8 - 8 with skip connection
- right branch: 16 - 12 - 8
- concat both branches - 16 features - output 10 classes
- trained 10 epochs, plots loss and accuracy curves
- weights saved using pickle, submission.csv generated from test set

**Bonus - MLP Autoencoder:**
- encoder: 784 - 256 - 128 - latent_dim
- decoder: latent_dim - 128 - 256 - 784
- experimented with latent_dim = 64, 32, 16
- visualised original vs reconstructed images across all 3 sizes

## Applied ML Domain -RAG Pipeline
built after completing the base task

- ingested 7 NLP research papers: Attention, BERT, GPT-3, RAG, Sentence-BERT, LoRA, Llama 2
- stack: LangChain + FAISS + MiniLM embeddings + Zephyr-7B via HuggingFace Inference API
- chunk size 700, overlap 150 for better context continuity
- answers include source paper citations
- interactive Streamlit UI, runs on Google Colab via LocalTunnel

## Files
- `Rajbir_SpiderML_BaseTask_BonusTask.ipynb` - classification + autoencoder
- `Rajbir_SpiderML_AppliedML.ipynb` - RAG pipeline

## Stack
PyTorch, LangChain, FAISS, HuggingFace, Streamlit, Matplotlib, Pandas, Pickle
