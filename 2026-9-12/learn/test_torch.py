# 2.Pytorch简单学习
## 2.1.tensor张量与标量
import torch

x = torch.tensor([1])
y = torch.tensor([1, 2, 3])
print(f"{x}\n{y}")

## 2.2.简单四则运算（以加法运算为例）
z = torch.rand(size=y.shape)
print(z)
print(y + z)
s = torch.rand(size=(2, 3))
d = torch.rand(size=(2, 3))
print(torch.matmul(s, d.T))

## 2.3.创建特殊矩阵
### torch.eye()单位矩阵
a = torch.eye(3, 3)
print(a)
### torch.zeros()创建全0矩阵
b = torch.zeros(3, 3)
print(b)
### torch.ones()创建全1矩阵
c = torch.ones(3, 3)
print(c)

## 2.4.reshape重置维度
d = torch.rand(size=(3, 4))
print(d)
e = d.reshape(shape=(2, 6))
print(e)

## 2.5.device操作
some = torch.rand(size=(3, 4))
print(some)
print(some.device)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
some = some.to(device=device)
print(some.device)

## 2.6.求导
### requires_grad is True and y backward() and x.grad()
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = (x**2 + 2).sum()
y.backward()
print(x.grad)
