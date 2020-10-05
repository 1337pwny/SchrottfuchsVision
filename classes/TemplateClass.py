class TemplateClass:
    def __init__(self, template, canny, r):
        self.template = template
        self.canny = canny
        (self.tH, self.tW) = self.template.shape[:2]
        self.r = r