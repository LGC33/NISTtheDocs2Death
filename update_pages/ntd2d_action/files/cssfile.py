import textwrap

from .pagesfile import PagesFile

class CSSFile(PagesFile):
    def __init__(self, variant, variants_url):
        self.variant = variant
        self.variants_url = variants_url
        super().__init__(repo=variant.repo)

    @property
    def path(self):
        return (self.repo.working_dir / "html" / self.variant.name
                / "_static" / "ntd2d.css")

    def get_contents(self):
        with self.path.open(mode='r') as file:
            contents = file.read()

        contents += f"""
        
        .ntd2d_{self.variant} li a {{
          font-style: bold
        }}
        """

        return contents
