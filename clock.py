# Катя узнала, что ей для сна надо
# X
# минут. В отличие от Коли, Катя ложится спать после полуночи в
# H
# часов и
# M
#  минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через
# X
#  минут после того, как она ляжет спать.
#
# На стандартный ввод, каждое в своей строке, подаются значения
# X
# ,
# H
#  и
# M
# . Гарантируется, что Катя должна проснуться в тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.

x = int(input())
h = int(input())
m = int(input())

count_min = (60 * h) + m + x

print(count_min // 60)
print(count_min % 60)



