from tacape.logo import logo
from tacape.utils.load import load_data
from tensorflow import keras
from tacape.models import build_model
from sklearn.preprocessing import LabelEncoder
from argparse import ArgumentParser
import tensorflow as tf
import pickle
import json

def main():

    print(logo)

    argument_parser = ArgumentParser(prog='TACaPe: Model Training')
    argument_parser.add_argument('--positive-train', required=True, help='Input file containing positive peptides for training')
    argument_parser.add_argument('--negative-train', required=True, help='Input file containing negative peptides for training')
    argument_parser.add_argument('--positive-test', required=True, help='Input file containing positive peptides for testing')
    argument_parser.add_argument('--negative-test', required=True, help='Input file containing negative peptides for testing')
    argument_parser.add_argument('--format', choices=['text', 'fasta'], default='text', help='[optional] Input file format (default: text)')
    argument_parser.add_argument('--output', required=True, help='Path prefix of the output files containing the trained model')
    argument_parser.add_argument('--epochs', type=int, default=30, help="[optional] Number of epochs to be used during training (default: 30)")
    argument_parser.add_argument('--max-peptide-length', type=int, default=60, help="[optional] Max length for peptides (for sequence padding / truncation) (default: 60)")

    arguments = argument_parser.parse_args()

    train_model(
        arguments.positive_train, 
        arguments.negative_train,
        arguments.positive_test, 
        arguments.negative_test, 
        format=arguments.format, 
        output=arguments.output,
        epochs=arguments.epochs,
        max_peptide_length=arguments.max_peptide_length
    )

def train_model(positive_train, negative_train, positive_test, negative_test, output, format='text', epochs=30, max_peptide_length=60):

    config = {
        'max_peptide_length': max_peptide_length
    }

    with open(output + '_config.json', 'w') as writer:
        writer.write(
            json.dumps(config)
        )

    raw_X_train = [*load_data(positive_train, format), *load_data(negative_train, format)]
    raw_X_test  = [*load_data(positive_test, format), *load_data(negative_test, format)]

    y_train = [1 for _ in load_data(positive_train, format)] + [0 for _ in load_data(negative_train, format)]
    y_test  = [1 for _ in load_data(positive_test, format)] + [0 for _ in load_data(negative_test, format)]

    tokenizer = keras.preprocessing.text.Tokenizer(char_level = True)
    tokenizer.fit_on_texts(raw_X_train)

    X_train = keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences(raw_X_train), maxlen = max_peptide_length)
    X_test  = keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences(raw_X_test), maxlen = max_peptide_length)

    with open(output + '.tokenizer', 'wb') as writer:
        writer.write(pickle.dumps(tokenizer))

    le = LabelEncoder()
    le.fit(y_train)

    y_train_encode = keras.utils.to_categorical(le.transform(y_train))
    y_test_encode  = keras.utils.to_categorical(le.transform(y_test))

    with open(output + '.le', 'wb') as writer:
        writer.write(pickle.dumps(le))

    callbacks = [tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        min_delta=0,
        patience=5,
        verbose=0,
        mode="auto",
        baseline=None,
        restore_best_weights=True,
        start_from_epoch=0,
    )]
    
    model = build_model(vocab_size=len(tokenizer.word_index) + 1, output_shape=(len(le.classes_)))
    model.fit(X_train, y_train_encode, validation_data=(X_test, y_test_encode), epochs=epochs, callbacks=callbacks)
    model.save_weights(output + '.weights')

if __name__ == '__main__':
    main()