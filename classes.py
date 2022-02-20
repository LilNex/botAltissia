
from selenium.webdriver.remote.webelement import *
from selenium import *
from typing import List




class cardTheme:
  def __init__(self, name, childs:WebElement):
    self.name = name
    self.childs = childs
  def click(self):
    self.childs.click()
class Theme:
  # listCards=[]
  listCards:List[cardTheme] = list()

  def __init__(self, name:str, childs:WebElement):
    self.name = name
    self.childs = childs

  def getCountExCards(self):
    return len(self.childs.find_elements_by_class_name('mission-lesson-item'))


class question:
  def __init__(self, num:int):
    self.num = num
    self.reponses = []



def elementHasClass(element, active):
    return element.getAttribute("class").contains(active)
