# 1. Daily Revenue Analysis.
import numpy as np
income = np.array([45, 50, 38, 60, 72, 55, 49, 80, 90, 65, 70, 52, 48, 77, 85, 66, 59, 61, 73, 68, 74,
58, 62, 71, 69, 64, 67, 75, 78, 82])
avg = np.mean(income)
print(avg)

max_val = np.max(income)
print(max_val)

max_index_day = np.argmax(income) + 1
print(max_index_day)

above_avg = np.where(income > avg)
days = above_avg[0] + 1
print(days)

total = np.sum(income)
print(total)

# 2. Temperature Analysis.
temps = np.array([12, 15, 18, 22, 25, 28, 30, 27, 24, 20, 16, 10, 5, -2, 0, 3, 8, 14, 19, 23, 26, 29, 31,
33, 35, 32, 28, 24, 20, 17])

avg_temp = np.mean(temps)
print(avg_temp)

above_25 = temps[temps > 25]
print(above_25)

min_val = np.min(temps)
max_val = np.max(temps)
print(min_val)
print(max_val)

temps_to_positive = np.where(temps < 0, 0, temps)
print(temps_to_positive)

count = np.sum(temps >= 20)
print(count)

# 3. Store Sales Matrix.

sales = np.array([[200,220,210,205,215,230,240],[180,190,200,210,205,195,185],
[300,310,320,330,340,350,360],[150,160,155,165,170,175,180],
[220,230,240,235,245,255,265]])

store_totals = np.sum(sales, axis=1)
print(store_totals)

day_totals = np.sum(sales, axis=0)
print(day_totals)

best_store = np.argmax(store_totals)
print(best_store + 1)

best_day = np.argmax(day_totals)
print(best_day + 1)

avg_overall = np.mean(sales)
print(avg_overall)

# 4. Plan vs Actual.

plan = np.array([100,120,130,110,115,140,150])
fact = np.array([90,125,128,105,120,135,160])

dev = fact - plan
print(dev)

avg_dev = np.mean(dev)
print(avg_dev)

abs_err = np.abs(dev)
print(abs_err)

mae = np.mean(abs_err)
print(mae)

above_plan = fact > plan
print(above_plan)

day_indices = np.where(fact > plan)[0]
print(day_indices + 1)

# 5. Missing Data Handling.

data_with_nan = np.array([10,15,np.nan,20,25,np.nan,30])

mean_val = np.nanmean(data_with_nan)
print(mean_val)

replace_nan = np.where(np.isnan(data_with_nan), mean_val, data_with_nan)
print(replace_nan)

median = np.nanmedian(data_with_nan)
print(median)

std = np.nanstd(data_with_nan)
print(std)

# 6. Student Scores.

scores = np.array([78,85,92,88,76,95,89,84,91,87])

top5 = np.sort(scores)[-5:]
print(top5)

avg_score = np.mean(scores)
print(avg_score)

count = np.sum(scores > 90)
print(count)

# 7. Outlier Detection.

data = np.array([10,12,11,13,12,11,50,12,13,11])

mean_outlier_detection = np.mean(data)
print(mean_outlier_detection)

std_outlier_detection = np.std(data)
print(std_outlier_detection)

threshold = mean_outlier_detection + 2 * std_outlier_detection
print(threshold)

outliers = data[data > threshold]
print(outliers)

# 8. Expected Value.

game = np.array([10,-2,-2,10,-2,-2,-2,10,-2,-2])

total = np.sum(game)
print(total)

avg_gain = np.mean(game)
print(avg_gain)

p_win = np.sum(game > 0) / len(game)
print(p_win)

values, counts = np.unique(game, return_counts=True)
probs = counts / len(game)

print(values, counts)
print(probs)

expected = np.sum(values * probs)
print(expected)







