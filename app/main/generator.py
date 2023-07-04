import subprocess

class Generator():

    def index_generator(self):
        index_view_script = ['app/templates/index']
        with open('app/templates/index.html', 'w') as index_view:
            subprocess.run(index_view_script, stdout=index_view)

    def integer_input_generator(self, integer, count):
        with open("app/templates/integer_input.html", "w") as integer_input_view:
            subprocess.run(['bash', \
                './app/templates/./integer_input', \
                str(integer), str(count)], stdout=integer_input_view)

    def uptime_generator(self):
        with open("app/templates/uptime.html", "w") as uptime_view:
            subprocess.run(['bash', './app/templates/./uptime'], \
                stdout=uptime_view)

    def disk_space_generator(self):
        with open("app/templates/disk_space.html", "w") as disk_space_view:
            subprocess.run(['bash', './app/templates/./disk_space'], \
                stdout=disk_space_view)

    def home_space_generator(self):
        with open("app/templates/home_space.html", "w") as home_space_view:
            subprocess.run(['bash', './app/templates/./home_space'], \
                stdout=home_space_view)
