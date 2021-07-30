import os
basedir = os.path.abspath(os.path.dirname(__file__))

PROJECT_NAME = "klarna-assignement"
DEBUG = False
TESTING = False
CSRF_ENABLED = True

ERROR_404_HELP = False
DEFAULT_CHANNEL_NAME= "Klarna"

LOG_CONFIG = {
   "version":1,
   "handlers":{
      "file":{
         "level":"INFO",
         "class":"logging.handlers.RotatingFileHandler",
         "filename":"/app/logs""+""/%s.log""% PROJECT_NAME",
         "formatter":"customFormatter",
         "maxBytes":1024 * 1024 * 100,
         "backupCount":10
      },
      "console":{
         "level":"INFO",
         "class":"logging.StreamHandler",
         "formatter":"customFormatter"
      }
   },
   "loggers":{
      "":{
         "handlers":[
            "file"
         ],
         "level":"INFO"
      }
   },
   "formatters":{
      "customFormatter":{
         "format":"(""@timestamp %(asctime)s || @filename %(name)s || @ loglevel %(levelname)s ||""@process %(process)d || @thread %(thread)d || ""@path %(pathname)s || @line %(lineno)d || ""@environment %(environment)s || @project %(project)s ||""@module %(name)s || @message %(message)s ||"")"
      }
   },
   "disable_existing_loggers":False
}