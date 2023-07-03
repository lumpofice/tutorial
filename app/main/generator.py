import subprocess

class Generator():

    def index_generator(self):
        index_view = ['app/templates/index']
        with open('app/templates/index.html', 'w') as outfile:
            subprocess.run(index_view, stdout=outfile)

    def integer_input_generator(self, integer):
        with open("app/templates/integer_input.html", "w") as integer_input_view:
            subprocess.run(['bash', \
                './app/templates/./integer_input', \
                str(integer)], stdout=integer_input_view)
