# 1.numpy基础
## 1.1.导入
import random

import numpy as np

## 1.2.查看帮助文档
# help(np.abs)

## 1.3.创建numpy数组
### 1.3.1.从0开始，创建numpy数组
nums = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]
)

print(nums)
### 1.3.2.查看数组维度ndim，形状shape和数据类型dtype
print(f"[数组维度]:{nums.ndim}")
print(f"[数组形状]:{nums.shape}")
print(f"[数据类型]:{nums.dtype}")
### 1.3.3.从已有对象之中创建
some = [[random.random() for _ in range(10)] for _ in range(3)]
print(type(some))
some = np.array(some)
print(type(some))
### 1.3.4.创建随机数组
#### np.random.random((a,b))来创建随机数组（随机小数）
nums_1 = np.random.random((3, 3, 8))
print(nums_1)
#### np.random.randint(low=*,high=*,size=(a,b))（随机整数）
nums_2 = np.random.randint(low=1, high=30, size=(3, 3))
print(nums_2)
### 1.3.5.np.random.seed(seed_number)生成可复现的随机数组
#### 设置随机种子——》生成随机数组——》再次设置随机种子——》再次生成数组
#### 每个随机种子生成的随机数组都是可复现的
np.random.seed(123)
nums_2 = np.random.randint(low=1, high=30, size=(3, 3))
print(nums_2)
np.random.seed(123)
nums_2 = np.random.randint(low=1, high=30, size=(3, 3))
print(nums_2)

## 1.4.访问numpy数组
some = np.random.random((4, 5))
print(some)
print(some[1][3])

## 1.5.算数运算
### 1.5.1.逐元素乘法（a*b）
a = np.ones(shape=(3, 1))
b = np.ones(shape=(3, 1))
print(a * b)
### 1.5.2.矩阵乘法（np.matmul(a,b)）
c = np.matmul(a, b.T)
# print(a)
print(f"[c]:{c}")
## 1.6.reshape(a,b)重塑维度
arr = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [1, 2, 3],
        [4, 5, 6],
    ]
)
print(arr)
arr = arr.reshape(2, 6)
print(arr)
