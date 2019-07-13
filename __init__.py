import config as global_settings

Class EnvConfig:

	def __init__(self):
		print(global_settings)
		for setting in dir(global_settings):
			print setting

if __name__ == '__main__':
	EnvConfig()
		