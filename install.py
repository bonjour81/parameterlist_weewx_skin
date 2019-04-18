# Installer for Parameterlist weewx skin
# Bonjour81  2019

from setup import ExtensionInstaller

def loader():
    return ExfoliationInstaller()

class ExfoliationInstaller(ExtensionInstaller):
    def __init__(self):
        super(ExfoliationInstaller, self).__init__(
            version="0.1",
            name='Parameterlist',
            description='A simple table to list $labels available in weewx',
            author="Bonjour81",
            config={
                'StdReport': {
                    'parameterlist': {
                        'skin':'parameterlist',
                        'HTML_ROOT':'parameterlist'
                    },
                }
            },
            files=[('skins/parameterlist',['skins/parameterlist/parameterlist.html.tmpl',
                                          'skins/parameterlist/parameterlist.css',
                                          'skins/parameterlist/skin.conf',
                                          ]
                   ),
                  ]
        )
