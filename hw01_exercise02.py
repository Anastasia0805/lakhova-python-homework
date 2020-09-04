time = int(input('Введите время в секундах'))

hours = int(time//3600)
minutes = int(time%3600/60)
seconds= int(time % 60)
print (f" {time} секунд равно  {hours} чч: {minutes} мм: {seconds} сc.")