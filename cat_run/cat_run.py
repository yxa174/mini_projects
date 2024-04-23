import rumps
import psutil

class ImageApp(rumps.App):
    def __init__(self):
        super(ImageApp, self).__init__("Image App")
        self.icons = ["icon1.png", "icon2.png", "icon3.png", "icon4.png"]  # Список изображений
        self.current_icon_index = 0
        self.timer = rumps.Timer(self.update_icon, 0.1)  # Инициализируем таймер с интервалом 1 секунда
        self.timer.start()
        self.update_icon()

    def update_icon(self, sender=None):
        # Меняем иконку на следующую в списке
        self.icon = self.icons[self.current_icon_index]
        self.current_icon_index = (self.current_icon_index + 1) % len(self.icons)

        # Обновляем интервал таймера
        self.update_timer_interval()

    def update_timer_interval(self):
        # Получаем текущее процентное использование CPU
        cpu_percent = psutil.cpu_percent(interval=0.05)

        # Устанавливаем интервал таймера в зависимости от процентного использования CPU
        if cpu_percent > 5:  # Если загрузка процессора высокая
            self.timer.interval = 0.3  # Устанавливаем короткий интервал времени
        else:
            self.timer.interval = 0.31  # Устанавливаем стандартный интервал времени

if __name__ == "__main__":
    app = ImageApp()
    app.run()






















# "icon1.png", "icon2.png", "icon3.png", "icon4.png""icon1.png", "icon2.png", "icon3.png", "icon4.png"
