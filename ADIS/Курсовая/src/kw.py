from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

model2 = RandomForestRegressor()
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
mae2 = mean_absolute_error(y_test, y_pred2)
mse2 = mean_squared_error(y_test, y_pred2)
r2_2 = r2_score(y_test, y_pred2)

model3 = DecisionTreeRegressor()
model3.fit(X_train, y_train)
y_pred3 = model3.predict(X_test)
mae3 = mean_absolute_error(y_test, y_pred3)
mse3 = mean_squared_error(y_test, y_pred3)
r2_3 = r2_score(y_test, y_pred3)

# Visualize the Random Forest Regression predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred2, color='green')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Random Forest Regression Prediction Visualization')
plt.show()

plt.rcParams["figure.figsize"] = (15, 4)
plt.gca().axes.get_yaxis().set_visible(False)
# True results
plt.scatter(X_test.index, y_test, color='y', marker='x', label='True result')
# Predicted results from Linear Regression model
plt.plot(X_test.index, y_pred2, 'b+', label='Predicted result (Random Forest Regression)')
plt.legend(loc='center right', shadow=True)
plt.show()

# Visualize the Random Forest Regression predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred3, color='purple')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Decision Tree Regression Prediction')
plt.show()

plt.rcParams["figure.figsize"] = (15, 4)
plt.gca().axes.get_yaxis().set_visible(False)
# True results
plt.scatter(X_test.index, y_test, color='y', marker='x', label='True result')
# Predicted results from Linear Regression model
plt.plot(X_test.index, y_pred3, 'b+', label='Predicted result (Decision Tree Regression)')
plt.legend(loc='center right', shadow=True)
plt.show()

# Plotting the predictions and actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred1, color='blue', label='Linear Regression')
plt.scatter(y_test, y_pred2, color='green', label='Random Forest Regression')
plt.scatter(y_test, y_pred3, color='purple', label='Decision Tree Regression')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Comparison of Predicted Values')
plt.legend()
plt.show()