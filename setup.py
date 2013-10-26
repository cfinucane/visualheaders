from distutils.core import setup
import py2app

plist = dict(NSPrincipalClass='VisualHeadersPlugin',
             SupportedPluginCompatibilityUUIDs=['0941BB9F-231F-452D-A26F-47A43863C991'])
setup(
    plugin = ['VisualHeadersPlugin.py'],
    options=dict(py2app=dict(extension='.mailbundle', plist=plist))
 )
