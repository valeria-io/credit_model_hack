from src.models.utils import train_test_split, prepare_dataset, category_to_numerical, XY_train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


def build_logistic_model():
    df = prepare_dataset()
    df = category_to_numerical(df)
    train_df, train_y, test_df, test_y = XY_train_test_split(df.drop(columns=['Repaid']), df['Repaid'], 0.2)
    clf = RandomForestClassifier(random_state=0)
    clf.fit(train_df, train_y)
    filename = 'finalized_model.sav'
    pickle.dump(clf, open(filename, 'wb'))

    # loaded_model = pickle.load(open(filename, 'rb'))
    # result = loaded_model.score(X_test, Y_test)
    train_score = clf.score(train_df, train_y)
    test_score = clf.score(test_df, test_df)

    print('training accuracy...')
    print(train_score)
    print('testing accuracy...')
    print(test_score)


def load_model_and_prediction(X_test, filename='finalized_model.sav'):
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(X_test)
    print(result)
