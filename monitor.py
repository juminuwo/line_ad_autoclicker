if __name__ == '__main__':
    import time


    import pyscreenshot
    from pynput import keyboard, mouse

    from utils import check_ad_ready, check_ad_screen, image_loader, mse

    res = pyscreenshot.grab().size
    _, ad_not_ready_1, ad_ready_1, _ = image_loader()

    Mouse = mouse.Controller()
    Keyboard = keyboard.Controller()

    time_limit = 10
    for i in range(time_limit):
        print(
            'Please switch to fullscreen Scrcpy with LINE play ad screen in: {} sec'
            .format(time_limit - i))
        time.sleep(1)

    while True:
        time.sleep(5)
        if check_ad_screen(ad_ready_1, ad_not_ready_1):
            if check_ad_ready(ad_ready_1):
                Mouse.position = (res[0] / 2, res[1] / 2)
                Mouse.click(mouse.Button.left)
        else:
            Keyboard.press(keyboard.Key.esc)
            Keyboard.release(keyboard.Key.esc)
