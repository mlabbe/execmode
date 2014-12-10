
class Version:
    """
    ver is a tuple
    """
    def __init__( self, ver ):
        self.ver = ver

    def __str__(self):
        ver_str = str(self.ver[0])
        for marker in self.ver[1:]:
            ver_str = ver_str + (".%i" % int(marker))
        return ver_str

class UniqueInstance:
    """
    An object that serializes to a unique string for each program's execution.
    """
    
    def __init__( self, prog_name, version ):
        from socket import gethostname
        from datetime import datetime
        from uuid import uuid4

        self.prog_name = prog_name
        self.stamp = datetime.now()
        self.hostname = gethostname()
        self.version = version
        self.uuid = uuid4()

    def get_timestamp_filesystem(self):
        # compatible with alpha sort
        return self.stamp.strftime( "%Y%m%d-%H%M%S" )

    def get_timestamp_human(self):
        # human readable
        return self.stamp.strftime( '%b %d %I:%M%p')
        

    def __str__( self ):
        return "%s v%s %s on %s (%s)" % ( self.prog_name, \
                                     self.version, \
                                     self.hostname, \
                                     self.get_timestamp_human(),
                                     self.uuid )
