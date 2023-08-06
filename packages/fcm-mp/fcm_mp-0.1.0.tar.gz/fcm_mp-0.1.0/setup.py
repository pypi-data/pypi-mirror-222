from setuptools import setup

setup(
    name='fcm_mp',
    version='0.1.0',
    description='Fuzzy Cognitive Map with Moore-Penrose inverse learning',
    long_description="The package implements a learning method based on the Moore-Penrose inverse for hybrid Fuzzy " +
                     "Cognitive Maps. In this hybrid model, the user can specify how the problem features interact " +
                     "or let the algorithm compute that matrix from the data using unsupervised learning. The " +
                     "supervised learning step focuses on computing the relationships between the last hidden state " +
                     "of the Fuzzy Cognitive Maps and the outputs. Therefore, the model is devoted to solving " +
                     "multi-output regression problems where problem features are connected in non-trivial ways.",
    url='https://github.com/gnapoles/fcm_mp',
    author='Gonzalo Nápoles',
    author_email='g.r.napoles@uvt.nl',
    license='Apache License 2.0',
    packages=['fcm_mp'],
    install_requires=['numpy', 'scikit-learn'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.8',
    ],
)
