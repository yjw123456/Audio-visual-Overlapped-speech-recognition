import os
mp4=open("mp4.scp","r").readlines()
mp3=open("wav.scp",'r').readlines()

for item in mp3:
  item = item.strip()
  path='/'+'/'.join(item.split('/')[:-1])+'/'
  index= item.split('/')[-1].split('.')[0]
  a=index+".mp3"
  avi=index+".avi"
  index = index.replace("SPH_","")
  mix = index+".mp4"
  for vmp4 in mp4:
    vmp4 = vmp4.strip()
    if index in vmp4:
       v=vmp4
       #print(index,v)
       break
  #print(v,avi)
  os.system("rm %s %s" %(path+avi,path+mix))
  os.system("ffmpeg -i %s -vcodec copy -an %s"%(v,path+avi))
  os.system("ffmpeg -i %s -i %s  -vcodec mpeg4 -acodec copy %s"%(path+avi,path+a,path+mix))
