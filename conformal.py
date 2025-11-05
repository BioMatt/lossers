# ============================================================
# GET PREDICTIONS
# ============================================================
print("\n📊 Getting predictions on all splits...")

our_results_val = predict_v2(loaded_model, val_loader_v2, device)
our_results_test = predict_v2(loaded_model, test_loader_v2, device)

y_val_np = our_results_val[0].cpu().numpy()
y_test_np = our_results_test[0].cpu().numpy()

print("✓ Predictions complete")


non_conformity_scores = 1 - y_val_np

# 4. Determine the confidence threshold (q-hat)
alpha = 0.1 # For 90% coverage
n = len(non_conformity_scores)
# Finite sample correction: use (n+1) * (1 - alpha) quantile
q_hat = np.quantile(non_conformity_scores, np.ceil((n + 1) * (1 - alpha)) / (n + 1))
q_hat

# y_train_np = our_results_train[0].cpu().numpy().ravel()
y_val_true = our_results_val[1].cpu().numpy()
y_test_true = our_results_test[1].cpu().numpy()

y_calib = y_val_true

from scipy.special import softmax

predictions_calib = softmax(y_val_np)

# Get the probability of the true class for each calibration sample
prob_true_class = predictions_calib[np.arange(len(y_calib)), y_calib]
# Non-conformity score is 1 - P(true class)
non_conformity_scores = 1 - prob_true_class

# 4. Determine the confidence threshold (q-hat)
alpha = 0.1 # For 90% coverage
n = len(non_conformity_scores)
# Finite sample correction: use (n+1) * (1 - alpha) quantile
q_hat = np.quantile(non_conformity_scores, np.ceil((n + 1) * (1 - alpha)) / (n + 1))
q_hat

predictions_test = softmax(y_test_np)
prediction_sets = (1 - predictions_test) <= q_hat


conformal_set_sizes = np.sum(prediction_sets, axis=1)


plt.hist(conformal_set_sizes)