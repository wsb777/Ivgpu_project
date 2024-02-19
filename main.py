# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
import os
import shutil
import sys
import lxml

sys.stdout.reconfigure(encoding="utf-8")
 
directory = 'backup-moodle2-course-4505-vedenie_v_pd-20240110-1220-nu\moodle_backup.xml'

f = open(directory, 'r', encoding='utf-8')

file=f.read()

soup = BeautifulSoup(file, 'lxml')
courseName = soup.find('original_course_fullname')
courseNameFilter = []
for data in courseName:
    courseNameFilter=data.get_text()
    os.mkdir(courseNameFilter)
    os.chdir(courseNameFilter)

activityContent =soup.find_all('activity')
sectionNameFilter = []
for section in soup.find_all('section'):
    for title in section.findAll('title'):
        sectionNameFilter = title.get_text()
        os.mkdir(sectionNameFilter)
# sectionId=[]

# for section in soup.find_all('section'):
#     for sectionId in section.findAll('sectionid'):
#         sectionId = sectionId.get_text()


# for activity in soup.find_all('activity'):
#     for direct in activity.findAll('directory'):
#         directoryFile = direct.get_text()
#         print(directoryFile)
           





# exec('{} = sectionNameFilter'.format(','.join([f'var_{i}' for i in range(len(sectionNameFilter))])))
# print(var_0, var_1, var_2, var_3, var_4)