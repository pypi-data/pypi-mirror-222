from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = str(f.read())

setup(
    name='iluxaMod',
    version='2.9',  # Версия вашего пакета
    packages=['iluxaMod'],  # Автоматически найдет все пакеты в корневой директории
    install_requires=[  # Зависимости вашего пакета
        'geopy',
        'psycopg2-binary',
        'pyTelegramBotAPI',
        'requests',
        'pyfirmata',
        'Pillow',
        'pyzbar',
        'qrcode',
        'numpy',
        'opencv-python',
        'selenium'

    ],
    author='Illya Lazarev',
    author_email='lazarevillya031@gmail.com',
    description='Module for simplified work with libraries: TG, PostgreSQL, locations and more...',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://sbdt.pro',
    classifiers=[  # Классификаторы, чтобы помочь пользователям понять ваш пакет
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',

    ],

)
