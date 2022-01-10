from distutils.core import setup
import setuptools
VERSION = "1.0.0" # BURAYI AKLINIZDA TUTUN (Değiştirebilirsiniz)
long_description = ""
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()
setup(
    name='yenidil',         # How you named your package folder (MyLib)
    packages=setuptools.find_packages(),
    # Start with a small number and increase it with every change you make
    version=VERSION,
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='python kodlarını türkçeye çeviren paket',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yasir Mohamed',                   # Adınızı soyadınız yazın
    author_email='yasireposta@gmail.com',      # E-posta adresiniz
    # Provide either the link to your github or to your website
    url='https://github.com/yasirmohamedfathi/yenidil.git',
    # I explain this later on
    download_url=f'https://github.com/yasirmohamedfathi/yenidil.git/archive/{VERSION}.tar.gz',
    # Keywords that define your package best
    keywords=['python', 'türkçe'],
    # install_requires=[], # Bağımlılıklar
    classifiers=[
    # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Development Status :: 3 - Alpha',
    # Define that your audience are developers
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    # Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ]
)
# Komut isteminden kullanılacaksa, main'e verilen yol
# entry_points={
#     # Komut isteminden çalıştırma
#     # örndeğin: ypackage
#     # Kullanım: 'ypackge = ypackage.ypackage:main
#     'console_scripts': [
#         'komut_ismi = dizin.dosya:main',
#     ]
# },