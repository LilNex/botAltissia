
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

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class lesson:
    activities = list()
    def __init__(self,id:str):
        self.id = id
        self.activities = list()

    # self.childs = childs
class mission:
    lessons:List[lesson]= list()
    def __init__(self, id:str):
        self.id = id
        self.lessons = list()



def elementHasClass(element, active):
    return element.getAttribute("class").contains(active)
