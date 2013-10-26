from AppKit import *
from Foundation import *
import objc

MVMailBundle = objc.lookUpClass('MVMailBundle')
class VisualHeadersPlugin(MVMailBundle):
    @classmethod
    def initialize(cls):
        MVMailBundle.registerBundle()
        NSLog("VisualHeadersPlugin registered with Mail")
