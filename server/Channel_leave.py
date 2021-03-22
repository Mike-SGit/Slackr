from Channels_list import channels_list

def Channel_leave (token, channel_id):
   if is_channel (token, channel_id):
      if in_channel (token, channel_id):
         #do something
         pass
      else:
         return ValueError("User not in channel")
   else:
      return ValueError("Channel is invalid")

def in_channel (token, channel_id):
   if channel_id in channels_list(token):
      return True
   else:
      return False
    
def is_channel (token, channel_id):
   pass