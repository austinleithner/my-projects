# Sentiment analysis on IMDB movie reviews using an LSTM model with pretrained GloVe embeddings.
import os
import zipfile
from keras.utils import get_file
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from keras.layers import TextVectorization
# unnsed imports commented out
# import pandas as pd
# import tensorflow as tf

# Notes on model performance:
# After training for 6 epochs, Training Acc: 0.8626, Validation Acc: 0.8560 with non-trainable embeddings.
# Model overfits so I am early stopping at 6 epochs to get a "decent" validation accuracy.
# Model overfits quickly while fine-tuning embeddings.

# Fixed parameters for model
MAX_LEN = 100
EMB_DIM = 100
VOCAB_SIZE = 20000

# Hyperparameters
# Model overfits after 6 epochs so, keep it at that for demo purposes.
# Using the default learning rate of Adam optimizer.
EPOCHS = 6
BATCH_SIZE = 32
test_size = 0.01 # Percentage of total data to use for validation

# Prepare tokenizer for text preprocessing
def prepare_tokenizer(texts, max_vocab=20000, maxlen=100):
        vectorizer = TextVectorization(max_tokens=max_vocab, output_mode="int", output_sequence_length=maxlen)
        vectorizer.adapt(texts)
        return vectorizer

# Download GloVe embeddings
def download_glove(dim=100):
        glove_dir = os.path.join(os.path.expanduser("~"), ".glove")
        os.makedirs(glove_dir, exist_ok=True)
        zip_path = get_file("glove.6B.zip",
                                                "http://nlp.stanford.edu/data/glove.6B.zip",
                                                cache_dir=glove_dir, cache_subdir="")
        with zipfile.ZipFile(zip_path, "r") as z:
                name = f"glove.6B.{dim}d.txt"
                if name not in z.namelist():
                        raise ValueError("Requested GloVe dim not found in archive.")
                z.extract(name, path=glove_dir)
        return os.path.join(glove_dir, f"glove.6B.{dim}d.txt")

# Load GloVe embeddings into a dictionary
def load_glove_dict(glove_path):
        emb_index = {}
        with open(glove_path, encoding="utf8") as f:
                for line in f:
                        parts = line.rstrip().split(" ")
                        word = parts[0]
                        vec = np.asarray(parts[1:], dtype="float32")
                        emb_index[word] = vec
        return emb_index

# Build embedding matrix from vocabulary and GloVe embeddings
def build_embedding_matrix_from_vocab(vocab, emb_index, emb_dim):
        emb_matrix = np.zeros((len(vocab), emb_dim), dtype="float32")
        for i, word in enumerate(vocab):
                vec = emb_index.get(word)
                if vec is not None:
                        emb_matrix[i] = vec
        return emb_matrix


print("Loading IMDB data (tfds preferred, keras fallback)...")
try:
    import tensorflow_datasets as tfds
    ds_train = tfds.load('imdb_reviews', split='train', as_supervised=True)
    ds_test = tfds.load('imdb_reviews', split='test', as_supervised=True)
    texts = []
    labels = []
    for text, label in tfds.as_numpy(ds_train.concatenate(ds_test)):
        if isinstance(text, (bytes, bytearray)):
            texts.append(text.decode('utf-8'))
        else:
            texts.append(str(text))
        labels.append(int(label))
    labels = np.array(labels, dtype=np.int32)
except Exception:
    from tensorflow.keras.datasets import imdb
    word_index = imdb.get_word_index()
    index_word = {i+3: w for w, i in word_index.items()}
    index_word[0] = '<pad>'
    index_word[1] = '<start>'
    index_word[2] = '<unk>'
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=VOCAB_SIZE)
    def seq_to_text(seq):
        return ' '.join(index_word.get(i, '?') for i in seq)
    texts = [seq_to_text(s) for s in (list(x_train) + list(x_test))]
    labels = np.array(list(y_train) + list(y_test), dtype=np.int32)

print(f"Total samples loaded: {len(texts)}")

print("Preparing tokenizer and sequences...")
tokenizer = prepare_tokenizer(texts, max_vocab=VOCAB_SIZE, maxlen=MAX_LEN)
sequences = tokenizer(np.array(texts))
X = sequences.numpy()
y = np.array(labels)

# Split into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=42)

# Get vocabulary size
vocab = tokenizer.get_vocabulary()
vocab_size = len(vocab)

# Build embedding matrix from pretrained GloVe vectors
print("Downloading/locating GloVe and building embedding matrix (this may take a while)...")
glove_path = download_glove(dim=EMB_DIM)
emb_index = load_glove_dict(glove_path)
emb_matrix = build_embedding_matrix_from_vocab(vocab, emb_index, EMB_DIM)

num_classes = len(np.unique(y))
if num_classes == 2:
    final_activation = 'sigmoid'
    final_units = 1
    loss = 'binary_crossentropy'
else:
    final_activation = 'softmax'
    final_units = num_classes
    loss = 'sparse_categorical_crossentropy'

# Building the model
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=EMB_DIM,
              weights=[emb_matrix], trainable=False, mask_zero=True),
    Bidirectional(LSTM(64)),
    Dense(64, activation="relu"),
    Dropout(0.5),
    Dense(final_units, activation=final_activation)
])
model.compile(optimizer="adam", loss=loss, metrics=["accuracy"])
model.summary()

print(f"Training for {EPOCHS} epochs.")
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=EPOCHS, batch_size=BATCH_SIZE)

loss_val, acc_val = model.evaluate(X_val, y_val, verbose=0)
print(f"Validation loss: {loss_val:.4f}, accuracy: {acc_val:.4f}")
