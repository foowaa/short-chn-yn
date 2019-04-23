from prettyprinter import pprint 
import short_chn_yon as s
if __name__=="__main__":
    y1=s.yn()
    y1.initialize()
    s = "嗯是"
    result = y1.y_n(s)
    pprint(result)