import time
import xbmc
import xbmcaddon
import os
import xbmcgui

TITLE = 'Myo'

# add module's resources/lib dir to the system search path
my_addon = xbmcaddon.Addon()
addon_dir = xbmc.translatePath( my_addon.getAddonInfo('path') )
libdir = os.path.join( addon_dir, 'resources', 'lib' )
sys.path.append(libdir )

import myo
print '############################################'
xbmcgui.Dialog().notification(TITLE,'Module loading')

'''	if __name__ == '__main__':
	    monitor = xbmc.Monitor()
	 
	    while not monitor.waitForAbort(10):
	        xbmc.log("hello addon! %s" % time.time(), level=xbmc.LOGDEBUG)
''' 

myo.init(libdir)
xbmcgui.Dialog().notification(TITLE,'Starting 2')

class Listener(myo.DeviceListener):
    # return False from any method to stop the Hub
    def on_connect(self, myo, timestamp):
        myo.vibrate('short')
        myo.request_rssi()

    def on_rssi(self, myo, timestamp, rssi):
		pass

    def on_event(self, event):
        pass

    def on_event_finished(self, event):
        pass

    def on_pair(self, myo, timestamp):
        pass

    def on_disconnect(self, myo, timestamp):
        pass

    def on_pose(self, myo, timestamp, pose):
    	xbmcgui.Dialog().notification(TITLE,pose.name)
        pass

    def on_orientation_data(self, myo, timestamp, orientation):
#        print_('orientation')
        pass

    def on_accelerometor_data(self, myo, timestamp, acceleration):
#        print_('accelometer')
        pass

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
#        print_('gyro')
        pass

    def on_unlock(self, myo, timestamp):
        xbmcgui.Dialog().notification(TITLE,'unlocked')

    def on_lock(self, myo, timestamp):
        xbmcgui.Dialog().notification(TITLE,'locked')

    def on_sync(self, myo, timestamp):
        xbmcgui.Dialog().notification(TITLE,'Armband synced')

    def on_unsync(self, myo, timestamp):
        xbmcgui.Dialog().notification(TITLE,'Armband un-synced')
xbmcgui.Dialog().notification(TITLE,'3')

def main():
    hub = myo.Hub()
    hub.set_locking_policy(myo.locking_policy.none)
    hub.run(1000, Listener())
    try:
        while hub.running:
            myo.time.sleep(0.2)
    except KeyboardInterrupt:
        print_("Quitting ...")
        hub.stop(True)

if __name__ == '__main__':
    main()