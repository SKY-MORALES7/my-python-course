import time
import datetime
import pygame

# String Format Time

# str → string
# f → format
# time → time/date

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = 'music/myjam.mp3'
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f'You set Alarm for {alarm_time}, The current time is {current_time}')

        if current_time == alarm_time:
            print('WAKE UP! 😳')
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

          


        time.sleep(1)



if __name__ == '__main__':
    alarm_time = input("Enter The alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)