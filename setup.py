from setuptools import setup, find_packages

setup(
    name='valorant-live-game-predictor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'valorant-predictor=live_win_prob.gather_data:main'
        ]
    }
)