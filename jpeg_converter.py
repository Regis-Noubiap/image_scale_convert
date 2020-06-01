#!/usr/bin/env python3 

import os 
from PIL import Image 
import subprocess 

#subprocess.Popen(["cd"," ","/opt/icons/"])
#subprocess.Popen(["rm","*"])
user = os.environ.get('USER')
for file in os.listdir('/home/'+user+'/image_scale_convert/images'):
  if not file.startswith('.'):  
    f,e = os.path.splitext(file) 
    new_file = f + ".jpg"
    im = Image.open('/home/'+user+'/image_scale_convert/images/'+file).convert('RGB')
    new_im = im.rotate(90).resize((128,128)) 
    new_im.save('/opt/icons/'+new_file) 


