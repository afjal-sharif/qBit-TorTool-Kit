try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "b8982d0aceaaff4f23f49adac886c913"
        API_ID = "1389234"
        BOT_TOKEN = "1578011928:AAFIIw-pXSn1RyW8g-KD2RqfQXCfmvr3d5g"
        BASE_URL_OF_BOT = "https://rhqbit.herokuapp.com"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [1304152521,-1001319419576,-1001352599350]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 25

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1800000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DB_URI = "postgres://hrviabdqevjdzt:d71616b0344d7215814fcb4293d1fb3cc80220b3b15afdd48cd4106e75c8b4ab@ec2-3-215-207-12.compute-1.amazonaws.com:5432/d8d6i19hu4te7c"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = ""

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = True

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = True
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = "leech"

        # Max size of the videos in playlist allowed
        MAX_YTPLAYLIST_SIZE = 200
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 60

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [30,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





