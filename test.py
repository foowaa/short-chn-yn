from prettyprinter import pprint 
import short_chn_yn as yn
if __name__=="__main__":
    #实例化对象
    y1=yn.yn()
    s = "嗯是"
    #输入
    result = y1.y_n(s)
    pprint(result)