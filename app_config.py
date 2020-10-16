import os
### YOUR APP CONFIGS ###
# this is required for encrypting flask session cookies:
SECRET_KEY = os.environ.get('SAMPLE_APP_ENCRYPTION_KEY','enter-a-great-key') # should be loaded from a key vault or other secure location.
# write to filesystem:
SESSION_TYPE = 'filesystem'