from uiautomator import device as d
from uiautomator import Device
from time import sleep
import os
im = ['images(8).jpeg']
def crowdsource():
  print("Inside Call Method.")
  #image_capture = d(className='android.widget.TextView',
                   #  packageName='com.google.android.apps.village.boond',
                       # resourceId='com.google.android.apps.village.boond:id/tasktype_name',
                       # text = 'Image Capture').click()
#upload
  #sleep(1)
  upload =  d(className='android.widget.ImageButton',
                     packageName='com.google.android.apps.village.boond',
                        resourceId='com.google.android.apps.village.boond:id/image_capture_button').click()
#uload a photo
  #sleep(1)
  photo =  d(className='android.widget.TextView',
                     packageName='com.google.android.apps.village.boond',
                     text = 'Upload a photo'
                       ).click()
  #select file 
  #sleep(1)
  select =  d(className='android.widget.ImageButton',
                     packageName='com.android.documentsui',
                     
  ).click()
  #go to images

  gotoim =  d(className='android.widget.TextView',
                     packageName='com.android.documentsui',
                        resourceId='android:id/title',
                        text = 'Images').click()
 #goto selected file
  selectedfile = d(className='android.widget.TextView',
                     packageName='com.android.documentsui',
                        resourceId='android:id/title',
                        text = 'Download').click()

#open 
  selectedfile = d(className='android.widget.TextView',
                     packageName='com.android.documentsui',
                        resourceId='com.android.documentsui:id/date',
                        text = 'Oct 27' ).click()

  #write
  write = d(className='android.widget.EditText',
                     packageName='com.google.android.apps.village.boond',
                        resourceId='com.google.android.apps.village.boond:id/edit_text_input' , 
                        text =' Label key elements using commas, e.g., plant, vine, jasmine ').set_text("anime")
 #submit
  submit = d(className='android.widget.Button',
                     packageName='com.google.android.apps.village.boond',
                        resourceId='com.google.android.apps.village.boond:id/submit_button',
                        text = 'Upload' ).click()
#Call The main Method
n = 2
for i in range(n):
    crowdsource()

print("Your test is completed...")

