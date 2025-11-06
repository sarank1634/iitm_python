# write a piece of code to  find the dot product.

x=[1,7,3,4]
y=[8,6,3,2]

dot_product = 0

for i in range(len(x)):
    dot_product += x[i] * y[i]

print("Dot product: ",dot_product)

# break down:-
# Dot product=(1∗8)+(7∗6)+(3∗3)+(4∗2)
# =
# 8
# +
# 42
# +
# 9
# +
# 8
# =
# 67
# =8+42+9+8=67

dot_product = sum(a*b for a, b in zip(x, y))
print(dot_product)  # 67
