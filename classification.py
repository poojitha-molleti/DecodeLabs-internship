from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    print(" AI Data Classification Project\n")

    data = load_iris()
    X = data.data        
    y = data.target      

    print("Dataset loaded successfully!")
    print(f"Total samples: {len(X)}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Data split into training and testing sets.\n")

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, y_train)
    print("Model training completed.\n")

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%\n")

    print(" Try your own flower prediction!")
    sepal_length = float(input("Enter sepal length: "))
    sepal_width = float(input("Enter sepal width: "))
    petal_length = float(input("Enter petal length: "))
    petal_width = float(input("Enter petal width: "))

    user_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    prediction = model.predict(user_data)
    flower_name = data.target_names[prediction[0]]

    print(f"\n Predicted Flower Type: {flower_name}")

if __name__ == "__main__":
    main()