import pygame as py
from calculations import waterConsumed
from cropValues import iniCoefficients, midCoefficients, lateCoefficients, iniDuration, midDuration, lateDuration
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab
import numpy as np

py.init()
screen = py.display.set_mode((800, 400), py.RESIZABLE)
py.display.set_caption("Crops")
clock = py.time.Clock()
title_font = py.font.Font("fonts/Freedom-10eM.ttf", 32)
font = py.font.Font("fonts/Freedom-10eM.ttf", 16)
crop_font = py.font.Font("fonts/Freedom-10eM.ttf", 20)
temp_font = py.font.Font("fonts/OpenSans-Regular.ttf", 16)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)

class imageScaling():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = py.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
     screen.blit(self.image, (self.rect.x, self.rect.y))

class Slider():
  def __init__(self, pos, size, initial_value, min, max):
    self.pos = pos
    self.size = size

    self.slider_left_pos = self.pos[0] - (size[0] // 2)
    self.slider_right_pos = self.pos[0] + (size[0] // 2)
    self.slider_top_pos = self.pos[1] - (size[1] // 2)
                                           
    self.initial_value = (self.slider_right_pos - self.slider_left_pos) * initial_value
    self.min = min
    self.max = max

    self.container_rect = py.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
    self.button_rect = py.Rect(self.slider_left_pos + self.initial_value - 5, self.slider_top_pos, 10, self.size[1])
  def move_slider(self, mouse_pos):
    self.button_rect.centerx = mouse_pos[0]
  def render(self):
    py.draw.rect(screen, (110, 110, 110), self.container_rect)
    py.draw.rect(screen, "blue", self.button_rect)
  def get_value(self):
    val_range = self.slider_right_pos - self.slider_left_pos - 1
    button_val = self.button_rect.centerx - self.slider_left_pos

    return round((button_val/val_range)*(self.max-self.min)+self.min)

slider_list = [Slider((170, 120), (300, 40), 0.5, 0, 85*2), Slider((170, 230), (300, 40), 0.5, 0, 1000)] #Slider + text

potato = imageScaling(180, 85, py.image.load("assets/potato.png"), 0.2)
radish = imageScaling(380, 75, py.image.load("assets/radish.png"), 0.2)
lettuce = imageScaling(580, 75, py.image.load("assets/lettuce.png"), 0.2)
turnips = imageScaling(280, 250, py.image.load("assets/turnip.png"), 0.2)
alfalfa = imageScaling(485, 250, py.image.load("assets/alfalfa.png"), 0.2)

def input_crops(index):
  global draw_graph
  title = title_font.render("Input crop values", True, BLACK,)
  screen.blit(title, (220, 20))

  if (leave_box):
    py.draw.rect(screen, (110, 110, 110), (40, 290, 100, 50))
  else:
    py.draw.rect(screen, (180, 180, 180), (40, 290, 100, 50))

  if (update_box):
    py.draw.rect(screen, (110, 110, 110), (200, 290, 100, 50))
  else:
    py.draw.rect(screen, (180, 180, 180), (200, 290, 100, 50))

  leave_text = font.render("Leave", True, BLACK)
  screen.blit(leave_text, (leave.x+16, leave.y+15))

  update_text = font.render("Update", True, BLACK)
  screen.blit(update_text, (update.x+16, update.y+15))
  
  time_slider_text_one = font.render("Enter time period for water", True, BLACK)
  screen.blit(time_slider_text_one, (20, 65))

  time_slider_text_two = font.render("consumption in days", True, BLACK)
  screen.blit(time_slider_text_two, (55, 80))

  area_slider_text_one = font.render("Enter the area of the square meters", True, BLACK)
  screen.blit(area_slider_text_one, (20, 175))
  
  area_slider_text_two = font.render("crop in square meters", True, BLACK)
  screen.blit(area_slider_text_two, (55, 190))
  
  time = (slider_list[0].get_value())
  area = (slider_list[1].get_value())

  time_period_text = temp_font.render(str(time) + " days", True, BLACK)
  screen.blit(time_period_text, (330, 105))

  area_sqm_text = temp_font.render(str(area) + 
" m²", True, BLACK)
  screen.blit(area_sqm_text, (330, 215))

  res = waterConsumed(3, iniCoefficients[index], midCoefficients[index], lateCoefficients[index], iniDuration[index], midDuration[index], lateDuration[index], area, time)
  res_text = temp_font.render("Water consumed: " + str(round(res, 2)) + " liters", True, BLACK)
  screen.blit(res_text, (45, 260))

  return res

def draw_buttons():
  title_text = title_font.render("Choose a crop", True, BLACK)
  screen.blit(title_text, (260, 10))
  
  if (hover_box):
    py.draw.rect(screen, (110, 110, 110), (140, 125, 125, 65))
  else:
    py.draw.rect(screen, (180, 180, 180), (140, 125, 125, 65))

  if (hover_box2): 
    py.draw.rect(screen, (110, 110, 110), (340, 125, 125, 65))
  else: 
    py.draw.rect(screen, (180, 180, 180), (340, 125, 125, 65))

  if (hover_box3):
    py.draw.rect(screen, (110, 110, 110), (540, 125, 125, 65))
  else:
    py.draw.rect(screen, (180, 180, 180), (540, 125, 125, 65))

  if (hover_box4):
    py.draw.rect(screen, (110, 110, 110), (240, 200, 125, 65))
  else:
    py.draw.rect(screen, (180, 180, 180), (240, 200, 125, 65))
    
  if (hover_box5):
    py.draw.rect(screen, (110, 110, 110), (440, 200, 125, 65))
  else:
    py.draw.rect(screen, (180, 180, 180), (440, 200, 125, 65))
    
  potato_text = crop_font.render("Potato", True, BLACK)
  screen.blit(potato_text,(box.x-7, box.y+18))
  potato.draw()

  radish_text = crop_font.render("Radish", True, BLACK)
  screen.blit(radish_text, (box2.x-3, box2.y+18))
  radish.draw()

  lettuce_text = crop_font.render("Lettuce", True, BLACK)
  screen.blit(lettuce_text, (box3.x-13, box3.y+18))
  lettuce.draw()

  turnip_text = crop_font.render("Turnip", True, BLACK)
  screen.blit(turnip_text, (box4.x-5, box4.y+18))
  turnips.draw()

  alfalfa_text = crop_font.render("Alfalfa", True, BLACK)
  screen.blit(alfalfa_text, (box5.x-14, box5.y+18))
  alfalfa.draw()

box = py.Rect(170, 125, 125, 65)
box2 = py.Rect(370, 125, 125, 65)
box3 = py.Rect(570, 125, 125, 65)
box4 = py.Rect(270, 200, 125, 65)
box5 = py.Rect(470, 200, 125, 65)
leave = py.Rect(40, 290, 100, 50)
update = py.Rect(200, 290, 100, 50)

hover_box = False
hover_box2 = False
hover_box3 = False
hover_box4 = False
hover_box5 = False
leave_box = False
update_box = False
draw_graph = False

run = True
draw_calc = True
run_calc = False
crop_index = 0

def data(potato, radish, lettuce, turnip, alfalfa):
  # creating the dataset
  data = {'Potato': potato, 'Radish': radish, 'Lettuce': lettuce, 'Turnip': turnip, 'Alfalfa': alfalfa}
  courses = list(data.keys())
  values = list(data.values())
  
  fig = pylab.figure(figsize=(4.5, 4.0), 
     dpi=70,       
  )
  ax = fig.gca()
  ax.bar(courses, values, color ='maroon', 
        width = 0.6)
  ax.set_xlabel("Crop")
  ax.set_ylabel("Water Consumption (liters)")
  ax.set_title("Water Consumption of Crops")

  fig.subplots_adjust(left=0.2)
  
  canvas = agg.FigureCanvasAgg(fig)
  canvas.draw()
  renderer = canvas.get_renderer()
  raw_data = renderer.tostring_rgb()

  win = py.display.get_surface()
  size = canvas.get_width_height()

  surf = py.image.fromstring(raw_data, size, "RGB")
  win.blit(surf, (450, 60))
  py.display.flip()

potato_water = input_crops(0)
radish_water = input_crops(1)
lettuce_water = input_crops(2)
turnip_water = input_crops(3)
alfalfa_water = input_crops(4)

while run:
  for event in py.event.get():
    print(event)
    if event.type == py.QUIT:
      run = False
    if event.type == py.KEYDOWN:
      print("Key pressed")
    if event.type == py.MOUSEBUTTONDOWN and event.button == 1 and not run_calc:
      x, y = event.pos
      if (box.collidepoint(x, y)):
        screen.fill(GREEN)
        print("Box 1 clicked")
        crop_index = 0
        run_calc = True
      elif (box2.collidepoint(x, y)):
        screen.fill(GREEN)
        print("Box 2 clicked")
        crop_index = 1
        run_calc = True
      elif (box3.collidepoint(x, y)):
        screen.fill(GREEN)
        print("Box 3 clicked")
        crop_index = 2
        run_calc = True
      elif (box4.collidepoint(x, y)):
        screen.fill(GREEN)
        print("Box 4 clicked")
        crop_index = 3
        run_calc = True
      elif (box5.collidepoint(x, y)):
        screen.fill(GREEN)
        print("Box 5 clicked")
        crop_index = 4
        run_calc = True
        
    if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
      x, y = event.pos
      if (leave.collidepoint(x, y)):
        print("Leave button clicked")
        crop_index = 0
        run_calc = False   
        draw_graph = False
      if (update.collidepoint(x, y)):
        print("Update button clicked")
        potato_water = input_crops(0)
        radish_water = input_crops(1)
        lettuce_water = input_crops(2)
        turnip_water = input_crops(3)
        alfalfa_water = input_crops(4)
        draw_graph = False
        
  #BUTTON HOVER BELOW
  a,b = py.mouse.get_pos() #get pos of mouse
  mouse = py.mouse.get_pressed()
  
  if box.x <= a <= box.x + 100 and box.y <= b <= box.y + 50:
    hover_box = True
  else:
    hover_box = False
    
  if box2.x <= a <= box2.x + 100 and box2.y <= b <= box2.y + 50:
    hover_box2 = True
  else:
    hover_box2 = False
    
  if box3.x <= a <= box3.x + 100 and box3.y <= b <= box3.y + 50:
    hover_box3 = True
  else:
    hover_box3 = False
    
  if box4.x <= a <= box4.x + 100 and box4.y <= b <= box4.y + 50:
    hover_box4 = True
  else:
    hover_box4 = False
    
  if box5.x <= a <= box5.x + 100 and box5.y <= b <= box5.y + 50:
    hover_box5 = True
  else:
    hover_box5 = False

  if leave.x <= a <= leave.x + 100 and leave.y <= b <= leave.y + 50:
    leave_box = True
  else:
    leave_box = False

  if update.x <= a <= update.x + 100 and update.y <= b <= update.y + 50:
    update_box = True
  else:
    update_box = False

  if run_calc:
    screen.fill(GREEN, (0, 0, 450, 400))
    input_crops(crop_index)
    if not draw_graph:
      data(potato_water, radish_water, lettuce_water, turnip_water, alfalfa_water)
      draw_graph = True
    for slider in slider_list:
      if slider.container_rect.collidepoint(a, b) and mouse[0]:
        slider.move_slider((a, b))
      slider.render()
    py.display.update(py.Rect(0, 0, 450, 400))
  else:
    screen.fill(GREEN)
    draw_buttons()
    
  clock.tick(240)
  
  if not run_calc:
    py.display.update()
    
py.quit()
