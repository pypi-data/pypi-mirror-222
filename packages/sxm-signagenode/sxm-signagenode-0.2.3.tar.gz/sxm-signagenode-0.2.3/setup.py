import setuptools

_requires = [
    'setuptools-scm',
    'ebs-signagenode>=3.0.8',
    'ebs-linuxnode-modapi>=3.1.0',
    'ebs-linuxnode-exim>=2.0.0',
    'sw-faces-connector',
    'sw-faces',
]

setuptools.setup(
    name='sxm-signagenode',
    url='https://github.com/starxmedia/sxm-signagenode',

    author='Chintalagiri Shashank',
    author_email='shashank.chintalagiri@gmail.com',

    description='Generic StarXMedia Signage Node',
    long_description='',

    packages=setuptools.find_packages(),
    package_dir={'sxm-signagenode': 'sxm'},
    package_data={'sxm-signagenode': ['default/config.ini',
                                      'default/background.png']},

    install_requires=_requires,

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    entry_points={
        'console_scripts': [
            'sxm-signagenode = sxm.runnode:run_node'
        ]
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
    ],
)
