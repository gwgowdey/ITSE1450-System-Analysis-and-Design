# Reference: https://wiki.edgertronic.com/wiki/SDK
# Video angles diagram: https://github.com/gwgowdey/Tarrant-County-College-Baseball/tree/main/Images/14.jpg

# POE splitter and ethernet cable are connected to the Edgertronic cameras, which are in protective enclosures. 
# Cameras are connected via ethernet to a switch. User connects their computer to the switch.

# User interface captures each angle with a single trigger. 240 frames per second and each slow motion clip lasts 15 seconds.
# Trigger button is pressed once front foot of pitcher lands.
# Time stamps from each trigger are matched to TrackMan or Hawk-Eye CSV time stamps and the clips are merged in the video player.

# Not functional - just a proof of concept and what I was able to find on the Edgertronic website.

# [multicast-trigger]
# address = 224.1.1.1
# port = 600
# payload = 0x05AA9544

import sys, os, logging, json, ConfigParser, socket, hcamapi
sys.path.append('/home/root/ss-web')
from camconstants import *

class AppExt(object):

    pkg_name = "Multicast network trigger "
    pkg_version = "v1.0"

    mt_config = None

# =============================================================================
# Package and URL registration logic
# =============================================================================
    def __init__(self, _app, _cam, _ci, register_url_callback):
        """
        Register new URLs with camera's webserver.
        """
        urls = [
            ( '/trigger2', self.trigger2, "Sends a multicast network trigger packet to trigger all the cameras on the same local network, including trigging this camera." ),
            ( '/get_multicast_configuration', self.get_multicast_configuration, "Returns a JSON encoded dictionary of the camera's /etc/multicast-trigger.conf file contents." ),
            ]

        register_url_callback(self.pkg_name, self.pkg_version, urls)
        self.mt_config = self._mt_read_multicast_config_file('/etc/multicast-trigger.conf')
        logging.debug("Multicast trigger URL added: %s" % repr(self.mt_config))

# =============================================================================
# Multicast trigger helper methods
# =============================================================================
    def _mt_read_multicast_config_file(self, fn):
        """
        Returns dictionary with multicast trigger configuration information read from file fn.
        """
        if not os.path.exists(fn):
            logging.error("Missing file: %s" % fn)
            return None

        config = {}
        try:
            config_parser = ConfigParser.SafeConfigParser()
            config_parser.read(fn)
            c = config_parser.items('multicast-trigger')
            for (key, value) in c:
                if key == 'address':
                    config[key] = value
                elif key in ('port', 'payload'):
                    config[key] = int(value, 0)
        except Exception, e:
            logging.error("Bad file format: %s" % fn)
            logging.error("Ignoring multicast-trigger parameters due to exception - %s" % str(e))
            return None
        return config

# =============================================================================
# Exposed URLs - URL matches method name
# =============================================================================
    def trigger2(self):
        """
        Sends a multicast network packet to trigger all cameras on the same local network.
        """
        if self.mt_config == None:
            logging.error("Missing file: %s" % fn)
            ret = CAMAPI_STATUS_INVALID_PARAMETER
        else:
            try:
                logging.debug("Triggering cameras by sending multicast packet: address %s port %d with payload 0x%x" % (self.mt_config['address'], self.mt_config['port'], self.mt_config['payload']))
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
                data=""
                v = self.mt_config['payload']
                for i in range(4):
                    data = chr(v & 0xFF) + data
                    v = v >> 8
                sock.sendto(data, (self.mt_config['address'], self.mt_config['port']))
                ret = CAMAPI_STATUS_OKAY
            except Exception, e:
                logging.error("Multi-camera trigger error due to exception - %s" % str(e))
                ret = CAMAPI_STATUS_INVALID_PARAMETER
        return json.dumps(ret)

    def get_multicast_configuration(self):
        """
        Returns a JSON encoded dictionary of the camera's /etc/multicast-trigger.conf file.
        """
        logging.debug("Returning multicast trigger configuration: %s" % repr(self.mt_config))
        return json.dumps(self.mt_config)