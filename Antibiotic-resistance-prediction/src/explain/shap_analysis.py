import shap


def compute_shap_values(model, X):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    return shap_values


def plot_shap_summary(shap_values, X):
    shap.summary_plot(shap_values, X)