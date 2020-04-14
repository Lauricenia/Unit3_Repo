from scipy.stats import pearsonr
x = [1, 2, 3, 4, 5]

corr = [2, 4, 6, 8, 10]
corr, p_value = pearsonr(x, corr)

print(corr)