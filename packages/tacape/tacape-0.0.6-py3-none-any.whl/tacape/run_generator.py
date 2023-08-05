from tacape.logo import logo
from tacape.utils.load import load_data
from tensorflow import keras
from tacape.models import build_model
from sklearn.preprocessing import LabelEncoder
from argparse import ArgumentParser
from tqdm import tqdm
import warnings
import numpy as np
import tensorflow as tf
import pickle
import json

warnings.simplefilter('ignore')

def main():

    print(logo)

    argument_parser = ArgumentParser(prog='TACaPe: Generate')
    argument_parser.add_argument('--generator-prefix', required=True, help='Path to the file prefix of the trained generative model')
    argument_parser.add_argument('--classifier-prefix', help='[optional] Path to the file prefix of the trained classification model')
    argument_parser.add_argument('--number-of-sequences', default=1000, type=int, help='[optional] Number of sequences to be generated (default: 1000)')
    argument_parser.add_argument('--temperature', default=1.0, type=float, help='[optional] Temperature used for logit scaling when sampling aminoacids during auto-regressive generation (default: 1.0)')
    argument_parser.add_argument('--threshold', default=0.5, type=float, help='[optional] Classification probability threshold (default: 0.5)')
    argument_parser.add_argument('--output', required=True, help='Path to the output FASTA file')

    arguments = argument_parser.parse_args()

    run_generator(arguments.generator_prefix, arguments.classifier_prefix, arguments.output, arguments.number_of_sequences, arguments.temperature, arguments.threshold)

def run_generator(generator_prefix, classifier_prefix, output, number_of_sequences, temperature, threshold):

    with open(generator_prefix + '_config.json', 'r') as reader:
        config = json.loads(reader.read())

    with open(generator_prefix + '.tokenizer', 'rb') as reader:
        generator_tokenizer = pickle.loads(reader.read())

    with open(generator_prefix + '.le', 'rb') as reader:
        generator_le = pickle.loads(reader.read())    

    generator_model  = build_model(vocab_size=len(generator_tokenizer.word_index) + 1, output_shape=(len(generator_le.classes_)))
    generator_model.load_weights(generator_prefix + '.weights').expect_partial()

    if classifier_prefix:

        with open(classifier_prefix + '.tokenizer', 'rb') as reader:
            classifier_tokenizer = pickle.loads(reader.read())

        with open(classifier_prefix + '.le', 'rb') as reader:
            classifier_le = pickle.loads(reader.read())

        classifier_model  = build_model(vocab_size=len(classifier_tokenizer.word_index) + 1, output_shape=(len(classifier_le.classes_)))
        classifier_model.load_weights(classifier_prefix + '.weights')

    number_of_generated_sequences = 0

    progress_bar = tqdm(total=number_of_sequences)

    with open(output, 'w') as writer:

        while number_of_generated_sequences < number_of_sequences:
            sequence = generate_sequence(generator_model, generator_tokenizer, generator_le, temperature=temperature, max_len=config['max_peptide_length'])
            if classifier_prefix:
                score = classify_sequence(sequence, classifier_model, classifier_tokenizer)
                if score > threshold:
                    writer.write(f'>{number_of_generated_sequences+1} {score}\n{sequence}\n')
                    number_of_generated_sequences += 1
                    progress_bar.update(1)
            else:
                writer.write(f'>{number_of_generated_sequences+1}\n{sequence}\n')
                number_of_generated_sequences += 1
                progress_bar.update(1)
        progress_bar.close()

def sample(a, temperature=1.0):
    a = np.array(a).astype('float64')
    a = np.log(a) / temperature
    a = np.exp(a) / np.sum(np.exp(a))
    return np.argmax(np.random.multinomial(1, a, 1))

def generate_sequence(generator_model, generator_tokenizer, generator_le, min_len=5, max_len=50, temperature=1.0):

    while True:
        sequence = '$'
        next_token = None
        while True:
            tokenized  = keras.preprocessing.sequence.pad_sequences(generator_tokenizer.texts_to_sequences([sequence]), maxlen = 60)
            next_token = generator_le.inverse_transform([sample(generator_model.predict(tokenized, verbose=False)[0], temperature=temperature)])[0]
            sequence += next_token
            if next_token == '.' or len(sequence) > 60:
                break
        if min_len <= len(sequence)-2 <= max_len:
            return sequence.strip('$').strip('.')
        
def classify_sequence(sequence, classifier_model, classifier_tokenizer):
    X_tokens = keras.preprocessing.sequence.pad_sequences(classifier_tokenizer.texts_to_sequences([sequence]), maxlen = 60)
    y_pred   = classifier_model.predict(X_tokens, verbose=False)
    return y_pred[0][1]


if __name__ == '__main__':
    main()