import akshare as ak
from dtw import dtw
import numpy as np
import matplotlib.pyplot as plt

def DtwDist(series1, series2):
    manhattan_distance = lambda x, y: np.abs(x - y)
    dist, cost, acc, path = dtw(
        series1, series2, manhattan_distance)
    return dist


def draw(len):
    stock_zh_index_daily_em_df = ak.stock_zh_index_daily_em(symbol="sh000300")
    data = stock_zh_index_daily_em_df[-1000:]
    last_k = data["close"]
    last_ten = stock_zh_index_daily_em_df[-len:]["close"]
    last_ten = last_ten / last_ten.max()
    min = 1000000
    index = 0
    for i in range(450):
        temp = last_k[i:i+len]
        temp = temp / temp.max()
        current_dist = DtwDist(temp.values, last_ten.values)
        if current_dist < min :
            min = current_dist
            index = i
        
    print(data[index:index+len])
    plt.plot(stock_zh_index_daily_em_df[-len:]["close"].values, label='The last 10 days')
    plt.plot(data[index:index + len + 20]["close"].values, label='Match')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    draw(10)
    draw(20)
    draw(30)

