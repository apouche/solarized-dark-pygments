# Solarized (Dark) Pygments Style

## What Is It?

This is a simple style for [Pygments][pygments_home] that is inspired by the
[Solarized project][solarized_home] by Ethan Schoonover.

This style is for the dark background variant of Solarized. If you're looking
for a light background version, try
[john2x's `solarized-pygment`][light_bg_pygments].

[pygments_home]: http://pygments.org/
[solarized_home]: http://ethanschoonover.com/solarized
[light_bg_pygments]: https://github.com/john2x/solarized-pygment

## How Do I Install It?

You must first, find the path of the Pygments egg styles folder, this is usually something like
`/Library/Python/2.7/site-packages/Pygments-1.5-py2.7.egg/pygments/styles/`.

Then execute :

    sudo git clone git://github.com/gthank/solarized-dark-pygments.git && cd solarized-dark-pygments
    sudo python setup.py install

You're done, now you can do things like :

`pygmentize -O full,style=solarized -o ~/Desktop/test.html ~/.bashrc`

## Acknowledgements

I built it mostly by adapting the various editor syntax coloring themes that
are available in the project proper, especially the TextMate theme.

