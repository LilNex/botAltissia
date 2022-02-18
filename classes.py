
from selenium.webdriver.remote.webelement import *
from selenium import *
from typing import List
vector:List[float] = list()



class Theme:
  listCards=[]
  def __init__(self, name:str, childs:WebElement):
    self.name = name
    self.childs = childs


class cardTheme:
  def __init__(self, name, childs:WebElement):
    self.name = name
    self.childs = childs
  def click(self):
    self.childs.click()

def elementHasClass(element, active):
    return element.getAttribute("class").contains(active)
