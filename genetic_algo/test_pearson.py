import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
x = [3.63, 3.02, 3.82, 3.42, 3.56, 2.82, 3.03, 3.46, 3.36, 3.3]
y = [53.1, 49.7, 48.4, 54.2, 54.9, 43.7, 47.2, 45.2, 54.4, 50.4]

# Tính cov và Pearson correlation coefficient
covariance = np.cov(x, y)[0, 1]
correlation = np.corrcoef(x, y)[0, 1]

# In ra kết quả
print(f"Covariance: {covariance}")
print(f"Pearson Correlation Coefficient: {correlation}")

# Vẽ biểu đồ
plt.scatter(x, y, label=f'Pearson Correlation = {correlation:.2f}')
plt.xlabel('Weight (x)')
plt.ylabel('Length (y)')

# Tạo đường hồi quy tuyến tính
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
x_range = np.linspace(min(x), max(x), 100)
y_pred = polynomial(x_range)

# Vẽ đường hồi quy tuyến tính
plt.plot(x_range, y_pred, color='red', label='Linear Regression')
plt.legend()
plt.show()
