import datetime
import os
import shutil
from datetime import datetime

import matplotlib
import matplotlib.backends.backend_agg as agg
import pyautogui
import pygame
import pygame_gui
import pylab
import requests
from pycoingecko import CoinGeckoAPI

# Matlab
matplotlib.use("Agg")
graph = pylab.figure(figsize=[5, 5], dpi=100)
graph_string = ''
display_data = []
ax = graph.gca()

pygame.init()

# List's
name_list = list()
image_list = list()
sparkline_list = list()

market_cap_list = list()
price_list = list()
price_1h = list()
price_24h = list()
price_7d = list()

# Pygame Variables
WIDTH, HEIGHT = 800, 480
running = True
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.get_surface()
font = pygame.font.Font('roboto.ttf', 20)
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# CoinGecko
cg = CoinGeckoAPI()

current_data = cg.get_coins_markets(vs_currency='pln', order='market_cap_desc',
                                    per_page='100', sparkline='true', price_change_percentage='1h,24h,7d')
temp_data = []

current_coin = 0

# PygameUI
button_up = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800 - 200 - 50, 480 - 50), (100, 50)),
                                         text='↑',
                                         manager=manager)
button_down = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800 - 100, 480 - 50), (100, 50)),
                                           text='↓',
                                           manager=manager)

timer = 0


def update_buttons():
    if current_coin == 0:
        button_up.disable()
    elif current_coin == len(current_data) - 1:
        button_down.disable()
    else:
        button_down.enable()
        button_up.enable()


def update_graph():
    global display_data, ax, graph, graph_string

    graph.clear()
    ax = graph.gca()

    display_data = sparkline_list[current_coin]
    ax.plot(display_data)

    canvas = agg.FigureCanvasAgg(graph)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()

    graph_string = pygame.image.fromstring(raw_data, size, "RGB")


def draw_elements():
    global name_list, price_list, market_cap_list, price_1h, price_24h, price_7d
    # Current coin
    screen.fill((255, 255, 255))
    now = datetime.now()

    manager.draw_ui(screen)
    current_coin_num = font.render(str(current_coin + 1), False, (0, 0, 0))
    current_time = font.render(now.strftime("%H:%M:%S"), False, (0, 0, 0))

    name_text = font.render('Nazwa: ' + str(name_list[current_coin]), False, (0, 0, 0))
    price_text = font.render('Cena: ' + str(round(price_list[current_coin], 6)) + ' zł', False, (0, 0, 0))
    price_1h_text = font.render('1h: ' + str(round(price_1h[current_coin], 2)) + "%", False, (0, 0, 0))
    price_24h_text = font.render('24h: ' + str(round(price_24h[current_coin], 2)) + "%", False, (0, 0, 0))
    price_7d_text = font.render('7d: ' + str(round(price_7d[current_coin], 2)) + "%", False, (0, 0, 0))

    sparkline_min = font.render('Minimum: ' + str(round(min(sparkline_list[current_coin]), 5)) + " $", False, (0, 0, 0))
    sparkline_max = font.render('Maximum: ' + str(round(max(sparkline_list[current_coin]), 5)) + " $", False, (0, 0, 0))

    coin_img = pygame.transform.scale(pygame.image.load(os.path.join('images', name_list[current_coin] + '.png')),
                                      (45, 45))

    screen.blit(graph_string, (-4, -15))
    screen.blit(current_time, (580, 0))

    screen.blit(name_text, (465, 90))
    screen.blit(price_text, (465, 120))
    screen.blit(price_1h_text, (465, 150))
    screen.blit(price_24h_text, (465, 180))
    screen.blit(price_7d_text, (465, 210))
    screen.blit(sparkline_min, (465, 240))
    screen.blit(sparkline_max, (465, 270))

    screen.blit(coin_img, (652, 430))
    screen.blit(current_coin_num, (500, 435))

    pygame.display.update()


def process_events(time_delta):
    global running, current_coin

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:

                pyautogui.moveTo(20, 20)

                if event.ui_element == button_up:
                    current_coin = current_coin - 1
                    update_graph()

                if event.ui_element == button_down:
                    current_coin = current_coin + 1
                    update_graph()

        manager.process_events(event)
    manager.update(time_delta)


def get_coins():
    global current_data, temp_data

    temp_data = cg.get_coins_markets(vs_currency='pln', order='market_cap_desc',
                                     per_page='100', sparkline='true', price_change_percentage='1h,24h,7d')

    if current_data != temp_data:
        current_data = temp_data
        set_data()


def set_data():
    global name_list, image_list, sparkline_list, price_list, \
        market_cap_list, price_1h, price_24h, price_7d, current_data, temp_data

    name_list.clear()
    image_list.clear()
    sparkline_list.clear()
    market_cap_list.clear()
    price_list.clear()
    price_1h.clear()
    price_24h.clear()
    price_7d.clear()

    for i in current_data:
        name_list.append(i['id'])
        image_list.append(i['image'])
        sparkline_list.append(i['sparkline_in_7d']['price'])
        market_cap_list.append(i['market_cap'])
        price_list.append(i['current_price'])
        price_1h.append(i['price_change_percentage_1h_in_currency'])
        price_24h.append(i['price_change_percentage_24h_in_currency'])
        price_7d.append(i['price_change_percentage_7d_in_currency'])

    if os.path.exists('images'):
        pass
    else:
        os.mkdir('images')

    for o, y in zip(image_list, name_list):
        image_url = o

        path = os.path.join('images', y + '.png')

        if os.path.exists(path):
            pass
        else:
            r = requests.get(image_url, stream=True)

            # Check if the image was retrieved successfully
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True

                # Open a local file with wb ( write binary ) permission.
                with open(path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                print('error')


def main():
    global running, timer
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    update_graph()
    while running:
        draw_elements()

        if timer > 15:
            get_coins()
            timer = 0

        update_buttons()
        process_events(clock.tick(60) / 1000.0)
        timer = timer + 0.1


if __name__ == '__main__':
    set_data()
    main()
