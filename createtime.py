def createtime(audio):
    import time
    import os
    ctime = os.stat(audio).st_ctime
    file_create_time = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(ctime))
    #print("{0} 创建时间是: {1}".format('audio',file_create_time))
    return file_create_time