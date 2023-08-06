

class Termux:
    def __init__(self):
        pass

    @staticmethod
    def execute(command: str) -> str:
        import subprocess

        return subprocess.check_output(command, shell=True)

    @staticmethod
    def buttery_check():
        result = Termux.execute("termux-buttery-status")
        result = str(result)
        result = result.split('"percentage": ')[1]
        result = result.split(',')[0]
        return int(result)
