def modifytime(audio):
    import time
    import os
    mtime = os.stat(audio).st_mtime
    file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
    return file_modify_time
