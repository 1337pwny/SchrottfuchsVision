import yaml
class ConfigLoader:
    def __init__(self):
        configPath = "config.yml"
        with open(configPath, "r") as stream:
            try:
                config = yaml.safe_load(stream)
                self.modules = config['Modules']
                hardwareOpts = config['HardwareOptions']
                thresholds = config['Thresholds']

                self.distanceDev = hardwareOpts['distanceDev']
                self.laneCam = hardwareOpts['laneCam']
                self.signCam = hardwareOpts['signCam']
                self.obdDev = hardwareOpts['obdDev']

                self.distanceTresholdSlow = thresholds['distanceTresholdSlow']
                self.distanceThresholdFast = thresholds['distanceThresholdFast']
                self.distanceSlowThreshold = thresholds['distanceSlowThreshold']


            except yaml.YAMLError as exc:
                print(exc)