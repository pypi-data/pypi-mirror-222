"""Module to provide access to and control over push buttons.
"""
from systypes import ErrorCode
__author__ = "Oliver Maye"
__version__ = "0.1"
__all__ = ["Button"]

from pymitter import EventEmitter
from gpio import GPIO
import logging
from module import Module

class Button( Module, EventEmitter ):
    """Generic push button driver class.
    """
    
    LABEL_DEFAULT = "Button"
    _POLL_TIMEOUT = 1
    _DEBOUNCE_MS  = 2000
    
    
    def __init__(self):
        """Initialize the instance with defaults.
        """
        self.gpio = None
        self.label = Button.LABEL_DEFAULT
        EventEmitter.__init__( self )

    def _handleInterrupt(self):
        self.emit( self.label )
        logging.debug('Button <%s> emitted event.', self.label)
        return None
        
    #
    # Module API
    #

    @classmethod
    def Params_init(cls, paramDict):
        """Initializes configuration parameters with defaults.
        
        The following settings are supported:
        
        =============================    =====================================================================================================
        Key name                         Value type, meaning and default
        =============================    =====================================================================================================
        Button.label                     ``str``; A descriptive string label; :attr:`LABEL_DEFAULT`.
        All Button.gpio.* settings as documented at :meth:`.GPIO.Params_init`.
        ======================================================================================================================================
        
        Also see: :meth:`.Module.Params_init`, :meth:`.GPIO.Params_init`.
        """

        if not ("Button.label" in paramDict):
            paramDict["Button.label"] = Button.LABEL_DEFAULT
        paramDict["Button.gpio.direction"] = GPIO.DIRECTION_IN
        if not ("Button.gpio.bounce" in paramDict):
            paramDict["Button.gpio.bounce"] = Button._DEBOUNCE_MS
        gpioParams = {}
        GPIO.Params_init( gpioParams )
        for key, value in gpioParams.items():
            bkey = "Button." + key
            if not( bkey in paramDict):
                paramDict[bkey] = value
        return None

    def open(self, paramDict):
        ret = ErrorCode.errOk
        if not (self.gpio is None):
            ret = ErrorCode.errResourceConflict
        else:
            defaults = {}
            Button.Params_init(defaults)
            self.label = paramDict.get( "Button.label", defaults["Button.label"] )
            paramDict["Button.gpio.direction"] = defaults["Button.gpio.direction"]
            if not ("Button.gpio.bounce" in paramDict):
                paramDict["Button.gpio.bounce"] = defaults["Button.gpio.bounce"]
            self.gpio = GPIO()
            ret = self.gpio.open(paramDict)
            if (ret == ErrorCode.errOk):
                ret = self.gpio.registerInterruptHandler( \
                                GPIO.EVENT_DEFAULT, None, \
                                self._handleInterrupt )
        logging.debug('Button <%s> created, pin:%s, trigger:%d, returns: %s.',
                      self.label,
                      paramDict["Button.gpio.pinDesignator"],
                      paramDict["Button.gpio.trigger"], ret)
        return ret
            
    def close(self):
        ret = ErrorCode.errOk
        if not (self.gpio is None):
            ret = self.gpio.registerInterruptHandler( None, None, None )
            ret = self.gpio.close()
        logging.debug('Button <%s> closed, returns %s.',
                      self.label, ret)
        return ret

    def setRunLevel(self, level):
        if (self.gpio is None):
            ret = ErrorCode.errResourceConflict
        else:
            ret = self.gpio.setRunLevel(level)
        return ret
    
    #
    # Specific Button API
    #

    def get(self):
        value = self.gpio.get()
        logging.debug('Reading Button <%s> returns %s.', self.label, value)
        return value
    
    def setLabel(self, label):
        ret = ErrorCode.errOk
        logging.debug('Renaming Button <%s> into <%s>.', self.label, label)
        self.label = label
        return ret
        