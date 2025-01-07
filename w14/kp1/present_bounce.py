#!/usr/bin/env python3

import pyautogui, sys, time

class PresentBounce():
    def __init__(self, **kwargs):
        self.wx = kwargs['wx']
        self.wy = kwargs['wy']
        self.ww = kwargs['ww']
        self.wh = kwargs['wh']

    def get_kwargs(self):
        return {'wx': self.wx, 'wy': self.wy,
                'ww': self.ww, 'wh': self.wh}
        
    def skip_instruction(self):
        time.sleep(7)
        for _ in range(3):
            time.sleep(3)
            pyautogui.click(self.wx+int(self.ww/2),
                            self.wy+int(self.wh/2))
            
    def find_img(self, img: str, **kwargs):
        gray_scale = kwargs.pop('gray_scale', False)
        confidence = kwargs.pop('confidence', 0.8)
        for _ in range(30):
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    f"./input/{img}", grayscale=gray_scale,
                    confidence=confidence)
                break
            except:
                time.sleep(5)
        return x, y
        
    def drag_img(self, img: str, **kwargs):
        x, y = self.find_img(img, **kwargs)
        self.drag(x, y, **kwargs)
        
    def drag(self, x, y, **kwargs):
        pyautogui.moveTo(x, y)
        delta_x = kwargs.pop('delta_x', 0)
        delta_y = kwargs.pop('delta_y', 0)
        click_lr = kwargs.pop('click_lr', 'left')
        pyautogui.dragTo(x+delta_x, y+delta_y,
                         button=click_lr, duration=1)
        
    def click_img(self, img: str, **kwargs):
        x, y = self.find_img(img, **kwargs)
        click_lr = kwargs.pop('click_lr', 'left')
        pyautogui.click(x, y, button=click_lr)

    def launch_a_present(self):
        self.click_img('launcher.png')

class PresentBounceLv0(PresentBounce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resize_window()
        
    def resize_window(self, ww=700, wh=700):
        # 拡大縮小の場合（ウィンドウの左上の外縁:x=10, y=5）
        # 移動の場合（ウィンドウの左上の内縁:x=20, y=15）
        self.drag(x = self.wx + 20, y = self.wy + 15,
                  delta_x = 50 - self.wx,
                  delta_y = 50 - self.wy)
        self.wx = 50; self.wy = 50
        
        dx = ww - self.ww
        if dx > 0:
            # 右下方向へ移動して左上方向へ拡大
            self.drag(x = self.wx + 20, y = self.wy + 15,
                      delta_x = dx, delta_y = 0)
            self.wx += (dx)
            self.drag(x = self.wx + 10, y = self.wy + 5,
                      delta_x = -dx, delta_y = 0)
            self.wx += (-dx)
        elif dx < 0:
            # 右下方向へ縮小して左上方向へ移動
            self.drag(x = self.wx + 10, y = self.wy + 5,
                      delta_x = -dx, delta_y = 0)
            self.wx += (-dx)
            self.drag(x = self.wx + 20, y = self.wy + 15,
                      delta_x = dx, delta_y = 0)
            self.wx += (dx)
            
        dy = wh - self.wh
        if dy > 0:
            self.drag(x = self.wy + 20, y = self.wy + 15,
                      delta_x = 0, delta_y = dy)
            self.wy += (dy)
            self.drag(x = self.wy + 10, y = self.wy + 5,
                      delta_x = 0, delta_y = -dy)
            self.wy += (-dy)
        elif dy < 0:
            self.drag(x = self.wy + 10, y = self.wy + 5,
                      delta_x = 0, delta_y = -dy)
            self.wy += (-dy)
            self.drag(x = self.wy + 20, y = self.wy + 15,
                      delta_x = 0, delta_y = dy)
            self.wy += (dy)
        
class PresentBounceLv1(PresentBounce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skip_instruction()
        self.drag_img('conveyor.png', delta_x=-380, delta_y=-220)
        self.launch_a_present()
        
class PresentBounceLv2(PresentBounce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drag_img('conveyor.png', delta_x=-420, delta_y=-260)
        self.drag_img('conveyor.png', delta_x=-260, delta_y=-220)
        self.drag_img('spring.png', delta_x=-160, delta_y=-180)
        self.launch_a_present()

if __name__ == '__main__':
    pyautogui.PAUSE = 1
    kwargs = {k: v for k, v in zip(['wx', 'wy', 'ww', 'wh'],
                                   [int(v) for v in sys.argv[1:5]])}
    kwargs = PresentBounceLv0(**kwargs).get_kwargs()
    PresentBounceLv1(**kwargs)
    PresentBounceLv2(**kwargs)
