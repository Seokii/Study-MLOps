import tensorflow as tf
import argparse


def train():
    print("TensorFlow version: ", tf.__version__)

    parser = argparse.ArgumentParser()
    parser.add_argument('--learning_rate', default=0.01, type=float, required=False)
    parser.add_argument('--dropout', default=0.2, type=float, required=False)
    parser.add_argument('--opt', type=int, default=1, required=False)
    args = parser.parse_args()

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Reserve 10,000 samples for validation
    x_val = x_train[-10000:]
    y_val = y_train[-10000:]
    x_train = x_train[:-10000]
    y_train = y_train[:-10000]

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(args.dropout),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    sgd = tf.keras.optimizers.SGD(learning_rate=args.learning_rate)
    adam = tf.keras.optimizers.Adam(learning_rate=args.learning_rate)

    optimizers = [sgd, adam]

    model.compile(optimizer=optimizers[args.opt],
                  loss='sparse_categorical_crossentropy',
                  metrics=['acc'])

    model.fit(x_train, y_train,
              batch_size=64, epochs=5,
              validation_data=(x_val, y_val))

    loss, acc = model.evaluate(x_test, y_test, batch_size=128)
    print(f"model val-loss={loss:.4f} val-acc={acc:.4f}")


class KatibMetricLog(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        print("\nEpoch {}".format(epoch + 1))
        print("accuracy={:.4f}".format(logs['acc']))
        print("loss={:.4f}".format(logs['loss']))
        print("Validation-accuracy={:.4f}".format(logs['val_acc']))
        print("Validation-loss={:.4f}".format(logs['val_loss']))


if __name__ == '__main__':
    train()
