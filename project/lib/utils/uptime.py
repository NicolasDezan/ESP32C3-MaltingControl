import time

class Uptime:
    def __init__(self):
        self.start_time = time.ticks_ms()
    
    def milliseconds(self):
        """Retorna os milissegundos desde o início"""
        return time.ticks_diff(time.ticks_ms(), self.start_time)
    
    def seconds(self):
        """Retorna os segundos totais desde o início"""
        return self.milliseconds() // 1000
    
    def minutes(self):
        """Retorna os minutos totais desde o início"""
        return self.seconds() // 60
    
    def hours(self):
        """Retorna as horas totais desde o início"""
        return self.minutes() // 60
    
    def days(self):
        """Retorna os dias totais desde o início"""
        return self.hours() // 24
    
    def formatted(self):
        """Retorna o tempo formatado como HH:MM:SS"""
        uptime_sec = self.seconds()
        minutes, seconds = divmod(uptime_sec, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
    def formatted_dhms(self):
        """Retorna o tempo formatado como DDd HH:MM:SS"""
        uptime_sec = self.seconds()
        minutes, seconds = divmod(uptime_sec, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return "{}d {:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)
    
    def reset(self):
        """Reinicia a contagem do uptime"""
        self.start_time = time.ticks_ms()