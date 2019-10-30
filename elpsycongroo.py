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
#upload a photo
  #sleep(1)
  photo =  d(className='android.widget.TextView',
                     packageName='com.google.android.apps.village.boond',
                     text = 'Take a photo'
                       ).click()
  #click a photo 
  #sleep(1)
  click =  d(className='android.widget.ImageView',
                     packageName='com.android.camera',
                        resourceId='com.android.camera:id/camera_shutter_middle_button'
                        ).click()

 #tap 'tick'
  tick =  d(className='android.view.View',
                     packageName='com.android.camera',
                        resourceId='com.android.camera:id/save_btn').click()
 #goto selected file
 # selectedfile = d(className='android.widget.TextView',
               #      packageName='com.android.documentsui',
                  #      resourceId='android:id/title',
              #          text = 'Download').click()

#open 
 # selectedfile = d(className='android.widget.TextView',
                 #    packageName='com.android.documentsui',
                     #   resourceId='com.android.documentsui:id/date',
                    #    text = 'Oct 27' ).click()

  #write
  write = d(className='android.widget.EditText',
                     packageName='com.google.android.apps.village.boond',
                        resourceId='com.google.android.apps.village.boond:id/edit_text_input' , 
                        text =' Label key elements using commas, e.g., plant, vine, jasmine ').set_text("images")
 #submit
  sleep(3)
  submit = d(className='android.widget.Button',
                     packageName='com.google.android.apps.village.boond',
                        resourceId='com.google.android.apps.village.boond:id/submit_button',
                        text = 'Upload' ).click()
#Call The main Method
n = 1
for i in range(n):
    crowdsource()

print("Your test is completed...")

