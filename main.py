import turtle as t
t.shape("classic")#turtle,circle,square
t.speed(5)
b=input("введите цвет:")
t.color(b)

a=int(input("введите каличество старон:"))
size=int(input("введите длинну стороны:"))

for i in range(a):
  t.forward(size)
  t.left(360/a)
