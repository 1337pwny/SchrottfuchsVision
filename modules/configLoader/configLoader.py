import yaml
class ConfigLoader:
    def __init__(self):
        configPath = "config.yml"
        with open(configPath, "r") as stream:
            try:
                config = yaml.safe_load(stream)
                self.modules = config['Modules']
                hardwareOpts = config['HardwareOptions']

                self.distanceDev = hardwareOpts['distanceDev']
                self.laneCam = hardwareOpts['laneCam']
                self.signCam = hardwareOpts['signCam']
                self.obdDev = hardwareOpts['obdDev']

            except yaml.YAMLError as exc:
                print(exc)