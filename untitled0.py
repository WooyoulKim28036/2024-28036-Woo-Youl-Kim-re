# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xl18kWTKhesgxoHhlRqe7RNV9rrVxd-V
"""

#신입생 세미나 과제4 2024-28036 김우열
import matplotlib.pyplot as plt

def trapped_rainwater(block):
    answer = 0
    water_heights = [0] * len(block)

    for i in range(1, len(block) - 1):
        left = max(block[:i])
        right = max(block[i + 1:])

        wall = min(left, right)

        if wall > block[i]:
            water_heights[i] = wall - block[i]
            answer += wall - block[i]

    return answer, water_heights

def visualize_block_water(block, water_heights):
    x = range(len(block))

    plt.bar(x, block, color='blue', alpha=0.7, label='Block Height')

    plt.bar(x, water_heights, color='green', alpha=0.7, label='Trapped Water')

    plt.xlabel('Block')
    plt.ylabel('Height')
    plt.title('Trapped Rainwater Visualization')
    plt.legend()
    plt.show()

total_water, water_heights = trapped_rainwater(block)

print("Total trapped water:", total_water)
print("Water heights at each block:", water_heights)

# 첫 번째 예시: [3, 0, 2, 0, 4]
block_1 = [3, 0, 2, 0, 4]
total_water_1, water_heights_1 = trapped_rainwater(block_1)
print("첫 번째 예시:")
print("블록 높이:", block_1)
print("총 쌓인 물의 양:", total_water_1)
print("각 블록 위치에서 쌓인 물의 높이:", water_heights_1)
visualize_block_water(block_1, water_heights_1)
print()

# 두 번째 예시: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
block_2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
total_water_2, water_heights_2 = trapped_rainwater(block_2)
print("두 번째 예시:")
print("블록 높이:", block_2)
print("총 쌓인 물의 양:", total_water_2)
print("각 블록 위치에서 쌓인 물의 높이:", water_heights_2)
visualize_block_water(block_2, water_heights_2)
print()

# 세 번째 예시: [4, 2, 0, 3, 2, 5]
block_3 = [4, 2, 0, 3, 2, 5]
total_water_3, water_heights_3 = trapped_rainwater(block_3)
print("세 번째 예시:")
print("블록 높이:", block_3)
print("총 쌓인 물의 양:", total_water_3)
print("각 블록 위치에서 쌓인 물의 높이:", water_heights_3)
visualize_block_water(block_3, water_heights_3)