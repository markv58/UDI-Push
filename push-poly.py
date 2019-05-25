#!/usr/bin/env python3

import polyinterface
import sys
import time
import subprocess
import http.client
import urllib
import requests

LOGGER = polyinterface.LOGGER
          
ACTION = ['        ',
	  'On',
	  'Off',
	  'Light on',
	  'Light off',
	  'Open',
	  'Closed',
	  'Locked',
	  'Unlocked',
	  'Lock jammed',
	  'Motion detected',
	  'Water leak',
	  'Rang',
	  'At home',
	  'Away',
	  'Offline',
	  'Low battery',
	  'Armed',
	  'Disarmed',
	  'Triggered',
	  'Don''t forget!',
	  'WARNING',
	  'EMERGENCY',
	  'Heat warning',
	  'Cold warning',
	  'Reset'
         ] 

class Controller(polyinterface.Controller):
    def __init__(self, polyglot):
        super(Controller, self).__init__(polyglot)
        self.name = 'Push'
        self.api_key = 'none'
        self.user_key = 'none'
        self.d_read = False
        
    def start(self):
        self.removeNoticesAll()
        LOGGER.info('Started Push Nodeserver')
        self.check_params()
        self.setDriver('ST', 1)
        LOGGER.info('If you have just upgraded hit the Update Profile button and restart the Admin Console')
        
    def shortPoll(self):
        pass

    def longPoll(self):
        pass

    def query(self):
        for node in self.nodes:
            self.nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        pass
    
    def delete(self):
        LOGGER.info('Deleting the Push Nodeserver.')

    def stop(self):
        LOGGER.debug('NodeServer stopped.')

    def check_params(self):  # check for the keys and leave a message if they are not here.
        if 'api_key' in self.polyConfig['customParams']:
            self.api_key = self.polyConfig['customParams']['api_key']               
        if 'user_key' in self.polyConfig['customParams']:
            self.user_key = self.polyConfig['customParams']['user_key']
        if 'disclaimer_read' in self.polyConfig['customParams']:
            self.d_read = self.polyConfig['customParams']['disclaimer_read']
        
        _params = self.polyConfig['customParams']
        for key, val in _params.items():
            _key = key.lower()	
            if _key == 'api_key' or _key == 'user_key' or _key == 'disclaimer_read': # should parse out the keys, all others will be node
                pass 
            else:
                _val = key.lower()
                _cleanaddress = _val.replace(' ','')
                _address = _cleanaddress[0:12]
                _key = key[0:20]		
                self.addNode(thingnode(self, self.address, _address, _key))
		
        if self.api_key == 'none':
            self.addNotice('No api key, please enter your key.')                                                
        if self.user_key == 'none':
            self.addNotice('No user key, please enter your key.')
        if not self.d_read:
            self.addNotice('Please read the Disclaimer <a target="_blank" href="https://github.com/markv58/UDI-Push/blob/master/Disclaimer.md">here</a> to remove this notice.')

    def remove_notices_all(self,command):
        LOGGER.info('remove_notices_all:')
        # Remove all existing notices
        self.removeNoticesAll()

    def update_profile(self,command):
        LOGGER.info('update_profile:')
        st = self.poly.installprofile()
        return st

    id = 'controller'
    commands = {
        'UPDATE_PROFILE': update_profile,
        'REMOVE_NOTICES_ALL': remove_notices_all
    }

    drivers = [{'driver': 'ST', 'value': 0, 'uom': 2}]


    
class thingnode(polyinterface.Node):

    def __init__(self, controller, primary, address, name):
        super(thingnode, self).__init__(controller, primary, address, name)
        self.title = str(name)
        
    def start(self):
        pass

    def query(self):
        pass
    
    def send_pushover(self, command = None):
        _message = int(command.get('value'))
        try:
            LOGGER.info("Sending Pushover message %s %s", self.title, ACTION[_message])
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                    urllib.parse.urlencode({
                        "token": self.parent.api_key,
                        "user": self.parent.user_key,
                        "title": self.title,
                        "message": ACTION[_message],
                    }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
            conn.close()
        except Exception as inst:
            LOGGER.error("Error sending to pushover: " + str(inst))

    id = 'thingnodetype'

    commands = {
                'ACTIONS': send_pushover
                }
 
    
if __name__ == "__main__":
    try:
        polyglot = polyinterface.Interface('Push NodeServer')
        polyglot.start()
        control = Controller(polyglot)
        control.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
