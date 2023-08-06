

class Convertors:
    """
    Класс для работы с конвертерами различных форматов файлов
    """

    def __init__(self, input_file):
        self.input_file = input_file

    def webp2png(self, output_file: str):
        """
        Функция для конвертации из формата .webp в формат .png
        :param output_file: str
        :return:
        """
        from PIL import Image

        # Открываем исходный файл в формате .webp
        with Image.open(self.input_file) as im:
            # Сохраняем изображение в формате .png
            im.save(output_file, 'PNG')

    def webp2jpeg(self, output_file: str):
        """
        Функция для конвертации из формата .webp в формат .jpeg

        :param output_file:
        :return:
        """
        from PIL import Image

        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат JPEG
            im.convert('RGB').save(output_file, 'JPEG')

    def png2jpeg(self, output_file: str):
        """
                Функция для конвертации из формата .png в формат .jpeg

                :param output_file:
                :return:
                """
        from PIL import Image

        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат JPEG
            im.convert('RGB').save(output_file, 'JPEG')

    def jpeg2png(self, output_file: str):
        """
               Функция для конвертации из формата .jpeg в формат .png
               :param output_file: str
               :return:
               """
        from PIL import Image

        # Открываем исходный файл в формате .webp
        with Image.open(self.input_file) as im:
            # Сохраняем изображение в формате .png
            im.save(output_file, 'PNG')

    def png2ico(self, output_file: str):
        """
       Функция для конвертации из формата .png в формат .ico
       :param output_file: str
       :return:
       """
        from PIL import Image

        # Открываем изображение в формате PNG
        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат ICO
            im.save(output_file, format='ICO')

    def jpeg2ico(self, output_file: str):
        """
               Функция для конвертации из формата .jpeg в формат .ico
               :param output_file: str
               :return:
               """
        from PIL import Image

        # Открываем изображение в формате PNG
        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат ICO
            im.save(output_file, format='ICO')

