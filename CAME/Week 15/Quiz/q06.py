import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error

# Load dataset
df = pd.read_csv("house_prices.csv")

# Target
y = df["price_lkr_mn"]

# Features
X = df[["size_sqft", "rooms", "age_years", "distance_km"]]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# a) Intercept and coefficients
print(round(model.intercept_,4),round(model.coef_[0],4),round(model.coef_[1],4),round(model.coef_[2],4),round(model.coef_[3],4))

# b) Predictions on test set
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(round(mae,4),round(rmse,4),round(r2,4))

# c) Predict price for new house
new_house = pd.DataFrame({
    "size_sqft": [1800],
    "rooms": [3],
    "age_years": [12],
    "distance_km": [8]
})

predicted_price = model.predict(new_house)

print(round(predicted_price[0],4))