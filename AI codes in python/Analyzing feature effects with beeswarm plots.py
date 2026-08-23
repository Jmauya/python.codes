//Derive the shap_values using a TreeExplainer
//Use the derived shap_values to plot the beeswarm plot and analyze it

import shap
from sklearn.ensemble import RandomForestRegressor

# Train the model

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Create the SHAP explainer
explainer = shap.TreeExplainer(model)

# Calculate SHAP values

shap_values = explainer.shap_values(X_train)

# Plot the SHAP beeswarm (dot) plot

shap.summary_plot(
    shap_values,
    X_train,
    plot_type="dot"
)
