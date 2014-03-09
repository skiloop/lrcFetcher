#!/bin/python
import sys,urllib

# check if content has results
def hasResultsBaidu(content):
   return 1

# phase content from baidu results
def phaseBaiduContent(content):
   urls=[]
   if hasResultsBaidu(content)<1:
      return urls
   tag="down-lrc-btn"
   startIndex=content.find(tag);
   while startIndex>0:
      startIndex=startIndex+len(tag);
      tailIndex=content.find("href=",startIndex);
      if tailIndex<0:
         url=content[startIndex:]
      else:
         url=content[startIndex:tailIndex]
         
      # phase href
      url=url.split("'",4)
      url=url[3];
      # add new url
      urls.append(url);
      
      # find next tag
      startIndex=content.find(tag,startIndex);
   
   return urls;
      
   
# check input
inputLen=len(sys.argv)
if inputLen<2:
   print "Usage:"
   print sys.argv[0],"search_keys"
else:
   baiduBaseUrl="http://music.baidu.com/search/lrc?key="
   url=baiduBaseUrl+sys.argv[1]

   wp=urllib.urlopen(url);

   print"url:",url
   print "start downloading..."

   # download webpage
   content=wp.read()

   ## print content
   #print content

   #
   res=phaseBaiduContent(content);

   if len(res)>=1:
      for i in range(0,len(res)):
         res[i]=baiduBaseUrl+"#"+res[i]

   if len(res)>=1:
      for i in res:
         print i



